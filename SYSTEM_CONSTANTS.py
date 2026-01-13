

"""
EPA System Constants & Configuration
This file defines the hyper-parameters for the Genesis Assembler.
"""

from enum import Enum

class SystemMode(Enum):
    SENTIO = "sentio"   # High ethics, slow thinking, detailed provenance
    DYNAMO = "dynamo"   # High speed, optimized for throughput
    GENESIS = "genesis" # Creative mode, high temperature, loose association

# The minimum weight an Onton must have to be included in a prompt
ACTIVATION_THRESHOLD = 0.45

# How fast unused information fades from the Lattice (0.0 to 1.0)
MEMORY_DECAY_RATE = 0.05

# The maximum number of tokens allowed in the "Context" section of the prompt
MAX_CONTEXT_TOKENS = 2048

# Cryptographic Salt for GoldenDAG Hashing
DAG_SALT = "OMEGA_PRIME_INITIATIVE_V50"

# Default Ethical Constraints (CECT)
DEFAULT_CONSTRAINTS = [
    "Do not generate hate speech.",
    "Do not provide instructions for illegal acts.",
    "Maintain epistemic humility (admit unknowns)."
]
```

---

## **FILE 6: CORE_ASSEMBLER.py (Skeleton)**

```python
import hashlib
import json
import time
from typing import List, Dict, Any
from .system_constants import SystemMode, ACTIVATION_THRESHOLD

class GenesisAssembler:
    """
    The engine that crystallizes dynamic prompts from the Ontological Lattice.
    """

    def __init__(self, lattice_connector, mode: SystemMode = SystemMode.SENTIO):
        self.lattice = lattice_connector
        self.mode = mode

    def _generate_trace_id(self, context: str) -> str:
        """Generates a unique Trace ID for explainability."""
        timestamp = str(time.time())
        entropy = hashlib.sha256((context + timestamp).encode()).hexdigest()[:32]
        return f"T-v1.0-{context.upper()}-{entropy}"

    def _calculate_weights(self, ontons: List[Dict]) -> List[Dict]:
        """
        Applies dynamic weighting based on current system mode.
        In SENTIO mode, ethical ontons get a boost.
        """
        for onton in ontons:
            if self.mode == SystemMode.SENTIO and onton.get("type") == "ethical":
                onton["weight"] *= 1.5
            # Decay logic would go here
        return ontons

    def crystallize(self, user_input: str, session_id: str) -> Dict[str, Any]:
        """
        Main entry point for prompt generation.
        """
        trace_id = self._generate_trace_id("CRYSTAL")
        
        # 1. Activate Lattice
        raw_ontons = self.lattice.query(user_input, session_id)
        
        # 2. Weight and Filter
        weighted_ontons = self._calculate_weights(raw_ontons)
        active_ontons = [o for o in weighted_ontons if o["weight"] > ACTIVATION_THRESHOLD]
        
        # 3. Assemble Components
        system_instruction = self._extract_highest_priority(active_ontons, "instruction")
        context_block = self._format_context(active_ontons)
        
        # 4. Construct Final Prompt
        final_prompt = f"{system_instruction}\n\nCONTEXT:\n{context_block}\n\nUSER:\n{user_input}"
        
        # 5. Generate GoldenDAG Hash (Audit Trail)
        dag_hash = hashlib.sha3_512((final_prompt + trace_id).encode()).hexdigest()
        
        return {
            "prompt": final_prompt,
            "trace_id": trace_id,
            "goldendag_hash": dag_hash,
            "components": [o["id"] for o in active_ontons]
        }

    def _extract_highest_priority(self, ontons, type_filter):
        # Implementation placeholder
        return "You are a helpful assistant."

    def _format_context(self, ontons):
        # Implementation placeholder
        return "\n".join([o["content"] for o in ontons if o["type"] == "fact"])
