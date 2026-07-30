def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as f:
        text = input("Enter new line of content: ")
        while text != "stop":
            f.write(f"{text}\n")
            text = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
