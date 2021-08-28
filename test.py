import pygame
from gui_engine import GUI, Box, BoxButton, SysText, HorizontalSlider, TextInput, CheckBox, InvisibleButton

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("GUI Engine Test Window")

gui = GUI()
main_background = Box(800, 800, 0, 0, (30, 30, 30))
gui.add_element(main_background, -9999)

text_input = TextInput(0, 0, 150, 30, "Comic Sans MS", 20, (0, 0, 0), background_color=(255, 255, 255), scroll_after_max =True)
gui.add_element(text_input)

check = CheckBox(80, 80, 20, 20, 2, (255, 255, 255), (0, 0, 0), round=5)
gui.add_element(check, 50)


def callback():
    print("Clicked to Invisible Button")


inv_button = InvisibleButton(350, 350, 350, 350)
inv_button.direct_call = callback
gui.add_element(inv_button, 63945863)

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    data = gui.draw(screen)
    pygame.display.update()
