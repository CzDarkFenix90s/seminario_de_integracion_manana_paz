<<<<<<< HEAD
#  Enteros, Cadena de caracteres, Booleanos, none

nombre = 'Ana Garcia' #string
edad = 28             #int
altura = 1.65         #float
activo = True         #boolean
nulo = None           #NoneType
=======
#Enteros, Cadena de caracteres , booleano, None
nombre="Ana Garcia" #string
edad=28             #int
altura:1.65         #float
activo= True        #fool
nulo=None           #NoneType
>>>>>>> 51f428ebc607c993c742b2e79ae2c0153a998ec5

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(activo))
print(type(nulo))

<<<<<<< HEAD

#Asignar valor varias variables en una linea 
a, b, c = 12, 13, 14
=======
#Asignar valor varias variables en una linea
a, b, c = 1, 2, 3
>>>>>>> 51f428ebc607c993c742b2e79ae2c0153a998ec5
print(a)
print(b)
print(c)

<<<<<<< HEAD
#Asignar el mismo  valor a varias variables
=======
#Asignar el mismo valor a varias variables
>>>>>>> 51f428ebc607c993c742b2e79ae2c0153a998ec5
a = b = c = 0
print(a)
print(b)
print(c)

#Intercambiar valores
<<<<<<< HEAD
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

#Convenciones de nombres
nombre_completo = "Ana Garcia"     #snake_case
NombreCompleto = "Ana Garcia"      #NO USAR camelCase
MAX_REINTENTOS = 3                 #CONSTANTE, USAR MAYUSCULAS
_variable_interna = "privada"      #para uso interno

#Manejo de Enteros
pequeno = 42
negativo = -17
grande= 1_000_000_000_000
enorme = 2 ** 100
print(pequeno)
=======
x,y = 10,20
print(x,y)
x,y = y,x
print(x,y)

#Convenciones de nombres
nombre_completo="Rafael Urdaneta"       #snake_case
nombreCompleto="Rafael Urdaneta"        #no usar camelCase
MAX_REINTENTOS=3                        #Mayusculas sostenidas para constantes
_variable_interna="privada"             #para uso interno

# Manejo de Enteros
puqueno = 42
negativo = -17
grande=1_000_000_000_000
enorme= 2 ** 100

print(puqueno)
>>>>>>> 51f428ebc607c993c742b2e79ae2c0153a998ec5
print(negativo)
print(grande)
print(enorme)

<<<<<<< HEAD

#Bases Numericas
binario = 0b1010
octal = 0o17
hexadecimal = 0xFF
print(binario, octal, hexadecimal)


#convertir a decimal a otras bases
print(bin(255))   #binario
print(oct(255))   #octal
print(hex(255))   #hexadecimal

=======
# Bases Numericas
binario=0b1010
octal=0o17
exadecimal=0xFF
print(binario, octal, hexadecimal) 

print(bin(255))
print(oct(255))
print(hex(255))
>>>>>>> 51f428ebc607c993c742b2e79ae2c0153a998ec5
