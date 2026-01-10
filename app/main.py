def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as fil:
        while True:
            mes = input("Enter new line of content: ")
            if mes == "stop":
                break
            fil.write(f"{mes}\n")


if __name__ == "__main__":
    main()
