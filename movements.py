import pygame
import math


def keyboard_moves_car(car_angle, car_pos, dt, speed, rotation_speed, max_speed, acceleration, deceleration, reverse_speed, velocity):
    keys = pygame.key.get_pressed()

    rad = math.radians(car_angle)

    direction = pygame.Vector2(math.sin(rad), -math.cos(rad))

    if keys[pygame.K_w]:
        velocity += acceleration * dt
        velocity = min(velocity, max_speed)

        if keys[pygame.K_d]:
            car_angle += rotation_speed * dt
        if keys[pygame.K_a]:
            car_angle -= rotation_speed * dt


    elif keys[pygame.K_s]:
        velocity -= acceleration * dt
        velocity = max(velocity, reverse_speed)

        if keys[pygame.K_a]:
            car_angle += rotation_speed * dt
        if keys[pygame.K_d]:
            car_angle -= rotation_speed * dt

    else:
        if velocity > 0:
            velocity -= deceleration * dt
            velocity = max(velocity, 0)
        elif velocity < 0:
            velocity += deceleration * dt
            velocity = min(velocity, 0)

    car_pos += direction * velocity * speed

    return car_angle, velocity

