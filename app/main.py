def main():
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as f:

        while True:
            user_inpt = input("Enter new line of content: ")
            if user_inpt.lower() == "stop":
                break
            f.write(user_inpt + "\n")


if __name__ == "__main__":
    main()
