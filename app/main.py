def main() -> None:
    print("Enter name of the file: ")
    file_name = input()
    file_name += ".txt"

    while True:
        print("Enter new line of content:")
        file_content = input()

        if file_content == "stop":
            break
        with open(file_name, "a") as f:
            f.write(f"{file_content}\n")


if __name__ == "__main__":
    main()
