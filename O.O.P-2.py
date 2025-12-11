class fruit:
  def __init__(self,name,flavour,colour):
    self.name=name
    self.flavour=flavour
    self.colour=colour
  def intro(self):
    print ("Hello i am" ,self.name)
fruit1=fruit("Bannana","sweet","yellow")
fruit1.intro()
