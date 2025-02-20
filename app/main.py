def main() -> None:
    file = input("Enter name of the file: ")
    with open(file + ".txt", "a") as f:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            f.write(text + "\n")



if __name__ == "__main__":
    main()
