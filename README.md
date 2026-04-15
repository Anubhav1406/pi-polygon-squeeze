# π Approximation via Polygon Geometry (Squeeze Method)

This project approximates π using a geometric approach based on regular polygons and a squeeze argument involving the inradius and circumradius.

Instead of relying on infinite series or predefined constants, this method derives π through purely geometric reasoning, iterative refinement, and high-precision arithmetic.

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

## ⚡ Convergence

The method exhibits exponential convergence:

    Error ∝ 4^(-k)

where k is the number of iterations (doublings of n).

This corresponds to:

    ≈ log10(4) ≈ 0.60206 decimal digits per iteration

Empirical results confirm this rate, with a linear trend observed on a logarithmic error plot.

---

## 🚀 Implementation

The algorithm is implemented in Python using:

- `mpmath` for arbitrary precision arithmetic  
- `gmpy2` for faster high-precision numerical operations  

Precision is scaled dynamically:

    digits = 610 × scale  
    mp.mp.dps = digits  

Binary precision is set via:

    get_context().precision ≈ 4 × digits  (in bits)

---

## 📊 Benchmarking

The program is executed across increasing scales:

    scale ∈ [1, 84]

For each scale:

- iterations = 1000 × scale  
- precision increases proportionally  
- execution time is measured using `time.perf_counter()`  

Results are logged via:

    python pi_polygon_squeeze.py >> result.txt

---

## 📈 Results

- Error decreases exponentially with iteration count  
- High-precision agreement with π is achieved (tens of thousands of digits)  
- Runtime increases due to large integer arithmetic costs  

---

## 📁 Files

- pi_polygon_squeeze.py → optimized implementation  
- pi_polygon_derivation.ipynb → derivation, visualization, and analysis  
- result.txt → recorded outputs across scales  

---

## 🛠️ Requirements

Install dependencies:

    pip install mpmath gmpy2 matplotlib numpy

---

## ▶️ Run

    python pi_polygon_squeeze.py >> result.txt

---

## 📌 Key Insights

- π can be derived from purely geometric bounds  
- Symmetric normalization improves numerical stability  
- Doubling-based refinement leads to exponential convergence  
- High-precision arithmetic enables extreme accuracy  
- Performance depends heavily on underlying numeric libraries  

---

## 🧩 Future Work

- Compare with AGM / Gauss–Legendre methods  
- Optimize recurrence for lower computational cost  
- Analyze convergence order more formally  
- Explore vectorized or parallel implementations  