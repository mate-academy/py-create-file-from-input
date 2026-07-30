import re


def main() -> None:
    file_name = ""
    while not file_name:
        file_name = re.sub(
            r'[\\/:*?"<>|]',
            "",
            input("Enter name of the file: ")
        )
    with open(f"{file_name}.txt", "a") as file:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            file.write(f"{content}\n")


if __name__ == "__main__":
    main()
