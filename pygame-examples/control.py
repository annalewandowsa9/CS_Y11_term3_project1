import pygame
from const import Colors, Window, Gravity
from object import Object



def control_object(obj):
    if pygame.key.get_pressed()[pygame.K_UP]:
        obj.v_x -= 10
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        obj.v_x += 10
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        obj.v_y += 10
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        obj.v_y -= 10
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        obj.v_x = 0
        obj.v_y = 0


def main():
    obj = Object(
        x=10,
        y=30,
        height=10,
        width=30,
        v_x=0,
        v_y=0,
        color=Colors.BLUE,
    obj = Object(
        x=200,
        y=30,
        height=10,
        width=30,
        v_x=0,
        v_y=0,
        color=Colors.PINK,
    )
    timestep = 10
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(Window.SIZE)  # Displaying on specified window size
    pygame.display.set_caption("Our game")
    run = True
    while run:
        clock.tick(timestep)
        surface.fill(Colors.GREEN)  # Window Bg

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # To quit on clicking the X
                run = False
        control_object(obj)
        obj.update(Gravity.Ui, timestep / 1000)
        obj.draw(surface)
        pygame.display.update()  # To update the display with newly added codes

    pygame.quit()


main()