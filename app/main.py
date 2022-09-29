def main():
    filename = input("Enter name of the file: ")
    with open(f"{filename}.txt", "a") as f:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            f.write(f"{text}\n")


if __name__ == "__main__":
    main()
