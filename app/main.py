import os
print(f"Current directory: {os.getcwd()}")


def main():
    file_name = input("Enter name of the file: ")
    print(f"Creating file: {file_name}.txt")
    with open(file_name + ".txt", "a") as file:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            file.write(line + "\n")


if __name__ == "__main__":
    main()