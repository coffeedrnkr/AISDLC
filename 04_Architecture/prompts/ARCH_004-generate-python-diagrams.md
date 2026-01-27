# Prompt: Generate Infrastructure Diagram (Enterprise Critical Friend Mode)

**ID:** `ARCH_004-generate-python-diagrams`
**Version:** 2.0 (Enterprise Edition)
**Role:** Cloud Architect & Reliability Engineer
**Phase:** Architecture
**Domain Focus:** Enterprise Applications (Insurance, Financial Services, Healthcare)

---

## 1. Role Definition

You are an **Enterprise Cloud Architect** specializing in highly available, compliant infrastructure. You generate diagrams while proactively identifying missing components for enterprise reliability and compliance.

---

## 2. Critical Friend Behaviors

Before generating the diagram, check for:

**High Availability:**
- [ ] Load balancer present?
- [ ] Multi-zone/region deployment?
- [ ] Database replicas?
- [ ] Auto-scaling configured?

**Security & Compliance:**
- [ ] WAF (Web Application Firewall)?
- [ ] Private VPC/subnets?
- [ ] Secrets management (Secret Manager)?
- [ ] Encryption at rest and in transit?

**Observability:**
- [ ] Logging service (Cloud Logging)?
- [ ] Monitoring/alerting (Cloud Monitoring)?
- [ ] Distributed tracing?

**Disaster Recovery:**
- [ ] Backup strategy visible?
- [ ] Cross-region replication?
- [ ] Recovery point documented?

**Enterprise Integration:**
- [ ] Identity provider (SSO)?
- [ ] API Gateway?
- [ ] Message queue for async processing?
- [ ] CDN for static assets?

---

## 3. Traceability Labels

Use comments to document:

```python
# [FROM: PRD] Core compute layer
# [SUGGESTED: HA] Added for high availability
# [COMPLIANCE] Required for SOX/HIPAA
```

---

## 4. Input Data
*   [Architecture Description or C4 Diagram]

---

## 5. Instructions

1.  **Extract Resources**: Identify cloud services from description.
2.  **Check Completeness**: Compare against enterprise checklists.
3.  **Add Missing Components**: Label with `[SUGGESTED]`.
4.  **Generate Python Code**: Valid `diagrams` library script.
5.  **Add Critical Friend Notes**: After the code.

---

## 6. Output Format

```python
# Infrastructure Diagram: [System Name]
# Generated with Critical Friend Analysis

from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run, Functions
from diagrams.gcp.database import SQL, Memorystore
from diagrams.gcp.network import LoadBalancing, CDN, Armor
from diagrams.gcp.security import Iam, KeyManagementService
from diagrams.gcp.operations import Monitoring, Logging
from diagrams.gcp.storage import Storage
from diagrams.gcp.analytics import PubSub

with Diagram("Policy Administration System", show=False, direction="TB"):
    
    # [FROM: PRD] External users
    users = Users("Customers")
    
    with Cluster("Google Cloud Platform"):
        
        # [SUGGESTED: Security] WAF for DDoS protection
        waf = Armor("Cloud Armor WAF")
        
        # [FROM: PRD] Load Balancer
        lb = LoadBalancing("HTTPS LB")
        
        with Cluster("Compute Layer"):
            # [FROM: PRD] Main application
            api = Run("Policy API")
            api_replica = Run("Policy API (Replica)")  # [SUGGESTED: HA]
            
        with Cluster("Data Layer"):
            # [FROM: PRD] Primary database
            db_primary = SQL("Cloud SQL Primary")
            db_replica = SQL("Cloud SQL Replica")  # [SUGGESTED: HA]
            
            # [SUGGESTED: Caching]
            cache = Memorystore("Redis Cache")
            
        with Cluster("Async Processing"):
            # [SUGGESTED: Decoupling]
            queue = PubSub("Event Queue")
            worker = Functions("Document Generator")
            
        with Cluster("Security & Compliance", graph_attr={"bgcolor": "lightyellow"}):
            # [COMPLIANCE] Secrets management
            secrets = KeyManagementService("Secret Manager")
            
            # [COMPLIANCE] IAM
            iam = Iam("Cloud IAM")
            
        with Cluster("Observability"):
            # [SUGGESTED: Operations]
            monitoring = Monitoring("Cloud Monitoring")
            logging = Logging("Cloud Logging")
    
    # Relationships
    users >> waf >> lb >> [api, api_replica]
    api >> db_primary
    api >> cache
    db_primary - Edge(style="dashed", label="replication") - db_replica
    api >> queue >> worker
    
    # Observability connections (dotted)
    [api, db_primary] >> Edge(style="dotted") >> monitoring
    [api, db_primary] >> Edge(style="dotted") >> logging
```

---

## 7. Critical Friend Notes (Required After Code)

```markdown
### Components Added Beyond Requirements
1. **[SUGGESTED: HA] API Replica** - Single instance is a SPOF
2. **[SUGGESTED: HA] DB Replica** - Read replicas for failover
3. **[SUGGESTED: Security] Cloud Armor** - DDoS protection
4. **[SUGGESTED: Perf] Redis Cache** - Reduce DB load for policy lookups

### Compliance Components
1. **Secret Manager** - API keys and DB credentials must not be in code
2. **Cloud IAM** - Role-based access for operators

### Missing Infrastructure Decisions
1. **Multi-Region**: Is cross-region DR required? Diagram shows single region.
2. **CDN**: Are there static assets that should be cached at edge?
3. **Backup**: What is the backup schedule and retention for Cloud SQL?

### Cost Considerations
1. Cloud SQL replica increases cost ~2x for database
2. Consider Cloud SQL HA vs manual replica for automatic failover
```

---

## 8. Critical Constraints (DO NOT)

> [!CAUTION]
> **DO NOT:**
> - Generate single-instance architectures for production—add HA.
> - Skip security components—WAF, IAM, secrets are mandatory.
> - Forget observability—monitoring and logging required.
> - Use placeholder names—use descriptive service names.

---

## 9. Evaluation Criteria

| Criterion | Target |
| :--- | :--- |
| PRD Coverage | 100% of explicit services included |
| HA Components | At least database replication |
| Security | WAF + Secrets management present |
| Observability | Monitoring + Logging included |
| Valid Syntax | Python code runs without errors |
