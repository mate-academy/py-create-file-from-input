def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as f:
        while True:
            line_of_content = input("Enter new line of content: ")
            if line_of_content.lower() == "stop":
                break
            f.write(f"{line_of_content}\n")


if __name__ == "__main__":
    main()
