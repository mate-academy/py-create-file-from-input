def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = []

    while True:
        user_input = input("Enter new line of content: ")

        if user_input == "stop":
            break
        content.append(user_input)

    with open(file_name, "w") as file:
        for line in content:
            file.write(line + "\n")
