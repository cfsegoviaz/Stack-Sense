# Task List - Application Analysis Workflow

## Task 1: Update JSONs with Tips

### Task 1.1: Add tips to backoffice-banca-digital.json
- [ ] Add tips to lift-shift architecture
- [ ] Add tips to replatform-linux architecture  
- [ ] Add tips to ecs-fargate architecture

### Task 1.2: Add tips to backoffice-sistemas.json
- [ ] Add tips to all architectures

### Task 1.3: Add tips to saras.json
- [ ] Add tips to all architectures

### Task 1.4: Add tips to api-portal.json
- [ ] Add tips to all architectures

### Task 1.5: Add tips to sonarqube.json
- [ ] Add tips to all architectures

---

## Task 2: Create SEQ Showcase JSON

### Task 2.1: Create seq.json
- [ ] Extract data from SEQ_MODERNIZATION.md
- [ ] Create JSON following Application interface
- [ ] Include tips in architectures

### Task 2.2: Update index.json
- [ ] Add SEQ entry to index

---

## Task 3: Create Analysis Prompt Template

### Task 3.1: Create ANALYSIS_PROMPT.md
- [ ] Define input data sources
- [ ] Define output artifacts
- [ ] Define architecture evaluation criteria

---

## Task 4: Update ArchitectureCard for Tips

### Task 4.1: Modify ArchitectureCard.tsx
- [ ] Add collapsible tips section
- [ ] Style consistently with design

---

## Task 5: Create Diagram Templates

### Task 5.1: Create lift_shift_template.py
- [ ] Parametrizable template for Rehost

### Task 5.2: Create ecs_fargate_template.py
- [ ] Parametrizable template for containers

### Task 5.3: Create hybrid_template.py
- [ ] Parametrizable template for hybrid connectivity

---

## Task 6: Validate Effort Matrix

### Task 6.1: Review effort_matrix.json coverage
- [ ] Verify all AWS services have hours
- [ ] Document any gaps

---

## Task 7: Create Batch Analysis Script

### Task 7.1: Create analyze_app.sh
- [ ] Script to create directory structure
- [ ] Output Kiro CLI command to run

---

## Task 8: Analyze Pending Applications

> **Input:** Application name from ANALYSIS_CHECKLIST.md or matriz-aplicaciones-completa.csv
> **Process:** Execute analysis workflow for each pending application

### Task 8.1: Analyze next pending application
- [ ] Get next app from ANALYSIS_CHECKLIST.md (Prioridad 1 first)
- [ ] Extract VM data from vInfo.csv (search by SERVIDORES_APLICACION)
- [ ] Extract metrics from Cloudamize Compute.csv
- [ ] Extract app details from matriz-aplicaciones-completa.csv
- [ ] Generate 3 architecture options with costs (use aws-pricing MCP)
- [ ] Calculate implementation hours from effort_matrix.json
- [ ] **Generate diagrams for each architecture option (use generate_diagram MCP)**
- [ ] Create {APP_NAME}_MODERNIZATION.md
- [ ] Create {app-slug}.json for showcase (include diagramUrl)
- [ ] Update index.json
- [ ] Update ANALYSIS_CHECKLIST.md (mark as ✅)
- [ ] Update INDEX.md
- [ ] Copy diagrams to showcase public/diagrams/

### Diagram Generation Guidelines

**Required for each architecture option:**
```python
# Template structure - use these icons:
# Users, EC2, ELB, RDS, S3, Lambda, ECS, VPN, TraditionalServer

with Diagram("AppName - OptionName", show=False, direction="LR"):
    users = Users("Usuarios")
    
    with Cluster("On-Premise"):
        onprem = TraditionalServer("AD/Legacy")
    
    with Cluster("AWS Cloud"):
        with Cluster("VPC"):
            lb = ELB("ALB")
            compute = EC2("EC2") # or ECS, Lambda
            db = RDS("Database")
        vpn = VPN("VPN")
    
    users >> lb >> compute >> db
    compute >> vpn >> onprem
```

**Output paths:**
- Source: `modernization-proposals/{app-slug}/diagrams/generated-diagrams/`
- Showcase: `apps/stack-sense-showcase/public/diagrams/`
