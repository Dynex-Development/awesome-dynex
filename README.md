# Awesome Dynex [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated collection of example notebooks for the [Dynex](https://dynexcoin.org) neuromorphic quantum computing platform.

These notebooks demonstrate how to solve real-world problems using the Dynex SDK — from basic QUBO/BQM formulations to quantum machine learning and gate-circuit execution on the Dynex GPU/QPU network.

---

## Contents

- [Annealing Basics](#annealing-basics)
- [Optimization](#optimization)
- [Machine Learning](#machine-learning)
- [Advanced Applications](#advanced-applications)
- [Quantum Circuits](#quantum-circuits)
- [Benchmarks](#benchmarks)

---

## Annealing Basics

Introductory examples covering BQM, QUBO, Ising models, and core annealing concepts.

| Example | Description |
|---------|-------------|
| [BQM Example](basics/beginners_guide_example_bqm.ipynb) | Define and sample a Binary Quadratic Model |
| [QUBO Example](basics/beginners_guide_example_QUBO.ipynb) | Formulate and solve a QUBO problem |
| [Logic Gates](basics/beginners_guide_example_logic_gates.ipynb) | Encode AND, OR, NOT gates as QUBO |
| [Maximum Independent Set](basics/beginners_guide_example_MIS.ipynb) | Find the largest independent set in a graph |
| [Anti-Crossing Clique](basics/beginners_guide_example_anti_crossing_clique.ipynb) | Anti-crossing and clique detection |
| [BQM K4 Complete Graph](basics/beginners_guide_example_bqm_k4_complete_graph.ipynb) | BQM on a complete K4 graph |
| [Random NAE3SAT](basics/beginners_guide_example_random_nae3sat.ipynb) | Satisfiability problem — Not-All-Equal 3SAT |

---

## Optimization

Combinatorial and continuous optimization problems mapped to BQM/CQM and solved on the Dynex network.

| Example | Description |
|---------|-------------|
| [Portfolio Optimization](optimization/Dynex_Portfolio_Optimisation.ipynb) | Markowitz portfolio optimization with real market data |
| [Number Partitioning](optimization/quantum_number_partitioning.ipynb) | Partition a set of numbers into two equal-sum subsets |
| [Graph Partitioning](optimization/quantum_graph_partitioning.ipynb) | Divide a graph into balanced partitions minimizing cut edges |
| [Job Sequencing](optimization/quantum_job_sequencing.ipynb) | Minimize makespan across machines |
| [Set Cover](optimization/quantum_set_cover.ipynb) | Find the minimum collection of sets covering all elements |
| [Vertex Cover](optimization/quantum_vertex_cover.ipynb) | Minimum vertex cover on a graph |
| [K-Means Clustering](optimization/quantum_kmeans_clustering.ipynb) | Quantum-assisted clustering |
| [Binary Integer Linear Programming](optimization/quantum_BILP.ipynb) | General BILP via QUBO encoding |
| [Aircraft Loading](optimization/aircraft-loading-optim.ipynb) | Cargo loading optimization for aircraft weight balance |
| [Traffic Optimization](optimization/TrafficOptimizationCQMBUG.ipynb) | City traffic routing with CQM |

---

## Machine Learning

Quantum and neuromorphic machine learning algorithms: SVM, RBM, QBM, and PyTorch integration.

| Example | Description |
|---------|-------------|
| [Quantum SVM](machine_learning/example_support_vector_machine.ipynb) | Support vector machine kernel with Dynex |
| [Full QRBM](machine_learning/Dynex-Full-QRBM.ipynb) | 3-step QUBO Restricted Boltzmann Machine |
| [Quantum Boltzmann Machine](machine_learning/example_quantum_boltzmann_machine_QBM.ipynb) | Full QBM implementation |
| [Neuromorphic Torch Layers](machine_learning/example_neuromorphic_torch_layers.ipynb) | QBM as a PyTorch layer |
| [QSVM with PyTorch](machine_learning/Example_SVM_pytorch.ipynb) | QSVM integrated with PyTorch training loop |
| [Mode-Assisted QRBM](machine_learning/example_pytorch.ipynb) | Mode-assisted QRBM with PyTorch |
| [Scikit-Learn Plugin](machine_learning/Dynex_Scikit-Learn_Plugin.ipynb) | Drop-in replacement for scikit-learn estimators |
| [Feature Selection — Titanic](misc/example_feature_selection_titanic_survivals.ipynb) | Quantum feature selection on Titanic dataset |
| [Collaborative Filtering](misc/example_collaborative_filtering_CFQIRBM.ipynb) | CFQIRBM-based recommendation system |
| [Image Classification](misc/Medium_Image_Classification.ipynb) | Image classification with Q-RBM |

---

## Advanced Applications

Domain-specific quantum applications: biology, chemistry, logistics, and combinatorics.

| Example | Description |
|---------|-------------|
| [Protein Folding](advanced_applications/QuantumProteinFolding.ipynb) | Lattice protein folding via QUBO |
| [RNA Folding](misc/example_rna_folding.ipynb) | Predict minimum free energy RNA secondary structure |
| [Satellite Positioning](advanced_applications/QuantumSatellite.ipynb) | Optimal placement of satellites over target regions |
| [Sudoku Solver](advanced_applications/QuantumSudoku.ipynb) | Quantum constraint satisfaction for 9x9 Sudoku |
| [N-Queen Problem](advanced_applications/QuantumnQueenProblem.ipynb) | Place N non-attacking queens on an N×N board |
| [Grover Search](misc/Dynex_Grover_Search.ipynb) | Grover's algorithm for unstructured search |
| [Integer Factorization](misc/example_integer_factorisation.ipynb) | Factor integers via QUBO encoding |
| [Charging Station Placement](misc/example_placement_of_charging_stations.ipynb) | Optimal EV charging station placement |
| [Molecule Screening](misc/molecule_screening.ipynb) | Molecular similarity screening for drug discovery |

---

## Quantum Circuits

Gate-circuit execution via `DynexCircuit` — PennyLane, Qiskit, and OpenQASM interfaces.

| Example | Qubits | Description |
|---------|--------|-------------|
| [Simple PennyLane](quantum_circuits/circuit_example_pennylane.ipynb) | 2 | Bell state with RX, RY, CNOT |
| [Simple Qiskit](quantum_circuits/circuit_example_qiskit.ipynb) | 2 | Bell state in Qiskit |
| [Simple OpenQASM](quantum_circuits/circuit_example_openqasm.ipynb) | 2 | Bell state in OpenQASM 2.0 |
| [Medium Circuit](quantum_circuits/circuit_example_medium.ipynb) | 3 | H, CNOT, T, Toffoli, SWAP |
| [Complex Circuit — 4 qubit](quantum_circuits/circuit_example_complex_1.ipynb) | 4 | Full entanglement + controlled rotations |
| [Complex Circuit — 12 qubit](quantum_circuits/circuit_example_complex_2.ipynb) | 12 | Large-scale entanglement |
| [N-bit Adder — 13 qubit](quantum_circuits/circuit_example_nbit_adder.ipynb) | 13 | QFT-based addition |
| [N-bit Adder — 8 qubit](quantum_circuits/circuit_example_nbit_adder_8bit.ipynb) | 8 | QFT-based addition |
| [N-bit Adder — 16 qubit](quantum_circuits/circuit_example_nbit_adder_16bit.ipynb) | 16 | QFT-based addition |
| [N-bit Adder — 32 qubit](quantum_circuits/circuit_example_nbit_adder_32bit.ipynb) | 32 | QFT-based addition |
| [N-bit Adder — 64 qubit](quantum_circuits/circuit_example_nbit_adder_64bit.ipynb) | 64 | QFT-based addition |
| [N-bit Adder — 72 qubit](quantum_circuits/circuit_example_nbit_adder_72bit.ipynb) | 72 | QFT-based addition |
| [N-bit Adder — 80 qubit](quantum_circuits/circuit_example_nbit_adder_80bit.ipynb) | 80 | QFT-based addition |
| [N-bit Adder — 88 qubit](quantum_circuits/circuit_example_nbit_adder_88bit.ipynb) | 88 | QFT-based addition |
| [N-bit Adder — 96 qubit](quantum_circuits/circuit_example_nbit_adder_96bit.ipynb) | 96 | QFT-based addition |
| [N-bit Adder — 104 qubit](quantum_circuits/circuit_example_nbit_adder_104bit.ipynb) | 104 | QFT-based addition |
| [Grover Factorization](quantum_circuits/circuit_example_grover.ipynb) | 12 | Grover-based integer factorization |
| [Shor's Algorithm](quantum_circuits/circuit_example_shor.ipynb) | 8 | Period finding, N=35 |
| [Quantum Transformer](quantum_circuits/circuit_example_quantum_transformer.ipynb) | 8 | NLP self-attention mechanism |

---

## Benchmarks

Performance benchmarks comparing Dynex against classical and quantum hardware.

| Example | Description |
|---------|-------------|
| [MAX-CUT G70](benchmarks/G70_dynex.ipynb) | Gset G70 MAX-CUT — world-record solution (9578) |
| [Quantum Volume](benchmarks/QuantumVolume.ipynb) | Quantum Volume measurement protocol |
| [XEB 4x4](benchmarks/XEB-4x4.ipynb) | Cross-Entropy Benchmarking on 4×4 circuit |
| [XEB 10x10](benchmarks/XEB-10x10.ipynb) | Cross-Entropy Benchmarking on 10×10 circuit |
| [Q-Score](misc/Dynex_Q_Score.ipynb) | Q-Score metric for annealing performance |

---

## Getting Started

### Prerequisites

```bash
pip install dynex
```

Set your API credentials in `~/.dynex/dynex.ini`:

```ini
[DYNEX]
API_KEY    = <your-api-key>
API_SECRET = <your-api-secret>
```

### Running an Example

Open any `.ipynb` notebook in JupyterLab or VS Code. Each notebook is self-contained and includes installation notes, code, and expected output.

```bash
jupyter lab basics/beginners_guide_example_bqm.ipynb
```

### Compute Backends

| Backend | Description |
|---------|-------------|
| `ComputeBackend.GPU` | Dynex neuromorphic GPU chips — recommended for production |
| `ComputeBackend.QPU` | Dynex QPU network — `num_reads` 1–100, `annealing_time` 10–1000, `shots` up to 5 |
| `ComputeBackend.CPU` | CPU-based simulation |
| `ComputeBackend.LOCAL` | Local simulation for development |

---

## Documentation

Full SDK documentation: [docs.dynexcoin.org](https://docs.dynexcoin.org)

SDK repository: [Dynex-Development/PY-SDK-V2](https://github.com/Dynex-Development/PY-SDK-V2)

## License

[MIT](LICENSE)
