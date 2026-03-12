import numpy as np

G = 1.0

def compute_accelerations(r1, r2, r3, m1, m2, m3):
    """
    Calcula la aceleración de cada cuerpo debido a la gravedad mutua.
    Parámetros:
    r1, r2, r3 : np.array de tamaño 2 -> posiciones de los cuerpos
    m1, m2, m3 : float -> masas de los cuerpos
    Retorna:
    a1, a2, a3 : np.array de tamaño 2 -> aceleraciones de los cuerpos
    """
    def accel(ri, rj, mj):
        r = rj - ri
        dist = np.linalg.norm(r)
        if dist == 0:
            raise ValueError("Dos cuerpos están superpuestos (distancia = 0)")
        return G * mj * r / dist**3

    a1 = accel(r1, r2, m2) + accel(r1, r3, m3)
    a2 = accel(r2, r1, m1) + accel(r2, r3, m3)
    a3 = accel(r3, r1, m1) + accel(r3, r2, m2)

    return a1, a2, a3

def compute_energy(r1, r2, r3, v1, v2, v3, m1, m2, m3):
    """
    Calcula la energía total del sistema.
    """
    # Energía cinética
    Ek = (0.5 * m1 * np.dot(v1, v1) +
          0.5 * m2 * np.dot(v2, v2) +
          0.5 * m3 * np.dot(v3, v3))

    # Energía potencial
    d12 = np.linalg.norm(r2 - r1)
    d13 = np.linalg.norm(r3 - r1)
    d23 = np.linalg.norm(r3 - r2)
    Ep = (-G * m1 * m2 / d12
          - G * m1 * m3 / d13
          - G * m2 * m3 / d23)

    return Ek + Ep