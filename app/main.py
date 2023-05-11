import os


def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    with open(file_name, "a") as f:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            return
        f.write(new_line)
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            f.write("\n" + new_line)

    if os.path.isfile(file_name) and os.stat(file_name).st_size > 0:
        print(f"File '{file_name}' has been created.")

    else:
        print(f"File '{file_name}' is empty or does not exist.")


if __name__ == "__main__":
    main()
