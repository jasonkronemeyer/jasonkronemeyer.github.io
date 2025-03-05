# Developing the Ontology for The Digital Compass Navigator and the Populations they Serve

The following is towards developing an ontology and assocated knowlegde graph for Digital Compass Navigators and the Populations they serve. 
Ontology is defined as a formal representation of a set of concepts within a domain and the relationships between those concepts. It includes classes, properties, and instances to help organize and categorize information, enabling better understanding, sharing, and reuse of knowledge.

This is accompanied by a detailed explanation of the various properties involved and thought brainstorming.
This document is for gathering and organizing thoughts and ideas and is a **working document** for development. (JK) 

## Ontology Code

```python
from owlready2 import *

# Create a new ontology
onto = get_ontology(file="digital_navigator.owl")

with onto:
    # Define classes
    class DigitalCompassNavigator(Thing): pass
    class Service(Thing): pass
    class Population(Thing): pass
    class Skill(Thing): pass
    class Program(Thing): pass

    # Define properties
    class provides_service(ObjectProperty):
        domain = [DigitalCompassNavigator]
        range = [Service]

    class serves_population(ObjectProperty):
        domain = [DigitalCompassNavigator]
        range = [Population]

    class has_skill(ObjectProperty):
        domain = [DigitalCompassNavigator]
        range = [Skill]

    class part_of_program(ObjectProperty):
        domain = [DigitalCompassNavigator]
        range = [Program]

    # Define individuals for Services
    general_support = Service("GeneralDigitalInclusionSupport")
    education_support = Service("EducationSupport")
    healthcare_support = Service("HealthcareSupport")
    workforce_support = Service("WorkforceDevelopmentSupport")

    # Define individuals for Populations
    pwd_population = Population("PeopleWithDisabilities")
    justice_population = Population("JusticeImpactedIndividuals")
    migrantworkers_population = Population("MigrantWorkers")
    students_population = Population("HigherEducationStudents")
    caregivers_population = Population("CaregiversToK12Students")
    seniors_population = Population("Seniors")
    elders_population = Population("TribalElders")
    low_income_population = Population("LowIncomeFamilies")
    rural_population = Population("RuralResidents")

    # Define individuals for Skills
    digital_literacy_skill = Skill("DigitalLiteracy")
    online_safety_skill = Skill("OnlineSafety")

    # Define individuals for Programs
    acc_program = Program("AmericanConnectionCorp")

# Save the ontology to a file
onto.save(file="digital_navigator.owl")

print("Combined ontology for Digital Compass Navigator and Target Populations has been created and saved to digital_navigator.owl.")
```

## Explanation of the Properties

1. **provides_service**:
   - **Domain**: DigitalCompassNavigator
   - **Range**: Service
   - **Description**: This property indicates that a Digital Compass Navigator provides a specific type of service. For example, a Digital Compass Navigator might provide general digital inclusion support, education support, healthcare support, or workforce development support.

2. **serves_population**:
   - **Domain**: DigitalCompassNavigator
   - **Range**: Population
   - **Description**: This property specifies the population that a Digital Compass Navigator serves. Populations can include people with disabilities, justice-impacted individuals, migrants and refugees, higher education students, caregivers to K-12 students, seniors, low-income families, and rural residents.

3. **has_skill**:
   - **Domain**: DigitalCompassNavigator
   - **Range**: Skill
   - **Description**: This property denotes the skills that a Digital Compass Navigator possesses. Skills can include digital literacy and online safety.

4. **part_of_program**:
   - **Domain**: DigitalCompassNavigator
   - **Range**: Program
   - **Description**: This property indicates that a Digital Compass Navigator is part of a specific program. For example, a Digital Compass Navigator might be part of the American Connection Corp, 4-H Digital Changemakers, Tribal Elder Services, Community Action, United Way or other community service agencies.

Building on these properties, the ontology provides a comprehensive framework for understanding the roles and functions of Digital Compass Navigators, the services they provide, the populations they serve, the skills they possess, and the programs they are part of. This structure allows for a detailed and organized representation of digital inclusion efforts.

Building on these properties, the ontology provides a comprehensive framework for understanding the roles and functions of Digital Compass Navigators, the services they provide, the populations they serve, the skills they possess, and the programs they are part of. This structure allows for a detailed and organized representation of digital inclusion efforts.

