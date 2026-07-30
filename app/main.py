def main():
    name = input("Enter name of the file: ")
    while True:
        with open(f"{name}.txt", "a") as f:
            next_line = input("Enter new line of content: ")
            if next_line == "stop" or next_line == "Stop":
                break
            f.write(f"{next_line}\n")


if __name__ == "__main__":
    main()
