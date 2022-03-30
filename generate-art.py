from PIL import Image, ImageDraw
import random

r = lambda: random.randint(50,255)
rc = lambda: ('#%02X%02X%02X' % (r(),r(),r()))
list_sym = []

def create_square(border, draw, random_color, element, size):
    if (element == int(size/2)):
        draw.rectangle(border, random_color)
    elif (len(list_sym) == element+1):
        draw.rectangle(border,list_sym.pop())
    else:
        list_sym.append(random_color)
        draw.rectangle(border, random_color)

def create_invader(border, draw, size):
    x0, y0, x1, y1 = border
    square_size = (x0-x1) - size
    
    # 3 random colours for the sprite 
    random_colors = [rc(), rc(), rc(), (0,0,0), (0,0,0), (0,0,0)]
    incrementer = 1
    element = 0

    for y in range(0, size):
        incrementer *= -1
        element = 0
        for x in range(0, size):
            topleft_x = x * square_size + x0
            topleft_y = y * square_size + y0
            bottomright_x = topleft_x + square_size
            bottomright_y = topleft_y + square_size

            create_square((topleft_x, topleft_y, bottomright_x, bottomright_y), draw, random.choice(random_colors), element, size)
            if (element == int(size/2) or element == 0):
                incrementer *= -1
            element += incrementer

def generate_art(size, path: str):
    print("Generating Art!")
    image = Image.new("RGB", (128, 128))
    draw = ImageDraw.Draw(image)

    create_invader((99,99,102,0), draw, size)
    image.save(path)

if __name__ == "__main__":
    for i in range(10):
        generate_art(7, f"test_image_{i}.png")
