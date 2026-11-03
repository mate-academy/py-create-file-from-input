def main() -> None:
    fine_name = input("Enter name of the file: ")
    with open(f"{fine_name}.txt", "w") as file:
        while True:
            inp = input("Enter new line of content: ")
            if inp == "stop":
                break
            file.write(inp + "\n")


if __name__ == "__main__":
    main()
