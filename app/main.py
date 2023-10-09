def main():
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "a") as f:
        line = ""
        while line != "stop":
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
