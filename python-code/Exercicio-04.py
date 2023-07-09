while True:
    palavra = input("Digite uma palavra: ")

    if palavra.isalpha():
        output_str = palavra.capitalize()
        print("Palavra com a primeira letra maiúscula:", output_str)
        break
    else:
        print("Entrada inválida. Digite uma palavra válida.")