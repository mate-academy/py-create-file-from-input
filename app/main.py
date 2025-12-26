def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w") as f:
        dont_stop = True
        while dont_stop:
            text = input("Enter new line of content: ")
            if text == "stop":
                dont_stop = False
            else:
                f.write(text + "\n")


if __name__ == "__main__":
    main()
