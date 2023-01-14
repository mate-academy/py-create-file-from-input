def main() -> None:
    # write your code here
    filename = input("Enter name of the file: ")
    with open(filename + ".txt", "w") as f:
        while True:
            string_received_from_user = input("Enter new line of content: ")
            if string_received_from_user == "stop":
                break
            f.write(string_received_from_user + "\n")


if __name__ == "__main__":
    main()
