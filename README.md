# Gradient Method for Nonlinear Systems

This repository contains a **Python implementation** and **scientific report** (PDF, in Persian) for solving systems of nonlinear equations using the gradient (Newton-like) method.

---

## 📋 Overview

- **Goal:** Numerically solve systems of nonlinear equations of the form  
  $$
\vec{F}(\vec{x}) = \vec{0}
$$

  using an iterative gradient-based (quasi-Newton) method.
- **Features:**  
  - Symbolic Jacobian calculation using `sympy`
  - Iterative update based on gradient (Jacobian) direction
  - User-defined initial guess
  - Convergence criterion
  - Step-by-step matrix output for learning purposes

---

## 🛠 Files

- **`Gradient-Method.py`** — Main Python code with detailed comments
- **`Gradient-Method.pdf`** — Scientific report explaining theory, mathematical modeling, algorithm, and code

---

## 🚀 How to Run

1. **Install Dependencies:**  
   This code uses only [SymPy](https://www.sympy.org/) and [NumPy](https://numpy.org/) (most Python installations have these).
   ```bash
   pip install sympy numpy
   python Gradient-Method.py
