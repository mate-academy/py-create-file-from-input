def main() -> None:
    nome_arquivo = input("Digite o nome do arquivo: ")
    nome_arquivo += ".txt"
    conteudo = []

    while True:
        linha = input("Digite uma linha: ")
        if linha == "stop":
            break
        conteudo.append(linha)

    with open(nome_arquivo, "w") as arquivo:
        for linha in conteudo:
            arquivo.write(linha + "\n")


if __name__ == "__main__":
    main()
