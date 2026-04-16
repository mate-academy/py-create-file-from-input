def main() -> None:
    name = input("Enter name of the file: ")

    with open(f"{name}.txt", "w") as f:
        while True:
            cont = input("Enter new line of content: ")

            if cont.lower() == "stop":
                break

            f.write(cont + "\n")


if __name__ == "__main__":
    main()
