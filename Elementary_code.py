import pygame

pygame.init()

GameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("The best game ever")

clock = pygame.time.Clock()

teal = (0, 128, 128)
red = (255, 0, 0)
lime = (0, 255, 0)

begin = [400, 300]

done = True

while done:

    GameDisplay.fill(teal)

    pygame.draw.rect(GameDisplay, red, pygame.Rect(*begin, 60, 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == 1073741903:
                print("+", event)
                begin[0] += 30
                pygame.draw.rect(GameDisplay, red, pygame.Rect(*begin, 60, 60))
            elif event.key == 1073741904:
                begin[0] -= 30
                pygame.draw.rect(GameDisplay, red, pygame.Rect(*begin, 60, 60))
                print("-", event)
            elif event.key == 1073741906:
                begin[1] -= 30
                pygame.draw.rect(GameDisplay, red, pygame.Rect(*begin, 60, 60))
                print("-", event)
            elif event.key == 1073741905:
                begin[1] += 30
                pygame.draw.rect(GameDisplay, red, pygame.Rect(*begin, 60, 60))
                print("+", event)


    pygame.display.update()

    clock.tick(60)