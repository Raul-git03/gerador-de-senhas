import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    gerar = ''.join(random.choice(caracteres) for i in range(tamanho))
    return gerar
    
print('🔐 Gerador de Senhas\n')
tamanho = int(input('Digite o tamanho da senha: '))
print(f'Senha gerada: {gerar_senha(tamanho)}')