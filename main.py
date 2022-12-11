import pygame as pg
import os

# TESTING SURFACE COLLISION USING MASKS

WIDTH = 750
AREA = WIDTH, WIDTH

OWIDTH, OHEIGHT = 1410 // 10, 910 // 10
OAREA = (OWIDTH, OHEIGHT)

clock = pg.time.Clock()

BG = pg.transform.scale(
  pg.image.load(os.path.join("assets", "background-black.png")), AREA)
ORN = pg.transform.scale(pg.image.load(os.path.join("assets", "orn-bact.png")),
                         OAREA)
MASK = pg.mask.from_surface(ORN)

pg.init()
win = pg.display.set_mode(AREA)
pg.display.set_caption("surface test")


class Orn():

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def draw(self, window):
    window.blit(ORN, (self.x, self.y))


def redraw_window():
  win.blit(BG, (0, 0))
  orn = Orn(10, 10)
  orn.draw(win)
  pg.display.update()


### Main Loop
def main():
  run = True
  while run:
    redraw_window()
    for event in pg.event.get():
      if (event.type == pg.QUIT):
        run = False
        print("Player quit")
        pg.quit()
      if (event.type == pg.MOUSEBUTTONUP):
        if pg.mouse.get_pos == WIDTH - OWIDTH:
          print("TOUCH")
        else:
          print("NO TOUCH")

  # Clamp the FPS to an upper-limit
  clock.tick_busy_loop(60)
  pg.quit()


main()