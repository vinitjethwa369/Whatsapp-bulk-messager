## WhatsApp Bulk Messenger Automation

**This is a Python script for sending bulk WhatsApp messages along with image attachments using Selenium. It automates the process of opening WhatsApp Web, loading the contacts from a file, and sending messages or images.**

**Features**

* Sends a predefined message to multiple contacts.
* Allows attaching and sending images along with the message.
* Uses explicit waits to ensure elements are properly loaded before interacting.

**Prerequisites**

* Python 3.6 or higher
* Google Chrome browser
* WhatsApp Web login

**Installation**

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/whatsapp-bulk-messenger.git
```

2. **Navigate to the project directory:**

```bash
cd whatsapp-bulk-messenger
```

3. **Install the required Python packages:**

```bash
pip install -r requirements.txt
```

4. **Ensure files are formatted correctly:**

* `message.txt`: Contains the message to be sent.
* `numbers.txt`: Contains the phone numbers (without the country code) on separate lines.

**Usage**

1. **Edit the configuration in the script (optional):**

* `country_code`: Set your country code (default: None)
* `image_path`: Path to your image for attachment (default: None)

2. **Run the script:**

```bash
python whatsapp_bulk_messenger.py
```

**A Chrome window will open, and you'll need to log in to WhatsApp Web within the configured time (login_time). After logging in, the script will automatically send the message to all numbers in the numbers.txt file.**

**Files**

* `message.txt`: Text file containing the message to be sent.
* `numbers.txt`: Text file containing phone numbers in each line (without country code).
* `whatsapp_bulk_messenger.py`: Main Python script to send WhatsApp messages.

**Requirements**

* Selenium WebDriver
* ChromeDriver (Managed automatically using webdriver_manager)

**requirements.txt:**

```
selenium==4.4.3
webdriver-manager==3.8.0
```

**Steps to Run**

1. Clone the repository as shown above.
2. Navigate to the project directory.
3. Install the required packages using `pip install -r requirements.txt`.
4. Add your message in `message.txt` and phone numbers (one per line) in `numbers.txt`.
5. Run the script with `python whatsapp_bulk_messenger.py`.

**Make sure that Google Chrome is installed and ChromeDriver is updated. After running the script, log in to WhatsApp Web when prompted, and the messages will be sent automatically.**
