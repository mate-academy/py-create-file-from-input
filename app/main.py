def main():
    body = ""
    file_name = ""
    while not file_name:
        file_name = input("Please enter the file name")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    print('Now you will have to fill the file.\nPrint "stop" to finish.')

    while True:
        line = input("Enter data to file")
        if line.lower() == "stop":
            break
        body += line + "\n"

    print("Saving the file")

    with open(file_name, "w") as target:
        target.writelines(body)

    print(f"File was saved as {file_name} in working directory.")

    return

if __name__ == "__main__":
    main()
