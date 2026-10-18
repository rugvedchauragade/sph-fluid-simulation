import Config
import pygame
from Fluid import draw_grid

def handle_controls(keys):
    if keys[pygame.K_PLUS] or keys[pygame.K_EQUALS]:
        Config.delta = min(0.18, Config.delta + 0.005)
    elif keys[pygame.K_MINUS] or keys[pygame.K_UNDERSCORE]:
        Config.delta = max(0, Config.delta - 0.005)
    elif keys[pygame.K_UP]:
        Config.stiffness_constant += 10
    elif keys[pygame.K_DOWN]:
        Config.stiffness_constant = max(0, Config.stiffness_constant - 10)
    elif keys[pygame.K_w]:
        Config.interaction_radius += 1
    elif keys[pygame.K_s]:
        Config.interaction_radius = max(1, Config.interaction_radius - 1)
    elif keys[pygame.K_e]:
        Config.viscosity_strength += 0.05
    elif keys[pygame.K_d]:
        Config.viscosity_strength = max(0, Config.viscosity_strength - 0.05)
    elif keys[pygame.K_r]:
        Config.target_density = min(0.5, Config.target_density + 0.001)
    elif keys[pygame.K_f]:
        Config.target_density = max(0, Config.target_density - 0.001)
    elif keys[pygame.K_z]:
        Config.outlet_num_particles = max(0, Config.outlet_num_particles - 1)
    elif keys[pygame.K_x]:
        Config.outlet_num_particles += 1
    elif keys[pygame.K_l]:
        Config.drain_strength = max(0, Config.drain_strength - 1)
    elif keys[pygame.K_p]:
        Config.drain_strength += 20


def draw_debug_options(win, my_font, mouse_pos):
    draw_grid(win)
    pygame.draw.circle(win, (255, 0, 0), mouse_pos, Config.interaction_radius, 1)
    lines = [
        f'Delta (space/+/-): {Config.delta:.3f}',
        f'Stiffness/Pressure (up/down): {Config.stiffness_constant}',
        f'Interact Radius (w/s): {Config.interaction_radius}',
        f'Interact Strength: {Config.interaction_strength}',
        f'Viscosity (e/d): {Config.viscosity_strength:.2f}',
        f'Density (r/f): {Config.target_density:.4f}',
        f'Outlet particles (x/z): {Config.outlet_num_particles}',
        f'Outlet spray (c): {Config.outlet_spray},  paused (v): {Config.outlets_paused}',
        f'Drain strength (p/l): {Config.drain_strength},  paused (b): {Config.drains_paused}',
        f'Draw mode (n): {"drain" if Config.env_interact_drain else "outlet"}',
        f'Delete in drain (m): {Config.delete_particles_in_drain}',
    ]
    for i, line in enumerate(lines):
        win.blit(my_font.render(line, False, (255, 255, 255)), (0, 10 + i * 20))
