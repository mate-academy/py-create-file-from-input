def main():
    file_basename = input("Enter name of the file: ")
    with open(file_basename + ".txt", "w+") as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            f.write(content + "\n")


if __name__ == "__main__":
    main()
