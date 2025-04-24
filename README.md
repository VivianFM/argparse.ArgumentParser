## `argparse.ArgumentParser` - Quick Guide

If you're writing a Python script that needs command-line arguments, like --log-level, --test, or a file path — argparse is your best friend.

It lets you build intuitive Command-Line Interface (CLI) tools that:

   - Handle arguments (both required, like the filepath, and optional, like --test or --log-to-file)

   - Validate input types and values (e.g., ensuring the --log-level is one of DEBUG, INFO, WARNING, ERROR, or CRITICAL)

   - Automatically generate help messages with the --help flag

   - Provide default values (like --log-level defaulting to WARNING)

---

## Why Use a `parse_arguments()` Function?

- **cleaner, reusable, testable code**.

- Wrapping your argument parser inside a function (like `parse_arguments()`) keeps things organized, avoids cluttering your `main()` logic, and makes your script easier to scale, maintain, and test.

---

## Example: Argument Parsing with `argparse`

See [`example_argparse_usage.py`](./example_argparse_usage.py) for a complete example.

Run your script like this:

```bash
python example_argparse_usage.py textfile.txt --test --log-level DEBUG
```

And `args` will look like:

```python
Namespace(filepath='textfile.txt', test=True, log_level='DEBUG', log_to_file=False)
```

Breakdown of the features:

| Argument           | Action              | Behavior                                                                 |
|--------------------|---------------------|--------------------------------------------------------------------------|
| `filepath`         | Positional          | Required path to the `.txt` file to be processed                         |
| `--test`, `-t`     | `store_true`        | Sets `args.test = True` if flag is passed (default is `False`)          |
| `--log-level`      | `default`, `choices`| Accepts only: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` (default: `WARNING`) |
| `--log-to-file`    | `store_true`        | If passed, logs are written to `logfile.log` instead of the console      |
| `--help`, `-h`     | Built-in            | Displays the auto-generated usage guide with all arguments and exits     |

> **Note:** Logging levels are hierarchical. `DEBUG` < `INFO` < `WARNING` < `ERROR` < `CRITICAL`.  
> This means setting the log level to `INFO` will include `INFO`, `WARNING`, `ERROR`, and `CRITICAL` messages, but exclude `DEBUG`.
> --help is a built-in argument automatically added by argparse that displays a usage guide, showing all available arguments, their descriptions, and default values.

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
