def main():
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as f:
        content = input("Enter new line of content: ")
        while content.strip() != "stop":
            f.write(f"{content}\n")
            content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
