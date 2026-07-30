def main() -> None:
    name_file = input("Enter name of the file: ")
    if len(name_file) > 0:
        line = ""
        with open(name_file + ".txt", "a") as f:
            while True:
                line = input("Enter new line of content: ")
                if line == "stop":
                    break
                f.write(line + "\n")


if __name__ == "__main__":
    main()
