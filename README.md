# Password-Manager

A simple password manager built with Python's Tkinter for the user interface, JSON for data storage, and `pyperclip` for copying generated passwords to the clipboard.

## Features

- **Password Generator**: Generates secure random passwords with letters, numbers, and symbols.
- **Data Storage**: Saves website login information (email and password) securely in a local JSON file.
- **Search Functionality**: Allows users to search for previously saved credentials by website name.
- **Clipboard Copy**: Automatically copies the newly generated password to the clipboard for easy use.

## Getting Started

### Prerequisites

To run this project, you will need to have Python installed on your machine. Additionally, you will need to install the following Python packages:

- `pyperclip` for copying passwords to the clipboard.
  
Install `pyperclip` via pip:

```bash
pip install pyperclip
```

### Running the Application

1. **Clone this repository:**

    ```bash
    git clone https://github.com/your-username/password-manager.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd password-manager
    ```

3. **Install the required Python packages:**

    ```bash
    pip install pyperclip
    ```

4. **Run the application:**

    ```bash
    python main.py
    ```
    
## Usage

1. **Generate a Password**
   - Click the **"Generate Password"** button.
   - A random password will be generated and displayed in the password field.
   - The password will also be copied to your clipboard automatically.

2. **Save Credentials**
   - Fill in the following fields:
     - **Website**: The name of the website or service.
     - **Email/Username**: Your email or username for the website.
     - **Password**: The password you want to save.
   - Click the **"Add"** button to save the credentials.
   - If the `data.json` file does not exist, it will be created automatically.

3. **Search for Credentials**
   - Type the name of the website into the **"Website"** field.
   - Click the **"Search"** button to retrieve the stored email and password for the specified website.
   - If no credentials are found for the entered website, an error message will be displayed.


