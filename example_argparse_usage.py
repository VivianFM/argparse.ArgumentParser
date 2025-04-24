import argparse
import logging
import sys
import os

def parse_arguments():
    """Argument parser."""
    parser = argparse.ArgumentParser(description="Count lines in a text file with optional test mode and logging.")

    parser.add_argument(
        "filepath",
        help="Path to the .txt file to process."
    )

    parser.add_argument(
        "-t", "--test",
        action="store_true",
        help="Run in test mode (does not read the file)."
    )

    parser.add_argument(
        "--log-level",
        default="WARNING",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: WARNING)."
    )

    parser.add_argument(
        "--log-to-file",
        action="store_true",
        help="If set, logs will be saved to 'output.log' instead of printed to console."
    )

    return parser.parse_args()

def set_logger(args) -> None:
    """Configure logging based on parsed arguments."""
    if args.log_to_file:
        logging.basicConfig(
            filename="logfile.log",
            level=args.log_level.upper(),
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    else:
        logging.basicConfig(
            level=args.log_level.upper(),
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )


def count_lines_in_file(filepath, test_mode=False):
    """Counts the number of lines in a given file."""
    if test_mode:
        logging.info("Test mode: skipping actual file processing.")
        return

    if not os.path.exists(filepath):
        logging.error(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        line_count = len(lines)
        logging.info(f"Processed file: {filepath}")
        logging.info(f"Total lines: {line_count}")
        print(f" {filepath} has {line_count} lines.")

def main():
    args = parse_arguments()
    set_logger(args)
    count_lines_in_file(args.filepath, test_mode=args.test)

if __name__ == "__main__":
    main()
