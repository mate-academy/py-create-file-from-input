def main() -> None:
    file_name = input("Enter name of the file: ")
    content = ""
    stop_word = ""
    while stop_word != "stop":
        stop_word = input("Enter new line of content: ")
        if stop_word != "stop":
            content += stop_word + "\n"

    with open(f"{file_name}.txt", "a") as f:
        f.write(f"{content}")


if __name__ == "__main__":
    main()
