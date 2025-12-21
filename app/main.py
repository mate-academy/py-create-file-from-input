def main():
    file_base_name = input("Enter name of the file: ")
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.strip() == "stop":
            break
        content_lines.append(line)

    filename = file_base_name if file_base_name.endswith(".txt") else file_base_name + ".txt"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(content_lines))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
