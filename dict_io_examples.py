"""Examples for dictionary input and output.

Usage:
  python dict_io_examples.py --demo
  python dict_io_examples.py --items name=Alice age=30 city=NY
  python dict_io_examples.py --file sample.json --items a=1 b=two
"""

import argparse
import json
import sys
from typing import Dict, Any, List


def interactive_input() -> Dict[str, Any]:
    """Interactively build a dictionary from user input.

    Enter lines like "key=value". Leave blank to finish.
    Values that look like integers will be converted to int.
    """
    print("Enter key=value pairs (blank to finish):")
    result: Dict[str, Any] = {}
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            break
        if "=" not in line:
            print("Invalid input — expected key=value")
            continue
        key, val = line.split("=", 1)
        key = key.strip()
        val = val.strip()
        if val.isdigit():
            val_parsed: Any = int(val)
        else:
            # try float
            try:
                val_parsed = float(val)
            except ValueError:
                val_parsed = val
        result[key] = val_parsed
    return result


def parse_items(items: List[str]) -> Dict[str, Any]:
    d: Dict[str, Any] = {}
    for item in items:
        if "=" not in item:
            continue
        k, v = item.split("=", 1)
        k = k.strip()
        v = v.strip()
        if v.isdigit():
            d[k] = int(v)
        else:
            try:
                d[k] = float(v)
            except ValueError:
                d[k] = v
    return d


def save_json(obj: Dict[str, Any], filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def load_json(filename: str) -> Dict[str, Any]:
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def pretty_print(obj: Dict[str, Any]) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def demo() -> None:
    sample = {"name": "Alice", "age": 30, "scores": {"math": 95, "eng": 88}}
    print("Sample dictionary (in memory):")
    pretty_print(sample)

    fname = "sample.json"
    save_json(sample, fname)
    print(f"Saved to {fname}")

    loaded = load_json(fname)
    print("Loaded from file:")
    pretty_print(loaded)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Dictionary input/output examples")
    parser.add_argument("--demo", action="store_true", help="Run non-interactive demo")
    parser.add_argument("--file", help="JSON filename to save to / load from")
    parser.add_argument("--items", nargs="*", default=[], help="Key=value items to build a dict")
    parser.add_argument("--interactive", action="store_true", help="Build a dict interactively")
    args = parser.parse_args(argv)

    if args.demo:
        demo()
        return

    d = {}
    if args.items:
        d.update(parse_items(args.items))

    if args.interactive:
        d.update(interactive_input())

    if not d:
        print("No data provided. Use --items or --interactive, or --demo for an example.")
        return

    print("Resulting dictionary:")
    pretty_print(d)

    if args.file:
        save_json(d, args.file)
        print(f"Saved to {args.file}")


if __name__ == "__main__":
    main()
