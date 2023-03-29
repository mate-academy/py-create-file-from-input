def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as f:
        new_test = None
        while new_test != "stop":
            new_test = input("Enter new line of content: ")
            if new_test == "stop":
                break
            f.write(f"{new_test}\n")


if __name__ == "__main__":
    main()
