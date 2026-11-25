"""One Line, One Laugh -- Sock Escape.

Writes one funny line to /output/entry.txt.
"""

import os

ENTRY_TEXT = "The dryer ate one sock again; the other one is already halfway to Mexico with the passports."

DEFAULT_OUTPUT = "/output/entry.txt"


def validate_entry(text):
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    stripped = text.strip()
    if not 1 <= len(stripped) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in stripped:
        raise ValueError("entry must be a single line")
    return stripped


def resolve_output_path():
    output_path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    return output_path


def write_entry(text, output_path):
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return len(text.encode("utf-8"))


def main():
    text = validate_entry(ENTRY_TEXT)
    output_path = resolve_output_path()
    byte_count = write_entry(text, output_path)
    print(f"Wrote {len(text)} characters ({byte_count} bytes) to {output_path}")


if __name__ == "__main__":
    main()
