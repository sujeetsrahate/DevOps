import re
file = input("Enter the file path")
f = open(file)
pattern ="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# print(f.readlines())
l = []
for i in f.readlines():
    match = re.findall(pattern,i)
    l.append(match)
    print(match)
print(l)


# import re

# def extract_emails(text):
#     """Extracts all email addresses from the given text."""
#     email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#     emails = re.findall(email_pattern, text)
#     return emails

# def main():
#     """Main function to test email extraction."""
#     sample_text = """
#     Contact us at support@example.com for support.
#     You can also reach out to sales@example.org or hr@example.net.
#     """
#     emails = extract_emails(sample_text)
#     print("Extracted Emails:", emails)

# if __name__ == "__main__":
#     main()