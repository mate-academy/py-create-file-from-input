def main():
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "w") as f:
        while True:
            user = input("Enter new line of content: ")
            if user == "stop":
                break
            f.write(f"{user}\n")


if __name__ == "__main__":
    main()
