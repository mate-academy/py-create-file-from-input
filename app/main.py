def main():
    name = input("Enter name of the file: ")
    result = []
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        else:
            result.append(text)
    with open(f"{name}.txt", "a") as file_text:
        for text in result:
            file_text.write(text)
            file_text.write("\n")
