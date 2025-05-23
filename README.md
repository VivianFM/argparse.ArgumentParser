## `argparse.ArgumentParser` - Quick Guide

If you're writing a Python script that needs command-line arguments, like --log-level, --test, or a file path — argparse is an essential tool.

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

## Practical example

See [`example_argparse_usage.py`](./example_argparse_usage.py) for a complete example.

Run your script like this:

```bash
python example_argparse_usage.py textfile.txt --test --log-level INFO --log-to-file

```

And `args` will look like:

```python
Namespace(filepath='textfile.txt', test=True, log_level='DEBUG', log_to_file=True)
```

Breakdown of the features:

| Argument           | Action              | Behavior                                                                 |
|--------------------|---------------------|--------------------------------------------------------------------------|
| `filepath`         | Positional          | Required path to the `.txt` file to be processed                         |
| `--test`, `-t`     | `store_true`        | Sets `args.test = True` if flag is passed (default is `False`)          |
| `--log-level`      | `default`, `choices`| Accepts only: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` (default: `WARNING`) |
| `--log-to-file`    | `store_true`        | If passed, logs are written to `logfile.log` instead of the console      |
| `--help`, `-h`     | Built-in            | Displays the auto-generated usage guide with all arguments and exits     |

> **Note:**
> 
> Logging levels are hierarchical. `DEBUG` < `INFO` < `WARNING` < `ERROR` < `CRITICAL`.
> 
> This means setting the log level to `INFO` will include `INFO`, `WARNING`, `ERROR`, and `CRITICAL` messages, but exclude `DEBUG`.
> 
> `--help` is a built-in argument automatically added by argparse that displays a usage guide, showing all available arguments, their descriptions, and default values.

---

### Bonus Tip

Run your script with `--help` to get auto-generated usage docs:

```bash
python example_argparse_usage.py textfile.txt --help
```

Output:

```
usage: teste.py [-h] [-t] [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--log-to-file] filepath

Count lines in a text file with optional test mode and logging.

positional arguments:
  filepath              Path to the .txt file to process.

options:
  -h, --help            show this help message and exit
  -t, --test            Run in test mode (does not read the file).
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level (default: WARNING).
  --log-to-file         If set, logs will be saved to 'output.log' instead of printed to console.
```

---

# Logging

## `logging.basicConfig()`: Logging Configuration Explained

The `logging` module in Python is a powerful built-in library used for tracking events and errors that happen during the execution of your program. 

One of its key components is the function `logging.basicConfig()`, which is used to set up the basic configuration for the logging system. 

Purpose:

 - Configures log messages (their format, level of importance, etc.).

 - Determines the output destination (such as a file or the console).

 - Defines the severity level (e.g., DEBUG, INFO, WARNING).

Here’s your table updated with the code in a separate column for clarity:

| Parameter   | Code Example                                      | Purpose                                                                 |
|-------------|---------------------------------------------------|-------------------------------------------------------------------------|
| `filename`  | `filename="logfile.log"`                          | Path to the log file (only set if `--log-to-file` is used)              |
| `level`     | `level=args.log_level.upper()`                    | Sets the logging severity (e.g., `DEBUG`, `INFO`, `WARNING`, etc.)      |
| `format`    | `format="%(asctime)s - %(levelname)s - %(message)s"` | Specifies the format of each log message                                |
| `datefmt`   | `datefmt="%Y-%m-%d %H:%M:%S"`                     | Controls how timestamps appear in log messages                          |

Log message format:
```text
2025-04-24 15:45:23 - INFO - Something important happened!
```
    
## `set_logger(args)` Function
The `set_logger(args)` function wraps `logging.basicConfig()` to **centralize the configuration**, enable **conditional logic**, and **simplify the main code**.

   What `set_logger(args)` does:
   - Reads arguments from args (parsed by argparse)

   - Checks if the user passed `--log-to-file`

        - If yes: logs are saved to `logfile.log`

        - If no: logs are printed to the console (stdout)


This makes it easy to control what gets logged and where it goes — all from the command line. Very handy for debugging or monitoring script behavior in real scenarios.

# Summary
- `argparse.ArgumentParser` is used to handle command-line arguments. It parses user input from the command line (like --test, --verbose, filename.txt, etc.) and turns them into usable variables in your script.

- `logging.basicConfig()` is part of the logging module and is used to configure how your program outputs logs (like errors, info, warnings, etc.).

Sure! Here's your comparison neatly formatted as a table in Markdown:


| **Feature**         | **`argparse.ArgumentParser`**                             | **`logging` / `logging.basicConfig()`**                           |   
|---------------------|------------------------------------------------------------|--------------------------------------------------------------------|
| **Purpose**         | Parse and capture user input from the CLI                  | Display, store, or manage runtime messages (e.g., errors, info) |    
| **What it controls**| What the user wants the program to do                      | How the program communicates what it’s doing                    |    
| **Example usage**   | `--log-level DEBUG`, `input.txt`                           | `logging.basicConfig(level=logging.DEBUG)`, `logging.info("File opened")`, `logging.error("File not found")` |
| **Output**          | A structured object of arguments (`args`)                  | Text messages in the console or written to a log file            |

---

## References

- [Official Python `argparse` Documentation](https://docs.python.org/3/library/argparse.html)
- [Official Python `logging` Documentation](https://docs.python.org/3/library/logging.html)

