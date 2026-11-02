def criar_arquivo():
    # Solicita o nome do arquivo
    nome_arquivo = input("Enter name of the file: ")
    
    # Garante que a extensão .txt seja adicionada se o usuário não a incluiu
    if not nome_arquivo.endswith(".txt"):
        nome_arquivo += ".txt"
    
    linhas = []
    
    # Loop para coletar o conteúdo até que o usuário digite 'stop'
    while True:
        linha = input("Enter new line of content: ")
        if linha == "stop":
            break
        linhas.append(linha)
    
    # Abre o arquivo e escreve cada linha com a quebra de linha correspondente
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            arquivo.write(linha + "\n")

if __name__ == "__main__":
    criar_arquivo()
