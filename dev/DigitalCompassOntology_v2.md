# Digital Compass Ontology v2: Integrating Theory and Practice

This document represents the **Version 2.0** evolution of the Digital Compass Ontology. It expands the initial operational model (Navigators & Populations) to include the **theoretical foundations** (Sen, Appadurai, Dweck) and the **causal mechanisms** required for the Bayesian Intelligence Network.

## Core Evolution
- **v1:** Who is doing what? (Navigators -> Services -> Populations)
- **v2:** **WHY** does it work? (Interventions -> Theoretical Mechanisms -> Outcomes)

This ontology allows the system to reason: *"The Navigator provides training (Action) which builds Navigation Capacity (Appadurai) and converts Infrastructure (Resource) into Capability (Sen), leading to increased Adoption (Outcome)."*

## Ontology Code (Python/Owlready2)

```python
from owlready2 import *

# Create a new ontology
onto = get_ontology("http://digitalcompass.org/ontology/v2/compass.owl")

with onto:
    # ==========================================
    # 1. CORE ENTITIES (The "Who" and "What")
    # ==========================================
    class Person(Thing): pass
    class Population(Thing): pass
    class Location(Thing): pass
    class Resource(Thing): pass
    
    # ==========================================
    # 2. THEORETICAL DIMENSIONS (The "Why")
    # ==========================================
    class TheoreticalConstruct(Thing): pass
    
    # Sen's Capabilities Approach
    class Capability(TheoreticalConstruct): pass
    class ConversionFactor(TheoreticalConstruct): pass
    class Functioning(TheoreticalConstruct): pass
    
    # Appadurai's Capacity to Aspire
    class Aspiration(TheoreticalConstruct): pass
    class NavigationMap(TheoreticalConstruct): pass
    
    # Dweck's Mindset
    class Mindset(TheoreticalConstruct): pass
    
    # ==========================================
    # 3. OPERATIONAL ENTITIES (The "How")
    # ==========================================
    class Intervention(Thing): pass
    class DigitalNavigator(Person): pass
    class Outcome(Thing): pass

    # ==========================================
    # 4. PROPERTIES (The Relationships)
    # ==========================================
    
    # Causal Relationships (Crucial for Bayesian Network)
    class influences(ObjectProperty):
        domain = [Thing]
        range = [Thing]
        
    class enables(ObjectProperty):
        subproperty_of = influences
        
    class converts_to(ObjectProperty):
        """Sen: Resources + Conversion Factors -> Capability"""
        domain = [Resource, ConversionFactor]
        range = [Capability]

    class thickens_map(ObjectProperty):
        """Appadurai: Interventions thicken the navigational map"""
        domain = [Intervention]
        range = [NavigationMap]

    class fosters_mindset(ObjectProperty):
        """Dweck: Interventions foster growth mindset"""
        domain = [Intervention]
        range = [Mindset]

    # Operational Relationships
    class targets_population(ObjectProperty):
        domain = [Intervention]
        range = [Population]

    class located_in(ObjectProperty):
        domain = [Person, Resource]
        range = [Location]

    # ==========================================
    # 5. INSTANTIATION (The "Vertical Slice")
    # ==========================================
    
    # --- The Context (Location & Population) ---
    baraga_county = Location("BaragaCounty")
    rural_seniors = Population("RuralSeniors")
    
    # --- The Resources (Infrastructure) ---
    broadband_infra = Resource("FiberBroadband")
    broadband_infra.located_in.append(baraga_county)
    
    # --- The Theory (The "Hidden" Variables) ---
    # Sen: The ability to actually USE the internet
    digital_capability = Capability("DigitalCapability")
    
    # Appadurai: The ability to imagine digital futures
    nav_capacity = NavigationMap("DigitalNavigationMap")
    
    # Dweck: The belief in learning
    growth_mindset = Mindset("GrowthMindset")
    
    # --- The Intervention (The Navigator's Work) ---
    # A Navigator Program isn't just "Tech Support"
    # It is a multi-faceted theoretical intervention
    
    navigator_program = Intervention("BaragaNavigatorProgram")
    navigator_program.targets_population.append(rural_seniors)
    
    # The "Why" it works (The Edges):
    # 1. It acts as a Conversion Factor (Sen)
    navigator_program.is_a.append(ConversionFactor)
    navigator_program.converts_to.append(digital_capability)
    
    # 2. It thickens the map (Appadurai)
    navigator_program.thickens_map.append(nav_capacity)
    
    # 3. It fosters mindset (Dweck)
    navigator_program.fosters_mindset.append(growth_mindset)
    
    # --- The Outcome ---
    sustainable_adoption = Outcome("SustainableAdoption")
    
    # The Causal Chain for the Bayesian Network:
    # Capability + Aspiration + Mindset -> Outcome
    digital_capability.influences.append(sustainable_adoption)
    nav_capacity.influences.append(sustainable_adoption)
    growth_mindset.influences.append(sustainable_adoption)

# Save the ontology
onto.save(file="digital_compass_v2.owl")
```

## Detailed Explanation of New Theoretical Classes

### 1. Sen's Capabilities (`Capability`, `ConversionFactor`)
- **Why it's here:** To distinguish between having a connection (Resource) and being able to use it (Capability).
- **Role in AI:** The AI can now understand that giving a laptop (Resource) to a senior without training (Conversion Factor) will result in **Zero Capability**.
- **Bayesian Node:** `P(Capability | Resource, ConversionFactor)`

### 2. Appadurai's Navigation (`NavigationMap`)
- **Why it's here:** To model the "Demand Side" gap. Why don't people sign up even when it's free?
- **Role in AI:** The AI can diagnose "Thin Maps." If infrastructure is high but adoption is low, the system infers a lack of `NavigationMap` and recommends interventions that "show the way" (e.g., success stories, peer modeling).
- **Bayesian Node:** `P(Adoption | Capability, NavigationMap)`

### 3. Dweck's Mindset (`Mindset`)
- **Why it's here:** To model resilience. What happens when the user hits a snag?
- **Role in AI:** The AI tracks `GrowthMindset` as a predictor of long-term retention. High mindset = low churn.
- **Bayesian Node:** `P(Retention | Adoption, Mindset)`

## How This Connects to the "Intelligence" Layer

This ontology provides the **Structure** for the Bayesian Network.

1.  **Nodes:** Every instance of a Class (e.g., `BaragaNavigatorProgram`) becomes a node in the Bayesian graph.
2.  **Edges:** Every Property (e.g., `thickens_map`) becomes a causal link.
3.  **Probabilities:** The "Intelligence" layer learns the strength of these edges from data.
    *   *Example:* How strongly does `BaragaNavigatorProgram` influence `GrowthMindset`? The data (surveys) will tell us, and the Bayesian network will update the probability $P(Mindset | Program)$.

This v2 Ontology transforms the system from a **Directory of Services** into a **Causal Engine for Equity**.
