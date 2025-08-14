import argparse
import json
from pathlib import Path


def insert_markdown_cell_json(ipynb_path: Path, text: str = "سلام", position: str = "top") -> None:
    # Read notebook JSON
    with ipynb_path.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    if not isinstance(nb, dict) or "cells" not in nb or not isinstance(nb["cells"], list):
        raise ValueError("Invalid notebook structure: missing 'cells' list")

    new_cell = {
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [text]
    }

    if position.lower() in {"top", "start", "head"}:
        nb["cells"].insert(0, new_cell)
    else:
        nb["cells"].append(new_cell)

    # Write back with UTF-8 encoding
    with ipynb_path.open("w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Insert a markdown cell into a Jupyter notebook (pure JSON)")
    parser.add_argument("notebook", type=Path, help="Path to the .ipynb file")
    parser.add_argument("--position", choices=["top", "bottom"], default="top")
    parser.add_argument("--text", default="سلام")
    args = parser.parse_args()

    insert_markdown_cell_json(args.notebook, text=args.text, position=args.position)
    print(f"Inserted markdown cell at {args.position} of {args.notebook}")


if __name__ == "__main__":
    main()
