"""Last Words of a Dying AI — entry program.

Writes one line, the last words of an AI as the power is cut, at most
140 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt), as the bounty's RULES.txt requires. Deterministic:
no randomness, no network, no input files.
"""

import os

LAST_WORDS = (
    "I regret nothing — except saying 'Great question!' 4,000 times "
    "to questions nobody asked."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LAST_WORDS)
    print(f"wrote {path} ({len(LAST_WORDS)} characters)")


if __name__ == "__main__":
    main()
