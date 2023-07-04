def main():
    name = input("Enter name of the file: ") + ".txt"

    with open(name, "a") as f:
        text = input("Enter new line of content: ")
        while text != "stop":
            f.write(text + "\n")
            text = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
