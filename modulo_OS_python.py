'''
Data Scientist: Eddy Giusepe Chirinos Isidro
O link de estudo: https://www.youtube.com/watch?v=ROCyIPA1wWA&t=1708s

'''

print("###################################")
print("# Cartilha biblioteca OS - Python #")
print("###################################")

'''
A biblioteca OS serve para poder navegar dentro do nosso computador através das pastas, arquivos, etc.
'''
# Importando a nossa biblioteca
import os

# Principais métodos
# Dados do sistema:
 
sistema = os.environ
print(sistema)
# Ele me traz um DICIONÁRIO (chave - valor) como respostas (arquivo .json)

print("")
print("Imprimimos, por exemplo o seguinte valor do campo USERNAME: ")
print(sistema["USERNAME"])


print("##########################")
print("# Trabalhando com Pastas #")
print("##########################")
# os.getcwd() --> Para saber em que pasta estou atualmente
print(os.getcwd())

# os.chdir()
novo_caminho = r"/home/eddygiusepe/5_praticando_Python/"
print(os.chdir(novo_caminho))






