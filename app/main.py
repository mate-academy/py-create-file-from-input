def main() -> None:
    file_name = input("Enter name of the file: ")
    try:
        with open(file_name + ".txt", "a") as work_file:
            stop = False
            while not stop:
                line = input("Enter new line of content: ")
                if line == "stop":
                    stop = True
                else:
                    work_file.write(line + "\n")
    except FileNotFoundError:
        print(f"File '{file_name}.txt' not found.")


if __name__ == "__main__":
    main()
