def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    print(file_name)
    with open(file_name, "w") as f:
        while True:
            writen = input("Enter new line of content: ")
            if writen.lower() == "stop":
                break
            f.write(f"{writen}" + "\n")


if __name__ == "__main__":
    main()
