from PyPDF2 import PdfReader
import re
import os

def extract_titles_and_summary(file_path):
    try:
        reader = PdfReader(file_path)
        first_pages_text = "\n".join([reader.pages[i].extract_text() for i in range(min(3, len(reader.pages)))])
        
        # Attempt to find titles
        title_match_german = re.search(r'^(.*?)\n', first_pages_text, re.MULTILINE)
        title_match_english = re.search(r'^(.*?)\n', first_pages_text[title_match_german.end():], re.MULTILINE) if title_match_german else None
        
        german_title = title_match_german.group(1).strip() if title_match_german else "German title not found"
        english_title = title_match_english.group(1).strip() if title_match_english else "English title not available"
        
        # Extract summary by taking a portion of text after titles
        summary_start = title_match_english.end() if title_match_english else title_match_german.end() if title_match_german else 0
        summary_text = first_pages_text[summary_start:summary_start+50000]  # Adjust length as needed
        summary = " ".join(summary_text.split('\n')[1:10]).strip()  # Clean and limit the summary length

        return {"file_path": file_path, "german_title": german_title, "english_title": english_title, "summary": summary}
    except Exception as e:
        return {"file_path": file_path, "german_title": "Error processing file", "english_title": str(e), "summary": "Summary extraction failed"}

def process_pdf_folder(folder_path):
    documents_info = []
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith('.pdf'):
            file_path = os.path.join(folder_path, file_name)
            documents_info.append(extract_titles_and_summary(file_path))
    return documents_info

# Example usage
folder_path = r'pathToFiles'  # Update this path to your folder containing PDF files
extracted_info = process_pdf_folder(folder_path)
for doc_info in extracted_info:
    print(f"File: {doc_info['file_path']}\nGerman Title: {doc_info['german_title']}\nEnglish Title: {doc_info['english_title']}\nSummary: {doc_info['summary']}\n")

