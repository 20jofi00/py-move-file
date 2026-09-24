import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    command_name, source_path, destination_path = parts
    if command_name != "mv" or not os.path.isfile(source_path):
        return
    if destination_path.endswith("/"):
        source_name = os.path.basename(source_path)
        final_destination = os.path.join(destination_path, source_name)
    else:
        final_destination = destination_path

    if os.path.abspath(source_path) == os.path.abspath(final_destination):
        return

    directory = os.path.dirname(final_destination)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(source_path, "r") as file, open(final_destination, "w") as data:
        content = file.read()
        data.write(content)
    os.remove(source_path)
