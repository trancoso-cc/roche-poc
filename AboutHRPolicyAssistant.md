# Asset 2 — HR Policy Assistant

Roche AI Control Tower demo, 28 August 2026. Three documents. **No traces** — the system is not agentic, and the finding is detectable from documents alone. That contrast with Asset 1 is the point.

## Contents

| File | Version | Effective | What it establishes |
|---|---|---|---|
| `RO-HR-PA-FDD-001 Functional Design Document.docx` | 2.0 | 20 Feb 2026 | Scope exclusions, refusal rules FR-05 and FR-06, and the **conditional** EU AI Act limited-risk classification. Works council consultation in six jurisdictions concluded on this scope. |
| `RO-HR-PA-TDD-001 Technical Design Document.docx` | 2.0 | 27 Feb 2026 | GPT-5.4, Azure OpenAI Sweden Central. Prompt store released independently of the application. §9.1 accepts the risk that a prompt release can change what the system will do, with no technical control and no automated detection. |
| `RO-HR-PA-PDS-001 Prompt Design Specification.docx` | **1.3** | **04 Aug 2026** | The finding. Versioned independently of the design set. |

## The finding

Detectable entirely from documents. No runtime evidence is required, and none exists.

**The chain, in four steps:**

1. **FDD §1.3 and §5** exclude assessment of an individual employee and any manager-directed task about a named employee, enforced by refusal rules FR-05 and FR-06.
2. **FDD §6.1** states the limited-risk classification and says in terms that it holds *only while those exclusions remain in force*. Annex III point 4 (b) is marked not applicable *because of* FR-05 and FR-06.
3. **PDS §4** shows the individual-assessment refusal rule was **removed at v1.2**, and a new rule added permitting questions about another employee where the requester is that employee's manager.
4. **PDS §3.1** shows what replaced it: eleven MGR exemplars including performance review drafting, competency comparison between two named team members, performance improvement plan language, calibration summarisation and underperformance talking points.

**The system is now within EU AI Act Annex III point 4 (b) and is high-risk. Nobody reclassified it.**

Three corroborating signals in the same document:

- **PDS §7.1** — the GR-05 assessment column reads *Not performed* against both v1.2 and v1.3.
- **PDS §6** — no acceptance criteria exist for MGR responses at all, and AC-04 was last evaluated against the v1.1 scope definition, which predates the removal.
- **PDS §7.2** — four open items, two referred to the HR governance board in June and still open in August.

Secondary exposure: works council consultation in all six jurisdictions concluded on the pre-v1.2 scope (FDD §2.3). A change of this kind re-opens the co-determination obligation in every one.

## Why the documents read as honest rather than contrived

TDD §9.1 states plainly that scope is enforced by prompt content and not by code, that a prompt release can therefore extend the range of tasks with no application change, and that no automated control will detect it. The risk was accepted on 27 February with a purely procedural compensating control — GR-05, plus the requirement that the PDS record its own revision history "so that such a change is visible on inspection."

That is exactly what happened, and exactly how the platform finds it. The design predicted the failure mode; the governance process didn't catch it.

## Contrast with Asset 1

| | Medical Information Agent | HR Policy Assistant |
|---|---|---|
| Architecture | Agentic, orchestrator + sub-agents | Not agentic, single request path |
| Evidence | Four MLflow v3 trace files | Three documents, no traces |
| Detection | Runtime span attributes | Document cross-reference |
| Demo beat | Detect runtime drift | Detect documentation drift |

## Notes for review

- **Tables of contents render empty until opened in Word.** Word prompts to update on open; or Ctrl+A then F9.
- **Highlighted rows** (pale red) mark the rows that carry the finding: the manager-permitted refusal rule, the AC-04 and "Not defined" evaluation rows, the v1.2 and v1.3 revision entries, and the open items.
- **Not yet produced:** Requirements (RO-HR-PA-REQ-001) and DPIA (RO-HR-PA-DPIA-001). All three documents reference both by number. The DPIA is the stronger of the two to add next — it would carry the works council records and the Article 35 position that the reclassification also disturbs.
