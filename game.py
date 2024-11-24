def init_state():
  return [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

class Game:
  def __init__(self):
    self.state = init_state()

  def running(self):
    return True;