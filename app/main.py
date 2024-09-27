def main():
    name_file = input("Enter name of the file: ")
    with open(f"{name_file}.txt", "w") as f:
        while True:
            file_contetn = input("Enter new line of content: ")
            if file_contetn == "stop":
                break
            else:
                f.write(f"{file_contetn}\n")
    with open(f"{name_file}.txt", "r") as file:
        print(file.read())


if __name__ == "__main__":
    main()
