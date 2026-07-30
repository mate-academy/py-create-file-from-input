def main():
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "a") as f:
        line = input("Enter new line of content: ")

        while line != "stop":
            line += "\n"
            f.write(line)
            line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
