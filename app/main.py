def main() -> None:
    """
    Create a file from input
    """
    file_name = input("Enter name of the file: ")
    if file_name:
        lines = []
        is_continue = True
        while is_continue:
            new_line = input("Enter new line of content: ")
            if new_line.lower() != "stop":
                lines.append(new_line)
            else:
                is_continue = False

        with open(file_name + ".txt", "wt") as file_obj:
            for line in lines:
                file_obj.write(line + "\n")

    else:
        print("Warning! The filename cannot be empty. Program stopped!")


if __name__ == "__main__":
    main()
