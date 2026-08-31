def main() -> list:

    file_name = input("Enter name of the file: ")
    result_list = []

    while True:
        file_content = input("Enter new line of content: ")

        if file_content == "stop":
            break

        result_list.append(file_content)

    with open(f"{file_name}.txt", "a") as file:
        result_list.append(file.write("\n".join(result_list)))

    return result_list


if __name__ == "__main__":
    main()
