def main():
    # 1. Запитуємо ім'я файлу
    file_name = input("Enter name of the file: ")
    
    # Додаємо розширення .txt
    full_file_name = f"{file_name}.txt"
    
    content_lines = []
    
    # 2. Запитуємо контент у циклі
    while True:
        line = input("Enter new line of content: ")
        
        # 3. Перевіряємо умову виходу
        if line.lower() == "stop":
            break
            
        content_lines.append(line)
        
    # 4. Записуємо зібраний контент у файл
    try:
        with open(full_file_name, "w") as f:
            # Об'єднуємо всі рядки, додаючи між ними символ нового рядка
            f.write("\n".join(content_lines))
            
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    main()
