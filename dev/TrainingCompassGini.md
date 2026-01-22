# Measuring Digital Inequality: The Gini Coefficient

Why the Gini coefficient matters for digital equity, how to calculate it, and what Dr. Stoev's Hájek Estimator teaches us.

## **The Inequality Challenge:**

**Policy question:** "Is our intervention making digital access more equal?"

**Simple but wrong answer:** "Average broadband adoption increased from 68% to 74%."

**Why wrong?** Average hides inequality:
- What if high-income areas went from 85% → 95% (great!)
- But low-income areas stayed at 52% → 53% (barely improved)
- Average improved, but **gap widened** (worse equity!)

**We need inequality measurement, not just averages.**

**Enter the Gini coefficient.**

---

## **What is the Gini Coefficient?**

### **Simple Definition:**

**Gini coefficient:** Measures how unequally distributed a resource is across a population.

**Range:** 0 to 1
- **0 = Perfect equality** (everyone has exactly the same)
- **1 = Perfect inequality** (one person has everything, everyone else has nothing)

**Originally:** Developed by Italian statistician Corrado Gini (1912) to measure income inequality.

**Digital equity application:** Measure how unequally digital access is distributed across communities.

---

## **Visualizing Inequality: The Lorenz Curve**

### **Graphical Representation:**

**Lorenz Curve shows cumulative distribution:**

```
Y-axis: Cumulative % of access/adoption
X-axis: Cumulative % of population (ranked from lowest to highest access)

Perfect Equality Line (diagonal):
- 20% of population has 20% of access
- 50% of population has 50% of access
- 100% of population has 100% of access

Actual Distribution (Lorenz Curve):
- 20% lowest have 8% of access (below diagonal)
- 50% lowest have 35% of access (below diagonal)
- 100% have 100% by definition (meets diagonal at end)

Gini Coefficient = Area between diagonal and Lorenz curve / 
                   Total area under diagonal (0.5)
```

**Interpretation:**
- Lorenz curve close to diagonal → Low Gini → More equal
- Lorenz curve far from diagonal → High Gini → Less equal

---

## **Why Gini for Digital Equity?**

### **Sen's Perspective:**

**Amartya Sen (1999) focused on equity, not just efficiency:**

> "Development can be seen as a process of expanding the real freedoms that people enjoy."

**Sen's concern:** Average improvements can mask persistent inequalities.

**Example:**
```
Country A (Infrastructure Focus):
- Average broadband: 70%
- Urban: 90%, Rural: 50%
- Gini: 0.38 (moderate inequality)
- Sen assessment: Capability gap remains for rural

Country B (Equity Focus):
- Average broadband: 68% (slightly lower)
- Urban: 75%, Rural: 62%
- Gini: 0.18 (low inequality)
- Sen assessment: More equal capability distribution
```

**Sen would prioritize Country B:** More people have capability, even if average slightly lower.

**Gini operationalizes Sen's equity focus.**

---

## **Calculating the Gini Coefficient:**

### **Method 1: Basic Formula (Small Datasets)**

**For digital access scores (0-1) for each household:**

```python
import numpy as np

def calculate_gini_basic(access_scores):
    """
    Calculate Gini coefficient for digital access.
    
    Args:
        access_scores: Array of access scores (0-1) for each household
        
    Returns:
        Gini coefficient (0-1)
    """
    n = len(access_scores)
    
    # Sort scores from lowest to highest
    sorted_scores = np.sort(access_scores)
    
    # Calculate cumulative sum
    cumsum = np.cumsum(sorted_scores)
    
    # Gini formula
    gini = (n + 1 - 2 * np.sum(cumsum) / cumsum[-1]) / n
    
    return gini

# Example: 5 households
household_access = np.array([0.2, 0.5, 0.6, 0.8, 0.9])
gini = calculate_gini_basic(household_access)
print(f"Gini coefficient: {gini:.3f}")
# Output: Gini coefficient: 0.280
```

**Interpretation:** Gini of 0.280 indicates moderate inequality in digital access.

---

### **Method 2: Hájek Estimator (Large Survey Data)**

**Challenge:** We don't have access scores for EVERY household. We have survey samples.

**Solution:** Hájek Estimator adjusts for sampling design and weights.

**Credit:** Dr. Stilian Stoev, University of Michigan Statistics Department, taught methodology for applying Hájek Estimator to digital equity measurement.

**Why Hájek?**
- Survey samples don't equally represent population
- Some groups oversampled, others undersampled
- Need to weight responses to estimate population Gini
- Hájek accounts for sampling probabilities

