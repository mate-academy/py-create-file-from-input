def main():
    file_name = input("Enter name of the file: ")
    content = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        content.append(new_line + "\n")
    with open(f"{file_name}.txt", "w") as file:
        file.writelines(content)



if __name__ == "__main__":
    main()
