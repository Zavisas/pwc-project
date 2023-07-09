def isAnagramOfPalindrome(s):
    char_count = {}
    odd_count = 0

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

        if char_count[char] % 2 == 0:
            odd_count -= 1
        else:
            odd_count += 1

    return odd_count <= 1

# Solicitar entrada do usuário
input_str = input("Digite uma palavra: ")

# Verificar se a palavra é um anagrama de um palíndromo
output = isAnagramOfPalindrome(input_str)

# Imprimir o resultado
print(output)
