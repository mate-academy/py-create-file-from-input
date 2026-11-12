def main():
    content = ""
    new_filename = input("Enter name of the file: ")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line.strip().lower() == "stop":
            break
        content += f"{new_line}\n"
    new_file = open(f"{new_filename}.txt", "a")
    new_file.write(content)
    new_file.close()


if __name__ == "__main__":
    main()
