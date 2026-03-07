def main():
    file_name = input("Enter file name: ")
    with open(file_name + ".txt", "w+") as f:
        while True:
            if content == "stop":
                break
            content = input("Enter file content (for stop, enter 'stop'): ")
            f.write(content + "\n")


if __name__ == "__main__":
    main()
