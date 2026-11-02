def criar_arquivo():
    # Solicita o nome do arquivo ao usuário
    nome_arquivo = input("Enter name of the file: ")
    
    # Garante que a extensão seja .txt
    if not nome_arquivo.endswith(".txt"):
        nome_arquivo += ".txt"
    
    linhas = []
    
    # Loop para coletar o conteúdo até que o usuário digite 'stop'
    while True:
        linha = input("Enter new line of content: ")
        if linha.lower() == "stop":
            break
        linhas.append(linha)
    
    # Cria o arquivo e escreve o conteúdo coletado
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for l in linhas:
            arquivo.write(l + "\n")

    print(f"\nArquivo '{nome_arquivo}' criado com sucesso!")

# Executa o aplicativo
if __name__ == "__main__":
    criar_arquivo()
