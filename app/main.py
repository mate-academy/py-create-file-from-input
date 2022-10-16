class FileManager:
    def __init__(self) -> None:
        self.name = input("Enter name of the file: ")
        self.mode = "a"
        self.file = None

    def __enter__(self) -> object:
        self.file = open(f"{self.name}.txt", self.mode)
        return self.file

    def __exit__(self, exc_type: str, exc_val: int, exc_tb: str) -> None:
        self.file.close()


def main() -> None:
    with FileManager() as curr_file:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            curr_file.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
