def main() -> None:
    comand = ""
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as f:
        while True:
            comand = input("Enter new line of content: ")

            if comand == "stop":
                break
            elif comand != "":
                f.write(comand)
                f.write("\n")


if __name__ == "__main__":
    main()
