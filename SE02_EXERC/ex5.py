# Auth: Margarida Balola
# Version: 0.0.1
# data: 02/03/2022
# dupdateat: --/--/--

# declaracao de variaveis
a = 2
b = 3
c = 5
d = 7

#b toma o valor de c
def variavel_global():
    global b
    b = c
print(b)

variavel_global()
print(b)

#c toma o valor de a
def variavel_global():
    global c
    c = a
print(c)

variavel_global()
print(c)

#a toma o valor de d
def variavel_global():
    global a
    a = d
print(a)

variavel_global()
print(a)

#d toma o valor de b
def variavel_global():
    global d
    d = b
print(d)

variavel_global()
print(d)
#está a ficar com o valor de C porque o b ja tinha ficado com o valor de c


