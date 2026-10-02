import os


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination = parts[2]

    # Якщо destination закінчується на /,
    # файл має зберегти своє старе ім'я
    if destination.endswith("/"):
        destination = destination + source.split("/")[-1]

    directories = destination.split("/")[:-1]

    current_path = ""

    for directory in directories:
        current_path = os.path.join(current_path, directory)

        if not os.path.exists(current_path):
            os.mkdir(current_path)

    with open(source, "rb") as source_file:
        content = source_file.read()

    with open(destination, "wb") as destination_file:
        destination_file.write(content)

    os.remove(source)
