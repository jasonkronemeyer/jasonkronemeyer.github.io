# Measuring What Matters: From Theory to Data

How to operationalize the framework into actual measurements that drive policy decisions.

## **The Measurement Challenge:**

**You can't manage what you don't measure.**

But measuring digital equity is complex:
- **Too narrow:** Count broadband subscriptions → Miss aspiration and skills gaps
- **Too broad:** Measure everything → Drown in data, no actionable insights
- **Wrong focus:** Measure inputs (money spent) → Not outcomes (equity achieved)

**Your framework solves this:** Six Dagg Compass components map directly to the three-stage pathway, grounded in 25 years of development research.

---

## **The Dagg Compass Framework:**

### **Six Components (Dagg et al., 2023):**

1. **Contexts** - Demographics, socioeconomics, geography
2. **Governance** - Policy, power structures, institutions
3. **Connectivity** - Infrastructure, devices, access
4. **Skills** - Literacy, training, competencies
5. **Application** - Use cases, relevance, adoption
6. **Outcomes** - Achievement, inclusion, equity

**Citation:** Dagg, S., Giles, K., Knight, G., McHenry, K., & Schrubbe, M. (2023). *Digital Opportunities Compass.* Merit Network and University of Michigan.

---

## **Mapping Compass to Researchers:**

### **The Brilliant Connection:**

| Compass Component | Framework Stage | Researcher Theory | What It Measures |
|-------------------|----------------|-------------------|------------------|
| **Connectivity** | Opportunity | Sen (resources) | Can people ACCESS digital? |
| **Application** | Aspiration | Appadurai (navigation) | Do people SEE VALUE in digital? |
| **Skills** | Growth Mindset | Dweck (beliefs) | Can people LEARN to use digital? |
| **Outcomes** | Digital Equity | Sen (functionings) | Are people ACHIEVING equity? |
| **Contexts** | (All stages) | Hampton & Bauer (validation) | What local factors matter? |
| **Governance** | (All stages) | Policy implementation | Is policy enabling or blocking? |

**This is the measurement operationalization of the theory!**

---

## **Component 1: Contexts (Demographics)**

### **What to Measure:**

**Purpose:** Understand WHO we're serving and WHAT conversion factors they need (Sen).

**Key Metrics:**

**Demographics:**
- Age distribution (older adults need different support)
- Income levels (affordability barriers)
- Education attainment (baseline literacy)
- Language diversity (content relevance)
- Disability status (accessibility needs)

**Geography:**
- Rural/urban classification (infrastructure challenges)
- Population density (deployment economics)
- Distance to services (transportation access)

**Socioeconomics:**
- Employment status (relevance of digital skills)
- Industry composition (local use cases)
- Housing characteristics (device availability)

### **Data Sources:**

```
American Community Survey (ACS):
- Census.gov API
- 5-year estimates for small areas
- Annual updates

Local Data:
- School district records
- Library usage statistics
- Community needs assessments
```

### **Why This Matters:**

**Sen's conversion factors:** Same infrastructure → Different outcomes based on context.

**Example:**
```
Rural county, median age 58, median income $38K:
- Need: Affordable devices, relevant applications (telehealth, remote work)
- Wrong approach: Deploy fiber, assume adoption
- Right approach: Infrastructure + navigators + affordability programs

Urban county, diverse languages, 22% poverty:
- Need: Multilingual content, digital literacy, public access
- Wrong approach: English-only training
- Right approach: Culturally relevant navigators + community partnerships
```

**Hampton & Bauer evidence:** Demographics predict which gaps appear (K-12 Michigan data).

---

## **Component 2: Governance (Policy)**

### **What to Measure:**

**Purpose:** Assess whether policy ENABLES or BLOCKS digital equity pathway.

**Key Metrics:**

