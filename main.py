import re
from data import rows

def main():
    VALUE_PATTERN = re.compile(
        r"""
        # Group 1:
        (
            '(?:[^']|''|\\')*(?<![\\])'     # String literal
            |                               # or...
            [^',()]+                        # NULL, TRUE, etc.
        )
        # Group 2:
        (
            [,)]                            # Comma or closing parenthesis.
        )
        """,
        re.VERBOSE,
    )

    for row in rows:
        pos = 1
        values = []
        row_len = len(row)

        while pos < row_len:
            match = VALUE_PATTERN.match(row, pos)
            if not match:
                print(f"This row is breaking things:\n{row}\n")
                print(f"The bad character is: {row[pos]}\n")
                print(f"Bad character with surrounding chars: {row[pos-3]+row[pos-2]+row[pos-1]+row[pos]+row[pos+1]+row[pos+2]+row[pos+3]}")
                print("----------------------------------------")
                break

            value = match.group(1)
            pos += len(value) + 1
            if match.group(2) == ")":
                # Skip comma and open parenthesis ",("
                pos += 2


main()
