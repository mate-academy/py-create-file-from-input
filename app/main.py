def main():
    file_name = input("Enter name of the file: ")
    file = f"{file_name}.txt"
    text = ""
    # text += f"File name: \"{file}\"\nFile content:\n"
    while True:
        fraze = input("Enter new line of content: ")
        if fraze == "stop":
            break
        text += fraze + "\n"
    with open(file, "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
