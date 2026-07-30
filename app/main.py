def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []

    while True:
        if file_content and file_content[-1] == "stop\n":
            file_content.remove("stop\n")
            with open(f"{file_name}.txt", "a") as file:
                file.writelines(file_content)
            break

        text = input("Enter new line of content: ")

        file_content.append(f"{text}\n")


if __name__ == "__main__":
    main()
