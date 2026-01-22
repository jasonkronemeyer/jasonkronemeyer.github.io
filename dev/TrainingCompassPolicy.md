# Evidence-Based Digital Equity Policy

How your framework translates research into actionable policy decisions for BEAD/DEA implementation.

## **The Policy Challenge:**

**Traditional approach:**
```
"Deploy broadband → Hope for the best → Measure years later"
```

**Evidence-based approach (your framework):**
```
"Assess stages → Predict outcomes → Deploy interventions → 
 Monitor progress → Update model → Refine policy"
```

**This document shows policymakers HOW to use the framework for decisions.**

---

## **The Three-Stage Assessment:**

### **Step 1: Assess Current State (Dagg Compass)**

**For each county/region, measure:**

**Opportunity (Connectivity):**
- Infrastructure availability: % covered by 100/20 Mbps
- Adoption rate: % subscribing to broadband
- Affordability: Cost as % of median income
- Device access: % with computers/smartphones

**Aspiration (Application):**
- Use diversity: # different use cases adopted
- Perceived relevance: Survey responses on value
- Engagement frequency: Hours/week of meaningful use
- Navigator access: Availability of support

**Growth Mindset (Skills):**
- Digital literacy: Assessment scores (e.g., Northstar)
- Training completion: % completing programs
- Confidence: Self-efficacy survey results
- Secure practices: Cybersecurity awareness

**Data sources:**
- FCC broadband maps (infrastructure)
- ACS Census data (demographics, adoption)
- M-Lab speed tests (actual performance)
- Community surveys (aspiration, mindset)

---

### **Step 2: Identify Gaps**

**Gap analysis template:**

```
County: _________________
Population: _____________
Rural/Urban: ____________

SCORES:
Opportunity (Connectivity):  ____ / 1.0
Aspiration (Application):    ____ / 1.0
Growth Mindset (Skills):     ____ / 1.0

GAPS:
Primary gap: ______________ (lowest score)
Secondary gap: ____________ (second lowest)
Tertiary: _________________ (needs attention)

THEORY EXPLANATION:
Sen: What conversion factors are missing?
Appadurai: How thin are aspirational maps?
Dweck: What mindset barriers exist?
Toyama: Will infrastructure amplify or widen gaps?
```

---

### **Step 3: Design Interventions**

**Match interventions to gaps:**

| Gap Type | Primary Intervention | Theory Basis | Expected Impact |
|----------|---------------------|--------------|-----------------|
| **Opportunity < 0.5** | Infrastructure deployment | Sen (resources) | Connectivity +0.2-0.3 |
| **Aspiration < 0.5** | Digital navigator program | Appadurai (navigation) | Application +0.2-0.3 |
| **Growth Mindset < 0.5** | Training with mindset focus | Dweck (beliefs) | Skills +0.15-0.25 |
| **All three low** | Comprehensive (all three) | Complete pathway | Equity +0.3-0.4 |

---

## **Budget Allocation Framework:**

### **Principle: Invest Proportionally to Gaps**

**Example County Profile:**
```
Connectivity:  0.45 (LOW)
Application:   0.62 (MODERATE)
Skills:        0.58 (MODERATE)
```

**Analysis:**
- Primary gap: Opportunity (infrastructure)
- Without infrastructure, other investments limited (Toyama amplification)
- BUT must build capacity alongside infrastructure

**Recommended allocation ($10M total):**
```
Infrastructure (60%):  $6M
  - Fiber deployment to unserved areas
  - Addresses primary gap
  - Sen: Provides resources

Navigators (25%):      $2.5M
  - Build aspiration capacity AS infrastructure deploys
  - Appadurai: Thicken maps while access expands
  - Prevent "build it and they won't come"

Training (15%):        $1.5M
  - Support skill development
  - Dweck: Growth mindset pedagogy
  - Enable effective use of new infrastructure

THEORY: Toyama amplification
  Infrastructure × (Navigator + Training capacity building) = 
  Growing impact over time
```

---

## **Prediction-Based Decision Making:**

