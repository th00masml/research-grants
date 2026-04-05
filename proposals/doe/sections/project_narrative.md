# DOE Project Narrative - Large Language Models for Energy Materials Discovery

## SCIENTIFIC CHALLENGE AND SIGNIFICANCE

The development of new energy materials (batteries, catalysts, solar cells, superconductors) faces critical bottlenecks:

1. **Literature Integration**: Materials science has produced millions of papers; manually synthesizing knowledge is infeasible
2. **Hypothesis Generation**: Discovering novel materials requires combining insights across subfields
3. **Experimental Planning**: Designing optimal experiments requires integrating materials knowledge with computational predictions
4. **Data Analysis**: High-throughput experiments produce massive datasets requiring intelligent analysis

**Solution**: Large language models integrated with computational materials science can accelerate discovery by:
- Synthesizing vast materials literature to identify promising directions
- Generating novel hypotheses combining chemistry, physics, and materials science
- Designing experiments by integrating computational predictions with literature
- Analyzing high-throughput data to extract design principles

---

## RESEARCH OBJECTIVES

### Objective 1: Materials Knowledge Integration

Create integrated LLM/knowledge base system combining:
- Materials databases (ICSD, Materials Project, OQMD)
- Published materials properties and relationships
- Computational predictions (DFT, ML models)
- Experimental characterization data

**Significance**: Enable LLMs to reason over comprehensive materials knowledge, generating novel material designs

### Objective 2: Experiment-Guided Discovery

Develop methods for LLMs to design high-impact experiments by:
- Learning experimental efficiency through literature
- Integrating computational predictions with experimental feasibility
- Recommending next experiments based on existing data
- Suggesting characterization approaches for novel materials

**Significance**: Dramatically increase experimental efficiency in materials discovery

### Objective 3: Scalable Production Assessment

Enable LLMs to assess materials from discovery to deployment:
- Evaluate scalability and manufacturing feasibility
- Estimate costs and environmental impact
- Identify commercialization pathways
- Recommend materials with highest real-world impact

**Significance**: Bridge gap between lab discovery and practical deployment

### Objective 4: Computational Integration

Combine LLMs with domain-specific computational tools:
- First-principles calculations (DFT, DMRG)
- Machine learning models (structure, properties)
- Molecular dynamics and coarse-graining
- Multiscale simulations

**Significance**: Enable reasoning combining empirical knowledge (LLM) and first-principles predictions

---

## TECHNICAL APPROACH

### Phase 1: Materials Knowledge System (Months 1-12)

**Task 1.1: Knowledge Base Integration**
- Integrate Materials Project, ICSD, OQMD databases
- Implement entity resolution matching materials across sources
- Create unified knowledge graph covering:
  * Crystal structures and properties
  * Phase diagrams and stability
  * Functional properties (electronic, thermal, mechanical)
  * Synthesis methods and conditions

**Task 1.2: LLM Materials Specialization**
- Fine-tune open-source LLMs on materials literature (2M+ papers)
- Implement knowledge-grounded decoding using materials graphs
- Develop uncertainty quantification for property predictions
- Create verification against first-principles calculations

**Deliverables**:
- Integrated materials knowledge base
- Fine-tuned materials LLM with open-source release
- Benchmarks comparing LLM predictions to databases

**Metrics**:
- Entity resolution accuracy >95%
- Property prediction RMSE within 10% of database values
- Latency <1 second for discovery queries

---

### Phase 2: Experiment Design System (Months 10-20)

**Task 2.1: Experiment Planning AI**
- Analyze high-throughput experimental databases
- Learn experimental efficiency patterns from literature
- Implement Bayesian optimization for materials discovery
- Develop active learning strategies

**Task 2.2: Computational Integration**
- Interface LLM with Materials Project REST API
- Integrate with local computational resources (VASP, GAUSSIAN)
- Create predictive models combining ML + first-principles
- Implement feedback loops from experiments to models

**Task 2.3: Human-AI Collaboration**
- Design interfaces for materials scientists
- Implement explanation generation for AI recommendations
- Create trust and interpretability mechanisms
- Develop user study validating usability

