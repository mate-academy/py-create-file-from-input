class FileExistsError(Exception):
    def __str__(self) -> str:
        return "File already exists"


class FileNameError(Exception):
    def __init__(self, info: str) -> None:
        self.info = info

    def __str__(self) -> str:
        return self.info


def main():
    def validating_filename(name: str) -> Exception:
        def is_valid_name(name: str) -> bool:
            bad = {
                " ", ",", "-",
                "/", "\\", ":",
                "*", "?", "\"",
                "'", ">", "<",
                "|", "&"
            }
            for char in name:
                if char in bad:
                    raise FileNameError(f"{char} is unauthorized symbol")
        if name == "":
            raise FileNameError("Empty file name")
        if is_valid_name(name) is False:
            raise FileNameError("file name contains bad symbols")
        if f"{name}.txt"[-5] in [".", "_"]:
            raise FileNameError(f"{name[-1]} before .txt")
        return f"{name}.txt"

    try:
        new_file = open(
            file=validating_filename(input("Enter name of the file: ")),
            mode="x"
        )
        file = open(new_file.name, "a")
    except FileExistsError as error:
        print(error)
        main() if input("try again? : (y)") == "y" else exit()

    content = ""
    while True:
        input_txt = input("Enter new line of content: ")

        if input_txt == "":
            content += "\n"
            file.write(f"{content}")
        if input_txt == "stop":
            break
        content += f"{input_txt}\n"

    file.write(f"{content}")
    file.close()


if __name__ == "__main__":
    main()
