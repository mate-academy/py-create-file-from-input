def main() -> None:
    nome_arquivo = input("Enter name of the file: ")
    nome_arquivo += ".txt"
    conteudo = []

    while True:
        linha = input("Enter new line of content: ")
        if linha == "stop":
            break
        conteudo.append(linha)

    with open(nome_arquivo, "w") as arquivo:
        for linha in conteudo:
            arquivo.write(linha + "\n")


if __name__ == "__main__":
    main()