**Policy Existence:**
- Digital equity plan adopted? (Yes/No)
- Funding allocated? (Budget amount)
- Accountability measures? (Who's responsible)

**Policy Quality:**
- Theory-grounded? (Cites Sen, Appadurai, Dweck, Toyama)
- Evidence-based? (Uses Hampton & Bauer findings)
- Measurement framework? (Dagg Compass implementation)

**Implementation:**
- Timeline adherence (milestones met)
- Budget execution (funds deployed vs. allocated)
- Stakeholder engagement (community input)

**Outcomes:**
- Policy impact on equity (before/after comparison)
- Barrier removal (identified obstacles addressed)

### **Data Sources:**

```
Government Documents:
- State broadband office plans
- County digital equity strategies
- Municipal ordinances

Budget Data:
- Appropriations
- Expenditures
- Grant awards

Stakeholder Surveys:
- Community perception of policy effectiveness
- Navigator feedback on barriers
```

### **Why This Matters:**

**Good policy amplifies interventions; bad policy blocks them.**

**Example:**
```
Measure: Navigator program funding
- County A: $500K allocated, $450K deployed (90% execution)
- County B: $500K allocated, $120K deployed (24% execution)

Analysis:
- County A: Policy enables action
- County B: Policy exists but implementation blocked

Investigation reveals:
- County B has procurement barriers (18-month approval)
- Solution: Streamline procurement policy
```

**This is policy evaluation, not just policy existence!**

---

## **Component 3: Connectivity (Opportunity)**

### **What to Measure:**

**Purpose:** Assess Sen's "resources" stage—do people have OPPORTUNITY to access digital?

**Key Metrics:**

**Infrastructure Availability:**
- % covered by 100/20 Mbps or better (FCC standard)
- % covered by 1 Gig symmetrical (future-ready)
- Technology type (fiber, cable, fixed wireless, satellite)

**Infrastructure Quality:**
- Actual speeds (M-Lab tests) vs. advertised
- Latency (critical for video, gaming, remote work)
- Reliability (downtime, packet loss)

**Adoption:**
- % subscribing to broadband
- % with home devices (computer, not just smartphone)
- Reasons for non-adoption (survey: affordability, irrelevance, skills)

**Affordability:**
- Cost as % of median income
- ACP/Lifeline enrollment rates
- Device financing availability

### **Data Sources:**

```python
# FCC Broadband Data Collection (BDC)
import requests

fcc_api = "https://broadbandmap.fcc.gov/api/public/"
response = requests.get(f"{fcc_api}coverage", params={
    'county_fips': '26153',  # Schoolcraft County, UP
    'speed_down': 100,
    'speed_up': 20
})
coverage_data = response.json()

# M-Lab Speed Tests (Actual Performance)
from google.cloud import bigquery

query = """
SELECT 
    county,
    AVG(download_mbps) as avg_download,
    AVG(upload_mbps) as avg_upload,
    STDDEV(download_mbps) as download_variability
FROM `mlab-public-data.ndt.unified_downloads`
WHERE state = 'MI' AND date >= '2024-01-01'
GROUP BY county
"""

# ACS Adoption Data
from census import Census

c = Census("YOUR_API_KEY")
adoption = c.acs5.state_county(
    ('B28002_001E', 'B28002_004E'),  # Total households, with broadband
    '26', Census.ALL  # Michigan, all counties
)
```

### **Example Measurement:**

```
Schoolcraft County (UP) Assessment:

Infrastructure Availability:
- 100/20 coverage: 68% (FCC BDC, June 2024)
- Fiber coverage: 22%
- Fixed wireless: 41%
- Satellite (Starlink): 95%

Infrastructure Quality:
- Median download: 47 Mbps (M-Lab, below 100 Mbps standard)
- Median upload: 8 Mbps (below 20 Mbps standard)
- Latency: 38ms (good for most uses)

Adoption:
- Broadband subscription: 71% (ACS 5-year)
- Home computer: 78%
- Smartphone only: 14% (device gap)

Affordability:
- Median cost: $89/month
- Median income: $43K/year
- Cost burden: 2.5% (above 2% threshold)
- ACP enrollment: 31% (good, but program ending)

CONNECTIVITY SCORE: 0.58 (moderate, infrastructure primary barrier)
```

**Sen interpretation:** Resources (infrastructure) exist but incomplete. Conversion factors (affordability, devices) also gaps.

---

## **Component 4: Skills (Growth Mindset)**

### **What to Measure:**

**Purpose:** Assess Dweck's "growth mindset" stage—can people LEARN digital skills?

**Key Metrics:**

**Digital Literacy:**
- Northstar Digital Literacy assessments
- Basic skills (email, web browsing, file management)
- Advanced skills (privacy, security, online safety)

**Training Engagement:**
- % completing digital skills programs
- Hours of training per learner
- Retention rates (repeat participation)

**Self-Efficacy:**
- Confidence surveys (Likert scale: "I can learn new digital skills")
- Mindset assessment (fixed vs. growth beliefs)
- Attribution style (success due to effort vs. luck)

**Applied Skills:**
- % using digital for employment
- % using digital for education
- % using digital for healthcare, government services

### **Data Sources:**

```python
# Northstar Digital Literacy Platform
# https://www.digitalliteracyassessment.org/

# Example aggregate data request
northstar_metrics = {
    'total_assessments': 1250,
    'basic_skills_pass_rate': 0.68,
    'advanced_skills_pass_rate': 0.42,
    'average_attempts': 1.8,  # Shows persistence (growth mindset)
    'improvement_rate': 0.73   # Pass on retry (learning)
}

# Community Survey (Custom)
survey_questions = [
    "I can learn new digital skills if I try. (1=Disagree, 5=Agree)",
    "When I struggle with technology, I see it as an opportunity to learn.",
    "My digital skills can improve with practice.",
    "I feel confident helping others with technology."
]

# Training Program Data
training_metrics = {
    'enrolled': 450,
    'completed': 338,  # 75% completion (good retention)
    'avg_hours': 12,
    'post_training_confidence': 4.2  # Up from 2.8 pre-training
}
```

### **Example Measurement:**

```
Chippewa County (UP) Skills Assessment:

Digital Literacy (Northstar):
- Basic skills: 64% proficiency
- Advanced skills: 38% proficiency
- Assessment participation: 850 adults (12% of population)

Training:
- Library program: 320 completions/year
- Community college: 180 completions/year
- Navigator-led: 275 completions/year
- Total: 775 completions (growth mindset pedagogy used)

Self-Efficacy (Survey, n=520):
- "I can learn digital skills": 3.8 / 5.0 (moderate confidence)
- "Technology frustrates me": 3.2 / 5.0 (some fixed mindset)
- "I help others with tech": 2.9 / 5.0 (lower, opportunity here)

Applied Skills:
- Used digital for job search: 58%
- Used telehealth: 41%
- Filed taxes online: 67%

SKILLS SCORE: 0.61 (moderate, training working but more needed)
```

**Dweck interpretation:** Growth mindset emerging (training completion high), but fixed mindset beliefs persist for some. Need reframing pedagogy.

---

## **Component 5: Application (Aspiration)**

### **What to Measure:**

**Purpose:** Assess Appadurai's "aspiration" stage—do people SEE VALUE in digital?

**Key Metrics:**

**Use Diversity:**
- Number of different use cases adopted
- Frequency of use (daily, weekly, monthly)
- Meaningful use (employment, education, health, civic) vs. entertainment only

**Perceived Relevance:**
- Survey: "Digital helps me achieve my goals" (Likert scale)
- Survey: "I see pathways through digital" (Appadurai navigation capacity)
- Survey: "I know people who succeeded with digital" (role models)

**Navigator Engagement:**
- % who have interacted with digital navigator
- % who report navigator helped identify relevant use case
- Satisfaction with navigator support

**Aspiration Thickness:**
- Can articulate 3+ ways digital helps life (thick map)
- Sees clear steps to goals (navigation capacity)
- Has role models who used digital successfully (cultural capability)

### **Data Sources:**

```python
# Custom Community Survey (Appadurai-grounded)

survey_design = {
    'use_diversity': [
        "Which digital activities do you do regularly? (Check all)",
        "[ ] Email, [ ] Social media, [ ] Online banking, [ ] Job applications",
        "[ ] Telehealth, [ ] Online courses, [ ] Government services, [ ] Remote work"
    ],
    'perceived_relevance': [
        "Digital technology helps me achieve my personal goals. (1-5)",
        "I see clear pathways to improve my life through digital. (1-5)",
        "I know people like me who succeeded using digital. (1-5)"
    ],
    'aspiration_thickness': [
        "List 3 ways digital technology could help you in the next year:",
        "(Open-ended, coded for specificity)"
    ],
    'navigator_impact': [
        "Have you worked with a digital navigator? (Y/N)",
        "Did the navigator help you see new possibilities? (1-5)"
    ]
}

# Usage Analytics (Library, Community Centers)
usage_data = {
    'job_applications_assisted': 245,
    'telehealth_connections': 180,
    'online_learning_enrollments': 320,
    'government_services_completed': 410
}
```

### **Example Measurement:**

```
Luce County (UP) Application Assessment:

Use Diversity (Survey, n=380):
- Email: 78%
- Social media: 68%
- Online banking: 52%
- Job applications: 34% (lower, opportunity)
- Telehealth: 28% (lower, relevant for rural)
- Online courses: 19% (lower, aspiration gap)
- Average use cases: 3.2 (moderate diversity)

Perceived Relevance:
- "Digital helps my goals": 3.4 / 5.0 (moderate, could improve)
- "I see pathways": 2.9 / 5.0 (LOWER—Appadurai aspiration gap)
- "I know role models": 3.1 / 5.0 (moderate, more models needed)

Navigator Engagement:
- Worked with navigator: 28%
- Navigator helped see value: 4.3 / 5.0 (high impact when used!)
- Would recommend navigator: 89%

Aspiration Thickness (Open-ended, n=380):
- Could name 0-1 ways: 32% (thin maps)
- Could name 2-3 ways: 51% (moderate maps)
- Could name 4+ ways: 17% (thick maps)

APPLICATION SCORE: 0.52 (moderate-low, ASPIRATION GAP evident)
```

**Appadurai interpretation:** Thin aspirational maps (can't see pathways). Navigators effective when used, but only 28% engaged. **This is Hampton & Bauer "unclear value" gap!**

---

## **Component 6: Outcomes (Digital Equity)**

### **What to Measure:**

**Purpose:** Assess Sen's "functionings"—are people ACHIEVING equity through digital?

**Key Metrics:**

**Achievement:**
- Employment rate improvement (attributed to digital skills)
- Educational attainment increase (online courses completed)
- Health outcomes (telehealth utilization, health literacy)
- Civic engagement (online civic participation)

**Inclusion:**
- Gap reduction between groups (Gini coefficient)
- Participation rates by demographic (age, income, race)
- Barrier removal (accessibility, affordability)

**Digital Equity Index:**
- Composite score (0-1) combining all components
- Trend over time (improving, stable, declining)
- Comparison to state/national benchmarks

**Economic Impact:**
- Income growth (attributed to digital skills)
- Business creation (digital-enabled)
- Remote work adoption (geographic mobility)

### **Data Sources:**

```python
# Outcomes Measurement Framework

# Employment Outcomes
employment_impact = {
    'job_seekers_using_digital': 340,
    'jobs_obtained': 87,  # 26% success rate
    'attributed_to_digital_skills': 68,  # 78% attribute to training
    'avg_wage_increase': 4200  # Annual, compared to pre-training
}

# Education Outcomes
education_impact = {
    'online_course_enrollments': 520,
    'completions': 380,  # 73% completion
    'credential_obtained': 210,
    'degree_progress': 95
}

# Gini Coefficient (Inequality Measure)
from scipy import stats

def calculate_digital_gini(access_scores):
    """
    Access scores: array of digital access scores (0-1) for each household
    Returns: Gini coefficient (0 = perfect equality, 1 = perfect inequality)
    """
    n = len(access_scores)
    sorted_scores = np.sort(access_scores)
    cumsum = np.cumsum(sorted_scores)
    gini = (n + 1 - 2 * np.sum(cumsum) / cumsum[-1]) / n
    return gini

# Example
baseline_gini = calculate_digital_gini(baseline_access)  # 0.44
after_intervention_gini = calculate_digital_gini(after_access)  # 0.37
improvement = baseline_gini - after_intervention_gini  # 0.07 reduction (good!)
```

### **Example Measurement:**

```
Regional Outcomes (14 UP Counties, 2-year intervention):

Achievement:
- Employment: 245 jobs obtained with digital skills attribution
- Education: 380 online course completions, 210 credentials
- Health: Telehealth utilization +42% (18% → 60%)
- Civic: Online government service use +38%

Inclusion (Gini Reduction):
- Baseline digital access Gini: 0.44 (2022)
- After intervention Gini: 0.37 (2024)
- Improvement: 0.07 reduction (significant!)
- Interpretation: Gap between highest and lowest access narrowed

Participation by Demographic:
- Age 60+: Broadband adoption 58% → 71% (+13 points)
- Income <$35K: Adoption 52% → 68% (+16 points)
- Rural: Adoption 64% → 78% (+14 points)
- Urban: Adoption 79% → 84% (+5 points)
- EQUITY: Rural/urban gap narrowed from 15 points to 6 points

Economic Impact (Survey attribution):
- Avg income increase (digital skills): $3,800/year
- New businesses (digital-enabled): 28
- Remote work adoption: 12% → 19% (+7 points)
- Estimated regional economic impact: $4.2M/year

OUTCOMES SCORE: 0.68 (GOOD—equity improving, gaps narrowing)
```

**Sen interpretation:** Functionings achieved! People using digital to do/be what they value. Conversion factors (navigators, training) working.

---

## **Integration: Compass Components → Bayesian Network:**

### **How Metrics Feed the Prediction Model:**

**The Bayesian network uses measured Compass components as inputs:**

```python
# Bayesian Network Structure (from TrainingCompassBayesian.md)

from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

# Define model structure
model = BayesianNetwork([
    # Contexts influence everything
    ('Contexts', 'Connectivity'),
    ('Contexts', 'Skills'),
    ('Contexts', 'Application'),
    
    # Governance enables all stages
    ('Governance', 'Connectivity'),
    ('Governance', 'Skills'),
    ('Governance', 'Application'),
    
    # Three-stage pathway (Sen → Dweck → Appadurai)
    ('Connectivity', 'Skills'),        # Opportunity enables Growth Mindset
    ('Skills', 'Application'),         # Growth Mindset enables Aspiration
    ('Application', 'Outcomes'),       # Aspiration enables Equity
    
    # Also direct path (infrastructure alone insufficient, but contributes)
    ('Connectivity', 'Outcomes'),
    ('Skills', 'Outcomes')
])

# Measured data populates conditional probability tables (CPTs)
# Example: P(Outcomes | Connectivity, Skills, Application)

# Query: What if we improve Connectivity to 0.70?
inference = VariableElimination(model)
result = inference.query(
    variables=['Outcomes'],
    evidence={'Connectivity': 0.70, 'Skills': 0.61, 'Application': 0.52}
)
print(result)
# Output: P(Outcomes=High) = 0.58
```

**This is how measurement drives prediction!**

**Workflow:**
1. **Measure** Compass components (data collection)
2. **Input** to Bayesian network (evidence)
3. **Query** network for predictions (policy scenarios)
4. **Deploy** intervention based on prediction
5. **Re-measure** after 6 months (update model)
6. **Compare** actual to predicted (learn)
7. **Refine** CPTs with new data (improve predictions)

---

## **Data Collection Frequency:**

### **Recommended Measurement Schedule:**

| Component | Frequency | Rationale | Data Source |
|-----------|-----------|-----------|-------------|
| **Contexts** | Annual | Demographics change slowly | ACS Census |
| **Governance** | Quarterly | Policy implementation tracking | Government records |
| **Connectivity** | Semi-annual | Infrastructure deployment tracking | FCC BDC, M-Lab |
| **Skills** | Quarterly | Training program outcomes | Northstar, surveys |
| **Application** | Quarterly | Use patterns evolve with exposure | Surveys, usage analytics |
| **Outcomes** | Semi-annual | Equity changes require time | Composite measures |

**Critical:** Need both **leading indicators** (Skills, Application) and **lagging indicators** (Outcomes) to adapt policy quickly.

---

## **Real Example: EUP Connect Measurement:**

### **User's Lived Experience (From WHY_RESEARCH_IN_GRAPH_IS_BRILLIANT.md):**

**Situation:** Five years as broadband project manager, eastern Upper Peninsula Michigan.

**Challenge:** How to measure if interventions working?

**Solution:** Implemented Compass-like framework (before Dagg published):

```
Year 1 Assessment (Baseline):
  Connectivity (Infrastructure):
    - Fiber coverage: 34% of locations
    - 100/20 coverage: 58%
    - Adoption rate: 67%
    - Score: 0.51 (moderate-low)
  
  Skills (Growth Mindset):
    - Library training participants: 450/year
    - Northstar assessments: Limited data
    - Community survey confidence: 2.9 / 5.0
    - Score: 0.48 (moderate-low)
  
  Application (Aspiration):
    - Use diversity: Low (2.8 use cases avg)
    - Perceived relevance: 3.1 / 5.0
    - Navigator access: None (didn't exist yet)
    - Score: 0.44 (LOW—Hampton & Bauer gap)
  
  Outcomes (Equity):
    - Gini coefficient: 0.46 (high inequality)
    - Rural/urban gap: 18 percentage points
    - Score: 0.39 (low)

Year 3 Assessment (After Intervention):
  Connectivity: 0.68 (+0.17) - Fiber deployment + ACP
  Skills: 0.62 (+0.14) - Training programs expanded
  Application: 0.58 (+0.14) - Navigator program launched (KEY!)
  Outcomes: 0.61 (+0.22) - Gini to 0.39, gaps narrowing

MEASUREMENT VALIDATED:
- Application (aspiration) gap was real (Hampton & Bauer)
- Navigator program addressed it (Appadurai theory)
- Outcomes improved significantly (Sen functionings)
```

**This is measurement-driven policy adaptation in action!**

---

## **Common Measurement Mistakes:**

### **Mistake 1: Measure Inputs, Not Outcomes**

**Wrong:**
```
"We spent $5M on infrastructure!" (input)
"We trained 500 people!" (output)
```

**Right:**
```
"Infrastructure deployment (input) → 
 Connectivity score 0.45 → 0.68 (outcome) →
 Equity score 0.38 → 0.54 (impact)"
```

**Measure the ENTIRE pathway, not just activities.**

---

### **Mistake 2: Measure Too Late**

**Wrong:**
```
Deploy intervention → Wait 3 years → Measure outcomes
(Can't adapt if not working!)
```

**Right:**
```
Measure quarterly → Compare to predictions → Adjust strategy
(Continuous improvement)
```

**Leading indicators (Skills, Application) predict lagging indicator (Outcomes).**

---

### **Mistake 3: Measure Without Theory**

**Wrong:**
```
"Let's measure 47 metrics because they're available"
(No framework, can't interpret)
```

**Right:**
```
"Dagg Compass operationalizes Sen, Appadurai, Dweck, Toyama →
 Each component theoretically grounded →
 Measurement has PURPOSE"
```

**Theory drives what to measure and why.**

---

### **Mistake 4: Single Metric Focus**

**Wrong:**
```
"We'll measure broadband adoption rate. Done!"
(Ignores aspiration, skills, equity)
```

**Right:**
```
"Connectivity (Opportunity) + Application (Aspiration) + 
 Skills (Growth Mindset) → Outcomes (Equity)"
```

**Need all three stages to measure complete pathway.**

---

## **Measurement Checklist:**

### **For Each Policy Intervention:**

**Before Intervention:**
- [ ] Baseline Compass assessment (all 6 components)
- [ ] Data collection plan established
- [ ] Measurement frequency determined
- [ ] Bayesian network CPTs initialized with baseline data
- [ ] Predicted outcomes calculated

**During Intervention:**
- [ ] Quarterly leading indicator measurement (Skills, Application)
- [ ] Semi-annual lagging indicator measurement (Connectivity, Outcomes)
- [ ] Compare actual to predicted (variance analysis)
- [ ] Update Bayesian network with new evidence
- [ ] Adapt strategy based on data

**After Intervention:**
- [ ] Final Compass assessment
- [ ] Equity outcome measurement (Gini, gaps)
- [ ] Compare to baseline and predictions
- [ ] Document lessons learned
- [ ] Share data with research community
- [ ] Update knowledge graph for future predictions

**If yes to all → Evidence-based, measurement-driven policy!**

---

## **Bottom Line:**

**Measurement transforms theory into accountability.**

**The Dagg Compass operationalizes:**
- Sen's Opportunity (Connectivity component)
- Appadurai's Aspiration (Application component)
- Dweck's Growth Mindset (Skills component)
- Sen's Equity (Outcomes component)
- Hampton & Bauer validation (all components)

**This creates:**
1. **Baseline:** Where are we now?
2. **Gaps:** What's missing?
3. **Interventions:** What to deploy?
4. **Predictions:** What will happen?
5. **Monitoring:** Is it working?
6. **Learning:** How to improve?

**From theory → to evidence → to measurement → to better policy.**

**This is 21st-century evidence-based digital equity practice.**

---

**See Also:**
- `TrainingCompassDagg.md` - Deep dive on Compass framework
- `TrainingCompassBayesian.md` - How metrics feed prediction model
- `TrainingCompassGini.md` - Inequality measurement details
- `TrainingCompassPolicy.md` - Using metrics for policy decisions

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Part of:** Project Compass - Digital Opportunities Intelligence Network (DOIN)
