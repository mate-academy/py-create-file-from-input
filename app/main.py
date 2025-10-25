def main(content: list, file_basename: str) -> None:
    with open(f"{file_basename}.txt", "w") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    main([], "")
