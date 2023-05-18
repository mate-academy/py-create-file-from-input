def main():
    file_name = input("Enter file name: ")
    file_name += ".txt"
    f = open(file_name, "w")
    with open(file_name, "a") as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            else:
                f.write(content)
                f.write("\n")


if __name__ == "__main__":
    main()
