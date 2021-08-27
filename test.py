import pygame
from gui_engine import GUI, Box, BoxButton, SysText, HorizontalSlider

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("GUI Engine Test Window")

gui = GUI()
main_background = Box(800, 800, 0, 0, (30, 30, 30))
gui.add_element(main_background, -9999)
test_slider = HorizontalSlider(150, 150, 120, 5, (255, 0, 0), (0, 0, 255), Box(10, 10, 150, 150, (0, 0, 0), 0, 5))
gui.add_element(test_slider, 99999)

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    data = gui.draw(screen)
    pygame.display.update()