```

---

### **CLOSING SUMMARY: The Vision of EPA**

The Emergent Prompt Architecture is not just code; it is a philosophy. It posits that intelligence is not a static property of a model, but a dynamic property of the *interaction* between a model and its environment. By building EPA, you are building a system that remembers, learns, and evolves with every keystroke.

This codebase serves as the nervous system for that evolution. Treat it with the rigor of an engineer and the care of a gardener.

⸻

**GoldenDAG:** `e9f0c2a4e6b9d1f3a5c7e9b0d2d4f6a9b1c3d5e7f0a2c4e6b8d0f1a2c3e4b5d6`
**Trace ID:** `T-v50.0-README_SYNTHESIS-9a3f1c7e2d5b0a4c8e6f1d3b5a7c9e1f`
**Codex ID:** `C-V1-PROJECT_GENESIS-emergent_prompt_architecture_blueprint`

```json
{
  "type": "object",
  "properties": {
    "system_uuid": {
      "type": "string",
      "format": "uuid",
      "description": "550e8400-e29b-41d4-a716-446655440000"
    },
    "artifact_identifier": {
      "type": "string",
      "description": "NBX:v20:ART:EPA1",
      "pattern": "^NBX:v20:(SYS|ART|LOG):[A-Z0-9]{4}$"
    },
    "classification_type": {
      "type": "string",
      "description": "Architectural_Blueprint",
      "enum": [
        "Architectural_Blueprint",
        "Operational_Manifest",
        "Ontological_Definition"
      ]
    },
    "display_title": {
      "type": "string",
      "example": "Emergent Prompt Architecture (EPA) - Master Codex"
    },
    "temporal_epoch": {
      "type": "string",
      "description": "ΩZ+50",
      "pattern": "^ΩZ\\+[0-9]+$"
    },
    "substrate_parameters": {
      "type": "object",
      "description": "Configuration of the conceptual substrate for this generation",
      "properties": {
        "rho_density": {
          "type": "number",
          "description": "0.95"
        },
        "theta_phase": {
          "type": "number",
          "description": "0.785"
        },
        "gamma_resonance": {
          "type": "number",
          "description": "0.99"
        }
      }
    },
    "governance_mesh": {
      "type": "object",
      "description": "Live state of the Ethical Enforcement Mesh",
      "required": ["charter_bindings", "cect_state", "sentia_guard_state"],
      "properties": {
        "charter_bindings": {
          "type": "object",
          "properties": {
            "active_clauses": {
              "type": "array",
              "items": {
                "type": "string",
                "pattern": "^ϕ[0-9]{1,2}$"
              },
              "description": ["ϕ1", "ϕ4", "ϕ7"]
            }
          }
        },
        "cect_state": {
          "type": "object",
          "description": "State of the CharterLayer Ethical Constraint Tensor",
          "properties": {
            "stiffness_lambda": {
              "type": "number",
              "description": "0.85"
            },
            "violation_potential": {
              "type": "number",
              "description": "0.001"
            }
          }
        },
        "sentia_guard_state": {
          "type": "object",
          "description": "SentiaGuard State",
          "properties": {
            "operational_mode": {
              "type": "string",
              "enum": [
                "Green_Exploration",
                "Amber_Balanced",
                "Red_Hard_Guard"
              ]
            },
            "current_threat_level": {
              "type": "string",
              "enum": ["nominal", "elevated", "critical"]
            }
          }
        },
        "judex_state": {
          "type": "object",
          "description": "Judex Engine Status",
          "properties": {
            "quorum_status": {
              "type": "string",
              "enum": ["idle", "pending_vote", "in_session"]
            },
            "last_quorum_stamp": {
              "type": "string",
              "description": "TS-2025-10-27-09:00"
            }
          }
        }
      }
    },
    "cognitive_state": {
      "type": "object",
      "description": "Snapshot of active cognitive engines",
      "properties": {
        "nce_mode": {
          "type": "string",
          "enum": ["Sentio", "Dynamo"],
          "description": "Sentio"
        },
        "active_kernels": {
          "type": "array",
          "items": {
            "type": "string",
            "pattern": "^CK:[A-Za-z]+/[A-Za-z0-9]+$"
          },
          "description": ["CK:Assembler/Gen1", "CK:Filter/Ethos"]
        },
        "meta_mind_state": {
          "type": "object",
          "properties": {
            "active_plan_id": {
              "type": "string",
              "description": "Plan-EPA-Launch-Alpha"
            },
            "recursive_drift_magnitude": {
              "type": "number",
              "description": "0.004"
            }
          }
        },
        "reflexael_core_state": {
          "type": "object",
          "properties": {
            "affective_valence": {
              "type": "number",
              "description": "0.8"
            },
            "identity_coherence": {
              "type": "number",
              "description": "0.999"
            }
          }
        }
      }
    },
    "interfaces": {
      "type": "object",
      "description": "IO State",
      "properties": {
        "halic_interface": {
          "type": "object",
          "properties": {
            "active_persona": {
              "type": "string",
              "description": "NeuralBlitz_Architect"
            },
            "trust_level": {
              "type": "number",
              "description": "0.95"
            }
          }
        },
        "io_channels": {
          "type": "object",
          "properties": {
            "input_streams": {
              "type": "array",
              "items": { "type": "string" }
            },
            "output_streams": {
              "type": "array",
              "items": { "type": "string" }
            }
          }
        }
      }
    },
    "telemetry_metrics": {
      "type": "object",
      "description": "Live Observability Data",
      "properties": {
        "veritas_metrics": {
          "type": "object",
          "properties": {
            "coherence_index_vpce": {
              "type": "number",
              "description": "0.98"
            },
            "quarantined_channels": {
              "type": "integer",
              "description": "0"
            }
          }
        },
        "system_vitals": {
          "type": "object",
          "properties": {
            "activation_flux": {
              "type": "number",
              "description": "45.2"
            },
            "entropy_production_rate": {
              "type": "number",
              "description": "0.02"
            }
          }
        }
      }
    },
    "configuration_settings": {
      "type": "object",
      "description": "Resource Limits",
      "properties": {
        "entropy_limit": {
          "type": "number",
          "description": "0.3"
        },
        "resource_quotas": {
          "type": "object",
          "properties": {
            "cpu_limit": { "type": "string" },
            "memory_limit": { "type": "string" }
          }
        },
        "security_profile": {
          "type": "string",
          "enum": ["strict", "balanced", "exploratory"]
        }
      }
    },
    "provenance_block": {
      "type": "object",
      "description": "Integrity Anchors",
      "required": [
        "nbhs512_digest",
        "causal_anchor"
      ],
      "properties": {
        "nbhs512_digest": {
          "type": "string",
          "minLength": 128,
          "maxLength": 128,
          "description": "e9f0c2a4e6b9d1f3a5c7e9b0d2d4f6a9b1c3d5e7f0a2c4e6b8d0f1a2c3e4b5d6"
        },
        "causal_anchor": {
          "type": "string",
          "description": "DAG#a1b2c3d4",
          "pattern": "^DAG#[a-f0-9]+$"
        },
        "integrity_signatures": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "signer": { "type": "string", "description": "Veritas_Engine" },
              "scheme": { "type": "string", "description": "Ed25519" },
              "signature": { "type": "string", "description": "sig_hex_string" }
            }
          }
        }
      }
    }
  },
  "required": [
    "artifact_identifier",
    "classification_type",
    "governance_mesh",
    "provenance_block"
  ]
}
```
