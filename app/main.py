def main() -> None:
    """ Get file name and content interactively
    and saved it to created txt file. """

    answer: str = input("Enter name of the file: ")
    answers: list[str] = []

    while answer != "stop":
        answers.append(answer)
        answer = input("Enter new line of content: ")

    with open(f"{answers.pop(0)}.txt", "w") as file:
        file.write("\n".join(answers))


if __name__ == "__main__":
    main()
