def criar_arquivo():
    # Solicita o nome do arquivo
    nome_arquivo = input("Enter name of the file: ")
    
    # Garante que a extensão seja .txt caso não tenha sido informada
    if not nome_arquivo.endswith(".txt"):
        nome_arquivo += ".txt"
    
    linhas = []
    
    # Loop para capturar o conteúdo até digitar 'stop'
    while True:
        linha = input("Enter new line of content: ")
        if linha.strip() == "stop":
            break
        linhas.append(linha)
    
    # Escreve o conteúdo no arquivo unindo as linhas por '\n' (sem quebra extra no final)
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(linhas))

if __name__ == "__main__":
    criar_arquivo()
