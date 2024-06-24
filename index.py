#PAsso 01 - Percorrer todos os arquivos das pasta base de dados
import os
lista_arquivo = os.listdir("vendas")
print(lista_arquivo)

#para cada arquivo dentro (in) da lista de arquivo - Passo 02
#For variavel in lista_items:

for arquivo in lista_arquivo:
     #print(arquivo)
    #Se tem vendas está no nome do arquivo eu vou importar o arquivo.
    if "vendas" in arquivo:
        print(f"/Python{arquivo}")    
