"""Utility functions for cleaning and formatting text strings."""

def clean_name(raw):
    """Clean a messy name string by:
    - Removing surrounding whitespace
    - Collapsing repeated inner spaces
    - Converting to title case
    """
    cleaned = " ".join(raw.split())   # collapse whitespace
    return cleaned.title()            # convert to title case

