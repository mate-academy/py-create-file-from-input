def main():
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w") as file:
        while True:
            enter = input("Enter new line of content: ")
            if enter == "stop":
                break
            file.write(f"{enter}\n")


if __name__ == "__main__":
    main()
