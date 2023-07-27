def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w") as f:
        while True:
            f_content = input("Enter new line of content: ")
            if f_content == "stop":
                break
            f.write(f"{f_content}\n")


if __name__ == "__main__":
    main()
