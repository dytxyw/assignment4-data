import re

def mask_ip_addresses(text):
    octet = r'(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)'
    ip_pattern = rf'\b{octet}\.{octet}\.{octet}\.{octet}\b'
    masked_text, count = re.subn(pattern=ip_pattern,
                                    repl='|||IP_ADDRESS|||',
                                    string=text)
    return masked_text, count