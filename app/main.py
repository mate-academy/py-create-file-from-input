def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as f:
        is_answer_not_stop = True
        while is_answer_not_stop:
            file_line = input("Enter new line of content: ")
            if file_line != "stop":
                f.write(file_line + "\n")
            else:
                is_answer_not_stop = False


if __name__ == "__main__":
    main()
