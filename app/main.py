def main():
    file_name = input("Enter file name: ")
    content = ""

    while True:
        user_input = input("Enter content: ")

        if user_input == "stop":
            break

        content += f"{user_input}\n"

    output = open(file_name, "w")
    output.write(content)
    output.close()


if __name__ == "__main__":
    main()
