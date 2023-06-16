import argparse
import re


# result: [{}]
def parse_file(filename):
    result = []
    with open(filename, "r") as f:
        key_group = []
        for line in f:
            match = re.match(r'\"(.*)\"\s*=\s*\"(.*)\"\s*;', line)
            if match:
                key, value = match.group(1), match.group(2)

                if key in key_group:
                    continue
                else:
                    key_group.append(key)

                result.append({key: value})

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to parse for strings files")
    args = parser.parse_args()
    result = parse_file(args.path)
    print(result)