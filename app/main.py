def main() -> None:
    enter_name = input("Enter name of the file: ")
    with open(f"{enter_name}.txt", "w") as f:
        while True:
            enter_text = input("Enter new line of content: ")
            if enter_text == "stop":
                break
            f.write(f"{enter_text}\n")


if __name__ == "__main__":
    main()
