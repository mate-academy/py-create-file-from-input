def main() -> None:

    filename = input("Enter name of the file: ")

    with open(f"{filename}.txt", "w") as file:

        while True:
            content = input("Enter new line of content: ")
            if content.lower() == "stop":
                break

            file.write(f"{content}\n")


if __name__ == "__main__":
    main()
