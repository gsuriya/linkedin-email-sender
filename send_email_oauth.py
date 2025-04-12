import os
import base64
import pickle
import pandas as pd
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the scope for Gmail API
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

# Authenticate & Create Gmail API Service
def get_gmail_service():
    creds = None
    token_file = "token.pickle"

    # Load existing credentials
    if os.path.exists(token_file):
        with open(token_file, "rb") as token:
            creds = pickle.load(token)

    # If no credentials, authenticate via OAuth
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            
            # Print the OAuth URL in case the browser doesn't open automatically
            print("\n🔗 If the browser does not open automatically, go to this URL manually:")
            print(flow.authorization_url()[0])  # Print authorization URL
            
            creds = flow.run_local_server(port=8080)  # Ensure it matches the redirect URI

        # Save credentials for future use
        with open(token_file, "wb") as token:
            pickle.dump(creds, token)

    return build("gmail", "v1", credentials=creds)

# Function to send an email
def send_email(service, recipient_email, recipient_name):
    sender_email = "your_email@example.com"  # Replace with your Gmail

    # Subject
    subject = "Your Email Subject Here"  # Replace with your desired subject

    # Email Body (with personalized name)
    body = f"""Hi {recipient_name},

This is a placeholder for your email content. 
Make sure to update this before running the script.

Best regards,
Your Name
"""

    # Create MIME message
    message = MIMEText(body, "plain")  # Use "plain" for text email or "html" for formatted emails
    message["to"] = recipient_email
    message["from"] = sender_email
    message["subject"] = subject

    # Encode and send email
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    message_body = {"raw": raw_message}
    service.users().messages().send(userId="me", body=message_body).execute()

# Load contacts from CSV
try:
    contacts = pd.read_csv("contacts.csv")
    contacts.columns = contacts.columns.str.strip()  # Remove extra spaces from column names
except FileNotFoundError:
    print("❌ Error: 'contacts.csv' not found. Please create it and try again.")
    exit()

# Get Gmail service
gmail_service = get_gmail_service()

# Send emails
for _, row in contacts.iterrows():
    send_email(gmail_service, row["Email"], row["Name"])

print("\n✅ Emails sent successfully!")