def main():
    file_name = input("Enter name of the file: ")
    new_line = input("Enter new line of content: ")
    if new_line == 'stop':
        open(f"{file_name}.txt", "a")
    else:
        while new_line != 'stop':
            with open(f"{file_name}.txt", "a") as f:
                f.write(f"{new_line}\n")
            new_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
