def main() -> None:
    file_name = input("Enter name of the file: ")
    condition_or_content = True
    final_content = ""
    while condition_or_content is True:
        condition_or_content = input("Enter new line of content: ")
        if condition_or_content == "stop":
            condition_or_content = False
        else:
            final_content += condition_or_content + "\n"
    with open(file_name + ".txt", "w") as file:
        print(final_content)
        file.write(final_content)


if __name__ == "__main__":
    main()
