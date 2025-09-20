def main() -> None:
    """
    Cria um arquivo com base no nome e conteúdo fornecidos pelo usuário.

    Solicita um nome de arquivo, depois coleta linhas de conteúdo em um loop
    até que o usuário digite "stop". Por fim, salva o conteúdo em um
    arquivo .txt sem gerar saídas extras no console.
    """
    # Adicionando um espaço no final do prompt
    file_name = input("Enter name of the file: ")

    full_file_name = f"{file_name}.txt"

    content_lines = []

    while True:
        # Adicionando um espaço no final do prompt
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content_lines.append(line)

    try:
        with open(full_file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(content_lines))
    except IOError:
        pass


if __name__ == "__main__":
    main()
