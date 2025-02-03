def main() -> None:
    name = input("Enter name of the file: ")
    file_name = f"{name}.txt"
    with open(file_name, "w") as f:
        f.close()

    with open(file_name, "a") as target_file:
        trigger = True
        while trigger:
            line = input("Enter new line of content: ")
            if line == "stop":
                trigger = False
            else:
                target_file.write(f"{line}\n")


if __name__ == "__main__":
    main()