**Deliverables**:
- Experiment design system (prototype)
- Integration with Materials Project computational APIs
- Validation on retrospective materials discovery cases

**Metrics**:
- 50%+ reduction in experiments needed to discover target properties
- Active learning improvements: 3-5x faster property space exploration
- User study: 80%+ scientist confidence in recommendations

---

### Phase 3: Scaling to Energy Applications (Months 16-36)

**Task 3.1: Battery Materials**
- Focus on high-energy-density cathode materials
- Integrate electrochemistry-specific knowledge
- Develop stability and cycle-life prediction
- Recommend compositional substitutions for improved properties

**Task 3.2: Catalysts for Carbon Capture**
- Integrate catalyst databases (CatHub)
- Implement reaction mechanism understanding
- Develop activity/selectivity prediction
- Suggest novel catalyst architectures

**Task 3.3: Solar Absorbers**
- Focus on halide perovskites and emerging absorbers
- Implement band-gap engineering knowledge
- Develop defect tolerance and stability assessment
- Recommend doping and interface modifications

**Deliverables**:
- Energy-specific materials discovery systems for 3 application areas
- Validation through comparison with experimental literature
- Open-source tools for broader materials community

**Metrics**:
- Identify 5+ novel promising materials in each application area
- Properties match experimental reports with <20% error
- Literature validation: 70%+ of predictions consistent with subsequent publications

---

## INNOVATION

**First Materials LLM System**: Specialized language model trained on materials science literature with integrated knowledge bases

**Materials-Computational Integration**: Novel architecture combining LLM reasoning with first-principles calculations and ML

**Active Learning Materials Discovery**: Combine LLM-based design suggestions with active learning to maximize experimental impact

---

## TEAM AND INSTITUTIONAL SUPPORT

### PI: [Name]
- PhD Materials Science, [X] years research
- Published [Y] papers on materials discovery AI
- Access to [Institution] computational resources

### Key Personnel
- Materials Scientist: Domain expertise in target materials
- Computer Scientist: LLM/AI systems expertise
- Software Engineer: System implementation and deployment

### Institutional Resources
- Access to HPC resources: [Institution] computing clusters
- Materials databases: Direct integration with Materials Project
- Experimental validation: Partnerships with national labs [Lab1, Lab2]

---

## RESULTS AND DELIVERABLES

### Year 1
- Integrated materials knowledge base
- Fine-tuned materials LLM (open-source release)
- Validation benchmarks
- Publication: Materials-LLM integration paper

### Year 2
- Experiment planning system prototype
- Integration with computational infrastructure
- User study with materials scientists
- Publication: Experiment design with AI

### Year 3
- Energy-focused discovery systems (batteries, catalysts, absorbers)
- Validation on retrospective cases
- Field testing at national labs
- Publications: Application papers in each domain
- Open-source tools for community use

---

## IMPACT

### Scientific Impact
- Enable discovery of high-energy-density batteries
- Accelerate carbon-capture catalyst development
- Identify next-generation solar absorbers
- Establish best practices for AI-guided materials discovery

### Economic Impact
- Reduce time-to-discovery for energy materials (2-5x speedup)
- Enable commercialization of promising candidates
- Position US leadership in AI-enabled materials discovery

### Education Impact
- Train PhD students in AI + materials science
- Develop open-source tools for educational use
- Create best practices for human-AI collaboration in science

### National Security
- Accelerate energy technology development
- Reduce dependence on materials imports
- Enable rapid materials prototyping

---

## BUDGET

**Total DOE Funding**: $2,500,000 over 36 months

- **Personnel** ($1,500,000): PI, postdocs, graduate students
- **Computing** ($600,000): HPC allocation, GPU resources
- **Materials/Equipment** ($200,000): Experimental validation
- **Travel** ($100,000): Collaboration with national labs
- **Other Direct** ($100,000): Software, databases, publications
- **Indirect Costs** ($0): No F&A (university cost-share)

---

## COST SHARING

Institution commits:
- $1,000,000 in faculty time (PI) and graduate student support
- $500,000 in computing resources and facilities
- Total cost-share: $1,500,000 (37.5% of total project cost)
