#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""

import sys
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)
line_count = 0

valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}


def print_stats():
    """Prints accumulated metrics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()

        if len(parts) >= 7:
            status = parts[-2]
            file_size = parts[-1]

            if status in valid_status_codes:
                status_counts[status] += 1

            try:
                total_size += int(file_size)
            except ValueError:
                pass

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
