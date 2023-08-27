# PDF Resume Email Extractor

This Python script allows you to extract email addresses from PDF resumes in a given directory and save them to a text file. Follow the steps below to set up and use the script.

## Prerequisites

### 1. Python Installation

If you don't have Python installed on your system, follow these steps:

a. Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
b. Choose the version suitable for your operating system (Windows, macOS, or Linux).
c. Download the installer and run it.
d. During the installation, make sure to check the option that adds Python to your system's PATH.

### 2. Git Installation (Optional)

If you're planning to clone this repository using Git, you can install Git from: [https://git-scm.com/downloads](https://git-scm.com/downloads)

## Setup

### 1. Clone the Repository

If you have Git installed, open your terminal/command prompt and navigate to the directory where you want to store the script. Then, run:

```bash
git clone https://github.com/your-username/your-repo.git
```

If you don't have Git, you can download the repository as a ZIP file from GitHub and extract it.

### 2. Install Required Libraries
Open your terminal/command prompt and navigate to the repository's directory:

```bash
cd your-repo
```
Install the required libraries using the following command:

```bash
pip install pdfplumber
```

## Usage
### 1. Prepare Your PDFs
Place the PDF resumes you want to extract emails from in a directory. Make sure that each PDF contains text that you want to extract emails from.

### 2. Run the Script
Open your terminal/command prompt and navigate to the repository's directory:

```bash
cd your-repo
```

Run the script by providing the input directory (where the PDFs are located) and the output directory (where the extracted emails will be saved):

```bash
python script.py --input_dir path/to/input/directory --output_dir path/to/output/directory
```

For example:

```bash
python script.py --input_dir /path/to/resumes --output_dir /path/to/output
```

The script will process the PDFs and save the extracted emails to a file named "Extracted_Emails.txt" in the output directory.

## Result
After running the script, you'll find a file named "Extracted_Emails.txt" in your specified output directory. This file will contain the extracted email addresses from the PDF resumes.

<mark> Make sure to replace your-username and your-repo with your actual GitHub username and repository name. </mark>

Happy email extracting! 📧👍
