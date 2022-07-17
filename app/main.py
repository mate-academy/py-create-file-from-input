def main():
    name = input("Enter name of the file: ")
    name = name + ".txt"
    with open(name, "x") as f:
        f.close()
    with open(name, "a") as f:
        result = []
        x = input("Enter new line of content: ")
        if x != "" and x != 'stop':
            result.append(x)
        while x != "stop":
            x = input("Enter new line of content: ")
            if x != "stop":
                result.append(x)
        result = "\n".join(result)
        f.writelines(result)


if __name__ == "__main__":
    main()
