def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    if file_name is not None:
        with open(file_name, "a") as f:
            while True:
                typed = input("Enter new line of content: ")
                if typed == "stop":
                    break
                f.write(f"{typed}\n")


if __name__ == "__main__":
    main()
