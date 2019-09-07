x = i = 0

def setup():
    background(255)
    size(400, 400)
    frameRate(24)

def draw():
    global x
    global i
    background(255)
    textSize(32)
    stroke(0)
    fill(0) 
    text(frameCount % 24, 100, 300)
    if (frameCount % 24) == 0:
        i += 30
    else:
        x = float( ( i * PI) / 180 )
    pushMatrix()
    translate(200,200)
    rotate(x)
    noFill()
    ellipse(0,0,100,100)
    line(0,0,0,-50)
    popMatrix()
    print(x)
    text("miReloj", 100, 50)
