import numpy as np
from three_body import compute_accelerations

def euler_step(r1, r2, r3, v1, v2, v3, m1, m2, m3, dt):
    a1, a2, a3 = compute_accelerations(r1, r2, r3, m1, m2, m3)
    r1_new = r1 + v1 * dt
    r2_new = r2 + v2 * dt
    r3_new = r3 + v3 * dt
    v1_new = v1 + a1 * dt
    v2_new = v2 + a2 * dt
    v3_new = v3 + a3 * dt
    return r1_new, r2_new, r3_new, v1_new, v2_new, v3_new

def verlet_step(r1, r2, r3, v1, v2, v3, m1, m2, m3, dt):
    a1, a2, a3 = compute_accelerations(r1, r2, r3, m1, m2, m3)
    r1_new = r1 + v1 * dt + 0.5 * a1 * dt**2
    r2_new = r2 + v2 * dt + 0.5 * a2 * dt**2
    r3_new = r3 + v3 * dt + 0.5 * a3 * dt**2
    a1_new, a2_new, a3_new = compute_accelerations(r1_new, r2_new, r3_new, m1, m2, m3)
    v1_new = v1 + 0.5 * (a1 + a1_new) * dt
    v2_new = v2 + 0.5 * (a2 + a2_new) * dt
    v3_new = v3 + 0.5 * (a3 + a3_new) * dt
    return r1_new, r2_new, r3_new, v1_new, v2_new, v3_new

def rk4_step(r1, r2, r3, v1, v2, v3, m1, m2, m3, dt):
    # k1
    a1_1, a2_1, a3_1 = compute_accelerations(r1, r2, r3, m1, m2, m3)

    # k2
    a1_2, a2_2, a3_2 = compute_accelerations(
        r1 + 0.5*v1*dt, r2 + 0.5*v2*dt, r3 + 0.5*v3*dt, m1, m2, m3)

    # k3
    a1_3, a2_3, a3_3 = compute_accelerations(
        r1 + 0.5*v1*dt, r2 + 0.5*v2*dt, r3 + 0.5*v3*dt, m1, m2, m3)

    # k4
    a1_4, a2_4, a3_4 = compute_accelerations(
        r1 + v1*dt, r2 + v2*dt, r3 + v3*dt, m1, m2, m3)

    r1_new = r1 + v1 * dt
    r2_new = r2 + v2 * dt
    r3_new = r3 + v3 * dt
    v1_new = v1 + (dt/6) * (a1_1 + 2*a1_2 + 2*a1_3 + a1_4)
    v2_new = v2 + (dt/6) * (a2_1 + 2*a2_2 + 2*a2_3 + a2_4)
    v3_new = v3 + (dt/6) * (a3_1 + 2*a3_2 + 2*a3_3 + a3_4)
    return r1_new, r2_new, r3_new, v1_new, v2_new, v3_new