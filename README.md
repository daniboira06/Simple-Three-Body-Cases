# Simple Three-Body Cases 🌍🌕⭐

Simulación numérica del problema de tres cuerpos en 2D usando Python.

## Descripción

Este proyecto implementa la simulación del movimiento de tres cuerpos bajo su atracción gravitacional mutua. Incluye casos clásicos con solución conocida y un modo personalizado para explorar comportamiento caótico.

## Estructura del proyecto
```
3-cossos/
├── main.py            # Script principal con menú interactivo
├── three_body.py      # Física: aceleraciones y energía
├── integrators.py     # Métodos de integración numérica
├── plots.py           # Gráficos y animación
├── requirements.txt   # Librerías necesarias
├── examples/
│   └── demo.ipynb     # Notebook de demostración
└── README.md
```

## Instalación
```bash
pip install -r requirements.txt
```

## Uso
```bash
python3 main.py
```

El programa te guiará por un menú interactivo:
```
╔══════════════════════════════════════╗
║   THREE-BODY SIMULATION              ║
╠══════════════════════════════════════╣
║  1. Lagrange (triángulo equilátero)  ║
║  2. Euler (colineal)                 ║
║  3. Órbita en 8                      ║
║  4. Personalizado                    ║
╚══════════════════════════════════════╝
```

## Casos disponibles

**1. Lagrange**
Los tres cuerpos forman un triángulo equilátero que rota. Solución estable con masas iguales.

**2. Euler**
Los tres cuerpos están alineados. Solución inestable, los cuerpos externos se disparan.

**3. Órbita en 8**
Los tres cuerpos se persiguen formando una figura de infinito. Solución periódica descubierta por Chenciner y Montgomery (2000).

**4. Personalizado**
Introduce tus propias masas, posiciones y velocidades iniciales y observa el comportamiento.

## Integradores disponibles

| Integrador | Precisión | Conserva energía |
|------------|-----------|-----------------|
| Euler      | Baja      | No              |
| Verlet     | Media     | Sí (aprox.)     |
| RK4        | Alta      | Sí              |

## Ejemplos de resultados

- **Lagrange**: órbitas circulares perfectas, energía constante
- **Euler**: inestabilidad inmediata, cuerpos que se escapan
- **Órbita en 8**: trayectoria periódica en forma de infinito