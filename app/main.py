def main():
    file_name = input("Enter name of the file: ")+".txt"
    with open(file_name, "a") as file:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            file.writelines(content+"\n")


if __name__ == "__main__":
    main()
