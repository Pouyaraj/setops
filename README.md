# Set Operations on Words from Text Files

## Description

This project performs set operations (difference, union, intersection) on words extracted from two text files. The words are case-insensitively sorted and processed to remove punctuation. The result of the set operation is written to an output file.

## Installation

### Prerequisites
 - Python 3.x must be installed on your system. You can download Python from the official website: https://www.python.org/downloads/

 ### Steps
 1. Make sure you have Python installed by running:

 python3 --version

 2. Clone the repository: https://github.com/Pouyaraj/setops.git

## Usage

Navigate to the directory and run the script using the correct command. Here's how you can do it:

1. Open a terminal.

2. Navigate to the project directory:

cd path/to/directory

3. Run the script using the following command:
python3 main.py "set1=[filename];set2=[filename];operation=[difference|union|intersection]"

- set1 and set2 should be replaced with the names of the text files containing the sets of words.
- operation should be one of difference, union, or intersection.

### Example
python3 main.py "set1=a1.txt;set2=b1.txt;operation=union"

## Modules

- file_handler.py
Handles file reading and word extraction.

- merge_sort.py
Contains the merge sort algorithm for sorting words.

- binary_search.py
Contains the binary search algorithm for searching within sorted lists.

- set_operations.py
Performs set operations (difference, union, intersection) on the lists of words.

- main.py
Main entry point for the script. Parses command-line arguments and initiates set operations.

## Output

The result of the set operation is written to result.txt. If the result is empty, the file will contain the text "empty set".


