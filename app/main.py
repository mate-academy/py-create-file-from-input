def main():
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "a") as f:
        while True:
            result = input("Enter new line of content: ")
            if result != "stop":
                f.write(result + "\n")
                continue
            break


if __name__ == "__main__":
    main()
