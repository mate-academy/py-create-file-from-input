def main() -> None:
    # Solicita o nome do arquivo
    file_name = input("Enter name of the file: ")

    # Garante que o arquivo tenha extensão .txt
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    lines: list[str] = []

    # Loop para coletar o conteúdo
    while True:
        line = input("Enter new line of content: ")

        if line.lower() == "stop":
            break

        lines.append(line)

    # Cria e escreve no arquivo
    with open(file_name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")

    print(f'File "{file_name}" created successfully!')


if __name__ == "__main__":
    main()
