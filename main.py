import os

ENTRY_TEXT = "The dryer ate one sock again; the other one is already halfway to Mexico with the passports."


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    text = ENTRY_TEXT.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {output_path}")


if __name__ == "__main__":
    main()
