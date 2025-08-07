import pygame

def normal_car(surface, world_pos: pygame.Vector2, angle):
    car_size = pygame.Vector2(60, 120)

    car_surf = pygame.Surface((car_size.x, car_size.y), pygame.SRCALPHA)
    pygame.draw.rect(car_surf, (0, 100, 190), (0, 0, car_size.x, car_size.y), border_radius=10)

    pygame.draw.rect(car_surf, (255, 0, 55), pygame.Rect(10, -10, 10, 20), border_radius=5)
    pygame.draw.rect(car_surf, (255, 0, 55), pygame.Rect(40, -10, 10, 20), border_radius=5)

    rotated_car = pygame.transform.rotate(car_surf, -angle)
    rotated_rect = rotated_car.get_rect(center=(world_pos.x, world_pos.y))

    surface.blit(rotated_car, rotated_rect.topleft)
