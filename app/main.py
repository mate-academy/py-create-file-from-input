def main():
    file_name = input("Enter name of the file: ")

    with open(file_name, "a") as file:
        input_ = ""
        while input_ != "stop":
            input_ = input("Enter new line of content: ")
            if input_ == "stop":
                continue
            file.write(f"{input_}\n")

    with open(file_name, "r") as file:
        print(f"File name: {file_name}.txt\nFile content: ")
        for line in file:
            print(line, end="")


if __name__ == "__main__":
    main()
