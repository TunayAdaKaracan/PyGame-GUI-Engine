#GUI Engine For Pygame
*Version 1.0.3*

###A GUI engine written using Python for the multimedia library Pygame. 


### Features:
* **Easy Usage**
* Check Box
* Buttons
* Image Buttons
* Horizontal Slider
* Text Input
* SysText (Text With Some Extra Features)
* Layering

Credits:
1. Shkryoav
2. Arctic Fox

#### Basic Example:
```py
# importing Engine
from gui_engine import GUI, Box, BoxButton

# Creating Main Gui
gui = GUI()

# Creating Box Object
background = Box(800, 800, 0, 0, (255, 0, 0)) # Look To Engine For Learning What Type Variables It Can Get

# Adding Box Element To A Layer
gui.add_element(background, -999)

# Finally Just Do This On Your Game Loop
gui.draw(surface)

# ----------------------

# Getting Values From Buttons And Etc.
my_button = BoxButton(100, 100, 50, 50, (255, 255, 255), (220, 220, 220))

gui.add_element(my_button, 10)

data = gui.draw(surface)

print(data[my_button])

# OR
def callback():
    print("Callback To MyButton Var")

my_button.direct_call = callback # This is going to be called on click
```