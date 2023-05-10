def main():
    file_name = input("Enter name of the file:")
    with open(file_name, "a") as f:
        new_line = input("Enter new line of content:")
        f.write(new_line)
        while new_line != "stop":
            f.write("\n" + new_line)
            new_line = input("Enter new line of content:")


if __name__ == "__main__":
    main()
