def criar_arquivo():
    nome_arquivo = input("Enter name of the file: ")
    
    # Abrimos o arquivo para escrita logo em seguida ou armazenamos as linhas
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        while True:
            linha = input("Enter new line of content: ")
            if linha == "stop":
                break
            arquivo.write(linha + "\n")

if __name__ == "__main__":
    criar_arquivo()
