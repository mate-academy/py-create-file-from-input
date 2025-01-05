def main():
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as f:
        while True:
            add_new_line = input("Enter new line of content: ")
            if add_new_line == "stop":
                break
            f.write(add_new_line + "\n")


if __name__ == "__main__":
    main()