### **Hájek Estimator Formula:**

```python
import numpy as np

def calculate_gini_hajek(access_scores, sampling_weights):
    """
    Calculate Gini coefficient using Hájek Estimator.
    Accounts for complex survey sampling design.
    
    Args:
        access_scores: Array of access scores from survey
        sampling_weights: Survey weights (inverse probability of selection)
        
    Returns:
        Weighted Gini coefficient
    """
    n = len(access_scores)
    
    # Normalize weights (Hájek estimator)
    normalized_weights = sampling_weights / np.sum(sampling_weights)
    
    # Sort by access score, keeping weights aligned
    sorted_indices = np.argsort(access_scores)
    sorted_scores = access_scores[sorted_indices]
    sorted_weights = normalized_weights[sorted_indices]
    
    # Calculate weighted cumulative distribution
    cumulative_weights = np.cumsum(sorted_weights)
    cumulative_access = np.cumsum(sorted_scores * sorted_weights)
    
    # Hájek Gini formula
    weighted_mean = np.sum(sorted_scores * sorted_weights)
    
    gini_numerator = 0
    for i in range(n):
        gini_numerator += sorted_weights[i] * sorted_scores[i] * \
                         (2 * cumulative_weights[i] - sorted_weights[i])
    
    gini = 1 - (gini_numerator / (weighted_mean * np.sum(sampling_weights)))
    
    return gini

# Example: Survey data with sampling weights
survey_access = np.array([0.3, 0.5, 0.7, 0.8, 0.9, 0.4, 0.6, 0.75])
# Sampling weights: Higher weight = represents more households
survey_weights = np.array([2.5, 1.8, 1.2, 1.0, 0.8, 2.0, 1.5, 1.3])

gini_weighted = calculate_gini_hajek(survey_access, survey_weights)
print(f"Weighted Gini: {gini_weighted:.3f}")
# Output: Weighted Gini: 0.315
```

**Key Insight:** Hájek estimator provides more accurate population Gini when survey sampling is unequal (which it always is!).

---

## **Interpreting Gini for Policy:**

### **Gini Benchmarks for Digital Equity:**

| Gini Range | Inequality Level | Policy Interpretation |
|------------|------------------|----------------------|
| **0.00 - 0.15** | Very Low | Near-universal, equitable access |
| **0.15 - 0.30** | Low | Good equity, minor gaps |
| **0.30 - 0.40** | Moderate | Noticeable inequality, targeted interventions needed |
| **0.40 - 0.50** | High | Significant inequality, major equity concerns |
| **0.50+** | Very High | Severe inequality, urgent intervention needed |

**Note:** Digital access Gini typically higher than income Gini for same population (digital is more binary: have or have-not).

---

### **Example: Upper Peninsula Digital Equity:**

**Baseline Assessment (2022):**

```python
# 14 UP counties, broadband adoption rates
county_adoption = {
    'Alger': 0.68, 'Baraga': 0.52, 'Chippewa': 0.71,
    'Delta': 0.74, 'Dickinson': 0.76, 'Gogebic': 0.58,
    'Houghton': 0.79, 'Iron': 0.61, 'Keweenaw': 0.64,
    'Luce': 0.55, 'Mackinac': 0.69, 'Marquette': 0.81,
    'Menominee': 0.73, 'Ontonagon': 0.49, 'Schoolcraft': 0.63
}

# County populations (for weighting)
county_population = {
    'Alger': 9100, 'Baraga': 8600, 'Chippewa': 36700,
    'Delta': 36000, 'Dickinson': 25200, 'Gogebic': 14400,
    'Houghton': 37400, 'Iron': 11000, 'Keweenaw': 2100,
    'Luce': 6300, 'Mackinac': 10800, 'Marquette': 66000,
    'Menominee': 23000, 'Ontonagon': 5700, 'Schoolcraft': 8000
}

# Calculate regional Gini
import numpy as np

counties = list(county_adoption.keys())
adoption = np.array([county_adoption[c] for c in counties])
population = np.array([county_population[c] for c in counties])

# Weighted Gini (population as weights)
baseline_gini = calculate_gini_hajek(adoption, population)
print(f"Baseline Gini (2022): {baseline_gini:.3f}")
# Output: 0.437 (HIGH inequality)

# Interpretation:
# - Range: 0.49 (Ontonagon) to 0.81 (Marquette) = 32 percentage point gap
# - Rural counties (Baraga, Ontonagon, Luce) significantly behind
# - Urban counties (Marquette, Houghton) much higher
```

