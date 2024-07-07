def char_to_value(char):
    if char.isdigit():
        return int(char)
    else:
        return ord(char) - 55

def validate_numero_documento(numero):
    # Remove espaços
    numero = numero.replace(" ", "")
    
    # Substituir letras
    numero_convertido = [char_to_value(c) for c in numero]
    
    # Passos 3 e 4
    soma = 0
    for i in range(len(numero_convertido) - 1, -1, -1):
        valor = numero_convertido[i]
        if (len(numero_convertido) - i) % 2 == 0:
            valor *= 2
            if valor >= 10:
                valor -= 9
        soma += valor
    
    # Passo 5
    return soma % 10 == 0

# Pergunta pelo seu número de documento
numero_documento = input("Digite o número de documento (formato: DDDDDDDD C AAT): ")

# Valida se está tudo bem
if validate_numero_documento(numero_documento):
    print("O número de documento é válido.")
else:
    print("O número de documento é inválido.")

# Faz uma pausa pra vc poder ler
input("Pressione Enter para sair...")