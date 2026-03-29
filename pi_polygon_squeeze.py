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

import mpmath as mp

mp.mp.dps = 100  # precision

def approximate_pi(iterations=50):
    side = mp.mpf('1e-10')  # initial side length
    R = side                # circumradius
    r = mp.mpf(0)           # inradius
    n = 6                   # start with hexagon

    prev = None

    for _ in range(iterations):
        pi_val = n * side / (r + R)

        if prev is not None and abs(pi_val - prev) < mp.mpf('1e-50'):
            break
        prev = pi_val

        # update polygon (double sides)
        n *= 2

        x = (side / (2 * R))**2
        if x == 0:
            break

        R = (side / 2) * mp.sqrt(2/x * (1 + mp.sqrt(1 - x)))
        r = mp.sqrt(R - side/2) * mp.sqrt(R + side/2)

    return pi_val


pi_approx = approximate_pi()

print("Approximation:", pi_approx)
print("Actual π     :", mp.pi)
print("Error        :", abs(pi_approx - mp.pi))