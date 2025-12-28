class reverse:
    def __init__(self, string = ""):
        self.string=string
    def reverse_str(self):
        words = self.string.split()
        return " ".join(words[::-1])
x=input("write a word ")
obj1 = reverse(x)
print (obj1.reverse_str())