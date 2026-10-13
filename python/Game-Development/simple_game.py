import pygame


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.width = 640
        self.height = 480
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)

        self.speed = [1, 1]

        self.black = (0, 0, 0)

        self.ball, self.ballrect = self.load_image("sq.png")

        self.runing = True

    @staticmethod
    def load_image(image_name: str):
        Surface = pygame.image.load(image_name, "png")
        Rect = Surface.get_rect()
        return Surface, Rect

    def move_ball(self) -> None:
        ballrect = self.ballrect.move(self.speed)
        if ballrect.left < 0 or ballrect.right > self.width:
            self.speed[0] = -1 * self.speed[0]
        if ballrect.top < 0 or ballrect.bottom > self.height:
            self.speed[1] = -1 * self.speed[1]

        self.ballrect = ballrect

    def draw(self) -> None:
        self.screen.fill(self.black)
        self.screen.blit(self.ball, self.ballrect)
        pygame.display.update()

    @staticmethod
    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


# screen = pygame.display.set_mode((800, 600))

# red = (255, 0, 0)
# blue = (0, 0, 255)
# white = (255, 255, 255)


# square_x = 0
# square_speed = 5

# colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
# color_index = 0
# running = True

# while running:

#     screen.fill(white)

#     pygame.draw.rect(screen, colors[color_index], (square_x, 250, 50, 50))

#     square_x += square_speed
#     if square_x > 800:
#         square_x = -50

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             pygame.quit()

#         elif event.type == pygame.KEYDOWN:
#             color_index = (color_index + 1) % len(colors)

#     pygame.display.update()
#     pygame.time.delay(20)

# pygame.quit()
