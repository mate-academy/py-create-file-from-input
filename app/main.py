def main() -> None:
    while True:
        file_name = input("Enter name of the file: ")

        if file_name.strip() == "":
            print("File name cannot be empty. Please enter a valid name.")
            continue

        content = []

        while True:
            line = input("Enter new line of content: ")
            if line.lower() == "stop":
                break
            content.append(line)

        with open(f"{file_name}.txt", "w") as file:
            for line in content:
                file.write(line + "\n")

        print(f"File '{file_name}.txt' has been created successfully "
              f"with the provided content.")
        break


if __name__ == "__main__":
    main()
