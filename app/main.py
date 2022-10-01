def main():
    name = input("Enter name of the file: ")
    stop = "stop"
    while True:
        with open(f"{name}.txt", "a") as f:
            content = input("Enter new line of content: ")
            if content == stop:
                break
            f.write(f"{content}\n")


if __name__ == "__main__":
    main()
