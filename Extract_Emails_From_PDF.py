import os
import re
import argparse
import pdfplumber

def extractEmails(text):
    emailPatternRegex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    emails = re.findall(emailPatternRegex, text)
    return emails

def processPdf(pdfPath):
    try:
        with pdfplumber.open(pdfPath) as pdf:
            text = ""
            for pageNum in range(len(pdf.pages)):
                page = pdf.pages[pageNum]
                text += page.extract_text()
            
            emails = extractEmails(text)
            return emails
    except Exception as e:
        print(f"Error processing {pdfPath}: {e}")
        return []

def main(inputDir, outputDir):
    allEmails = []
    for filename in os.listdir(inputDir):
        if filename.lower().endswith(".pdf"):
            pdfPath = os.path.join(inputDir, filename)
            emails = processPdf(pdfPath)
            if emails:
                allEmails.extend(emails)

    outputFilePath = os.path.join(outputDir, "Extracted_Emails.txt")
    with open(outputFilePath, 'w') as outputFile:
        outputFile.write('\n'.join(allEmails))

    print(f"All extracted emails have been saved to {outputFilePath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract emails from PDF resumes')
    parser.add_argument("--input_dir", type=str, help="Directory containing PDF resumes", required=True)
    parser.add_argument("--output_dir", type=str, help="Directory to save email addresses", required=True)
    args = parser.parse_args()
    
    main(args.input_dir, args.output_dir)
