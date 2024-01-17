def main():
    try:
        file = open(file=f"{input("Enter name of the file: ")}.txt", mode="x")

        while True:
            content = input("Enter new line of content: ")

            if content:
                if content == "stop":
                    file.close()
                    break
                else:
                    file.write(f"{content}\n")
            else:
                continue

    except FileExistsError:
        if input("file name already is exist\ntry again? : (y)") == "y":
            main()
        else:
            return None


if __name__ == "__main__":
    main()
