def main():
    new_file_name = input("Enter name of the file: ")
    with open(new_file_name + ".txt", "w") as new_file:
        next_line = ""
        while next_line != "stop":
            next_line = input("Enter new line of content: ")
            if next_line == "stop":
                break
            new_file.write(next_line + "\n")


if __name__ == "__main__":
    main()
