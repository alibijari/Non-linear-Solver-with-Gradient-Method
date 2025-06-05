import numpy as np
import sympy


# ===========================
# 1. Function: Create Input Vector
# ===========================
def create_vector(n):
    """
    Creates a symbolic column vector of size n×1, where user enters each value.
    This serves as the initial guess for the system of equations.
    """
    vector = sympy.zeros(n, 1)
    for i in range(n):
        element = float(input(f"Enter element [{i + 1}, 1] of initial guess vector: "))
        vector[i, 0] = element
    return vector


# ===========================
# 2. Function: Jacobian Calculation
# ===========================
def calculate_jacobian(functions, variables):
    """
    Calculates the Jacobian matrix J_ij = ∂f_i/∂x_j
    for a list of functions and variables (symbols).
    """
    n = len(functions)
    m = len(variables)
    J = sympy.zeros(n, m)
    for i in range(n):
        for j in range(m):
            J[i, j] = sympy.diff(functions[i], variables[j])
    return J


# ===========================
# 3. Define System of Nonlinear Equations
# ===========================
x, y, z = sympy.symbols('x y z')
f1 = 3 * x + x ** 2 - 2 * y * z - 0.1
f2 = 2 * y - y ** 2 + 3 * x * z - 0.2
f3 = -z + z ** 2 + 2 * x * y - 0.3

functions = [f1, f2, f3]
variables = [x, y, z]

# ===========================
# 4. User Input: Initial Guess
# ===========================
n = len(functions)
vector = create_vector(n)

# ===========================
# 5. Algorithm Parameters
# ===========================
max_iterations = 100  # Maximum number of iterations allowed
epsilon = 1e-5  # Convergence criterion (tolerance)

iterations = 0  # Counter for the number of iterations

# ===========================
# 6. Main Iteration Loop (Modified Newton-like method)
# ===========================
while iterations < max_iterations:
    # --- Compute Jacobian and its transpose symbolically ---
    Jacobian = calculate_jacobian(functions, variables)
    Jacobian_tra = Jacobian.transpose()

    # --- Substitute current vector values into functions and Jacobians ---
    x_val, y_val, z_val = vector[0, 0], vector[1, 0], vector[2, 0]
    f_vals = [f.subs([(x, x_val), (y, y_val), (z, z_val)]) for f in functions]
    f_vec = sympy.Matrix(f_vals)

    J_eval = Jacobian.subs([(x, x_val), (y, y_val), (z, z_val)])
    Jt_eval = Jacobian_tra.subs([(x, x_val), (y, y_val), (z, z_val)])

    # --- Compute the "weight" vector for update (steepest descent-inspired) ---
    # A0 = J * J^T * f
    A0 = J_eval * Jt_eval * f_vec
    # Scalars needed for the update parameter s3 (step size)
    numerator = (f_vec.transpose() * A0)[0, 0]
    denominator = (A0.transpose() * A0)[0, 0]
    if denominator == 0:
        print("Zero denominator encountered! Aborting iteration.")
        break
    s3 = numerator / denominator

    # --- Update rule: new_vector = old_vector - s3 * J * f ---
    vector_new = vector - (s3 * J_eval * f_vec)

    # --- Convergence Check: max absolute difference between vectors ---
    diff = abs(vector_new - vector)
    max_diff = np.max(diff)

    # --- Print Detailed Iteration Info (for learning/debugging) ---
    print("\n=== Iteration", iterations + 1, "===")
    print("Current guess vector:\n", vector)
    print("Jacobian (symbolic):\n", Jacobian)
    print("Jacobian transpose:\n", Jacobian_tra)
    print("Function values at current guess:\n", f_vec)
    print("Jacobian evaluated at current guess:\n", J_eval)
    print("Jacobian transpose evaluated at current guess:\n", Jt_eval)
    print("Step size (μ₀):", s3)
    print("Updated guess vector:\n", vector_new)
    print("Convergence metric (max diff):", max_diff)

    # --- Check for convergence ---
    if max_diff < epsilon:
        print("\nConverged successfully!")
        break

    # Prepare for next iteration
    vector = vector_new
    iterations += 1

# ===========================
# 7. Final Output
# ===========================
print("\n=== Final Result ===")
print("Final solution vector:\n", vector)
if iterations == max_iterations:
    print("Warning: Maximum iterations reached. Initial guess may be too far from solution.")
print("Total iterations performed:", iterations + 1)

# ===========================
# 8. Physics/Math Context
# ===========================
# This code numerically solves a system of nonlinear algebraic equations:
# f1(x, y, z) = 0
# f2(x, y, z) = 0
# f3(x, y, z) = 0
# The approach is similar to Newton-Raphson but with an adaptive step using the Jacobian
# and its transpose to ensure stability and possible convergence even with a poor initial guess.

# Example (test): You can also evaluate f1 at a certain solution:
# Uncomment to check with specific values (example: x = -3.03, y = -0.04, z = -0.03)
# result = 3 * (-3.03) + (-3.03) ** 2 - 2 * (-0.04) * (-0.03) - 0.1
# print("Check f1 at (x, y, z) = (-3.03, -0.04, -0.03):", result)
