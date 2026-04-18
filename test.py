"""
Approximate π using a geometric squeeze argument based on regular polygons.

Instead of using series expansions or classical Archimedean bounds,
this approach considers a regular n-sided polygon with:

- circumradius R
- inradius r
- side length l

The perimeter P of the polygon satisfies:

    2πr <= P <= 2πR

Dividing by (r + R), we obtain:

    π ≈ P / (r + R)

As the number of sides n increases (n → ∞), the polygon approaches a circle,
and both r and R converge to the same value. By the squeeze principle,
this ratio converges to π.

This implementation iteratively doubles the number of polygon sides and updates
the geometric parameters, achieving high-precision convergence using mpmath.
"""
import time
import mpmath as mp
import gmpy2
from gmpy2 import mpfr, get_context

for l in range(1, 101):
    p = 1000*l

    start = time.perf_counter()



    digits=int(610*l)

    get_context().precision = int(digits*4)  # bits, not digits!

    mp.mp.dps = digits  # precision

    def approximate_pi():
        side = mpfr('1e-10000')  # initial side length
        R = side                # circumradius
        r = mpfr(0)           # inradius
        n = mpfr(6)                   # start with hexagon

        # update polygon (double sides)
        n *= 2**p

        x = (side / (2 * R))**2

        curr = gmpy2.sqrt(1-x) + 1
        prod = mpfr(1)
        for i in range(p):
            prod *= 2*curr
            curr = gmpy2.sqrt(curr/2) + 1
            #if i%50 == 0:
            #    print(i, "done")

        R = (side/2)*gmpy2.sqrt(prod/x)

        r = gmpy2.sqrt(R**2 - side**2/4)
        pi_val = n * side / (r + R)

        return pi_val


    pi_approx = approximate_pi()

    end = time.perf_counter()
    print("Error        :", mp.nstr(abs(pi_approx - mp.pi), 10))
    print("Time taken   :", end - start)
    print("power        :", p)
    print()

    if l == 100:
        print("Approximation:", pi_approx)
        print("Actual π     :", mp.pi)