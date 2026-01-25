def main() -> None:
    name = input("Enter name of the file: ")

    with open(name + ".txt", "a") as f:
        new_content = input("Enter new line of content: ")

        while new_content != "stop":
            f.write(f"{new_content}\n")
            new_content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
