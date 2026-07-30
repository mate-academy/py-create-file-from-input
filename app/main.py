def main():
    file_name = input("Enter name of the file: ")
    ask = True
    text = ""
    while ask:
        content = input("Enter new line of content: ")
        if content == "stop":
            ask = False
        else:
            text += f"{content}\n"
    with open(f"{file_name}.txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
