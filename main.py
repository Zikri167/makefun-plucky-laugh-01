"""One Line, One Laugh — make.fun entry.

Writes a single original one-liner to ``entry.txt`` inside the output
directory. Deterministic, standard library only, no network, no randomness,
no clock access. The output is exactly the winning line: 64 characters,
one line, no trailing newline.
"""

import os

LINE = "My goldfish started a podcast about the ocean it has never seen."

MAX_LENGTH = 200


def validate(line):
    """Check the line satisfies the bounty gate.

    Returns True only when the line is 1-200 characters, a single line
    with no newline or carriage-return characters, not only whitespace,
    and free of leading or trailing whitespace.
    """
    if not isinstance(line, str):
        return False
    if not 1 <= len(line) <= MAX_LENGTH:
        return False
    if "\n" in line or "\r" in line:
        return False
    if not line.strip():
        return False
    if line != line.strip():
        return False
    if not line.isprintable():
        return False
    return True


def output_dir():
    """Resolve the output directory from the environment.

    OUTPUT_DIR wins, then MAKEFUN_OUTPUT_DIR, then the default /output.
    """
    return (
        os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )


def main():
    if not validate(LINE):
        raise ValueError("winning line failed validation")
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
