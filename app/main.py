def main():
    file_name = input("Enter name of the file: ")
    final_file_name = file_name + ".txt"

    content_list = []

    while True:
        file_content = input("Enter new line of content: ")
        if file_content.lower() == "stop":
            break
        content_list.append(file_content)

    with open(final_file_name, mode="a", encoding="utf-8") as f:
        for content in content_list:
            f.write(content + "\n")

    print(f"Arquivo '{final_file_name}' criado com sucesso!")

if __name__ == "__main__":
    main()
