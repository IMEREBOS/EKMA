import re


def clean_text(text):
    """
    Remove extra spaces, tabs, and blank lines.
    """

    text = re.sub(r'\s+', ' ', text)

    return text.strip()

def split_text(text, chunk_size=500):
    """
    Split text into chunks of approximately chunk_size characters.
    """

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks