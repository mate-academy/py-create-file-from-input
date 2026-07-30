def main() -> None:
    name_file = input("Enter name of the file: ")
    complete_name_file = name_file + ".txt"
    with open(complete_name_file, "w") as work_file:
        while True:
            line_text = input(
                "Enter new line of content: "
            )
            if line_text == "stop":
                break
            work_file.write(line_text + "\n")


if __name__ == "__main__":
    main()
