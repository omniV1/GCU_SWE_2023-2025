#!/usr/bin/env python3
# generate_diagrams.py - Generate architecture diagrams for presentation

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
import os

# Color palette
COLORS = {
    'primary': '#e94560',
    'secondary': '#0f3460',
    'success': '#00d9a5',
    'accent': '#4ecdc4',
    'bg_dark': '#1a1a2e',
    'bg_card': '#16213e',
    'text': '#eaeaea',
}

def create_architecture_diagram(output_path):
    """Create the main system architecture diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.patch.set_facecolor(COLORS['bg_dark'])
    ax.set_facecolor(COLORS['bg_dark'])
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(7, 9.5, 'Multi-Agent Code Quality System Architecture', 
            fontsize=18, fontweight='bold', ha='center', color=COLORS['text'])
    
    # Helper function to draw boxes
    def draw_box(x, y, width, height, label, color, sublabel=None):
        box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                            boxstyle="round,pad=0.05,rounding_size=0.3",
                            facecolor=color, edgecolor=COLORS['text'], linewidth=2)
        ax.add_patch(box)
        ax.text(x, y + 0.1, label, fontsize=11, fontweight='bold', 
                ha='center', va='center', color=COLORS['text'])
        if sublabel:
            ax.text(x, y - 0.3, sublabel, fontsize=8, 
                    ha='center', va='center', color=COLORS['text'], alpha=0.8)
    
    # Helper function to draw arrows
    def draw_arrow(x1, y1, x2, y2, label=None):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', color=COLORS['text'], lw=2))
        if label:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(mx + 0.2, my, label, fontsize=8, color=COLORS['accent'])
    
    # Source Code (Input)
    draw_box(2, 8, 2.5, 1, '📄 Source Code', COLORS['secondary'], 'Input')
    
    # NLP Agent
    draw_box(7, 8, 3, 1, '🔍 NLP Agent', COLORS['primary'], 'Feature Extraction')
    
    # Arrow from source to NLP
    draw_arrow(3.5, 8, 5.3, 8, 'code text')
    
    # Features box
    draw_box(7, 6.5, 2.5, 0.8, 'Features', COLORS['secondary'])
    
    # Arrow from NLP to Features
    draw_arrow(7, 7.4, 7, 6.95)
    
    # Bug Gate Classifier
    draw_box(4, 5, 2.5, 1, '🐛 Bug Gate', COLORS['primary'], 'Classifier')
    
    # Vulnerability Gate Classifier
    draw_box(10, 5, 2.8, 1, '🔒 Vulnerability Gate', COLORS['primary'], 'Classifier')
    
    # Arrows from Features to Classifiers
    draw_arrow(5.7, 6.4, 4.5, 5.6, 'bug features')
    draw_arrow(8.3, 6.4, 9.5, 5.6, 'vuln features')
    
    # Activation Function boxes
    ax.text(4, 4, 'Sigmoid | ReLU', fontsize=9, ha='center', 
            color=COLORS['accent'], style='italic')
    ax.text(10, 4, 'Sigmoid | ReLU', fontsize=9, ha='center', 
            color=COLORS['accent'], style='italic')
    
    # Supervisor Agents
    draw_box(4, 3, 2.5, 1, '📊 Supervisor', COLORS['secondary'], 'Confusion Matrix')
    draw_box(10, 3, 2.5, 1, '📊 Supervisor', COLORS['secondary'], 'Confusion Matrix')
    
    # Arrows to Supervisors
    draw_arrow(4, 4.4, 4, 3.6)
    draw_arrow(10, 4.4, 10, 3.6)
    
    # Architecture Agent
    draw_box(7, 1.5, 4, 1.2, '🏗️ Architecture Agent', COLORS['success'], 
             'Select Optimal Activation')
    
    # Arrows to Architecture Agent
    draw_arrow(4.5, 2.4, 6, 2.1, 'metrics')
    draw_arrow(9.5, 2.4, 8, 2.1, 'metrics')
    
    # Output
    draw_box(12, 1.5, 2.5, 1, '✅ Config', COLORS['primary'], 'Optimal Setup')
    draw_arrow(9.1, 1.5, 10.6, 1.5)
    
    # Legend
    ax.text(1, 0.5, 'Legend:', fontsize=10, fontweight='bold', color=COLORS['text'])
    
    legend_y = 0.2
    for color, label in [(COLORS['primary'], 'Processing Agents'),
                         (COLORS['secondary'], 'Data/Storage'),
                         (COLORS['success'], 'Decision Agents')]:
        box = FancyBboxPatch((1, legend_y - 0.15), 0.3, 0.3,
                            boxstyle="round", facecolor=color, edgecolor='none')
        ax.add_patch(box)
        ax.text(1.5, legend_y, label, fontsize=8, va='center', color=COLORS['text'])
        legend_y -= 0.4
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=COLORS['bg_dark'])
    plt.close()
    print(f"✓ Saved: {output_path}")

def create_activation_comparison_diagram(output_path):
    """Create a diagram comparing Sigmoid vs ReLU"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor(COLORS['bg_dark'])
    
    # Sigmoid subplot
    ax1 = axes[0]
    ax1.set_facecolor(COLORS['bg_card'])
    
    x = np.linspace(-10, 10, 100)
    sigmoid = 1 / (1 + np.exp(-x))
    
    ax1.plot(x, sigmoid, color=COLORS['primary'], linewidth=3, label='σ(x)')
    ax1.axhline(y=0.6, color=COLORS['accent'], linestyle='--', label='Threshold (0.6)')
    ax1.axhline(y=0.5, color='gray', linestyle=':', alpha=0.5)
    ax1.axvline(x=0, color='gray', linestyle=':', alpha=0.5)
    
    ax1.fill_between(x, sigmoid, 0.6, where=(sigmoid > 0.6), 
                     alpha=0.3, color=COLORS['primary'], label='FAIL region')
    
    ax1.set_xlabel('Weighted Score', fontsize=12, color=COLORS['text'])
    ax1.set_ylabel('Probability', fontsize=12, color=COLORS['text'])
    ax1.set_title('Sigmoid Activation\n(Soft Thresholds)', fontsize=14, 
                  fontweight='bold', color=COLORS['text'])
    ax1.legend(loc='upper left', facecolor=COLORS['bg_card'], 
               edgecolor=COLORS['text'], labelcolor=COLORS['text'])
    ax1.tick_params(colors=COLORS['text'])
    ax1.grid(alpha=0.3)
    
    # Add annotations
    ax1.annotate('Gradual\ntransition', xy=(2, 0.88), xytext=(5, 0.7),
                fontsize=10, color=COLORS['text'],
                arrowprops=dict(arrowstyle='->', color=COLORS['accent']))
    
    # ReLU subplot
    ax2 = axes[1]
    ax2.set_facecolor(COLORS['bg_card'])
    
    # ReLU-style threshold visualization
    x_vals = np.arange(0, 20, 0.1)
    threshold = 15
    
    colors = [COLORS['success'] if v <= threshold else COLORS['primary'] for v in x_vals]
    
    ax2.bar(x_vals, [1] * len(x_vals), width=0.1, color=colors, alpha=0.8)
    ax2.axvline(x=threshold, color=COLORS['accent'], linewidth=3, 
                linestyle='-', label=f'Threshold ({threshold})')
    
    ax2.text(7, 0.5, 'PASS', fontsize=20, fontweight='bold', 
             ha='center', color=COLORS['success'])
    ax2.text(17, 0.5, 'FAIL', fontsize=20, fontweight='bold', 
             ha='center', color=COLORS['primary'])
    
    ax2.set_xlabel('Complexity Value', fontsize=12, color=COLORS['text'])
    ax2.set_ylabel('Decision', fontsize=12, color=COLORS['text'])
    ax2.set_title('ReLU Activation\n(Hard Thresholds)', fontsize=14, 
                  fontweight='bold', color=COLORS['text'])
    ax2.tick_params(colors=COLORS['text'])
    ax2.set_yticks([])
    ax2.legend(loc='upper left', facecolor=COLORS['bg_card'],
               edgecolor=COLORS['text'], labelcolor=COLORS['text'])
    
    # Add annotation
    ax2.annotate('Sharp\ncutoff', xy=(15, 0.8), xytext=(17.5, 0.85),
                fontsize=10, color=COLORS['text'],
                arrowprops=dict(arrowstyle='->', color=COLORS['accent']))
    
    fig.suptitle('Activation Function Comparison', fontsize=16, 
                 fontweight='bold', color=COLORS['text'], y=1.02)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=COLORS['bg_dark'])
    plt.close()
    print(f"✓ Saved: {output_path}")

