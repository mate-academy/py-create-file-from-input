def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w") as file:
        while True:
            line = input("Enter new line of content: ")
            if line != "stop":
                file.write(f"{line}\n")
            else:
                break


if __name__ == "__main__":

    main()
