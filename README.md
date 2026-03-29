# π Approximation via Polygon Geometry (Squeeze Method)

This project approximates π using a geometric approach based on regular polygons and a squeeze argument involving the inradius and circumradius.

Instead of relying on infinite series or predefined constants, this method derives π through purely geometric reasoning and iterative refinement.

---

## 🧠 Idea

Consider a regular polygon with:

- n sides  
- side length l  
- circumradius R  
- inradius r  

The perimeter P = n · l satisfies:

    2πr ≤ P ≤ 2πR

Dividing by (r + R):

    (2πr)/(r+R) ≤ P/(r+R) ≤ (2πR)/(r+R)

As n → ∞, the polygon approaches a circle and r → R.

By the squeeze principle:

    P / (r + R) → π

Thus, we approximate:

    π ≈ (n · l) / (r + R)

---

## ⚙️ Method

We iteratively refine the polygon by doubling the number of sides:

    n → 2n

Instead of changing the side length, we keep l fixed and update the radii R and r.

This introduces a scaling of the geometry, but the ratio:

    (n · l) / (r + R)

remains invariant under scaling and still converges to π.

---

## 🔁 Recursion

Let:

    x = (l / (2R))²

Then the updated circumradius is:

    R' = (l / 2) * sqrt( (2/x) * (1 + sqrt(1 - x)) )

and the inradius is:

    r' = sqrt(R' - l/2) * sqrt(R' + l/2)

At each step:

    R ← R'
    r ← r'
    n ← 2n

---

## 🚀 Implementation

The algorithm is implemented in Python using the `mpmath` library for high-precision arithmetic.

It typically converges to high accuracy within a small number of iterations.

---

## 📊 Results

Two types of plots are used:

1. Convergence plot  
   Shows how the approximation approaches π over iterations  

2. Error plot (log scale)  
   Shows rapid convergence and numerical precision limits  

---

## 📁 Files

- pi_polygon_squeeze.py → clean implementation  
- pi_polygon_derivation.ipynb → full derivation, visualization, and analysis  

---

## 🛠️ Requirements

Install dependencies:

    pip install mpmath matplotlib numpy

---

## ▶️ Run

    python pi_polygon_squeeze.py

---

## 📌 Key Insight

This method demonstrates that:

- π can be derived from geometric bounds  
- iterative refinement of polygons leads to convergence  
- scaling does not affect the final ratio  
- numerical methods can emerge naturally from geometry  

---

## 🧩 Future Work

- Compare convergence with series-based methods  
- Extend to other geometric approximations  
- Analyze convergence rate formally  