def main() -> None:
    file_name = input("Enter name of the file: ")

    if not file_name:
        return

    content_list = get_content()

    file_with_extension = build_extension(file_name)

    write_to_file(content_list, file_with_extension)


def get_content() -> list[str]:
    content_list = []

    while True:
        content = input("Enter new line of content: ")

        if content.lower() == "stop":
            break

        content_list.append(content)

    return content_list


def build_extension(file_name: str) -> str:
    file_name = file_name.replace(".", "_")
    file_name = file_name.replace(" ", "_")

    return file_name + ".txt"


def write_to_file(content_list: list[str], file_with_extension: str) -> None:
    with open(file_with_extension, "w") as file:
        file.write("\n".join(content_list))


if __name__ == "__main__":
    main()
