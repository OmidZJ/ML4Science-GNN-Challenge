import argparse
from pathlib import Path
import nbformat as nbf


def insert_markdown_cell(ipynb_path: Path, text: str = "سلام", position: str = "top") -> None:
    nb = nbf.read(str(ipynb_path), as_version=4)
    new_cell = nbf.v4.new_markdown_cell(text)

    if position.lower() in {"top", "start", "head"}:
        nb.cells.insert(0, new_cell)
    else:
        nb.cells.append(new_cell)

    nbf.write(nb, str(ipynb_path))


def main():
    parser = argparse.ArgumentParser(description="Insert a markdown cell into a Jupyter notebook.")
    parser.add_argument("notebook", type=Path, help="Path to the .ipynb file")
    parser.add_argument("--position", choices=["top", "bottom"], default="top")
    parser.add_argument("--text", default="سلام")

    args = parser.parse_args()
    insert_markdown_cell(args.notebook, text=args.text, position=args.position)
    print(f"Inserted markdown cell at {args.position} of {args.notebook}")


if __name__ == "__main__":
    main()
