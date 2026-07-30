def main() -> None:
    # write your code here
    filename = input("Enter name of the file: ")
    with open(filename + ".txt", "a") as f:
        while True:
            text_str = input("Enter new line of content: ")
            if text_str == "stop" :
                break
            f.write(text_str + "\n")


if __name__ == "__main__":
    main()
