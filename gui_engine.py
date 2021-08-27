#   _____ _    _ ______   ______             _
#  / ____| |  | |_   _|  |  ____|           (_)
# | |  __| |  | | | |    | |__   _ __   __ _ _ _ __   ___
# | | |_ | |  | | | |    |  __| | '_ \ / _` | | '_ \ / _ \
# | |__| | |__| |_| |_   | |____| | | | (_| | | | | |  __/
#  \_____|\____/|____|   |______|_| |_|\__, |_|_| |_|\___|
#                                      __/ |
#                                     |___/
# Version: 1.0.0 | Alpha
import pygame


class GUI:
    def __init__(self):
        self.elements = []

    def __str__(self):
        return f"<GUI items={len(self.elements)}>"

    def draw(self, surface):
        returns = {}
        for level, element in sorted(self.elements):
            data = element.draw(surface)
            if data is not None:
                returns[element] = data
        return returns

    def add_element(self, element, level=0):
        self.elements.append([level, element])


class Box:
    def __init__(self, w, h, x=0, y=0, color=(0, 0, 0), width=0, rounded=0):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.width = width
        self.round = rounded

    def __str__(self):
        return f"<Box width={self.rect.w} height={self.rect.h} x={self.rect.x}" \
               f" y={self.rect.y} color= {self.color} draw_type={self.width}>"

    def draw(self, surface):
        max_round = min(self.rect.w, self.rect.h) / 2
        pygame.draw.rect(surface, self.color, self.rect, self.width, self.round if self.round <= max_round else 0)


class BoxButton:
    def __init__(self, w, h, x=0, y=0, color=(255, 255, 255), click_color=None, highlite_color=None, **kwargs):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.click_color = click_color
        self.highlite_color = highlite_color
        self.ticks = kwargs.get("ticks") or 50
        self._current_tick = 0
        self._click = False
        self._highlite = False

    def __str__(self):
        return f"<BoxButton width={self.rect.w} height={self.rect.h} x={self.rect.x}" \
               f" y={self.rect.y} color= {self.color}>"

    def draw(self, surface):
        self.update()
        if self._click:
            pygame.draw.rect(surface, self.click_color, self.rect)
        elif self._highlite:
            pygame.draw.rect(surface, self.highlite_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
        return {"click": self._click, "highlite": self._highlite}

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed(3)
        if self._current_tick != 0:
            self._current_tick -= 1
        else:
            self._click = False

        if self.rect.collidepoint(mouse_pos) and mouse_buttons[0]:
            self._click = True
            self._current_tick = self.ticks
        elif self.rect.collidepoint(mouse_pos):
            self._highlite = True
        else:
            self._highlite = False


class ImageButton:
    def __init__(self, x, y, Image, ClickImage=None, HighliteImage=None, **kwargs):
        self.image = Image.copy()
        self.rect = self.image.get_rect(x=x, y=y)
        self.click_image = ClickImage or Image.copy()
        self.highlite_image = HighliteImage
        self.ticks = kwargs.get("ticks") or 60
        self._current_tick = 0
        self._click = False
        self._highlite = False

    def __str__(self):
        return f"<ImageButton width={self.rect.w} height={self.rect.h} x={self.rect.x} y={self.rect.y}>"

    def draw(self, surface):
        self.update()
        if self._click:
            surface.blit(self.click_image, self.rect)
        elif self._highlite and self.highlite_image is not None:
            surface.blit(self.highlite_image, self.rect)
        else:
            surface.blit(self.image, self.rect)
        return {"click": self._click, "highlite": self._highlite}

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed(3)
        if self._current_tick != 0:
            self._current_tick -= 1
        else:
            self._click = False

        if self.rect.collidepoint(mouse_pos) and mouse_buttons[0]:
            self._click = True
            self._current_tick = self.ticks
        elif self.rect.collidepoint(mouse_pos):
            self._highlite = True
        else:
            self._highlite = False


class SysText:
    def __init__(self, x, y, font_name, font_size, text, color=(0,0,0), background_color=None, **kwargs):
        self.font = pygame.font.SysFont(font_name, font_size)
        self.text = text
        self.pos = (x, y)
        self.color = color
        self.background_color = background_color
        self.max_width = kwargs.get("max_width") or 0
        self.anti_allias = kwargs.get("anti_allias") or False
        self.transparent = kwargs.get("transparent") or False

    def __str__(self):
        return f"<SysText x={self.pos[0]} y={self.pos[1]} color={self.color} text={self.text}>"

    def draw(self, surface):
        if self.background_color == None:
            render = self.font.render(self.text, self.anti_allias, self.color)
        else:
            render = self.font.render(self.text, self.anti_allias, self.color, self.background_color)
        if self.transparent:
            render.convert_alpha()
        if self.max_width != 0 and render.get_width() > self.max_width:
            render = render.subsurface(render.get_rect(w=self.max_width))
        surface.blit(render, self.pos)

    def change_font(self, font_name, font_size):
        self.font = pygame.font.SysFont(font_name, font_size)


class HorizontalSlider:
    def __init__(self, x, y, length, height_bar, fill_color, empty_color, box: Box):
        self.fill_percent = 0
        self.fill_color = fill_color
        self.empty_color = empty_color
        self.click_box = box
        self.click_box.rect.centerx = x
        self.click_box.rect.centery = y + (height_bar / 2)
        self._borders = (x, x+length)
        self._fill_box = pygame.Rect(x, y, 0, height_bar)
        self._empty_box = pygame.Rect(x, y, length, height_bar)
        self._focus = False

    def __str__(self):
        return "<HorizontalSlider>"

    def draw(self, surface):
        self.update()
        pygame.draw.rect(surface, self.empty_color, self._empty_box)
        pygame.draw.rect(surface, self.fill_color, self._fill_box)
        self.click_box.draw(surface)
        return {"focus": self._focus, "percentage": self.fill_percent}

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        buttons = pygame.mouse.get_pressed(3)

        if self.click_box.rect.collidepoint(mouse_pos) and buttons[0]:
            self._focus = True
        elif self._focus and not buttons[0]:
            self._focus = False

        rel = pygame.mouse.get_rel()
        if self._focus:
            if self._borders[0] <= self.click_box.rect.centerx + rel[0] <= self._borders[1]:
                self.click_box.rect.x += rel[0]
                self.fill_percent = (self.click_box.rect.centerx - self._empty_box.x) / self._empty_box.w
            else:
                if rel[0] > 0:
                    self.click_box.rect.centerx = self._empty_box.x + self._empty_box.w
                    self.fill_percent = 1.0
                elif rel[0] < 0:
                    self.click_box.rect.centerx = self._empty_box.x
                    self.fill_percent = 0.0

        self._fill_box.w = self.fill_percent * self._empty_box.w