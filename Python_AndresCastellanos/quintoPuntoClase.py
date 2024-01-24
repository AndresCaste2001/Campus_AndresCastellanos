palabra = input("Escribe una palabra:  \n")
if palabra == palabra[::-1]:
    print("Es palindromo")
elif palabra != palabra[::-1]:
    print("no es palindromo")