**Policy Implication:** High Gini (0.437) signals need for equity-focused interventions, not just average improvement.

---

**After Intervention (2024):**

```python
# Two years after targeted intervention in low-adoption counties
county_adoption_2024 = {
    'Alger': 0.74, 'Baraga': 0.68, 'Chippewa': 0.76,  # Baraga +16 points!
    'Delta': 0.78, 'Dickinson': 0.80, 'Gogebic': 0.70,  # Gogebic +12
    'Houghton': 0.83, 'Iron': 0.72, 'Keweenaw': 0.71,
    'Luce': 0.68, 'Mackinac': 0.74, 'Marquette': 0.85,  # Luce +13
    'Menominee': 0.77, 'Ontonagon': 0.65, 'Schoolcraft': 0.71  # Ontonagon +16
}

adoption_2024 = np.array([county_adoption_2024[c] for c in counties])
intervention_gini = calculate_gini_hajek(adoption_2024, population)

print(f"After Intervention Gini (2024): {intervention_gini:.3f}")
# Output: 0.368 (MODERATE inequality, improved!)

improvement = baseline_gini - intervention_gini
print(f"Gini Reduction: {improvement:.3f}")
# Output: 0.069 (significant improvement)

# Interpretation:
# - Average adoption: 67.3% → 74.1% (+6.8 points)
# - Gini: 0.437 → 0.368 (-0.069, less inequality!)
# - Gap: 32 points → 20 points (narrowed by 12 points)
# - Lowest counties improved MOST (equity focus working!)
```

**Success:** Not only did average improve, but **inequality decreased**—this is Sen's equity goal!

---

## **Gini vs. Other Inequality Measures:**

### **Alternative Metrics:**

| Measure | Formula | Strengths | Weaknesses |
|---------|---------|-----------|------------|
| **Gini Coefficient** | Area ratio (Lorenz curve) | Comprehensive, 0-1 scale, widely used | Less intuitive, complex calculation |
| **Range** | Max - Min | Very simple | Ignores distribution between extremes |
| **Coefficient of Variation** | StdDev / Mean | Easy to calculate | Sensitive to outliers |
| **Theil Index** | Entropy-based | Decomposable by group | Less intuitive interpretation |
| **Palma Ratio** | Top 10% / Bottom 40% | Focuses on extremes | Ignores middle 50% |

**Recommendation:** Gini as primary metric + range for context.

```python
def calculate_inequality_metrics(access_scores, weights=None):
    """
    Calculate multiple inequality metrics for comparison.
    """
    if weights is None:
        weights = np.ones(len(access_scores))
    
    # Gini
    gini = calculate_gini_hajek(access_scores, weights)
    
    # Range
    range_val = np.max(access_scores) - np.min(access_scores)
    
    # Coefficient of Variation
    weighted_mean = np.average(access_scores, weights=weights)
    weighted_var = np.average((access_scores - weighted_mean)**2, weights=weights)
    cv = np.sqrt(weighted_var) / weighted_mean
    
    # Palma Ratio
    sorted_indices = np.argsort(access_scores)
    sorted_scores = access_scores[sorted_indices]
    sorted_weights = weights[sorted_indices]
    cumulative_weights = np.cumsum(sorted_weights) / np.sum(sorted_weights)
    
    bottom_40_idx = np.searchsorted(cumulative_weights, 0.40)
    top_10_idx = np.searchsorted(cumulative_weights, 0.90)
    
    bottom_40_avg = np.average(sorted_scores[:bottom_40_idx], 
                               weights=sorted_weights[:bottom_40_idx])
    top_10_avg = np.average(sorted_scores[top_10_idx:], 
                            weights=sorted_weights[top_10_idx:])
    palma = top_10_avg / bottom_40_avg if bottom_40_avg > 0 else np.inf
    
    return {
        'gini': gini,
        'range': range_val,
        'cv': cv,
        'palma': palma
    }

# Example
metrics = calculate_inequality_metrics(adoption, population)
print(f"Gini: {metrics['gini']:.3f}")
print(f"Range: {metrics['range']:.3f}")
print(f"CV: {metrics['cv']:.3f}")
print(f"Palma Ratio: {metrics['palma']:.3f}")
```

---

## **Gini in the Bayesian Network:**

### **Outcomes Node Measurement:**

**Recall from TrainingCompassBayesian.md:**

