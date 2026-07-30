

def main() -> None:
    file_content = []
    file_name = input("Enter name of the file: ")
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            result = open(file_name + ".txt", "w")
            for item in file_content:
                result.write(f"{item}\n")
            result.close()
            break
        file_content.append(user_input)


if __name__ == "__main__":
    main()
