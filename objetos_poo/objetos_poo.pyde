from walker import Walker

w1 = Walker(150, 150, [255, 100, 100])

def setup():
    background(0)
    size(600, 600)

def draw():
    w1.walk()
    w1.display()
