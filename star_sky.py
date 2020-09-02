import random
from PIL import Image, ImageDraw


def star_brightness():
    #favor dimmer stars
    rand_val = random.normalvariate(128, 100)

    if rand_val < 0:
        rand_val = 0
    elif rand_val > 255:
        rand_val = 255

    return int(rand_val)


def star_color():
    r_bound = 255
    g_bound = 255
    b_bound = 255

    roy = random.randint(200, r_bound)
    gee = random.randint(200, g_bound)
    biv = random.randint(200, b_bound)

    if gee > roy:
        gee = roy
    elif gee > biv:
        gee = biv

    return roy, gee, biv


def generate_image(image_size, star_freq):
    sky_im = Image.new("RGB", image_size, (0, 0, 0))
    print(sky_im.format, sky_im.mode, sky_im.size)

    star_im = ImageDraw.Draw(sky_im, "RGBA")

    for i in range(sky_im.size[0]):
        for j in range(sky_im.size[1]):
            if random.random() < star_freq:
                r, g, b = star_color()
                star_im.point((i, j), (r, g, b, star_brightness()))

    sky_im.show()
    return sky_im


