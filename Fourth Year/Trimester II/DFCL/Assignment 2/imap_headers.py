from imaplib import IMAP4_SSL
from email import message_from_bytes
from email.parser import HeaderParser
from getpass import getpass

# Getting the email address and password from the user
email = input("Enter your email: ")
password = getpass(prompt="Enter your password: ")

# Creating IMAP object
imap = IMAP4_SSL("imap.gmail.com")

# Login
imap.login(email, password)

# Getting all folders for mailbox
_, folders = imap.list()

# Printing the list of folders
print(
    "List of folders in inbox:\n",
    "\n".join(folder.decode().split(' "/" ')[1].replace('"', "") for folder in folders),
    end="\n\n\n",
)

# Selecting INBOX and getting all messages
imap.select("inbox")
_, all_messages = imap.search(None, "ALL")

# Printing total number of messages in inbox
print(f"Total number of mesages in INBOX : {len(all_messages[0].split())}\n\n\n")

# Get 'n'th mail and print headers
_, nth_mail = data = imap.fetch(
    all_messages[0].split()[int(input("Enter n for print headers of 'n'th mail: "))],
    "(RFC822)",
)
headers = []
parser = HeaderParser()
for response in nth_mail:
    if isinstance(response, tuple):
        headers.extend(
            parser.parsestr(message_from_bytes(response[1]).as_string()).items()
        )

# Print all the headers
print("\n\n".join(f"{key}:\n{value}" for key, value in headers))

# Closing connection
imap.close()
imap.logout()