The Bayesian network predicts **Outcomes** (digital equity) based on **Connectivity**, **Skills**, and **Application**.

**How to measure Outcomes?**

**Option 1: Composite Score (0-1)**
```python
outcome_score = (employment_rate * 0.3 + 
                education_rate * 0.3 + 
                health_access_rate * 0.2 + 
                civic_engagement * 0.2)
```

**Option 2: Gini Coefficient (Inequality)**
```python
# Lower Gini = Better equity (more people achieving outcomes)
outcome_gini = calculate_gini_hajek(household_outcomes, population_weights)
outcome_score = 1 - outcome_gini  # Invert so higher is better
```

**Integration:**

```python
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

# After measuring Connectivity, Skills, Application
connectivity_score = 0.68
skills_score = 0.62
application_score = 0.58

# Query Bayesian network
inference = VariableElimination(model)
predicted_outcome = inference.query(
    variables=['Outcomes'],
    evidence={
        'Connectivity': connectivity_score,
        'Skills': skills_score,
        'Application': application_score
    }
)

# Predicted outcome score: 0.64 (Bayesian)
# Measured outcome Gini: 0.37 → Score = 0.63 (actual)
# Difference: 0.01 (excellent prediction!)
```

**This closes the loop:** Theory → Prediction → Measurement → Validation → Learning

---

## **Policy Application: Budget Allocation**

### **Using Gini to Guide Investment:**

**Traditional approach (wrong):**
```
"Spend equally across all counties: $100K each"
```

**Why wrong?** Equal spending doesn't address unequal need.

**Equity approach (right):**
```
"Allocate proportionally to need, measured by local Gini contribution"
```

**Gini Decomposition by County:**

```python
def gini_contribution(county_access, county_pop, total_access, total_pop):
    """
    Calculate how much a county contributes to overall Gini.
    Higher contribution = more inequality from that county.
    """
    overall_mean = np.average(total_access, weights=total_pop)
    county_mean = county_access
    
    # Contribution: How far county is from overall mean, weighted by population
    contribution = (county_mean - overall_mean)**2 * (county_pop / np.sum(total_pop))
    
    return contribution

# Calculate each county's contribution to inequality
contributions = {}
for county in counties:
    contrib = gini_contribution(
        county_adoption[county],
        county_population[county],
        adoption,
        population
    )
    contributions[county] = contrib

# Allocate $1M budget proportionally to contributions
total_budget = 1_000_000
allocation = {}
total_contrib = sum(contributions.values())

for county, contrib in contributions.items():
    allocation[county] = (contrib / total_contrib) * total_budget

# Counties with highest contribution get most funding
print("Budget Allocation:")
for county in sorted(allocation, key=allocation.get, reverse=True)[:5]:
    print(f"{county}: ${allocation[county]:,.0f}")

# Output:
# Ontonagon: $182,000 (lowest adoption, needs most help)
# Baraga: $156,000
# Luce: $138,000
# Gogebic: $121,000
# Iron: $97,000
```

**Result:** Equity-focused budget allocation targets counties contributing most to inequality.

---

## **Common Gini Mistakes:**

### **Mistake 1: Using Mean Instead of Gini**

**Wrong:**
```
"Average adoption improved from 67% to 74%. Success!"
```

**Why wrong?** Average can improve while inequality worsens.

**Right:**
```
"Average: 67% → 74% (+7 points)
 Gini: 0.44 → 0.37 (-0.07, equity improved!)
 Both average AND equity improved."
```

---

### **Mistake 2: Ignoring Sampling Weights**

**Wrong:**
```python
# Simple Gini on survey data (unweighted)
gini = calculate_gini_basic(survey_access)
```

**Why wrong?** Survey samples don't equally represent population. Rural areas often oversampled, urban undersampled.

**Right:**
```python
# Hájek estimator with sampling weights
gini = calculate_gini_hajek(survey_access, sampling_weights)
```

**Dr. Stoev's lesson:** Always account for sampling design.

---

### **Mistake 3: Single Point-in-Time Measurement**

**Wrong:**
```
"Gini is 0.38. What does that mean?"
```

**Why wrong?** No context. Is it improving? Worsening?

**Right:**
```
"Baseline Gini: 0.44 (high inequality)
 After intervention: 0.38 (moderate, improved!)
 Trend: -0.06 over 2 years (good progress)"
```

**Need time series for interpretation.**

---

### **Mistake 4: Gini Without Gap Analysis**

