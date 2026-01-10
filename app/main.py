def main() -> None:
    user_name = input("Enter name of the file: ")
    with open(f"{user_name}.txt", "a") as f:
        while True:
            line_content = input("Enter new line of content: ")
            if line_content != "stop":

                f.write(f"{line_content}\n")
            else:
                break


if __name__ == "__main__":
    main()
