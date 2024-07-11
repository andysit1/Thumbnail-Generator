import os
import pygame as pg


#grabs the first frame (we can just call this after generating the video)
def grab_first_frame(self, filename):
  if os.path.exists(filename):
    raise TypeError("Path does not exist")
  img = pg.image.load(filename).convert_alpha()
  return pg.transform.scale(img, (1280, 720))




