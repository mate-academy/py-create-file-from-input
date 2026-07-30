def main() -> None:
    question = input("Enter name of the file: ")
    if question:
        with open(f"{question}.txt", "w") as file:
            while True:
                question2 = input("Enter new line of content: ")
                if question2 != "stop":
                    file.write(f"{question2}\n")
                if question2 == "stop":
                    break


if __name__ == "__main__":
    main()
