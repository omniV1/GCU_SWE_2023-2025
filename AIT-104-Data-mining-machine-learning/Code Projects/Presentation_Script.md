# Presentation Script: Gaussian Process Regression for Differential Gene Expression Analysis

**Duration: 5-6 minutes**  
**Authors: Owen Lindsey, Clay Kelly, John Hickox**

---

## Introduction (30 seconds)

Good [morning/afternoon]. Today we'll present our analysis using Gaussian Process Regression to detect differential gene expression in time-series data. 

The problem we're addressing is fundamental in computational biology: given gene expression measurements over time in control and treatment conditions, how do we determine if a gene responds significantly to treatment? Traditional methods test each time point independently, which ignores temporal correlations and reduces statistical power. Our approach uses Gaussian processes to model entire temporal trajectories as smooth functions, capturing the temporal structure of biological processes.

---

## Part I: Preliminary Steps (45 seconds)

Before implementing our analysis, we established the theoretical foundations. 

First, we reviewed gene expression concepts. Gene expression is the process by which DNA is converted into functional proteins. RNA sequencing measures mRNA levels, providing quantitative snapshots of gene activity. In our experiments, we compare control conditions—baseline states without intervention—against treatment conditions—experimental perturbations like drugs or stress.

We also explored the GPy package, a Python framework for Gaussian process modeling. While GPy offers extensive features, we primarily used scikit-learn for its accessible API and better integration with the Python scientific stack.

The key insight from our research is that traditional differential expression methods treat time points independently, missing overall patterns. Gaussian processes look at the entire time course at once, helping us better detect when genes truly respond to treatment.

---

## Part II: Implementation - Theory and Methods (2 minutes)

Our implementation began by generating synthetic gene expression data. We created two conditions: a control condition with stable baseline expression around 5.0 with Gaussian noise, and a treatment condition showing time-dependent upregulation following a sigmoid function, modeling gradual response to treatment.

A Gaussian process is a distribution over functions. Instead of choosing one specific function, we consider many possible functions, each with a probability based on how well it matches our data. A GP is specified by a mean function and a covariance function, or kernel, which encodes assumptions about function smoothness.

We used the Radial Basis Function, or RBF, kernel, which produces very smooth functions appropriate for biological processes. The kernel has two key hyperparameters: variance, which controls vertical scale, and lengthscale, which controls smoothness.

Gaussian processes can be viewed as a generalization of linear regression. A linear kernel produces straight lines, while an RBF kernel produces flexible curves. This demonstrates how kernel choice determines function flexibility.

For making predictions, the GP provides both mean predictions and uncertainty estimates. The predictive mean is a weighted combination of observed data points, where closer points have higher influence. The predictive variance decreases near data points and increases far from data, reflecting uncertainty.

We fit separate GP models to control and treatment data. Training involves optimizing hyperparameters—variance, lengthscale, and noise level—by maximizing the marginal likelihood. This automatically balances model complexity with data fit without requiring separate validation data.

The covariance matrix shows how correlated function values are at different time points. Nearby times are highly correlated, while distant times become nearly independent, capturing the biological prior that expression changes gradually.

---

## Part II: Testing for Differential Expression (1 minute)

Having trained GP models for both conditions, we tested whether the gene is differentially expressed using three complementary approaches.

First, the Likelihood Ratio Test compares two nested models: a single GP fitting pooled data versus separate GPs for each condition. Our test statistic was 62.82 with a p-value less than 0.000001, strongly rejecting the null hypothesis.

Second, the Bayes Factor quantifies relative evidence for differential expression. Our log Bayes Factor of 31.41 indicates extremely strong evidence—the separate models are over 43 trillion times more likely than the pooled model.

Third, Credible Interval Comparison examines whether confidence intervals overlap at each time point. We found that 55% of time points showed significant differences, well above our 10% threshold.

All three tests converged on the same conclusion: differential expression detected.

---

## Part III: Comparison with Non-Probabilistic Methods (45 seconds)

We compared Gaussian Process Classifiers with non-probabilistic alternatives like Support Vector Machines and Decision Trees.

The key distinction is probabilistic versus deterministic outputs. GP classifiers provide probability distributions, enabling statements like "90% confident this gene is differentially expressed." This uncertainty quantification supports decision-making and identifies ambiguous cases. In contrast, SVM and decision trees output hard decisions without uncertainty measures.

GP classifiers implement automatic complexity control through marginal likelihood, which penalizes overly complex models without requiring separate validation data. SVMs and decision trees require explicit regularization tuned via cross-validation.

However, GP complexity scales as O(n³) for n data points, limiting scalability. The practical limit is around 10,000 samples. For gene expression analysis, GPs are well-suited because RNA-seq experiments typically have small sample sizes, uncertainty quantification is critical, and temporal structure naturally encodes through kernel design.

---

## Results and Conclusion (45 seconds)

Our analysis revealed distinct temporal patterns. The control condition exhibited a flat trajectory around baseline, consistent with stable gene activity. The treatment condition showed progressive upregulation beginning around 5 hours post-treatment, following a sigmoid trajectory that stabilized at an elevated level.

The temporal pattern suggests two phases: an early phase from 0-5 hours where expression remains indistinguishable, indicating treatment effects haven't yet manifested. This delay reflects the time required for signal transduction and transcription factor activation. The late phase from 5-10 hours shows strong upregulation as treatment induces gene expression.

All three statistical tests detected significant differences, with strongest evidence emerging in late time points beyond 5 hours. The consistent results across multiple test approaches strengthen confidence in our conclusion.

**Key advantages of our GP approach:**
- Models entire trajectories rather than individual time points
- Built-in uncertainty quantification
- Non-parametric flexibility
- Handles missing data or irregular sampling
- Principled likelihood-based testing

**Limitations:**
- Computational cost scales as O(n³)
- Results depend on kernel choice
- Requires biological replicates for real experiments
- Multiple testing correction needed for genome-wide analysis

---

## Closing (15 seconds)

In conclusion, Gaussian Process Regression provides a powerful framework for detecting differential gene expression in time-series data. By modeling entire temporal trajectories with quantified uncertainty, we can make more informed biological inferences than traditional point-by-point methods.

Thank you for your attention. Are there any questions?

---

**Total estimated speaking time: 5-6 minutes**  
**Word count: ~750 words**  
**Speaking rate: ~120-150 words per minute**

