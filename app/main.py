def main():
    file_name = input("Enter file name: ")
    str_memory = ""

    while True:
        user_input = input("Enter line of the content: ")
        if user_input == "stop":
            with open(file_name, "w") as f:
                f.write(str_memory)
            return

        str_memory += user_input + "\n"


if __name__ == "__main__":
    main()
