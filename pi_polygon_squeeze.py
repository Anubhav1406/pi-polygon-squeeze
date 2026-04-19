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

for scale in range(1, 85):
    start = time.perf_counter()

    digits=610*scale

    get_context().precision = int(digits*4)  # bits, not digits!

    mp.mp.dps = digits  # precision

    def approximate_pi(iterations=1000*scale):
        side = mpfr('1e-100000')  # initial side length
        R = side                # circumradius
        r = mpfr(0)           # inradius
        n = 6                   # start with hexagon

        for _ in range(iterations):

            # update polygon (double sides)
            n *= 2

            x = (side / (2 * R))**2

            R = (side / 2) * gmpy2.sqrt(2/x * (1 + gmpy2.sqrt(1 - x)))

        r = gmpy2.sqrt(R - side/2) * gmpy2.sqrt(R + side/2)
        pi_val = n * side / (r + R)

        return pi_val


    pi_approx = approximate_pi()

    end = time.perf_counter()
    print("Error        :", mp.nstr(abs(pi_approx - mp.pi), 10))
    print("Time taken   :", end - start)
    print("iterations   :", 1000*scale, "\n")

    if scale == 84:
        print("Approximation:", pi_approx)
        print("Actual π     :", mp.pi)