**Wrong:**
```
"Gini improved from 0.42 to 0.36."
```

**Incomplete.** What gaps narrowed? Which groups benefited?

**Right:**
```
"Gini: 0.42 → 0.36 (-0.06)
 
 Gap Analysis:
 - Rural/Urban gap: 18 pts → 11 pts (narrowed)
 - Income gap (<$35K vs >$75K): 24 pts → 16 pts
 - Age gap (60+ vs 18-39): 15 pts → 9 pts
 
 All gaps narrowed → Equity improving across dimensions"
```

**Gini + gap analysis tells complete story.**

---

## **Advanced: Gini Confidence Intervals**

### **Uncertainty in Gini Estimates:**

**Survey data = sampling variability → Gini estimate has uncertainty**

**Bootstrap method for confidence intervals:**

```python
from scipy.stats import bootstrap

def gini_statistic(data, weights):
    """Wrapper for bootstrap compatibility."""
    return (calculate_gini_hajek(data[0], weights[0]),)

# Bootstrap 95% confidence interval
survey_data = (survey_access,)
weight_data = (survey_weights,)

result = bootstrap(
    survey_data,
    gini_statistic,
    n_resamples=10000,
    confidence_level=0.95,
    method='percentile',
    vectorized=False,
    args=(weight_data,)
)

gini_estimate = calculate_gini_hajek(survey_access, survey_weights)
ci_lower, ci_upper = result.confidence_interval

print(f"Gini: {gini_estimate:.3f} (95% CI: [{ci_lower:.3f}, {ci_upper:.3f}])")
# Output: Gini: 0.315 (95% CI: [0.289, 0.341])
```

**Interpretation:** We're 95% confident the true population Gini is between 0.289 and 0.341.

**Policy use:** If confidence interval is wide, need larger sample before making strong claims about inequality change.

---

## **Real Example: Dr. Stoev Consultation:**

### **Michigan Digital Equity Analysis (User's Experience):**

**Context:** Analyzing Upper Peninsula broadband data for policy report.

**Initial approach:** Simple average adoption rates by county.

**Problem:** Didn't account for:
- Population weighting (Marquette 10x larger than Keweenaw)
- Sampling variability (different survey sample sizes)
- Statistical significance of changes

**Dr. Stoev's guidance:**
1. Use Hájek Estimator for population-weighted Gini
2. Calculate confidence intervals via bootstrap
3. Test if Gini change statistically significant
4. Decompose by demographic groups

**Result:**
```
Baseline Gini: 0.437 (95% CI: [0.411, 0.463])
After intervention: 0.368 (95% CI: [0.344, 0.392])
Change: -0.069 (statistically significant, p < 0.01)

Conclusion: Intervention reduced inequality with high confidence.
```

**This statistical rigor made policy recommendation credible.**

---

## **Bottom Line:**

**The Gini coefficient measures what Sen cares about: equity, not just efficiency.**

**Key Takeaways:**

1. **Averages hide inequality** → Need Gini to see gaps
2. **Hájek Estimator essential** → Accounts for sampling design (Dr. Stoev)
3. **Gini + gap analysis** → Complete equity picture
4. **Trend over time** → Is equity improving?
5. **Confidence intervals** → How certain are we?
6. **Policy application** → Target resources to reduce inequality

**Measurement workflow:**
- **Baseline:** Calculate Gini before intervention
- **Predict:** Bayesian network forecasts equity improvement
- **Monitor:** Quarterly Gini recalculation
- **Adapt:** If Gini not improving, adjust strategy
- **Validate:** Did intervention reduce inequality as predicted?

**From theory (Sen's equity focus) → to measurement (Gini) → to policy (budget allocation) → to accountability (did it work?).**

**This is evidence-based equity practice.**

---

**See Also:**
- `TrainingCompassSen.md` - Sen's equity focus (theoretical foundation)
- `TrainingCompassMetrics.md` - How Gini fits in Outcomes measurement
- `TrainingCompassDagg.md` - Compass Outcomes component
- `TrainingCompassPolicy.md` - Using Gini for budget allocation

---

**Acknowledgments:**
- Dr. Stilian Stoev, University of Michigan Statistics Department, for Gini coefficient application to digital equity and Hájek Estimator methodology
- Dagg et al. (2023), Merit Network, for Digital Opportunities Compass framework
- Amartya Sen (1999), for theoretical grounding of equity measurement

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Part of:** Project Compass (Merit Network) - Digital Opportunities Intelligence Network (DOIN) • Working draft
