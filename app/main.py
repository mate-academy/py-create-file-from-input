def main():
    append_list = []
    name = input("Enter name of the file:")
    while True:
        x = input("Enter new line of content:")
        if x.lower() == "stop":
            break
        append_list.append(x)
    with open(f"{name}.txt", "a") as f:
        for i in append_list:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
