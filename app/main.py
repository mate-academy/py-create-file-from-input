def main() -> None:
    nome_arquivo = input("Enter name of the file: ")

    if not nome_arquivo.endswith(".txt"):
        nome_arquivo += ".txt"

    linhas = []

    while True:
        linha = input("Enter new line of content: ")
        if linha == "stop":
            break
        linhas.append(linha)

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            arquivo.write(linha + "\n")


if __name__ == "__main__":
    main()
