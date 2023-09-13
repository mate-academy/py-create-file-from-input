def main():
    name = input("Enter name of the file: ")
    content = ""
    word = input("Enter new line of content: ")
    while word != "stop":
        content += f"{word}\n"
        word = input("Enter new line of content: ")
    with open(f"{name}.txt", "w") as f:
        print(content, file=f, end="")


if __name__ == "__main__":
    main()
