import argparse
import re

def parse_file(filename):
    result = []
    with open(filename, "r") as f:
        for line in f:
            match = re.match(r'\"(.*)\"\s*=\s*\"(.*)\"\s*;', line)
            if match:
                key, value = match.group(1), match.group(2)
                result.append({key: value})

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to parse for strings files")
    args = parser.parse_args()
    result = parse_file(args.path)
    print(result)