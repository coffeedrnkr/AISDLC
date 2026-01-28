# Architecture Impact Assessment Prompt

## Purpose
Focused assessment of how a requirement change affects architecture.

## When to Use
- Technical design decision
- Non-functional requirement change
- Integration changes
- Technology selection

## Prompt Template

```
Assess the architecture impact of this change:

## Change Description
[Describe the requirement change]

## Current Architecture
[Provide or reference: C4 diagrams, component docs, data model, OpenAPI specs]

## Output Required
1. **Components Affected**
   - Existing components that need modification
   - Severity of changes (minor/major)
   
2. **New Components Needed**
   - New services/modules required
   - Integration points
   
3. **Interface Changes**
   - API changes (endpoints, contracts)
   - Internal interface changes
   - External interface changes
   
4. **Data Model Changes**
   - Schema modifications
   - Migration needed?
   - Backward compatibility?
   
5. **Non-Functional Implications**
   - Performance impact
   - Scalability considerations
   - Security implications
   - Reliability/availability
   
6. **ADRs Needed**
   - What decisions need to be documented?
   - What alternatives should be evaluated?
   
7. **Artifacts to Update**
   - C4 diagrams
   - OpenAPI specs
   - DBML
   - Other docs
```

## Example Input

```
Change: Add real-time notifications for claim status changes

Current Architecture:
- Monolithic API server (ClaimsService)
- PostgreSQL database
- React frontend
- No current push notification capability
```

## Example Output

```
ARCHITECTURE IMPACT ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OVERALL IMPACT: 🔴 HIGH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This requires new infrastructure and integration patterns.

COMPONENTS AFFECTED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Component | Change | Severity |
|:----------|:-------|:---------|
| ClaimsService | Add event publishing | 🟡 Moderate |
| Frontend | Add WebSocket client | 🟡 Moderate |

NEW COMPONENTS NEEDED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 NotificationService (NEW)
   - WebSocket server
   - Notification routing
   - User connection management

📦 MessageBroker (NEW - Infrastructure)
   - Pub/Sub for claim events
   - Options: Redis Pub/Sub, Cloud Pub/Sub, Kafka

INTERFACE CHANGES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

API Changes:
  🔗 GET /notifications/subscribe (WebSocket)
  🔗 GET /notifications (REST fallback)

Internal:
  🔗 ClaimsService → MessageBroker (event publishing)
  🔗 MessageBroker → NotificationService (event consuming)

DATA MODEL CHANGES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Table | Change |
|:------|:-------|
| notifications | NEW - Store notification history |
| user_preferences | ADD column: notification_settings |

Migration: Yes, backward compatible (additive only)

NON-FUNCTIONAL IMPLICATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ Performance: WebSocket connections add server load
📈 Scalability: Need connection load balancing
🔒 Security: WebSocket auth required
💾 Reliability: Message delivery guarantees needed

ADRs NEEDED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ADR-012: Message Broker Selection
   Options: Redis Pub/Sub vs Cloud Pub/Sub vs Kafka
   Factors: Scale, cost, operational complexity

2. ADR-013: Notification Delivery Guarantee
   Options: At-least-once vs At-most-once
   Factors: User experience, complexity

ARTIFACTS TO UPDATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  📝 C4-context.md - Add NotificationService
  📝 C4-container.md - Add MessageBroker, NotificationService
  📝 C4-component.md - Detail NotificationService internals
  📝 openapi.yaml - Add /notifications endpoints
  📝 schema.dbml - Add notifications table
```

## Follow-Up Actions
1. Review architecture impact with tech lead
2. Create ADRs for key decisions
3. Update architecture diagrams
4. Estimate implementation effort
