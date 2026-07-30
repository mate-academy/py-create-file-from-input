def main() -> None:
    user_input = input("Enter name of the file: ")
    file_name = f"{user_input}.txt"
    with open(file_name, "w") as f_out:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            f_out.write(line + "\n")
    f_out.close()


if __name__ == "__main__":
    main()