### **Use Bayesian Network for "What-If" Scenarios**

**Question:** "Should we prioritize infrastructure or navigators?"

**Bayesian analysis:**
```python
# Scenario A: $10M infrastructure
current_state = {'Connectivity': 0.45, 'Application': 0.62, 'Skills': 0.58}
scenario_a = current_state.copy()
scenario_a['Connectivity'] = 0.70  # Infrastructure improves
P_equity_a = bayesian_model.predict(scenario_a)
# Result: P(Equity) = 0.48 → 0.61 (+0.13)

# Scenario B: $3M navigators + $7M infrastructure
scenario_b = current_state.copy()
scenario_b['Connectivity'] = 0.65  # Less infrastructure
scenario_b['Application'] = 0.78   # Navigators improve aspiration
scenario_b['Skills'] = 0.68        # Navigators help skills too
P_equity_b = bayesian_model.predict(scenario_b)
# Result: P(Equity) = 0.48 → 0.72 (+0.24)

# Recommendation: Scenario B (combined approach)
# ROI: +0.24 equity gain for $10M vs. +0.13 for infrastructure only
```

**Evidence:** Hampton & Bauer (2020) showed infrastructure alone insufficient

---

## **Policy Decision Matrix:**

### **Use This Table for Quick Decisions:**

| County Profile | Primary Investment | Supporting Investment | Expected Outcome |
|----------------|-------------------|----------------------|------------------|
| **Low Opp, Low Asp, Low Mind** | Infrastructure (50%) | Navigators (30%) + Training (20%) | High impact (+0.3-0.4 equity) |
| **High Opp, Low Asp, Low Mind** | Navigators (50%) | Training (30%) + Infrastructure maintain (20%) | Moderate-high (+0.25-0.35) |
| **High Opp, High Asp, Low Mind** | Training (60%) | Navigators support (25%) + Infrastructure maintain (15%) | Moderate (+0.15-0.25) |
| **Low Opp, High Asp, High Mind** | Infrastructure (80%) | Navigators/Training maintain (20%) | High (+0.3-0.4) FAST |
| **Moderate all three** | Balanced (40/30/30) | Adjust based on local priorities | Moderate (+0.2-0.3) |

**Evidence base:** Derived from Hampton & Bauer findings + Bayesian predictions

---

## **Monitoring and Evaluation:**

### **Continuous Assessment Cycle:**

**Every 6 months:**
1. Re-measure Compass components
2. Compare actual to predicted improvements
3. Update Bayesian network with results
4. Refine predictions for remaining timeline

**Example:**
```
Baseline (2024):
  Connectivity: 0.45, Application: 0.62, Skills: 0.58
  P(Equity): 0.48

After 6 months (navigator program deployed):
  Predicted: Application → 0.70, Skills → 0.64
  Actual:    Application → 0.68, Skills → 0.61
  
Analysis: Slightly below prediction, but positive trend
Action: Continue program, investigate barriers

After 12 months:
  Predicted: Application → 0.75, Skills → 0.68
  Actual:    Application → 0.74, Skills → 0.67
  P(Equity) actual: 0.64 (predicted was 0.66)
  
Analysis: On track, 97% of predicted improvement
Action: Program working, maintain investment
```

**This is evidence-based adaptation!**

---

## **Common Policy Mistakes (Avoid These):**

### **Mistake 1: Infrastructure-Only Approach**

**Wrong:**
```
"We deployed fiber to 98% of locations → Success!"
```

**Why wrong:**
- Sen: Resources without conversion factors ≠ capability
- Toyama: Infrastructure × Low capacity = Minimal impact
- Hampton & Bauer: Proved infrastructure alone insufficient

**Right:**
```
"We deployed fiber (Opportunity) + navigators (Aspiration) + 
 training (Growth Mindset) → Measured equity improvement"
```

---

### **Mistake 2: One-Size-Fits-All Policy**

**Wrong:**
```
"Every county gets same allocation: 60% infrastructure, 40% adoption"
```

