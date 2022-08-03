def main():
    file_name = input("Enter name of the file: ")
    text_input = input("Enter new line of content: ")

    with open(file_name + ".txt", "a") as f:
        while text_input.lower() != "stop":
            f.write(text_input + "\n")
            text_input = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
