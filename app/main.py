def main() -> None:
    file_name = str(input("Enter name of the file: "))
    if file_name:
        while True:
            with open(f"{file_name}.txt", "a") as file:
                sentence = str(input("Enter new line of content: "))
                if sentence == "stop".lower():
                    break
                file.write(f"{sentence}\n")


if __name__ == "__main__":
    main()
