from typing import Any


def main() -> Any:
    name_txt = input("Enter name of the file: ")
    while True:
        with open(f"{name_txt}.txt", "a") as f:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            f.write(new_line)
            f.write("\n")


if __name__ == "__main__":
    main()
