def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    lines_of_content = []

    print("Enter new line of content: ")
    while True:
        line = input()
        if line.lower() == "stop":
            break
        lines_of_content.append(line)

    try:
        with open(file_name, "w") as file:
            for line in lines_of_content:
                file.write(line + "\n")
    except FileNotFoundError:
        pass
    except PermissionError:
        pass
    except IOError:
        pass


if __name__ == "__main__":
    main()
