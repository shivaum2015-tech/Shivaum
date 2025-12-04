class tootfruit:
 def __init__(self,name,flavour,colour):
    self.name=name
    self.flavour=flavour
    self.colour=colour
 def eat(self)  :
  print ("You can eat ",self.name)
apple=tootfruit("apple","sweet","red")
print (apple.eat())