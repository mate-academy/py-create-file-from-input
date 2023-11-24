def main():
    file_name = input("Enter name of the file: ")
    full_name = file_name + ".txt"

    with open(full_name, "a") as f:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            line = line + "\n"
            f.write(line)


if __name__ == "__main__":
    main()
