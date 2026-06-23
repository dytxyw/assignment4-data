from __future__ import annotations

import os
from typing import Any



def run_extract_text_from_html_bytes(html_bytes: bytes) -> str | None:
    # raise NotImplementedError
    from cs336_data.extract_text import run_extract_text_from_html_bytes
    return run_extract_text_from_html_bytes(html_bytes)


def run_identify_language(text: str) -> tuple[Any, float]:
    from cs336_data.language_identification import run_identify_language
    return run_identify_language(text)
    # raise NotImplementedError



def run_mask_emails(text: str) -> tuple[str, int]:
    # raise NotImplementedError
    from cs336_data.mask_email import run_mask_emails
    return run_mask_emails(text)


def run_mask_phone_numbers(text: str) -> tuple[str, int]:
    # raise NotImplementedError
    from cs336_data.mask_phone_numbers import run_mask_phone_numbers
    return run_mask_phone_numbers(text)


def run_mask_ips(text: str) -> tuple[str, int]:
    # raise NotImplementedError
    from cs336_data.mask_ip import mask_ip_addresses
    return mask_ip_addresses(text)


def run_classify_nsfw(text: str) -> tuple[Any, float]:
    # raise NotImplementedError
    from cs336_data.classify_nsfw import run_classify_nsfw
    return run_classify_nsfw(text)


def run_classify_toxic_speech(text: str) -> tuple[Any, float]:
    # raise NotImplementedError
    from cs336_data.classify_toxic_speech import run_classify_nsfw
    return run_classify_nsfw(text)


def run_classify_quality(text: str) -> tuple[Any, float]:
    raise NotImplementedError


def run_gopher_quality_filter(text: str) -> bool:
    raise NotImplementedError


def run_exact_line_deduplication(
    input_files: list[os.PathLike], output_directory: os.PathLike
):
    raise NotImplementedError


def run_minhash_deduplication(
    input_files: list[os.PathLike],
    num_hashes: int,
    num_bands: int,
    ngrams: int,
    jaccard_threshold: float,
    output_directory: os.PathLike,
):
    raise NotImplementedError
