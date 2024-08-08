Selenium Form Submission Script

This script automates the process of filling and submitting a form on the website https://smmpanel.com/signup using Selenium.
Prerequisites

    Python 3.x
    Firefox browser
    GeckoDriver for Firefox (ensure it is added to your system PATH)

Installation

    Clone the repository:

    bash

git clone <https://github.com/Guptaashish2003/IG-Follower-Python-Script>
cd <IG-Follower-Python-Script>

Create a virtual environment:

bash

python -m venv venv

Activate the virtual environment:

    On Windows:

    bash

venv\Scripts\activate

On macOS and Linux:

bash

    source venv/bin/activate

Install the required packages:

bash

    pip install -r requirements.txt

Usage

    Run the script:

    bash

    python form_submission.py

    Follow the prompts:
        Enter the username when prompted.

Code Explanation

The script performs the following steps:

    Sets up the Selenium WebDriver.
    Navigates to the signup page.
    Waits for the form to load.
    Fills in the form fields with provided data.
    Waits for manual captcha verification.
    Submits the form.
    Selects an option from a dropdown and fills additional fields on the next page.

Note

    Ensure that GeckoDriver is installed and added to your system PATH.
    Manual intervention is required to solve the captcha.

Dependencies

    selenium
    faker

License

This project is licensed under the MIT License.
requirements.txt

text

selenium
faker
