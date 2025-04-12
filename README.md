# Gmail Bulk Email Sender

This Python script sends personalized emails to a list of contacts using the Gmail API with OAuth 2.0 authentication.

## Prerequisites

*   Python 3.x
*   Google Account

## Setup

1.  **Clone or download this project.**

2.  **Install required libraries:**

    ```bash
    pip install pandas google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```

3.  **Enable the Gmail API and get credentials:**

    *   Go to the [Google Cloud Console](https://console.cloud.google.com/).
    *   Create a new project or select an existing one.
    *   Enable the **Gmail API** for your project.
    *   Go to "Credentials" in the left sidebar.
    *   Click "Create Credentials" and select "OAuth client ID".
    *   Configure the consent screen if you haven't already.
    *   Choose "Desktop app" as the application type.
    *   Give your client ID a name (e.g., "Gmail Sender Desktop App").
    *   Click "Create".
    *   **Download the JSON file** containing your client ID and secret. **Rename this file to `credentials.json`** and place it in the same directory as the `send_email_oauth.py` script.

4.  **Prepare your contacts list:**

    *   Open the `contacts.csv` file.
    *   Keep the header row: `Email,Name`
    *   Add your contacts below the header, one per line, with their email address and name separated by a comma.
    *   **Example:**
        ```csv
        Email,Name
        friend1@example.com,Friend One
        colleague@example.com,Colleague Two
        ```

5.  **Customize the email:**

    *   Open `send_email_oauth.py` in a text editor.
    *   **Replace `"your_email@example.com"` with your actual Gmail address** in the `sender_email` variable.
    *   **Modify the `subject` variable** with your desired email subject line.
    *   **Update the `body` variable** with your email content. You can use f-string formatting like `{recipient_name}` to personalize the email.

## Running the Script

1.  Open your terminal or command prompt.
2.  Navigate to the project directory.
3.  Run the script:

    ```bash
    python send_email_oauth.py
    ```

4.  **First Run - Authorization:**

    *   The script will print a URL to the console.
    *   Copy this URL and paste it into your web browser.
    *   Log in with the Google Account you want to send emails from.
    *   Grant the application permission to send emails on your behalf.
    *   After successful authorization, you'll be redirected to a page (likely showing a "localhost" address). The script will detect this and create a `token.pickle` file in the project directory. This file stores your authorization token for future runs.

5.  **Subsequent Runs:**

    *   The script will use the `token.pickle` file to automatically authenticate and will start sending emails immediately.

## Important Notes

*   **Gmail Sending Limits:** Be mindful of Gmail's daily sending limits to avoid getting your account flagged.
*   **Security:** Keep your `credentials.json` and `token.pickle` files secure. Do not share them publicly.
*   **Error Handling:** The script includes basic error handling for the `contacts.csv` file but may need more robust error checking for production use. 