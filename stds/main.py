# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Your code here
import sys

def main():
    # TODO: read text from stdin

    # TODO: Filter character given as an argument from the text

    # TODO: Print the result to stdout

    # TODO: Print the total number of removed characters to stderr
    text = sys.stdin.read()
    
    char = sys.argv[1]
    filtered_text = text.replace(char, "")
    num_char_removed = text.count(char)

    sys.stdout.write(f'{filtered_text}')
    sys.stderr.write(f'{str(num_char_removed)}')


if __name__ == "__main__":
    main()
