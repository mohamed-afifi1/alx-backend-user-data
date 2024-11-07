#!/usr/bin/env python3
"""personal data"""

from typing import List
import re


def filter_datum(fields: List,
                 redaction: str,
                 message: str,
                 separator: str):
    """
    Filters personal data according to the provided
    redaction pattern and returns the filtered message.
    """
    result = message
    for field in fields:
        old_pattern = field + '=.*?' + separator
        new_pattern = field + '=' + redaction + separator
        result = re.sub(old_pattern, new_pattern, result)
    return result