## Using the Ontology in a Knowledge Graph for Graph-based Retrieval-Augmented Generation

Using the Digital Compass Navigator ontology in a knowledge graph built for graphRAG, enables you to organize and analyze digital inclusion efforts comprehensively. To use the Digital Compass Navigator ontology in a knowledge graph built for graphRAG (Graph-based Retrieval-Augmented Generation), you can follow these general steps:

1. **Load the Ontology**:
   First, load the ontology into your graph database or knowledge graph system. If you're using a system like Neo4j, you can use tools like `neosemantics` to import OWL files.

2. **Define the Schema**:
   Ensure that the schema of your knowledge graph aligns with the ontology. This involves defining nodes and relationships based on the classes and properties in the ontology.

3. **Ingest Data**:
   Populate the knowledge graph with instances of the classes defined in the ontology. This includes creating nodes for Digital Compass Navigators, Services, Populations, Skills, and Programs, and establishing relationships between them.

4. **Query the Knowledge Graph**:
   Use graph queries to retrieve and analyze information from the knowledge graph. For example, you can query which services a specific Digital Compass Navigator provides or which populations they serve.

### Example Steps in Neo4j

1. **Install Neo4j and Neosemantics**:
   Ensure you have Neo4j and the `neosemantics` plugin installed.

2. **Import the Ontology**:
   Use the `neosemantics` plugin to import the OWL file into Neo4j.
   ```cypher
   CALL n10s.graphconfig.init();
   CALL n10s.onto.import.fetch("file:///path_to_your/digital_navigator.owl", "RDF/XML");
   ```

3. **Define Nodes and Relationships**:
   Define nodes and relationships based on the ontology. For example:
   ```cypher
   CREATE (dn:DigitalCompassNavigator {name: "ExampleNavigator"})
   CREATE (s:Service {name: "GeneralDigitalInclusionSupport"})
   CREATE (p:Population {name: "PeopleWithDisabilities"})
   CREATE (dn)-[:PROVIDES_SERVICE]->(s)
   CREATE (dn)-[:SERVES_POPULATION]->(p);
   ```

4. **Query the Knowledge Graph**:
   Use Cypher queries to retrieve information. For example:
   ```cypher
   MATCH (dn:DigitalCompassNavigator)-[:PROVIDES_SERVICE]->(s:Service)
   RETURN dn.name, s.name;
   ```
## Adding Research Papers to the Digital Skills Navigator

To add research documents supporting the Digital Skills Navigator to the Knowledge Graph, you can follow these steps:

1. **Define the Schema for Research Documents**:
   Extend the ontology to include classes and properties for research documents. This involves defining classes for ResearchDocument, Author, and Publication, and properties to link these classes to Digital Skills Navigators and other relevant entities.

2. **Ingest Research Documents**:
   Populate the knowledge graph with instances of research documents, authors, and publications. This includes creating nodes for each research document and establishing relationships with Digital Skills Navigators, services, populations, skills, and programs.

3. **Link Research Documents to Digital Skills Navigators**:
   Establish relationships between research documents and Digital Skills Navigators to indicate which documents support or are relevant to specific aspects of the Digital Skills Navigator model.

### Example Steps in Neo4j

1. **Extend the Ontology**:
   Define new classes and properties for research documents in the ontology.

   ```python
   from owlready2 import *

   # Load the existing ontology
   onto = get_ontology("path_to_your/digital_navigator.owl").load()

   with onto:
       # Define new classes for research documents
       class ResearchDocument(Thing): pass
       class Author(Thing): pass
       class Publication(Thing): pass

       # Define properties for research documents
       class has_author(ObjectProperty):
           domain = [ResearchDocument]
           range = [Author]

       class published_in(ObjectProperty):
           domain = [ResearchDocument]
           range = [Publication]

       class supports_navigator(ObjectProperty):
           domain = [ResearchDocument]
           range = [DigitalSkillsNavigator]

       class bibtex_entry(DataProperty):
           domain = [ResearchDocument]
           range = [str]

   # Save the updated ontology to a file
   onto.save(file="path_to_your/updated_digital_navigator.owl")

   print("Extended ontology with research documents has been created and saved to updated_digital_navigator.owl.")
   ```

