# Solicitar entrada do usuário
input_str = input("Digite uma frase ou palavra: ")

# Inverter a frase ou palavra mantendo a ordem das palavras
inverted_str = ' '.join(reversed(input_str.split()))

# Imprimir o texto original
print("Texto: " + input_str)

# Imprimir a frase ou palavra invertida
print("Inverso: " + inverted_str)
