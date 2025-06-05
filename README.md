# 🌄 Gradient Method for Nonlinear Systems

A **Python toolkit** for numerically solving nonlinear systems of equations using a gradient-based (quasi-Newton) iterative method. Includes a fully-documented Persian scientific report for theoretical foundations and educational purposes.

---

## 🧩 Project Overview

- **🎯 Goal:**  
  Efficiently solve nonlinear vector equations of the form
  
  $$
  \vec{F}(\vec{x}) = \vec{0}
  $$
  
  using symbolic Jacobian computation and a gradient/Newton-like iterative approach.

- **✨ Features:**  
  - **Symbolic Jacobian:** Automatically computed via [`sympy`](https://www.sympy.org/)
  - **Stepwise Solution:** Iterative update along the Jacobian direction
  - **Custom Initialization:** User provides the initial guess interactively
  - **Convergence Check:** Flexible tolerance for precision
  - **Educational Output:** Step-by-step matrices printed for transparency and learning

---

## 📂 Files in this Repository

| File Name              | Description                                                           |
|------------------------|-----------------------------------------------------------------------|
| `Gradient-Method.py`   | Python code with full in-line explanations and outputs                |
| `Gradient-Method.pdf`  | Scientific report: theory, equations, algorithm, sample runs  |

---

## 🚀 Quick Start

1. **Install Dependencies:**  
   ```bash
   pip install sympy numpy
