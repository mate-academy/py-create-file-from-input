def create_file_from_input() -> None:
    # Solicita o nome do arquivo
    file_name = input("Enter name of the file: ").strip()
    content_lines = []

    # Loop para coletar conteúdo até que o usuário digite "stop"
    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)

    # Adiciona a extensão .txt ao nome do arquivo
    full_file_name = f"{file_name}.txt"

    # Cria e escreve o conteúdo no arquivo
    with open(full_file_name, "w", encoding="utf-8") as f:
        for line in content_lines:
            f.write(line + "\n")

    print(
        f'File "{full_file_name}" created successfully with '
        f'{len(content_lines)} lines.'
    )
