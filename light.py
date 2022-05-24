import pygame

"""
    pygame.draw functions will not draw with alpha. The documentation says:

Most of the arguments accept a color argument that is an RGB triplet. These can also accept an RGBA quadruplet. The alpha value will be written directly into the Surface if it contains pixel alphas, but the draw function will not draw transparently.

What you can do is create a second surface and then blit it to the screen. Blitting will do alpha blending and color keys. Also, you can specify alpha at the surface level (faster and less memory) or at the pixel level (slower but more precise). You can do either:

s = pygame.Surface((1000,750))  # the size of your rect
s.set_alpha(128)                # alpha level
s.fill((255,255,255))           # this fills the entire surface
windowSurface.blit(s, (0,0))    # (0,0) are the top-left coordinates
or,

s = pygame.Surface((1000,750), pygame.SRCALPHA)   # per-pixel alpha
s.fill((255,255,255,128))                         # notice the alpha value in the color
windowSurface.blit(s, (0,0))
Keep in mind in the first case, that anything else you draw to s will get blitted with the alpha value you specify. So if you're using this to draw overlay controls for example, you might be better off using the second alternative.

Also, consider using pygame.HWSURFACE to create the surface hardware-accelerated.

Check the Surface docs at the pygame site, especially the intro.
"""

class Light:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.on = False
        self.intensity = 0
        self.radius = radius

    def draw(self, win):
        circle = pygame.draw.circle(
            win,
            (255, 255, 255),
            (self.x, self.y),
            self.radius
        )
        circle.set_alpha(self.intensity)
