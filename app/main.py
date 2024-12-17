def main():
    filename = input("Enter name of the file: ").strip() + ".txt"
    with open(filename, "a") as file:
        while True:
            line = input("Enter new line of content: ").strip()
            if line.lower() == "stop":
                break
            file.write(line + "\n")



if __name__ == "__main__":
    name = input("Enter file name (without extension): ")
    message = input("Enter message (type 'stop' to exit): ")
    main()

