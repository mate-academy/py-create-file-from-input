def main():
    name = input("Enter name of the file: ")
    filename = f"{name}.txt"
    new_line = ""
    with open(filename, "a") as f:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line.lower() == 'stop':
                break
            f.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