def create_flow_diagram(output_path):
    """Create a flowchart showing the training process"""
    fig, ax = plt.subplots(figsize=(10, 12))
    fig.patch.set_facecolor(COLORS['bg_dark'])
    ax.set_facecolor(COLORS['bg_dark'])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Title
    ax.text(5, 11.5, 'Training Process Flow', 
            fontsize=18, fontweight='bold', ha='center', color=COLORS['text'])
    
    # Helper functions
    def draw_box(x, y, width, height, label, color, shape='rect'):
        if shape == 'diamond':
            diamond = plt.Polygon([(x, y + height/2), (x + width/2, y), 
                                   (x, y - height/2), (x - width/2, y)],
                                 facecolor=color, edgecolor=COLORS['text'], linewidth=2)
            ax.add_patch(diamond)
        else:
            box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                                boxstyle="round,pad=0.02,rounding_size=0.2",
                                facecolor=color, edgecolor=COLORS['text'], linewidth=2)
            ax.add_patch(box)
        ax.text(x, y, label, fontsize=9, fontweight='bold', 
                ha='center', va='center', color=COLORS['text'], wrap=True)
    
    def draw_arrow(x1, y1, x2, y2):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', color=COLORS['text'], lw=2))
    
    # Start
    draw_box(5, 10.5, 3, 0.7, '1. Load Training Data', COLORS['secondary'])
    
    # NLP
    draw_box(5, 9.3, 3, 0.7, '2. Extract Features', COLORS['primary'])
    draw_arrow(5, 10.1, 5, 9.7)
    
    # Test Sigmoid
    draw_box(3, 8, 2.5, 0.7, '3a. Test Sigmoid', COLORS['accent'])
    draw_arrow(4.2, 8.9, 3.3, 8.4)
    
    # Test ReLU
    draw_box(7, 8, 2.5, 0.7, '3b. Test ReLU', COLORS['accent'])
    draw_arrow(5.8, 8.9, 6.7, 8.4)
    
    # Confusion Matrices
    draw_box(3, 6.7, 2.5, 0.7, '4a. Build Matrix', COLORS['secondary'])
    draw_arrow(3, 7.6, 3, 7.1)
    
    draw_box(7, 6.7, 2.5, 0.7, '4b. Build Matrix', COLORS['secondary'])
    draw_arrow(7, 7.6, 7, 7.1)
    
    # Calculate Metrics
    draw_box(5, 5.5, 3, 0.7, '5. Calculate Metrics', COLORS['primary'])
    draw_arrow(3.5, 6.3, 4.3, 5.9)
    draw_arrow(6.5, 6.3, 5.7, 5.9)
    
    # Decision
    draw_box(5, 4.2, 3.5, 0.8, '6. Compare\nSpecificity', COLORS['success'], 'diamond')
    draw_arrow(5, 5.1, 5, 4.65)
    
    # Select Best
    draw_box(5, 2.8, 3, 0.7, '7. Select Best\n(ReLU wins!)', COLORS['success'])
    draw_arrow(5, 3.75, 5, 3.2)
    
    # Save Config
    draw_box(5, 1.5, 3, 0.7, '8. Save Config', COLORS['secondary'])
    draw_arrow(5, 2.4, 5, 1.9)
    
    # Side annotations
    ax.text(9, 8, 'For each\nQuality Gate', fontsize=8, color=COLORS['accent'], 
            style='italic', ha='center')
    
    ax.text(1, 4.2, 'Optimize for\nSpecificity\n(min FP)', fontsize=8, 
            color=COLORS['accent'], style='italic', ha='center')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=COLORS['bg_dark'])
    plt.close()
    print(f"✓ Saved: {output_path}")

def main():
    """Generate all diagrams"""
    print("Generating presentation diagrams...\n")
    
    # Create output directory
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'results', 'diagrams')
    os.makedirs(output_dir, exist_ok=True)
    
    create_architecture_diagram(os.path.join(output_dir, 'architecture_diagram.png'))
    create_activation_comparison_diagram(os.path.join(output_dir, 'activation_comparison.png'))
    create_flow_diagram(os.path.join(output_dir, 'training_flow.png'))
    
    print(f"\n✓ All diagrams saved to: {output_dir}")

if __name__ == "__main__":
    main()
