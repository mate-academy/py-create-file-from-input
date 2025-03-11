def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "a") as file:
        line = ""
        while line != "stop":
            line = input("Input content, or raise 'stop'.")
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
