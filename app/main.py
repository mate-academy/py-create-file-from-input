def main():
    with open(input("Enter name of the file: ") + ".txt", "w") as f:
        valid = True
        while valid:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            f.write(text + "\n")


if __name__ == "__main__":
    main()
