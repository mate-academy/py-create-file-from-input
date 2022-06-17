def main():
    file_name = input("Enter name of the file: ")
    f = open(f"{file_name}.txt", "w")
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        f.write(content + "\n")
    f.close()


if __name__ == "__main__":
    main()
