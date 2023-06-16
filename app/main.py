def main():
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as f:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            f.write(f"{text}\n")
