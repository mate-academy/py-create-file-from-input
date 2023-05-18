def main() -> None:
    file_name = input("Enter file name: ")
    file_name += ".txt"
    file = open(file_name, "w")
    with open(file_name, "a") as file:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            else:
                file.write(content)
                file.write("\n")


if __name__ == "__main__":
    main()
