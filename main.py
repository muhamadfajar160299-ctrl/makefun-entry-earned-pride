"""Write the one-line entry to the grader output directory.

Reads entry.txt next to this file and copies it byte for byte to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) with mode 0644,
using a single direct write and no temporary file.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    try:
        data = (HERE / "entry.txt").read_bytes()
    except FileNotFoundError:
        raise SystemExit("entry.txt not found next to main.py")
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / "entry.txt"
    target.write_bytes(data)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
