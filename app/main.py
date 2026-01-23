def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as f:
        while True:
            inside_text = (input("Enter new line of content: "))
            if inside_text == "stop":
                break
            else:
                f.write(f"{inside_text}\n")


if __name__ == "__main__":
    main()
