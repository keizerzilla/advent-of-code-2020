# Parte 1
with open("input_3.txt") as infile:
    lines = [line.strip() for line in infile.readlines()]
    l = len(lines[0])
    x = 0
    i = 0
    trees = 0
    while i+1 < len(lines):
        x += 3
        trees += (lines[i+1][x%l] == "#")
        i += 1

print(trees)

# Parte 2 (errado)
with open("input_3.txt") as infile:
    lines = [line.strip() for line in infile.readlines()]
    l = len(lines[0])
    ax = 0
    bx = 0
    cx = 0
    dx = 0
    ex = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    i = 0
    while i+1 < len(lines):
        ax += 1
        bx += 3
        cx += 5
        dx += 7
        ex += 1
        
        a += (lines[i+1][ax%l] == "#")
        b += (lines[i+1][bx%l] == "#")
        c += (lines[i+1][cx%l] == "#")
        d += (lines[i+1][dx%l] == "#")
        if i+2 < len(lines):
            e += (lines[i+2][ex%l] == "#")
        
        i += 1

print(a, b, c, d, e, ">>>", a*b*c*d*e)

