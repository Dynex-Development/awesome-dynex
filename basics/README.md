# Annealing Basics

Introductory notebooks for the Dynex annealing SDK. Each example is self-contained and demonstrates a fundamental concept.

## Examples

| Notebook | Description |
|----------|-------------|
| [BQM Example](beginners_guide_example_bqm.ipynb) | Define and sample a Binary Quadratic Model using `dimod` |
| [QUBO Example](beginners_guide_example_QUBO.ipynb) | Build and solve a QUBO problem from scratch |
| [Logic Gates](beginners_guide_example_logic_gates.ipynb) | Encode AND, OR, NOT, XOR gates as QUBO penalties |
| [Maximum Independent Set](beginners_guide_example_MIS.ipynb) | Find the largest independent set in a graph |
| [Anti-Crossing Clique](beginners_guide_example_anti_crossing_clique.ipynb) | Anti-crossing problem and clique detection on a graph |
| [BQM K4 Complete Graph](beginners_guide_example_bqm_k4_complete_graph.ipynb) | BQM defined on a complete K4 graph |
| [Random NAE3SAT](beginners_guide_example_random_nae3sat.ipynb) | Not-All-Equal 3SAT satisfiability benchmark |

## Quick Start

```python
import dynex
import dimod
from dynex import DynexConfig, DynexSampler, BQM
from dynex.enums import ComputeBackend

bqm = dimod.BinaryQuadraticModel({'x': -1, 'y': -1}, {'xy': 2}, 0, vartype='BINARY')
config = DynexConfig(compute_backend=ComputeBackend.GPU)
model = BQM(bqm)
sampler = DynexSampler(model, config=config)
sampleset = sampler.sample(num_reads=1000, annealing_time=200, shots=5)
print(sampleset)
```
