import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
screen.fill((255, 255, 255))
pygame.display.update()
pen_color = (0, 0, 0)
pen_size = 1

while True:
    command = input()
    command_parts = command.split()

    if command_parts[:2] == ["change", "color"]:
        red, green, blue = map(int, command_parts[2:])
        pen_color = (red, green, blue)

    elif command_parts[:2] == ["change", "size"]:
        pen_size = int(command_parts[2])

    elif command_parts[:2] == ["draw", "line"] and len(command_parts) == 6:
        x1, y1, x2, y2 = map(int, command_parts[2:])
        pygame.draw.line(screen, pen_color, (x1, y1), (x2, y2), pen_size)
        pygame.display.update()

    elif command_parts[:2] == ["draw", "circle"] and len(command_parts) == 5:
        cx, cy, rad = map(int, command_parts[2:])
        pygame.draw.circle(screen, pen_color, (cx, cy), rad, pen_size)
        pygame.display.update()

    elif command_parts[:2] == ["draw", "polygon"]:
        coordinates = list(map(int, command_parts[2:]))

        points = []
        for i in range(0, len(coordinates), 2):
            points.append((coordinates[i], coordinates[i + 1]))

        pygame.draw.polygon(screen, pen_color, points, pen_size)
        pygame.display.update()

    elif command == "end drawing":
        pygame.image.save(screen, "draw.png")
        break
