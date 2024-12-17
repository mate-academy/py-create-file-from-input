def main():
    a = input("Enter name of the file: ")
    file_name = f"{a}.txt"
    content = False
    while True:
        user_input = input("Enter new line of content: ")
        if user_input.lower() == "stop":
            break
        with open(file_name, "a") as f:
            f.write(user_input + "\n")
            content = True
    if not content:
        open(file_name, "w").close()

if __name__ == "__main__":
    main()
