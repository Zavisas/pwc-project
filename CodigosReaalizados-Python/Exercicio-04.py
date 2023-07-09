def capitalizeFirstLetter(sentence):
    # Remove espaços em branco extras no início e no fim da frase
    sentence = sentence.strip()

    # Verifica se a frase não está vazia
    if sentence:
        # Aplica a capitalização na primeira letra da frase
        sentence = sentence[0].capitalize() + sentence[1:]

    return sentence

# Solicitar entrada do usuário
input_str = input("Digite uma frase ou palavra: ")

# Colocar a primeira letra em maiúscula
output_str = capitalizeFirstLetter(input_str)

# Imprimir a string com a primeira letra em maiúscula
print("Palavra/Frase com a primeira letra em maiúscula:", output_str)
