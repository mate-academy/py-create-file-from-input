def main() -> None:
    # write your code here
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as f:
        stop = 0
        while stop == 0:
            text = input("Enter new line of content: ")
            if text == "stop":
                stop = 1
            else:
                f.write(f"{text}\n")


if __name__ == "__main__":
    main()
