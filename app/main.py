def main():
    file_name = input("Enter name of the file: ") + ".txt"
    line = ""
    with open(file_name, "w") as f:
        while line != "stop":
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            f.write(line + "\n")


if __name__ == "__main__":
    main()
