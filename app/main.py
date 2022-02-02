def user_management_cli():
    file_name = input("Input the name of file: ")
    print("File content: ")

    while True:
        content = input()

        if content.lower() == "stop":
            break
        else:
            with open(file_name, "a") as f:
                f.write(content + "\n")


if __name__ == "__main__":
    user_management_cli()
