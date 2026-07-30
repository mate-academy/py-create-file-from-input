def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    app_is_work = True
    content = []

    with open(file_name, "a") as file:
        while app_is_work:
            file_content = input("Enter new line of content: ")

            if file_content == "stop":
                file.write("\n".join(content))
                app_is_work = False
            else:
                content.append(file_content)


if __name__ == "__main__":
    main()