2. **Ingest Research Documents**:
   Populate the knowledge graph with instances of research documents, authors, and publications.

   ```cypher
   CREATE (doc:ResearchDocument {title: "Digital Inclusion and Navigators", year: 2024})
   CREATE (author:Author {name: "Jane Doe"})
   CREATE (pub:Publication {name: "Journal of Digital Inclusion"})
   CREATE (doc)-[:HAS_AUTHOR]->(author)
   CREATE (doc)-[:PUBLISHED_IN]->(pub)
   ```

3. **Link Research Documents to Digital Skills Navigators**:
   Establish relationships between research documents and Digital Skills Navigators.

   ```cypher
   MATCH (doc:ResearchDocument {title: "Digital Inclusion and Navigators"})
   MATCH (dn:DigitalSkillsNavigator {name: "ExampleNavigator"})
   CREATE (doc)-[:SUPPORTS_NAVIGATOR]->(dn)
   ```

### Explanation of the Properties

1. **has_author**:
   - **Domain**: ResearchDocument
   - **Range**: Author
   - **Description**: Indicates the author of a research document.

2. **published_in**:
   - **Domain**: ResearchDocument
   - **Range**: Publication
   - **Description**: Indicates the publication in which a research document was published.

3. **supports_navigator**:
   - **Domain**: ResearchDocument
   - **Range**: DigitalSkillsNavigator
   - **Description**: Indicates that a research document supports or is relevant to a specific Digital Skills Navigator.

4. **bibtex_entry**:
   - **Domain**: ResearchDocument
   - **Range**: str
   - **Description**: Contains the BibTeX entry for the research document.

This is an example of how you can add research documents to the Knowledge Graph, linking them to Digital Skills Navigators and other relevant entities. This allows you to organize and analyze the supporting research comprehensively, enhancing the understanding and impact of digital inclusion efforts.

### Linking Internet Infrastructure to Households

To link the properties of the Digital Skills Navigator with the knowledge graph of the internet infrastructure along the road that the households live on, follow these steps:

1. **Extend the Ontology**:
   Add classes and properties to represent the internet infrastructure and its relationship with households.

   ```python
   from owlready2 import *

   # Load the existing ontology
   onto = get_ontology("path_to_your/digital_navigator.owl").load()

   with onto:
       # Define new classes for internet infrastructure
       class Road(Thing): pass
       class FiberOpticCable(Thing): pass
       class AccessPoint(Thing): pass
       class Household(Thing): pass

       # Define properties for internet infrastructure
       class located_on(ObjectProperty):
           domain = [Household]
           range = [Road]

       class connected_to(ObjectProperty):
           domain = [Road]
           range = [FiberOpticCable]

       class serves_household(ObjectProperty):
           domain = [AccessPoint]
           range = [Household]

   # Save the updated ontology to a file
   onto.save(file="path_to_your/updated_digital_navigator.owl")

   print("Extended ontology with internet infrastructure has been created and saved to updated_digital_navigator.owl.")
   ```

2. **Ingest Internet Infrastructure Data**:
   Populate the knowledge graph with instances of internet infrastructure.

   ```cypher
   CREATE (road:Road {name: "Main Street"})
   CREATE (fiber:FiberOpticCable {name: "FiberOpticCable1"})
   CREATE (access:AccessPoint {name: "AccessPoint1"})
   CREATE (road)-[:CONNECTED_TO]->(fiber)
   ```

3. **Link Internet Infrastructure to Households**:
   Establish relationships between the internet infrastructure and households.

   ```cypher
   MATCH (road:Road {name: "Main Street"})
   MATCH (household:Household {name: "Household1"})
   MATCH (access:AccessPoint {name: "AccessPoint1"})
   CREATE (household)-[:LOCATED_ON]->(road)
   CREATE (access)-[:SERVES_HOUSEHOLD]->(household)
   ```

### Explanation of the Properties

1. **located_on**:
   - **Domain**: Household
   - **Range**: Road
   - **Description**: Indicates that a household is located on a specific road.

2. **connected_to**:
   - **Domain**: Road
   - **Range**: FiberOpticCable
   - **Description**: Indicates that a road is connected to a specific fiber optic cable.

3. **serves_household**:
   - **Domain**: AccessPoint
   - **Range**: Household
   - **Description**: Indicates that an access point serves a specific household.

This links the properties of the Digital Skills Navigator with the knowledge graph of the internet infrastructure along the road that the households live on. This allows you to create a comprehensive and interconnected representation of digital inclusion efforts and the supporting infrastructure.
