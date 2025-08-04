def main():
    name = input("Enter name of the file: ")
    content = input("Enter new line of content: ")
    all_content = ""
    while content != "stop":
        all_content += content + "\n"
        content = input("Enter new line of content: ")
    with open(f"{name}.txt", "w") as f:
        f.write(all_content)


if __name__ == "__main__":
    main()
