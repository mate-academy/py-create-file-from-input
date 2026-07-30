def main():
    name_file = input("Enter name of the file: ")

    with open(f"{name_file}.txt", "w") as f:
        while True:
            new_text = input("Enter new line of content: ")
            if new_text.lower() == "stop":
                break
            f.write(new_text + "\n")


if __name__ == "__main__":
    main()
