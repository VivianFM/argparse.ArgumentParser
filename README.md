## `argparse.ArgumentParser` - Quick Guide

If you're writing a Python script that needs command-line arguments — flags like `--verbose`, `--config path`, or `--test-mode` — `argparse` is your best friend.

It lets you build intuitive CLI tools that:
- Handle arguments (both required and optional)
- Validate input types and values
- Generate help messages automatically
- Provide default values

---

## Why Use a `parse_arguments()` Function?

Short answer: **cleaner, reusable, testable code**.

Long answer: Wrapping your argument parser inside a function (like `parse_arguments()`) keeps things organized, avoids cluttering your `main()` logic, and makes your script easier to scale, maintain, and test.

---

## Example: Argument Parsing with `argparse`

```python
import argparse

def parse_arguments():
    """Argument parser."""
    parser = argparse.ArgumentParser(description="")
    
    parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        help="Test mode (does not connect to S3 bucket).",
    )
    
    parser.add_argument(
        "--log-level",
        default="WARNING",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: WARNING).",
    )
    
    parser.add_argument(
        "--log-to-file",
        action="store_true",
        help="If set, log messages will be saved to a file instead of printed to the console.",
    )

    return parser.parse_args()

def main():
    args = parse_arguments()
    print(args)

if __name__ == "__main__":
    main()
```

---

## Real-World Examples

Run your script like this:

```bash
python script.py --test --log-level DEBUG --log-to-file
```

And `args` will look like:

```python
Namespace(test=True, log_level='DEBUG', log_to_file=True)
```

Breakdown of the features:

| Argument         | Action         | Behavior                                                         |
|------------------|----------------|------------------------------------------------------------------|
| `--test`, `-t`   | `store_true`   | Sets `args.test = True` if flag is passed (default is False)     |
| `--log-level`    | `default`, `choices` | Accepts only specified levels, defaults to `'WARNING'`     |
| `--log-to-file`  | `store_true`   | Same as `--test`, turns on the flag if passed                    |

---

## Bonus Tip

Run your script with `--help` to get auto-generated usage docs:

```bash
python script.py --help
```

Output:

```
usage: script.py [-h] [-t] [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--log-to-file]

Compute analytics data.

options:
  -h, --help            show this help message and exit
  -t, --test            Test mode (does not connect to S3 bucket).
  --log-level           Set the logging level (default: WARNING).
  --log-to-file         If set, log messages will be saved to a file instead of printed to the console.
```

---

## Summary

Use `argparse` + a `parse_arguments()` function when:
- You want clean CLI parsing
- You need flexibility (defaults, types, choices, etc.)
- You value readable, testable, professional-looking code

This pattern works for everything from quick scripts to full-blown CLI apps. No excuses — parse like a pro. 
