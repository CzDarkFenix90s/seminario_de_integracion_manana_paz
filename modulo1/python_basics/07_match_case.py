<<<<<<< HEAD
print("Match Case")
comando = input("Comando proceso iniciar/parar/reiniciar: ")
=======
print("match case")
comando = input("Comando proceso iniciar /para reiniciar")
>>>>>>> 51f428ebc607c993c742b2e79ae2c0153a998ec5
match comando:
    case "iniciar":
        print("Sistema iniciando")
    case "parar":
        print("deteniendose")
    case "reiniciar":
        print("reiniciando el sistema")
    case _:
<<<<<<< HEAD
        print(f"Comando '{comando}' no reconocido")

print("match condiciones")
numero = 7
match numero:
    case n if n<0:
        print(f"El numero {n} es negativo")
    case 0:
        print("Es cero")
    case n if n%2==0:
        print(f"El numero {n} es par")
=======
        print(f"comando `{comando}` no encontrado")

print("match condiciones")
numero=7
match numero:
    case n if n<0:
        print(f"{n}es negativo")
    case 0:
        print("Es cero")
    case n if n%2==0:
        print(f"{n} es par")
>>>>>>> 51f428ebc607c993c742b2e79ae2c0153a998ec5
    case n:
        print(f"{n} es positivo e impar")