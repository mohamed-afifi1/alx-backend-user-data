#!/usr/bin/env python3
"""personal data"""

from typing import List
import re


def filter_datum(fields: List,
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Filters personal data"""
    result = message
    for field in fields:
        new_pattern = field + '=' + redaction + separator
        result = re.sub(field + '=.*?' + separator,
                        field + '=' + redaction + separator, result)
    return result
