colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []


pHit = sensor_right
pMiss = 1.0 - sensor_right
pExact = p_move
pUndershoot = 1.0 - p_move

def sense(p, Z):
    q=[]
    s = 0
    for i in range(len(p)):
        r = []
        for j in range(len(p[0])):
            hit = (Z == colors[i][j])
            r.append(p[i][j] * (hit * pHit + (1-hit) * pMiss))
        q.append(r)
        s += sum(r)

    for i in range(len(q)):
        for j in range(len(p[0])):
            q[i][j] = q[i][j] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        r = []
        for j in range(len(p[0])):
            s = pExact * p[(i-U[0]) % len(p)][(j-U[1]) % len(p[i])]
            s = s + pUndershoot * p[i][j]

            r.append(s)
        q.append(r)
    return q

def calculate():
    global pHit
    global pMiss
    global pExact
    global colors
    global pOvershoot
    global pUndershoot
    global motions
    global measurements

    pHit = sensor_right
    pMiss = 1.0 - sensor_right
    pExact = p_move
    pOvershoot = 1.0 - p_move
    pUndershoot = 1.0 - p_move
    q = []

    count = len(colors) * len(colors[0])
    for i in range(len(colors)):
        q.append([])
        for j in range(len(colors[i])):
            q[i].append( 1. / count )

    for k in range(len(motions)):
        q = move(q, motions[k])
        q = sense(q, measurements[k])


    return q

p = calculate()

#Your probability array must be printed
#with the following code.

show(p)




