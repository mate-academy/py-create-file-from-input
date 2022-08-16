def main():
    file_name = input("Enter name of the file: ")
    text = ""
    while True:
        context = input("Enter new line of content: ")
        if context == "stop":
            break
        text += context + "\n"
    with open(file_name + ".txt", "w") as f:
        f.write(text)
    # f.close()


if __name__ == "__main__":
    main()
