from resiliparse.extract.html2text import extract_plain_text
from resiliparse.parse.encoding import detect_encoding

def run_extract_text_from_html_bytes(html_bytes: bytes) -> str | None:
    if html_bytes is None or len(html_bytes) == 0:
        return None
    try:
        html_str = html_bytes.decode("utf-8")
    except UnicodeDecodeError:
        encoding = detect_encoding(html_bytes)
        html_str = html_bytes.decode(encoding)
    text = extract_plain_text(html_str)
    return text