def main():
    name = input("Enter name of the file: ")
    name += ".txt"
    with open(name, "a") as f:
        while True:
            txt = input("Enter new line of content: ")
            if txt != "stop":
                f.write(f"{txt}\n")
            else:
                break


if __name__ == "__main__":
    main()
