# s = "Hello"

class Sol:
    def Print(self,n):
        if n == 0:
            return
        self.Print(n-1)
        print(n,end=" ")

d = Sol()
d.Print(5)
print()