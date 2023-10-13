def main() -> None:

    name = input("Enter name of the file: ")

    resps = []
    while 1:
        resp = input("Enter new line of content: ")
        if resp == "stop":
            break
        resps.append(resp)

    with open(f"{name}.txt", "a") as f:
        for i in resps:
            f.write(i + "\n")


if __name__ == "__main__":
    main()
