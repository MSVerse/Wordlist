# Wordlist
wordlist generator 

# Announcement 
The creator of the wordlist tool is not responsible for any consequences or misuse that may arise from using this tool. The tool is provided as-is without any warranty. Please use it responsibly and at your own risk. The creator shall not be held liable for any damages or issues caused by the use or misuse of this tool.

# Usage 
```
Usage: python wordlist.py [--characters CHARACTERS] [--min_length MIN_LENGTH] [--max_length MAX_LENGTH] [--output_file OUTPUT_FILE]

Options:
  --characters CHARACTERS    Characters used in the wordlist (default: "abcdefghijklmnopqrstuvwxyz0123456789")
  --min_length MIN_LENGTH    Minimum password length (default: 1)
  --max_length MAX_LENGTH    Maximum password length (default: 5)
  --output_file OUTPUT_FILE  Output file name to save the wordlist (default: "wordlist.txt")
```

# Example 
```
python wordlist.py --characters "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*" --min_length 3 --max_length 10 --output_file wordlist.txt
```

This example generates a wordlist with characters from lowercase letters, uppercase letters, numbers, and special characters. The wordlist will have passwords with lengths ranging from 3 to 10 characters, and it will be saved in a file named "wordlist.txt".

## Support Me

If you would like to support me, please visit my website at [https://www.msverse.site](https://www.msverse.site).
