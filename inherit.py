class Parent:
    def __init__(self):
        self.from_parent = True
        print(f"Hello, I'm parent!")

    def get_eye_color(self):
        return 'blue'

    def hi(self):
        return f'Hi, my eye color is: {self.get_eye_color()}'


class Child(Parent):
    def __init__(self):
        super().__init__()
        print(f"Hello, I'm Child!")

    def get_eye_color(self):
        return 'pink'

    def test(self):
        return super().get_eye_color()

child = Child()
print(child.hi())
print(child.test())

print('------------------------------------')
parent = Parent()