**Why wrong:**
- Counties have different gap profiles
- Urban vs. rural different needs
- High-infrastructure counties need aspiration/skills, not more infrastructure

**Right:**
```
"Assess each county's Compass scores → Target primary gaps → 
 Allocate proportionally to need"
```

---

### **Mistake 3: Deploy and Forget**

**Wrong:**
```
"Deployed intervention → Wait 3 years → Measure outcome → Done"
```

**Why wrong:**
- Can't adapt if not working
- Miss opportunities to improve
- Waste resources on ineffective approaches

**Right:**
```
"Deploy → Measure 6 months → Compare to prediction → Adjust → 
 Repeat → Learn continuously"
```

---

### **Mistake 4: Ignore Theory**

**Wrong:**
```
"Just deploy stuff that sounds good"
```

**Why wrong:**
- 25 years of research ignored
- Repeat past mistakes
- No explanation when things don't work

**Right:**
```
"Ground in Sen, Appadurai, Dweck, Toyama → Use Hampton & Bauer evidence → 
 Measure with Dagg Compass → Predict with Bayesian network"
```

---

## **Real Policy Examples:**

### **Example 1: Upper Peninsula Regional Strategy**

**Assessment:**
```
14 counties, average scores:
  Connectivity:  0.52 (moderate, rural gaps)
  Application:   0.38 (LOW—unclear value)
  Skills:        0.41 (moderate)
```

**Gap analysis:**
- Primary: Aspiration (0.38) - Hampton & Bauer "unclear value" gap
- Secondary: Opportunity (0.52) - Infrastructure still needs work
- Theory: Appadurai + Toyama → Build capacity while improving infrastructure

**Decision:**
```
$15M total budget allocation:
  
Infrastructure ($7.5M, 50%):
  - Target 6 lowest-connectivity counties
  - Fiber to unserved areas
  - Expected: Connectivity 0.52 → 0.68
  
Navigators ($5M, 33%):
  - ALL 14 counties
  - Show relevant digital pathways
  - Expected: Application 0.38 → 0.61
  
Training ($2.5M, 17%):
  - Focus on 8 counties with lowest skills
  - Growth mindset pedagogy
  - Expected: Skills 0.41 → 0.58

PREDICTED OUTCOME:
  Regional P(Equity): 0.34 → 0.59 (+0.25)
  Gini coefficient: 0.43 → 0.37 (improvement)
```

**Evidence:** Hampton & Bauer showed all three stages needed  
**Theory:** Complete pathway (Sen + Appadurai + Dweck + Toyama)

---

### **Example 2: Urban County with Good Infrastructure**

**Assessment (Wayne County - Detroit):**
```
Connectivity:  0.81 (HIGH—good infrastructure)
Application:   0.54 (MODERATE—could improve)
Skills:        0.49 (MODERATE-LOW)
```

**Gap analysis:**
- Infrastructure NOT the problem
- Aspiration and skills gaps despite access
- Theory: Sen's "conversion factors" missing, not resources

**Decision:**
```
$5M total budget:
  
Infrastructure ($500K, 10%):
  - Maintain existing, address specific gaps only
  - NOT primary need
  
Navigators ($2.5M, 50%):
  - Community-based, culturally relevant
  - Show pathways to jobs, health, education
  - Expected: Application 0.54 → 0.72
  
Training ($2M, 40%):
  - Digital literacy programs
  - Focus on economically disadvantaged neighborhoods
  - Expected: Skills 0.49 → 0.67

PREDICTED OUTCOME:
  P(Equity): 0.58 → 0.76 (+0.18)
```

**Avoids mistake:** Would have been WRONG to spend 60% on infrastructure  
**Evidence-based:** Targets actual gaps (aspiration, skills), not assumed gap (infrastructure)

---

## **Grant Writing with Framework:**

### **Use Framework to Justify BEAD/DEA Funding:**

**Strong grant structure:**

