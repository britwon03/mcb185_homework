import sys

def generate_matrix(letters, match, mismatch):
    match, mismatch = int(match), int(mismatch)
    print("  " + " ".join(letters))
    for l1 in letters:
        row_values = []
        for l2 in letters:
            if l1 == l2:
                row_values.append(str(match))
            else:
                row_values.append(str(mismatch))
        print(l1, " ".join(row_values))

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <alphabet> <match> <mismatch>")
        return
    generate_matrix(sys.argv[1], sys.argv[2], sys.argv[3])

main()
