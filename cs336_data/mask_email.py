import re
def run_mask_emails(text: str) -> tuple[str, int]:
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    masked_text, count = re.subn(
        pattern=email_pattern,
        repl='|||EMAIL_ADDRESS|||',
        string=text
    )
    return (masked_text, count)