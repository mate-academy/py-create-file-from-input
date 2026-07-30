def main():
    with open(input("Enter name of the file: ") + ".txt", "w") as new_file:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            new_file.write(f"{text}\n")


if __name__ == "__main__":
    main()
