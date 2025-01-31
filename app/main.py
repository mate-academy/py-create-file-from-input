def main() -> None:
    def create_text_file() -> None:
    file_name = input("Enter the file name (without extension): ")
    file_name += ".txt"
    
    print("Enter file content line by line. Type 'stop' to finish.")
    content = []
    
    while True:
        line = input()
        if line.lower() == "stop":
            break
        content.append(line)
    
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(content))
    
    print(f"File '{file_name}' has been created successfully.")



if __name__ == "__main__":
    main()
