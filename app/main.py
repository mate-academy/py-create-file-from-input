def main():
    # Pede o nome do arquivo
    file_name = input("Enter name of the file: ").strip()
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    lines = []

    # Loop para receber conteúdo até digitar 'stop'
    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    # Cria o arquivo e escreve o conteúdo
    with open(file_name, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


# Permite rodar diretamente pelo terminal
if __name__ == "__main__":
    main()

