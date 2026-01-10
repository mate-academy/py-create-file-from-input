def main():
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "w") as f:
        while True:
            user_input = input("Enter new line of content: ")
            if user_input == "stop":
                break
            f.write(f"{user_input}\n")


if __name__ == "__main__":
    main()
