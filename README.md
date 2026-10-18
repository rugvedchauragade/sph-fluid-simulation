# 💧 SPH Fluid Simulation

A real-time 2D fluid simulation built from scratch in Python using Smoothed Particle Hydrodynamics (SPH).

---

## About

Started as a gravity sim, pivoted to fluid simulation after watching a Veritasium video. Had to learn the actual math — SPH kernels, pressure gradients, viscosity — and implement everything by hand.

---

## Features

- SPH kernels from scratch (spiky, viscosity laplacian, pressure gradient)
- Spatial grid hashing for O(n) neighbor lookup — runs smoothly at 600+ particles
- XSPH velocity correction for smoother fluid behaviour
- Symmetric pressure forces — conserves momentum correctly
- Mouse interaction — attract or repel particles in real time
- Place fluid outlets and drains interactively
- Live parameter tuning — viscosity, pressure, density, timestep, all without restarting
- Particles coloured by speed using matplotlib viridis colormap

---

## Getting Started

### Install dependencies

```
pip install -r requirements.txt
```

### Run

```
python main.py
```

---

## Controls

| Input | Action |
|---|---|
| `Left click` | Attract particles toward cursor |
| `Right click` | Repel particles from cursor |
| `Middle click drag` | Place outlet or drain (toggle with N) |
| `Space` | Pause / unpause |
| `+` / `-` | Increase / decrease timestep |
| `↑` / `↓` | Increase / decrease pressure stiffness |
| `E` / `D` | Increase / decrease viscosity |
| `R` / `F` | Increase / decrease target density |
| `W` / `S` | Increase / decrease interaction radius |
| `X` / `Z` | Increase / decrease outlet particle count |
| `P` / `L` | Increase / decrease drain strength |
| `C` | Toggle outlet spray |
| `V` | Pause / unpause outlets |
| `B` | Pause / unpause drains |
| `N` | Switch between outlet and drain mode |
| `M` | Toggle particle deletion inside drains |
| `Enter` | Toggle debug overlay |
| `F5` | Reset simulation |

---

## How It Works

SPH represents fluid as a set of particles. Each particle's density, pressure and velocity are estimated by interpolating contributions from nearby neighbours using kernel functions.

**Each frame:**
1. Particles registered into a spatial grid for fast neighbour lookup
2. Density computed per particle via the spiky smoothing kernel
3. Pressure derived from density using a stiffness equation of state
4. Pressure gradient and viscosity forces accumulated per particle
5. Velocities integrated (semi-implicit Euler) and corrected with XSPH
6. Boundary collisions resolved with damping

**Kernels:**
- Density/pressure — Spiky: `(15 / π h⁶)(h − r)³`
- Viscosity — Müller Laplacian: `(45 / π h⁶)(h − r)`
- Pressure gradient — Spiky gradient

---

## Project Structure

```
├── main.py        # Main loop and event handling
├── Fluid.py       # All SPH physics
├── Controls.py    # Keyboard controls and debug overlay
├── Config.py      # All simulation parameters
├── requirements.txt
```

---

## Tuning Tips

- Particles exploding → lower timestep with `-`
- Fluid too stiff → lower stiffness with `↓`
- Particles clumping → increase target density with `R`
- Want thicker fluid → increase viscosity with `E`

---

## References

- Müller et al. (2003) — *Particle-Based Fluid Simulation for Interactive Applications*
- Monaghan (1992) — *Smoothed Particle Hydrodynamics*
- Schechter & Bridson (2012) — XSPH correction
