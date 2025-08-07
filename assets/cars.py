import pygame

def draw(surface, pos: pygame.Vector2):
    car_size = pygame.Vector2(60, 120)
    car_body = pygame.Rect(pos.x, pos.y, car_size.x, car_size.y)

    pygame.draw.rect(surface, (0, 100, 255), car_body, border_radius=10)
    car_left_light = pygame.Rect(pos.x+10, pos.y-30, car_size.x, car_size.y)
    car_right_light = pygame.Rect(pos.x-10, pos.y-30, car_size.x, car_size.y)
    pygame.draw.rect(surface, (0, 100, 255), car_left_light, border_radius=10)
    pygame.draw.rect(surface, (0, 100, 255), car_right_light, border_radius=10)

