def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as f:
        while True:
            txt = input("Enter new line of content: ")
            if txt.lower() == "stop":
                break
            f.write(txt + "\n")
    pass


if __name__ == "__main__":
    main()
