WIDTH, HEIGHT = 800, 600
delta = 0.12
num_particles = 600
particle_size = 3
gravity = (0, 10)
mass = 5

max_speed = 100
collision_damping = 0.9
smoothing_radius = 12

target_density = 0.0038
viscosity_strength = 1.0
stiffness_constant = 500
xsph_epsilon = 0.1

interaction_strength = 0
interaction_radius = 100

grid_size = int(smoothing_radius * 1.2)

debug_mode = False

color_scheme = "viridis"

outlet_num_particles = 1
outlet_spray = True
outlets_paused = False

drain_strength = 100
drains_paused = False

env_interact_drain = True

delete_particles_in_drain = False
