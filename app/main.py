def main() -> None:
    """
    Cria um arquivo com base no nome e conteúdo fornecidos pelo usuário.

    Solicita um nome de arquivo, depois coleta linhas de conteúdo em um loop
    até que o usuário digite "stop". Por fim, salva o conteúdo em um
    arquivo .txt.
    """
    file_name = input("Enter name of the file: ")
    full_file_name = f"{file_name}.txt"

    content_lines = []

    # O print() foi removido daqui.
    # O prompt agora está dentro do input() no loop.
    while True:
        line = input("Enter new line of content: ")  # <-- CORREÇÃO AQUI
        if line == "stop":
            break
        content_lines.append(line)

    try:
        with open(full_file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(content_lines))

        print(f"\n# Arquivo '{full_file_name}' criado com sucesso.")
        print("# Conteúdo do arquivo:")
        for content_line in content_lines:
            print(f"#{content_line}")

    except IOError as e:
        error_message = f"Ocorreu um erro ao escrever o arquivo: {e}"
        print(error_message)


if __name__ == "__main__":
    main()
