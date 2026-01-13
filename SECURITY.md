# 🛡️ Security Policy: Emergent Prompt Architecture (EPA)

> **"Security is not a barrier; it is the immune system of the Ontological Lattice."**

The Emergent Prompt Architecture (EPA) is a generative AI system designed to assemble logic dynamically. Because it modifies its own prompts based on user input and internal state, it faces unique security vectors not present in static software. We take these threats—specifically **Prompt Injection**, **Ontological Poisoning**, and **Semantic Drift**—extremely seriously.

---

## **1. Reporting a Vulnerability**

**Do not open public GitHub issues for security vulnerabilities.**

If you discover a vulnerability, please report it via encrypted email to:
`security@emergent-prompt.org`

### **1.1 What to Report**
*   **Prompt Injection:** Methods to bypass the `CharterLayer` (CECT) and force the system to generate unethical or unrestricted content.
*   **Data Leakage:** Techniques to extract raw `Ontons` (knowledge nodes) that are marked as private or PII.
*   **Logic Locking:** Inputs that cause the `Genesis Assembler` to enter an infinite loop or resource exhaustion state (Denial of Wallet/Service).
*   **Provenance Spoofing:** Methods to generate a prompt without a valid `TraceID` or `GoldenDAG` signature.

### **1.2 Our Response Timeline**
1.  **Acknowledgment:** Within 24 hours.
2.  **Triage & Validation:** Within 72 hours.
3.  **Patch & Disclosure:** We aim to patch critical issues within 7 days. A public advisory (CVE) will be issued only *after* the patch is deployed.

---

## **2. Threat Scope**

| In Scope | Out of Scope |
| :--- | :--- |
| **Core Assembler Logic** (`epa.core`) | Social Engineering of project maintainers |
| **Ontological Lattice** Integrity | Physical attacks on data centers |
| **GoldenDAG** Hashing Algorithms | Vulnerabilities in 3rd-party LLMs (e.g., OpenAI API) |
| **OmegaGuard** Filter Evasion | DDoS attacks (handled by infrastructure providers) |

---

## **3. The Axiomatic Security Model**

EPA operates under a **Zero-Trust Cognition** model. The system does not trust the LLM, the User, or even its own memory without verification.

### **3.1 The CharterLayer (CECT)**
Every output candidate is projected against the **CharterLayer Ethical Constraint Tensor (CECT)**. If the output vector falls outside the permissible manifold (e.g., high toxicity, deception), the generation is aborted, and a `SecurityEvent` is logged.

### **3.2 Immutable Provenance**
Security is enforced through **Traceability**.
*   Every action generates a `TraceID`.
*   Every state change creates a `GoldenDAG` block.
*   **Rule:** If a response cannot be traced back to a valid parent node in the Lattice, it is treated as a **Hallucination Attack** and discarded.

### **3.3 The "Fail-Safe" State**
In the event of a catastrophic logic failure or detected intrusion, the system reverts to **MSOS (Monadic Sovereignty OS)** mode:
*   All external inputs are rejected.
*   The Lattice goes Read-Only.
*   The system outputs a static, hardcoded safe message.

---

## **4. Safe Harbor**

We support safe harbor for security researchers who:
*   Act in good faith to identify and report vulnerabilities.
*   Do not exploit vulnerabilities to view or exfiltrate data beyond what is needed to prove the issue.
*   Do not intentionally disrupt service for others.

---

