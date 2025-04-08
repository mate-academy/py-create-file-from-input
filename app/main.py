def main() -> None:
    file_name = input("Enter the name of file: ") + ".txt"

    with open("new_file.txt", "a") as file:
        #print(f"File name: {file_name}.txt")
        #print("File content:")
        while True:
            baka = input("Enter new line of content: ")
            if baka.lower() == "stop":
                break
            file.write(f"{baka}" + "\n")


if __name__ == "__main__":
    main()
