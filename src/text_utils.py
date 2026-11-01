"""Utilities for cleaning text."""

def clean_name(raw):
    """Clean a name by removing extra spaces and using title case."""
    cleaned = " ".join(raw.split())
    return cleaned.title()
