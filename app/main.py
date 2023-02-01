def main():
    filename = input("Enter name of the file: ")
    file = open(filename+".txt", "w+")
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        file.write(content+"\n")
    file.close()


if __name__ == "__main__":
    main()
