def main():
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "w") as file:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            file.write(new_line)
            file.write("\n")


if __name__ == "__main__":
    main()
