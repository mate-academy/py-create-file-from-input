def main() -> None:
    """
    Captura el nombre de un archivo y su contenido línea por línea
    desde la terminal, guardándolo como un archivo .txt.
    """
    # 1. Solicitar el nombre del archivo
    file_name = input("Enter name of the file: ")
    
    # Aseguramos la extensión .txt
    full_path = f"{file_name}.txt"
    
    content_lines = []

    # 2. Bucle para capturar el contenido
    while True:
        line = input("Enter new line of content: ")
        
        # Condición de salida
        if line.lower() == "stop":
            break
            
        content_lines.append(line)

    # 3. Escritura del archivo
    # Usamos '\n'.join() para insertar saltos de línea entre las entradas
    with open(full_path, mode="w", encoding="utf-8") as file:
        file.write("\n".join(content_lines))
        
    print(f"File '{full_path}' has been created successfully.")


if __name__ == "__main__":
    main()
