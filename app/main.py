def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    file_content = ""
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        file_content += f"{line}\n"

    with open(file_name, "w") as file_hand:
        file_hand.write(file_content)


if __name__ == "__main__":
    main()
