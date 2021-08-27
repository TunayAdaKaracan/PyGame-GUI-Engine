import pygame
from gui_engine import GUI, Box, BoxButton, SysText, HorizontalSlider, TextInput

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("GUI Engine Test Window")

gui = GUI()
main_background = Box(800, 800, 0, 0, (30, 30, 30))
gui.add_element(main_background, -9999)

text_input = TextInput(0, 0, 150, 30, "Comic Sans MS", 20, (0, 0, 0), background_color=(255, 255, 255), scroll_after_max =True)
gui.add_element(text_input)

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    data = gui.draw(screen)
    print(data)
    pygame.display.update()
