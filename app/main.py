def main():
    file_name = input("Enter the name of the file: ").strip()
    file_name += ".txt"
    content_lines = []
    print("Enter new lines of content (type 'stop' to finish):")

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(file_name, "w") as file:
        file.write("\n".join(content_lines))

    print(f"File '{file_name}' created successfully.")


if __name__ == "__main__":
    main()