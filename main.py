import numpy as np
from three_body import compute_accelerations, compute_energy
from integrators import euler_step, verlet_step, rk4_step
from plots import plot_trajectory, plot_energy, animate_trajectory
import matplotlib.pyplot as plt

G = 1.0

# ── Menú de casos ─────────────────────────────────────────────────
print("\n╔══════════════════════════════════════╗")
print("║   THREE-BODY SIMULATION              ║")
print("╠══════════════════════════════════════╣")
print("║  1. Lagrange (triángulo equilátero)  ║")
print("║  2. Euler (colineal)                 ║")
print("║  3. Órbita en 8                      ║")
print("║  4. Personalizado                    ║")
print("╚══════════════════════════════════════╝")
caso = input("\nElige un caso (1-4): ").strip()

# ── Condiciones iniciales ─────────────────────────────────────────
if caso == "1":
    print("\n→ Caso Lagrange")
    m1 = m2 = m3 = 1.0
    r1 = np.array([-0.5,  np.sqrt(3)/2])
    r2 = np.array([-0.5, -np.sqrt(3)/2])
    r3 = np.array([ 1.0,  0.0])
    L  = np.linalg.norm(r2 - r1)
    v_orb = np.sqrt(G * m1 / L)
    v1 = v_orb * np.array([-r1[1], r1[0]]) / np.linalg.norm(r1)
    v2 = v_orb * np.array([-r2[1], r2[0]]) / np.linalg.norm(r2)
    v3 = v_orb * np.array([-r3[1], r3[0]]) / np.linalg.norm(r3)
    titulo = "Lagrange"

elif caso == "2":
    print("\n→ Caso Euler")
    m1 = m2 = m3 = 1.0
    r1 = np.array([-1.0, 0.0])
    r2 = np.array([ 0.0, 0.0])
    r3 = np.array([ 1.0, 0.0])
    L  = 1.0
    v_orb = np.sqrt(G * m1 / L)
    v1 = np.array([0.0, -v_orb * 0.5])
    v2 = np.array([0.0,  0.0])
    v3 = np.array([0.0,  v_orb * 0.5])
    titulo = "Euler"

elif caso == "3":
    print("\n→ Órbita en 8")
    m1 = m2 = m3 = 1.0
    r1 = np.array([-0.97000436,  0.24308753])
    r2 = np.array([ 0.97000436, -0.24308753])
    r3 = np.array([ 0.0,         0.0])
    v3 = np.array([-0.93240737, -0.86473146])
    v1 = -v3 / 2
    v2 = -v3 / 2
    titulo = "Órbita en 8"

elif caso == "4":
    print("\n→ Caso personalizado")

    def pedir_float(mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("  ⚠ Introduce un número válido (ej: 1.0)")

    def pedir_vector(mensaje):
        while True:
            try:
                raw = input(mensaje)
                # limpia paréntesis, comas y corchetes
                raw = raw.replace("(","").replace(")","").replace("[","").replace("]","").replace(",", " ")
                valores = list(map(float, raw.split()))
                if len(valores) != 2:
                    raise ValueError
                return np.array(valores)
            except ValueError:
                print("  ⚠ Introduce dos números separados por espacio (ej: 1.0 0.5)")

    print("Introduce las masas:")
    m1 = pedir_float("  m1: ")
    m2 = pedir_float("  m2: ")
    m3 = pedir_float("  m3: ")
    print("Introduce las posiciones iniciales:")
    r1 = pedir_vector("  r1 (x y): ")
    r2 = pedir_vector("  r2 (x y): ")
    r3 = pedir_vector("  r3 (x y): ")
    print("Introduce las velocidades iniciales:")
    v1 = pedir_vector("  v1 (x y): ")
    v2 = pedir_vector("  v2 (x y): ")
    v3 = pedir_vector("  v3 (x y): ")
    titulo = "Personalizado"

else:
    print("Opción no válida, usando Lagrange por defecto.")
    caso = "1"

# ── Parámetros de simulación ──────────────────────────────────────
print("\nElige el integrador:")
print("  1. Euler")
print("  2. Verlet")
print("  3. RK4")
integ = input("Integrador (1-3): ").strip()
integradores = {"1": euler_step, "2": verlet_step, "3": rk4_step}
integrador = integradores.get(integ, rk4_step)

dt = float(input("Paso de tiempo dt (recomendado 0.01): ") or "0.01")
N  = int(input("Número de pasos N (recomendado 2000): ") or "2000")

# ── Bucle de simulación ───────────────────────────────────────────
r1_list = [r1.copy()]
r2_list = [r2.copy()]
r3_list = [r3.copy()]
E_list  = [compute_energy(r1, r2, r3, v1, v2, v3, m1, m2, m3)]

for i in range(N):
    r1, r2, r3, v1, v2, v3 = integrador(r1, r2, r3, v1, v2, v3, m1, m2, m3, dt)
    r1_list.append(r1.copy())
    r2_list.append(r2.copy())
    r3_list.append(r3.copy())
    E_list.append(compute_energy(r1, r2, r3, v1, v2, v3, m1, m2, m3))

r1_list = np.array(r1_list)
r2_list = np.array(r2_list)
r3_list = np.array(r3_list)

print(f"\nSimulación completada! | Pasos: {N} | dt: {dt} | Integrador: {integrador.__name__}")

# ── Gráficos ──────────────────────────────────────────────────────
plot_trajectory(r1_list, r2_list, r3_list, title=f"{titulo} - {integrador.__name__}")
plot_energy(E_list, title=f"Energía - {titulo} - {integrador.__name__}")
ani = animate_trajectory(r1_list, r2_list, r3_list, title=f"Animación - {titulo}")
plt.show()