def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        while True:
            newline = input("Enter new line of content: ")
            if newline.lower() == "stop":
                break
            else:
                file.write(newline + "\n")

if __name__ == "__main__":
    main()