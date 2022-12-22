def main():
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as f:
        while True:
            some_input = input("Enter new line of content: ")
            if some_input == "stop":
                break
            f.write(f"{some_input}\n")


if __name__ == "__main__":
    main()
