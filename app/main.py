def create_file_from_input() -> None:
    # Solicita o nome do arquivo ao usuário
    file_name = input("Enter name of the file: ")
    
    # Lista para armazenar as linhas de conteúdo temporariamente
    content_lines = []
    
    # Loop para capturar o conteúdo até que a palavra 'stop' seja digitada
    while True:
        line = input("Enter new line of content: ")
        
        if line.lower() == "stop":
            break
            
        content_lines.append(line)
    
    # Cria o arquivo com a extensão .txt e escreve o conteúdo
    full_file_name = f"{file_name}.txt"
    
    with open(full_file_name, "w") as file:
        # Escreve cada linha seguida por uma quebra de linha
        for line in content_lines:
            file.write(line + "\n")


if __name__ == "__main__":
    create_file_from_input()
