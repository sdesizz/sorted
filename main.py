from rich import print
from rich.progress import track
from time import sleep

arq = open("numbers.txt", "w+")
arqAux = open("numbersAux.txt", "w+")

print(":robot: Let's start!\n")
print("Instruções:\nI - Digite apenas valores inteiros entre 1 e 64;\nII - Digite -1, caso queira encerrar a execução do programa e visualizar, em ordem crescente, os valores salvos.\n")

# parte responsável por salvar os valores digitados no primeiro arquivo, sem repetição
while True:
    print("[bold]- Digite um valor: [/]", end = "")
    x = input()
    try:
        if int(x) != -1:
            if int(x) >= 1 and int(x) <= 64:
                arq.seek(0)
                if str(x) + "\n" not in arq.readlines():
                    arq.write(str(x) + "\n")
            else:
                print(":robot: [red]Alerta! Esse valor não foi salvo.[/]")    
        else:
            break
    except:
       print(":robot: [red]Apenas números![/]")
arq.seek(0)
print("\n")

# parte responsável por percorrer o primeiro arquivo e achar os menores valores sucessivamente e, assim, escrevê-los no segundo arquivo
menorAux = 0

for j in track(arq.readlines(), "Processando..."):
    menor = 65
    arq.seek(0)
    for i in arq.readlines():
        if int(i.split("\n")[0]) < menor and int(i.split("\n")[0]) > menorAux:
            menor = int(i.split("\n")[0])  
    arqAux.write(str(menor) + " ")
    menorAux = menor
    sleep(1)
arqAux.seek(0)
print("\n:robot: Valores em ordem crescente:", arqAux.readline(), "\n")
arq.close()
arqAux.close()