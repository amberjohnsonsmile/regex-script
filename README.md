# Regex Script

This script can identify "bad" rows in a dataset based on regex from the python-database-sanitizer library. This can help narrow down issues with the data failing to be sanitized.

# How to Run

1. [Install python 3.6](https://www.python.org/downloads/) or newer to run the script. 
2. Make a copy of data-example.py. The gitignore is set up to ignore data.py. From this directory, run:
```
cp data-example.py data.py
```
3. Open data.py and insert the rows in question into the array.
4. From this directory, run the script:
```
python3 main.py
```

The script will log all rows that have issues with the regex and details on which characters caused the issue. Items will be flagged if they DO NOT match the regex.
