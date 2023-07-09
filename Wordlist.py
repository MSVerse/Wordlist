import itertools
import argparse

def generate_wordlist(characters, min_length, max_length, output_file):
    with open(output_file, "w") as file:
        for length in range(min_length, max_length + 1):
            for combination in itertools.product(characters, repeat=length):
                password = "".join(combination)
                file.write(password + "\n")

    print("Wordlist generated successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wordlist Generator")
    parser.add_argument("--characters", type=str, default="abcdefghijklmnopqrstuvwxyz0123456789",
                        help="Characters used in the wordlist")
    parser.add_argument("--min_length", type=int, default=1,
                        help="Minimum password length")
    parser.add_argument("--max_length", type=int, default=5,
                        help="Maximum password length")
    parser.add_argument("--output_file", type=str, default="wordlist.txt",
                        help="Output file name to save the wordlist")
    args = parser.parse_args()

    characters = args.characters + "!@#$%^&*"  # special characters
    generate_wordlist(characters, args.min_length, args.max_length, args.output_file)