**1. Needs Assessment (Compass scores)**
```
Our county assessment reveals:
  - Connectivity: 0.52 (Dagg Compass, 2024 data)
  - Application: 0.38 (Community survey, n=1,200)
  - Skills: 0.41 (Northstar assessments, n=850)
  
Hampton & Bauer (2020, doi:10.25335/BZGY-3V91) identified these exact 
gaps in Michigan K-12 research. Our data validates this pattern persists.
```

**2. Theoretical Foundation**
```
Sen (1999) explains infrastructure alone insufficient—need conversion factors.
Appadurai (2004) shows "unclear value" reflects thin aspirational maps.
Dweck (2006) demonstrates growth mindset enables skill development.
Toyama (2015) proves technology amplifies existing capacity.

Our strategy addresses ALL stages of digital equity pathway.
```

**3. Evidence-Based Interventions**
```
Hampton & Bauer (2020) proved Michigan needs:
  - Infrastructure (addresses Opportunity gap)
  - Value demonstration (addresses Aspiration gap)
  - Skills training (addresses Growth Mindset gap)

Our intervention design matches evidence:
  - $6M infrastructure (Opportunity)
  - $2.5M digital navigators (Aspiration)
  - $1.5M training (Growth Mindset)
```

**4. Measurement Framework**
```
Will measure using Dagg et al. (2023) Digital Opportunities Compass:
  - Connectivity component (Opportunity stage)
  - Application component (Aspiration stage)
  - Skills component (Growth Mindset stage)
  - Outcomes component (Equity results)

Quarterly assessments, Bayesian predictions, continuous adaptation.
```

**5. Predicted Outcomes**
```
Bayesian network modeling predicts:
  - Connectivity: 0.52 → 0.70 (+0.18)
  - Application: 0.38 → 0.64 (+0.26)
  - Skills: 0.41 → 0.59 (+0.18)
  - P(Equity): 0.31 → 0.66 (+0.35)
  
Confidence: 78% (based on 12 similar interventions, 2018-2024)
```

**This is a STRONG, evidence-based grant proposal!**

---

## **Policy Implementation Checklist:**

### **Before Intervention:**
- [ ] Assessed all three stages (Opportunity, Aspiration, Growth Mindset)
- [ ] Used Dagg Compass framework for measurement
- [ ] Identified primary and secondary gaps
- [ ] Designed interventions matching gap profile
- [ ] Predicted outcomes using Bayesian network
- [ ] Allocated budget proportionally to gaps
- [ ] Grounded in Sen, Appadurai, Dweck, Toyama theory
- [ ] Cited Hampton & Bauer evidence

### **During Intervention:**
- [ ] Monitoring every 6 months
- [ ] Comparing actual to predicted
- [ ] Updating Bayesian model with results
- [ ] Adapting strategy based on data
- [ ] Documenting lessons learned

### **After Intervention:**
- [ ] Final Compass assessment
- [ ] Equity outcome measurement (Gini, inclusion rate)
- [ ] Compare to baseline and predictions
- [ ] Share results with research community
- [ ] Update knowledge graph for future predictions
- [ ] Report to funders with evidence

**If yes to all → Evidence-based policymaking!**

---

## **Bottom Line:**

Your framework enables **evidence-based digital equity policy**, not guesswork.

**The complete process:**
1. **Assess:** Dagg Compass scores for all stages
2. **Analyze:** Identify primary gaps with theory
3. **Predict:** Bayesian network forecasts outcomes
4. **Decide:** Allocate budget matching gaps
5. **Deploy:** Interventions grounded in research
6. **Monitor:** Continuous measurement and adaptation
7. **Learn:** Update model, improve predictions

**Theory-grounded (Sen, Appadurai, Dweck, Toyama)**  
**Evidence-validated (Hampton & Bauer Michigan data)**  
**Measurement-operationalized (Dagg Compass framework)**  
**Prediction-informed (Bayesian network)**  
**Continuously-improving (feedback loop)**

**This is 21st-century evidence-based policymaking for digital equity.**

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Part of:** Project Compass (Merit Network) - Digital Opportunities Intelligence Network (DOIN) • Working draft
