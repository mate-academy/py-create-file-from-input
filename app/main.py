def main() -> None:
    filename = get_name()
    content = fill_content()
    save_input(filename, content)


def get_name() -> str:
    return input("Enter name of the file: ")


def fill_content() -> list:
    res = list()
    while True:
        curr_data = input("Enter new line of content: ")
        if curr_data == "stop":
            break
        res.append(curr_data)
    return res


def save_input(filename: str, content: list, extension: str = "txt") -> None:
    with open(f"{filename}.{extension}", "w+") as file:
        for curr_row in content:
            file.write(curr_row + "\n")


if __name__ == "__main__":
    main()
