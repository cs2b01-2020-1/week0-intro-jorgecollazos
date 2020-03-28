def comparacion(aa, bb):
    list = []
    list.append(open(aa).readlines())
    list.append(open(bb).readlines())

    for i in range(len(list)):
        list[i].pop(0)
        for j in range(len(list[i])):
            list[i][j] = list[i][j].replace("\n", "")

    coincidencia = 0

    txt1 = ""
    for i in list[0]:
        txt1 += i
    txt2 = ""
    for i in list[1]:
        txt2 += i

    if len(txt1) < len(txt2):
        mayor = txt2
        menor = txt1
    else:
        mayor = txt1
        menor = txt2

    for i in range(len(mayor)):
        if i <= len(menor)-1:
            if txt1[i] == txt2[i]:
                coincidencia += 1

    porcentaje = (coincidencia / len(mayor)) * 100
    return porcentaje

def imprime(x, y):
    return round(comparacion(x, y), 2)

title = 'Porcentaje de coincidencias entre genomas'
print(title.center(60, " "))
print()

a = 'AY274119.txt'
b = 'AY278488.2.txt'
c = 'MN908947.txt'
d = 'MN988668.txt'
e = 'MN988669.txt'

print('{:^11}{:^11}{:^11}{:^11}{:^11}{:^11}'.format('        ', 'AY274119', 'AY278488.2', 'MN908947', 'MN988668', 'MN988669'))
for i in range(5):
    if i == 0:
        print('{:^11}{:^11}{:^11}{:^11}{:^11}{:^11}'.format('AY274119', imprime(a, a), imprime(a, b), imprime(a, c), imprime(a, d), imprime(a, e)))
    elif i == 1:
        print('{:^11}{:^11}{:^11}{:^11}{:^11}{:^11}'.format('AY278488.2', imprime(b, a), imprime(b, b), imprime(b, c), imprime(b, d), imprime(b, e)))
    elif i == 2:
        print('{:^11}{:^11}{:^11}{:^11}{:^11}{:^11}'.format('MN908947', imprime(c, a), imprime(c, b), imprime(c, c), imprime(c, d), imprime(c, e)))
    elif i == 3:
        print('{:^11}{:^11}{:^11}{:^11}{:^11}{:^11}'.format('MN988668', imprime(d, a), imprime(d, e), imprime(d, c), imprime(d, d), imprime(d, e)))
    elif i == 4:
        print('{:^11}{:^11}{:^11}{:^11}{:^11}{:^11}'.format('MN988669', imprime(e, a), imprime(e, b), imprime(e, c), imprime(e, d), imprime(e, e)))
