def main() -> None:
    enter = input("Enter name of the file: ")
    with open(f"{enter}.txt", "a") as file:
        while enter != "stop":
            enter = input("Enter new line of content: ")
            if enter != "stop":
                file.write(f"{enter}\n")


if __name__ == "__main__":
    main()
