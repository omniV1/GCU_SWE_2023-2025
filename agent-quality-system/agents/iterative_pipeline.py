# agents/iterative_pipeline.py
"""
Iterative Feedforward Pipeline with Confidence Scoring
Performs multiple passes until predictions converge or confidence threshold is met.
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class ConfidenceLevel(Enum):
    """Confidence levels for predictions"""
    HIGH = "HIGH"      # >90% confident
    MEDIUM = "MEDIUM"  # 70-90% confident
    LOW = "LOW"        # 50-70% confident
    UNCERTAIN = "UNCERTAIN"  # <50% confident


@dataclass
class GatePrediction:
    """Prediction result for a single gate"""
    gate_name: str
    result: str  # PASS or FAIL
    confidence: float  # 0.0 to 1.0
    confidence_level: ConfidenceLevel
    score: float  # Raw score before thresholding
    iterations: int  # Number of iterations to converge


@dataclass
class PipelineResult:
    """Complete pipeline result with all gates"""
    gates: Dict[str, GatePrediction]
    overall_result: str
    overall_confidence: float
    total_iterations: int
    converged: bool


class IterativeFeedforwardPipeline:
    """
    Multi-pass classification pipeline with confidence scoring.
    
    The pipeline performs multiple iterations, refining predictions
    until they converge or a maximum iteration count is reached.
    """
    
    def __init__(self, config: Optional[Dict] = None, verbose: bool = False):
        self.config = config or {}
        self.verbose = verbose
        
        # Iteration settings
        self.max_iterations = 5
        self.convergence_threshold = 0.01  # Change threshold for convergence
        self.confidence_threshold = 0.85   # Target confidence level
        
        # Gate weights for confidence calculation
        self.gate_weights = {
            'bug_gate': 1.0,
            'vulnerability_gate': 1.5,  # Security issues weighted higher
            'security_hotspot_gate': 0.8,
            'reliability_gate': 0.9,
            'security_gate': 1.5,
            'maintainability_gate': 0.7,
            'coverage_gate': 0.5,
            'duplication_gate': 0.6,
        }
    
    def log(self, message: str):
        if self.verbose:
            print(f"[Iterative Pipeline] {message}")
    
    @staticmethod
    def sigmoid(x: float, steepness: float = 1.0) -> float:
        """Sigmoid activation with adjustable steepness"""
        return 1 / (1 + np.exp(-steepness * np.clip(x, -500, 500)))
    
    def calculate_bug_score(self, features: Dict, iteration: int) -> Tuple[float, str]:
        """Calculate bug gate score with iteration-based refinement"""
        complexity = features.get('max_complexity', 0)
        nesting = features.get('max_nesting', 0)
        length = features.get('max_function_length', 0)
        
        # Base score
        base_score = (
            0.4 * self.sigmoid(complexity - 10) +
            0.3 * self.sigmoid(nesting - 3) +
            0.3 * self.sigmoid(length - 50)
        )
        
        # Refinement based on iteration (reduce noise each pass)
        noise_reduction = 1 - (0.1 * iteration)
        refined_score = base_score * noise_reduction + base_score * (1 - noise_reduction)
        
        threshold = 0.5 - (0.05 * iteration)  # Slightly lower threshold each iteration
        result = 'FAIL' if refined_score > threshold else 'PASS'
        
        return refined_score, result
    
    def calculate_vuln_score(self, features: Dict, iteration: int) -> Tuple[float, str]:
        """Calculate vulnerability gate score"""
        total_signals = features.get('total_vulnerability_signals', 0)
        eval_usage = features.get('eval_exec', features.get('eval_usage', 0))
        sql_injection = features.get('sql_injection', 0)
        secrets = features.get('hardcoded_secrets', 0)
        
        # Critical vulnerability weighting
        critical_score = (
            0.4 * self.sigmoid(total_signals - 1) +
            0.3 * min(eval_usage, 1) +
            0.2 * min(sql_injection, 1) +
            0.1 * min(secrets / 2, 1)
        )
        
        # Any critical issue = high score
        if eval_usage > 0 or sql_injection > 0 or secrets > 0:
            critical_score = max(critical_score, 0.7)
        
        threshold = 0.4
        result = 'FAIL' if critical_score > threshold else 'PASS'
        
        return critical_score, result
    
    def calculate_hotspot_score(self, features: Dict, iteration: int) -> Tuple[float, str]:
        """Calculate security hotspot score"""
        hotspots = features.get('security_hotspots', 0)
        crypto = features.get('crypto_usage', 0)
        file_ops = features.get('file_operations', 0)
        network = features.get('network_operations', 0)
        
        total = hotspots + crypto + file_ops + network
        score = self.sigmoid(total - 2)
        
        threshold = 0.5
        result = 'FAIL' if score > threshold else 'PASS'
        
        return score, result
    
    def calculate_reliability_score(self, features: Dict, iteration: int) -> Tuple[float, str]:
        """Calculate reliability gate score"""
        complexity = features.get('max_complexity', 0)
        nesting = features.get('max_nesting', 0)
        error_handling = features.get('error_handling_score', 50)
        
        # Reliability score (higher is better)
        reliability = 100
        reliability -= min(complexity * 2, 30)
        reliability -= min(nesting * 5, 25)
        reliability -= (100 - error_handling) * 0.2
        
        # Normalize to 0-1 (inverted - high reliability = low failure score)
        score = 1 - (reliability / 100)
        
        threshold = 0.4  # Fail if reliability < 60%
        result = 'FAIL' if score > threshold else 'PASS'
        
        return score, result
    
    def calculate_security_score(self, features: Dict, iteration: int) -> Tuple[float, str]:
        """Calculate security gate score"""
        sql = features.get('sql_injection', 0)
        cmd = features.get('command_injection', 0)
        secrets = features.get('hardcoded_secrets', 0)
        eval_exec = features.get('eval_exec', 0)
        xss = features.get('xss_risk', 0)
        
        critical = sql + cmd + secrets
        high = eval_exec + xss
        
        score = self.sigmoid(critical * 2 + high - 1)
        
        threshold = 0.5
        result = 'FAIL' if score > threshold else 'PASS'
        
        return score, result
    
    def calculate_maintainability_score(self, features: Dict, iteration: int) -> Tuple[float, str]:
        """Calculate maintainability gate score"""
        avg_complexity = features.get('avg_complexity', 0)
        avg_length = features.get('avg_function_length', 0)
        
        complexity_ratio = min(avg_complexity / 10, 1.0)
        length_ratio = min(avg_length / 30, 1.0)
        
        # Score 0-1 (higher = worse maintainability)
        score = (complexity_ratio * 0.5 + length_ratio * 0.5)
        
        threshold = 0.6  # Fail if maintainability < 40%
        result = 'FAIL' if score > threshold else 'PASS'
        
        return score, result
    
    def calculate_coverage_score(self, features: Dict, iteration: int) -> Tuple[float, str]:
        """Calculate coverage gate score"""
        has_tests = features.get('has_test_files', 0)
        test_ratio = features.get('test_file_ratio', 0)
        has_framework = features.get('has_test_framework', 0)
        
        # Estimate coverage
        estimated = test_ratio * 100
        if has_framework:
            estimated += 10
        
        # Score (higher = lower coverage = worse)
        score = 1 - (min(estimated, 100) / 100)
        
        threshold = 0.2  # Fail if coverage < 80%
        result = 'FAIL' if score > threshold else 'PASS'
        
        return score, result
    
    def calculate_duplication_score(self, features: Dict, iteration: int) -> Tuple[float, str]:
        """Calculate duplication gate score"""
        dup_ratio = features.get('duplication_ratio', 0)
        
        score = self.sigmoid((dup_ratio - 3) / 2)  # Target < 3%
        
        threshold = 0.5
        result = 'FAIL' if score > threshold else 'PASS'
        
        return score, result
    
    def calculate_confidence(self, score: float, threshold: float = 0.5) -> float:
        """
        Calculate confidence based on distance from threshold.
        Scores further from threshold = higher confidence.
        """
        distance = abs(score - threshold)
        # Confidence scales with distance from threshold
        confidence = min(distance * 2, 1.0)
        return confidence
    
    def get_confidence_level(self, confidence: float) -> ConfidenceLevel:
        """Map confidence score to level"""
        if confidence >= 0.9:
            return ConfidenceLevel.HIGH
        elif confidence >= 0.7:
            return ConfidenceLevel.MEDIUM
        elif confidence >= 0.5:
            return ConfidenceLevel.LOW
        else:
            return ConfidenceLevel.UNCERTAIN
    
    def classify_iterative(
        self,
        bug_features: Dict,
        vuln_features: Dict,
        project_features: Dict
    ) -> PipelineResult:
        """
        Perform iterative classification until convergence or max iterations.
        """
        self.log("Starting iterative classification...")
        
        # Gate score calculators
        gate_calculators = {
            'bug_gate': (self.calculate_bug_score, bug_features),
            'vulnerability_gate': (self.calculate_vuln_score, vuln_features),
            'security_hotspot_gate': (self.calculate_hotspot_score, vuln_features),
            'reliability_gate': (self.calculate_reliability_score, bug_features),
            'security_gate': (self.calculate_security_score, vuln_features),
            'maintainability_gate': (self.calculate_maintainability_score, bug_features),
            'coverage_gate': (self.calculate_coverage_score, project_features),
            'duplication_gate': (self.calculate_duplication_score, project_features),
        }
        
        # Track scores across iterations
        history: Dict[str, List[float]] = {gate: [] for gate in gate_calculators}
        final_results: Dict[str, GatePrediction] = {}
        
        converged = False
        iteration = 0
        
        for iteration in range(self.max_iterations):
            self.log(f"Iteration {iteration + 1}/{self.max_iterations}")
            
            current_scores = {}
            
            for gate_name, (calculator, features) in gate_calculators.items():
                score, result = calculator(features, iteration)
                current_scores[gate_name] = score
                history[gate_name].append(score)
                
                # Calculate confidence
                confidence = self.calculate_confidence(score)
                conf_level = self.get_confidence_level(confidence)
                
                final_results[gate_name] = GatePrediction(
                    gate_name=gate_name,
                    result=result,
                    confidence=confidence,
                    confidence_level=conf_level,
                    score=score,
                    iterations=iteration + 1
                )
                
                self.log(f"  {gate_name}: {result} (score={score:.3f}, conf={confidence:.2f})")
            
            # Check convergence (scores stabilized)
            if iteration > 0:
                max_change = max(
                    abs(history[g][-1] - history[g][-2])
                    for g in gate_calculators
                )
                
                if max_change < self.convergence_threshold:
                    self.log(f"Converged at iteration {iteration + 1}")
                    converged = True
                    break
                
                # Check if all gates have high confidence
                all_confident = all(
                    final_results[g].confidence >= self.confidence_threshold
                    for g in gate_calculators
                )
                
                if all_confident:
                    self.log(f"All gates confident at iteration {iteration + 1}")
                    converged = True
                    break
        
        # Calculate overall result
        failed_gates = [g for g, p in final_results.items() if p.result == 'FAIL']
        overall_result = 'FAIL' if failed_gates else 'PASS'
        
        # Overall confidence (weighted average)
        total_weight = sum(self.gate_weights.values())
        overall_confidence = sum(
            self.gate_weights.get(g, 1.0) * p.confidence
            for g, p in final_results.items()
        ) / total_weight
        
        return PipelineResult(
            gates=final_results,
            overall_result=overall_result,
            overall_confidence=overall_confidence,
            total_iterations=iteration + 1,
            converged=converged
        )
    
    def display_result(self, result: PipelineResult):
        """Display result in a formatted way"""
        from rich.console import Console
        from rich.table import Table
        from rich.panel import Panel
        
        console = Console()
        
        # Header
        status = "✓ PASSED" if result.overall_result == "PASS" else "✗ FAILED"
        color = "green" if result.overall_result == "PASS" else "red"
        
        console.print(Panel.fit(
            f"[bold {color}]{status}[/bold {color}]\n"
            f"Confidence: {result.overall_confidence:.1%}\n"
            f"Iterations: {result.total_iterations} ({'converged' if result.converged else 'max reached'})",
            title="Iterative Pipeline Result",
            border_style=color
        ))
        
        # Gate details
        table = Table(title="Gate Results with Confidence")
        table.add_column("Gate", style="cyan")
        table.add_column("Result", justify="center")
        table.add_column("Score", justify="center")
        table.add_column("Confidence", justify="center")
        table.add_column("Level", justify="center")
        
        for gate_name, pred in result.gates.items():
            result_color = "green" if pred.result == "PASS" else "red"
            conf_color = "green" if pred.confidence >= 0.7 else "yellow" if pred.confidence >= 0.5 else "red"
            
            table.add_row(
                gate_name.replace('_', ' ').title(),
                f"[{result_color}]{pred.result}[/{result_color}]",
                f"{pred.score:.3f}",
                f"[{conf_color}]{pred.confidence:.1%}[/{conf_color}]",
                pred.confidence_level.value
            )
        
        console.print(table)
