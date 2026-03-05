# Machine Learning

Quantum and neuromorphic machine learning algorithms implemented with the Dynex SDK.

## Examples

| Notebook | Description |
|----------|-------------|
| [Quantum SVM](example_support_vector_machine.ipynb) | Support vector machine with a quantum kernel |
| [Full QRBM](Dynex-Full-QRBM.ipynb) | 3-step QUBO Restricted Boltzmann Machine |
| [Quantum Boltzmann Machine](example_quantum_boltzmann_machine_QBM.ipynb) | Full QBM training and inference |
| [Neuromorphic Torch Layers](example_neuromorphic_torch_layers.ipynb) | QBM integrated as a PyTorch layer |
| [QSVM with PyTorch](Example_SVM_pytorch.ipynb) | QSVM inside a PyTorch training loop |
| [Mode-Assisted QRBM](example_pytorch.ipynb) | Mode-assisted training for QRBM with PyTorch |
| [Scikit-Learn Plugin](Dynex_Scikit-Learn_Plugin.ipynb) | Drop-in replacement for scikit-learn estimators |

## Background

Dynex neuromorphic computing is particularly effective for training energy-based models (RBMs, QBMs) because the annealer naturally samples from the Boltzmann distribution of the model's energy landscape. This enables training without explicit MCMC or contrastive divergence.
