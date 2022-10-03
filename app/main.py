def main():
    file_name = input("Enter name of the file:")
    with open(file_name, "a") as f:
        while True:
            file_content = input("Enter new line of content:")
            if file_content.lower() == "exit":
                print("Exiting")
                break
            f.write(f"{file_content}\n")


if __name__ == "__main__":
    main()
