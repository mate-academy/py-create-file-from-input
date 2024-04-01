def main() -> None:
    file_name = input("Enter name of the file: ")
    endline = ""
    with open(file_name + ".txt", "w") as file:
        while True:
            endline = input("Enter new line of content: ")
            if endline == "stop":
                break
            else:
                file.write(endline + "\n")


if __name__ == "__main__":
    main()
