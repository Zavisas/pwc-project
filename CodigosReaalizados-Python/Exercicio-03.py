def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

def longestPalindrome(s):
    if len(s) < 2:
        return s

    longest = ""
    for i in range(len(s)):
    
        substr1 = expandAroundCenter(s, i, i)
        if len(substr1) > len(longest):
            longest = substr1

       
        substr2 = expandAroundCenter(s, i, i + 1)
        if len(substr2) > len(longest):
            longest = substr2

    return longest

while True:
    # Solicitar entrada do usuário
    input_str = input("Digite a palavra de exemplo: ")

    # Verificar se a entrada é um número
    if input_str.isdigit():
        print("Entrada inválida. Digite uma palavra válida.")
    else:
        # Encontrar a maior substring palindrômica
        output_str = longestPalindrome(input_str)

        # Imprimir a substring palindrômica
        print("Substring palindrômica:", output_str)
        break
