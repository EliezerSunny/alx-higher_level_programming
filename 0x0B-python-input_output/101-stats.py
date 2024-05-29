#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """Print the statistics of total file size and status code counts"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def parse_line(line):
    """Parse a log line to extract the status code and file size"""
    parts = line.split()
    status_code = int(parts[-2])
    file_size = int(parts[-1])
    return status_code, file_size

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        try:
            status_code, file_size = parse_line(line)
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        except Exception as e:
            # Skip lines that don't match the expected format
            continue

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    pass

finally:
    print_stats(total_size, status_codes)
