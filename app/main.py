def main():
    string = ""
    name = input("Enter name of the file: ")
    while True:
        content = input("Enter new line of content: ")
        if content != "stop":
            string += content + "\n"
        else:
            break
    with open(f"{name}.txt", "w") as file:
        file.write(string)


if __name__ == "__main__":
    main()
