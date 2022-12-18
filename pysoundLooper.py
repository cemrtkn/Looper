import threading
import pygame

pygame.mixer.init()

class loopingThread (threading.Thread):
  def __init__(self,file_name):
    threading.Thread.__init__(self)
    self.file_name=file_name
  def run(self):
    self.channel=pygame.mixer.Sound(self.file_name)
    self.channel.play(loops=-1)
  def stop(self):
    self.channel.stop()
