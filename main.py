import sys
from set_operations import SetOperations
from file_handler import FileHandler
from merge_sort import MergeSort

def extract_filename(arg):
    return arg.split('=')[1]

def write_result(result):
    sorted_result = MergeSort.merge_sort(list(result))
    with open('result.txt', 'w') as output_file:
        if not result:
            output_file.write("empty set")
        else:
            output_file.write('\n'.join(sorted_result))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 setops.py \"set1=[filename];set2=[filename];operation=[difference|union|intersection]\"")
        sys.exit(1)

    command_line = sys.argv[1]
    set1_filename = extract_filename(command_line.split(';')[0])
    set2_filename = extract_filename(command_line.split(';')[1])
    operation = command_line.split(';')[2].split('=')[1]

    set_ops = SetOperations(set1_filename, set2_filename, operation)
    result = set_ops.perform_operation()

    if result is not None:
        write_result(result)
