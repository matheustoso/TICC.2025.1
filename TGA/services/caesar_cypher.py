import math

#region LOCAL CONSTANTS

#endregion

#region ENCRYPT
def encrypt(input, key) -> str:
    output = ""
    
    # verificamos cada caracter da mensagem
    for char in input:
        # caso o caracter esteja no alfabeto ele será cifrado, caso contrário, permanecerá o mesmo caracter
        if char.isalpha():
            # aqui a função ord() nos retorna o valor decimal do caracter na tabela ASCII, utilizamos ele pois a tabela ASCII tem todos os caracteres do alfabeto ordenados, maiúsculos e minúsculos.
            # inicialmente pegamos a diferença do caracter e da primeira letra do alfabeto, cuidando para checar se é minúsculo ou maiúsculo, assim temos a posição do caracter no alfabeto.
            # então somamos a chave à posição, e pegamos o resto da divisão da posição+chave por 26 (comprimento do alfabeto), assim temos a posição do caracter que será cifrado no local do original
            # e no fim adicionamos novamente o decimal do primeiro caracter do alfabeto em ASCII para a função chr() buscar o valor correto na tabela ASCII
            output += chr(((ord(char) - ord('A') + key) % 26) + ord('A')) if char.isupper() else chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            
        else:
            output += char
    
    return output
#endregion

#region DECRYPT
def decrypt(input, key) -> str: 
    output = ""
    
    # verificamos cada caracter da mensagem
    for char in input:
        # caso o caracter esteja no alfabeto ele será decifrado, caso contrário, permanecerá o mesmo caracter
        if char.isalpha():
            # aqui a função ord() nos retorna o valor decimal do caracter na tabela ASCII, utilizamos ele pois a tabela ASCII tem todos os caracteres do alfabeto ordenados, maiúsculos e minúsculos.
            # inicialmente pegamos a diferença do caracter e da primeira letra do alfabeto, cuidando para checar se é minúsculo ou maiúsculo, assim temos a posição do caracter no alfabeto.
            # então subtraímos a chave da posição, e pegamos o resto da divisão da posição-chave por 26 (comprimento do alfabeto), assim temos a posição do caracter original que será decifrado
            # e no fim adicionamos novamente o decimal do primeiro caracter do alfabeto em ASCII para a função chr() buscar o valor correto na tabela ASCII
            output += chr(((ord(char) - ord('A') - key) % 26) + ord('A')) if char.isupper() else chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            
        else:
            output += char
    
    return output
#endregion