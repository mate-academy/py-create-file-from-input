from typing import Any


def main() -> Any:
    name = input("Enter name of the file: ")
    my_file = open(f"{name}.txt", "a")
    content = ""
    while content != "stop":
        content = input("Enter new line of content: ")
        if content == "stop":
            continue
        my_file.write(f"{content}\n")
    my_file.close()


if __name__ == "__main__":
    main()
