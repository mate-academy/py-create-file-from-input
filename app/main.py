def main() -> None:
    name_txt = input("Enter name of the file: ")
    name_txt = name_txt + ".txt"
    open(name_txt, "a").close()

    while True:
        content = input("Enter new line of content: ")
        if content.lower() == "stop":
            break

        with open(name_txt, "a") as file:
            file.write(f"{content}\n")


if __name__ == "__main__":
    main()
