def main():
    file_name = input("Enter name of the file: ")
    file_txt = open(f"{file_name}.txt", "w")

    while True:
        text = input("Enter new line of content: ")
        if text.lower() == "stop":
            break
        file_txt.write(f"{text}\n")
    file_txt.close()


if __name__ == "__main__":
    main()
