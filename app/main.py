def main():
    name_file = input("Enter name of the file: ")
    with open(name_file + ".txt", "w") as f:
        new_file = input("Enter new line of content: ")
        f.write(new_file)
    with open(name_file + ".txt", "w") as f:
        while new_file != "stop":
            f.write(new_file + "\n")
            new_file = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
