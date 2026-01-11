def main() -> None:
    name1:str = input("Enter name of the file: ")
    with open(f"{name1}.txt", "a") as f:
        while True:
            line:str = input("Enter new line of content: ")
            if line == "stop":
                break
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
