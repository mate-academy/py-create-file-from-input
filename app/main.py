def main():
    name_for_task = input('Enter name of the file: ')
    content = ""
    while True:
        line = input('Enter new line of content: ')
        if line == "stop":
            break
        content = content + line + "\n"
    with open(name_for_task + ".txt", 'w') as f:
        f.write(content)


if __name__ == "__main__":
    main()
