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
    "\n".join(folder.decode().split(' "/" ')[1].replace('\"', '') for folder in folders),
    end="\n\n\n",
)

# Getting the meassage and header of first mail
_, all_messages = imap.select("inbox")
_, first_mail = imap.fetch(all_messages[0].decode("utf-8"), "rfc822")

# iterate over response and print headers
headers = []
parser = HeaderParser()
for response in first_mail:
    if isinstance(response, tuple):
        headers.extend(
            parser.parsestr(message_from_bytes(response[1]).as_string()).items()
        )

# Print all the headers
print("\n\n".join(f"{key}:\n{value}" for key, value in headers))

# Closing connection
imap.close()
imap.logout()
