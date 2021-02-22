class A:
    def display():
        print("class A, called")

class B:
    def display():
        print("class B, called")
    def D():
        print("D, called")

class C(A, B):
    def main(self):
        A.display()
        B.display()
        

z = C()
z.main()

