"""One-line laugh lab entry for the make.fun 'One-Liner Laugh Lab' bounty.

Writes a single one-line joke — the excuse a robot vacuum gives after
eating a sock — to /output/entry.txt.
"""

import os

JOKE = (
    "I didn't eat your sock — I was conducting a taste test. "
    "Verdict: cotton, 2/10, would not chew again."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
