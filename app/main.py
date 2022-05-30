def main():
    file_name = input("Enter name of the file: ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    with open(file_name, "a") as nf:
        while True:
            line_content = input("Enter new line of content: ")

            if line_content == "stop":
                break

            nf.write(line_content + "\n",)


if __name__ == "__main__":
    main()
