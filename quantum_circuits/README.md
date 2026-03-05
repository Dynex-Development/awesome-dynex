# Quantum Circuits

Gate-circuit examples using the `DynexCircuit` interface. Supports PennyLane functions, Qiskit `QuantumCircuit` objects, and raw OpenQASM 2.0 strings.

## Examples

### Basic Circuits

| Notebook | Qubits | Description |
|----------|--------|-------------|
| [Simple PennyLane](circuit_example_pennylane.ipynb) | 2 | Bell state: RX, RY, CNOT, H |
| [Simple Qiskit](circuit_example_qiskit.ipynb) | 2 | Bell state in Qiskit |
| [Simple OpenQASM](circuit_example_openqasm.ipynb) | 2 | Bell state in OpenQASM 2.0 |

### Intermediate Circuits

| Notebook | Qubits | Description |
|----------|--------|-------------|
| [Medium Circuit](circuit_example_medium.ipynb) | 3 | H, CNOT, T, Toffoli, SWAP gates |
| [Complex Circuit — 4 qubit](circuit_example_complex_1.ipynb) | 4 | Full entanglement + controlled rotations |
| [Complex Circuit — 12 qubit](circuit_example_complex_2.ipynb) | 12 | Large-scale entanglement |

### N-bit Adder Series

QFT-based quantum adder circuits at increasing qubit counts, demonstrating Dynex scalability.

| Notebook | Qubits |
|----------|--------|
| [8 qubit](circuit_example_nbit_adder_8bit.ipynb) | 8 |
| [13 qubit](circuit_example_nbit_adder.ipynb) | 13 |
| [16 qubit](circuit_example_nbit_adder_16bit.ipynb) | 16 |
| [32 qubit](circuit_example_nbit_adder_32bit.ipynb) | 32 |
| [64 qubit](circuit_example_nbit_adder_64bit.ipynb) | 64 |
| [72 qubit](circuit_example_nbit_adder_72bit.ipynb) | 72 |
| [80 qubit](circuit_example_nbit_adder_80bit.ipynb) | 80 |
| [88 qubit](circuit_example_nbit_adder_88bit.ipynb) | 88 |
| [96 qubit](circuit_example_nbit_adder_96bit.ipynb) | 96 |
| [104 qubit](circuit_example_nbit_adder_104bit.ipynb) | 104 |

### Advanced Algorithms

| Notebook | Qubits | Description |
|----------|--------|-------------|
| [Grover Factorization](circuit_example_grover.ipynb) | 12 | Grover-based integer factorization |
| [Shor's Algorithm](circuit_example_shor.ipynb) | 8 | Period finding for N=35 |
| [Quantum Transformer](circuit_example_quantum_transformer.ipynb) | 8 | NLP self-attention via quantum circuit |

## Quick Start

```python
from dynex import DynexConfig, DynexCircuit
from dynex.enums import ComputeBackend
import pennylane as qml

def bell_circuit(params, wires):
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])

config = DynexConfig(compute_backend=ComputeBackend.GPU)
circuit = DynexCircuit(config=config)

result = circuit.execute(
    bell_circuit, params=[], wires=2, method='probs',
    num_reads=100, integration_steps=200, shots=1
)
print(result)
```

> **QPU constraints:** `num_reads` 1–100, `integration_steps` 10–1000, `shots` up to 5.
