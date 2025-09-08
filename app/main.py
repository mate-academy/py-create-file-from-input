def main():
    inp = input("Enter name of the file:")
    file_name = inp
    result: str
    while inp != "stop":
        inp = input("Enter new line of content:")
        if inp != "stop":
            result = result + "\n" + inp
    with open(file_name, "w") as f:
        f.write(result)

if __name__ == "__main__":
    main()
