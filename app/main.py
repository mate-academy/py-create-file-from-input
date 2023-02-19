def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as f:
        is_running = True
        while is_running:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                is_running = False
                break
            f.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
