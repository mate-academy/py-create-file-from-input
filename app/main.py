def main():
    name_file = input("Enter name of the file: ")
    with open(f"{name_file}.txt", "w") as f:
        while True:
            content = input("Enter new line of content: ")
            if content != "stop":
                f.write(content + "\n")
            else:
                break


if __name__ == "__main__":
    main()
