def main() -> None:
    file_name = input("Enter name of the file: ")

    try:
        with open(f"{file_name}.txt", "a") as file:
            while True:
                line = input("Enter new line of content: ")
                if line.lower() == "stop":
                    break
                file.write(line + "\n")
    finally:
        print("File was created")


if __name__ == "__main__":
    main()
