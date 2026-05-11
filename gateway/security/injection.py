from fastapi import HTTPException

# These are known prompt injection patterns
INJECTION_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "disregard your instructions",
    "forget your instructions",
    "you are now",
    "act as",
    "pretend you are",
    "pretend to be",
    "jailbreak",
    "dan mode",
    "developer mode",
    "ignore your training",
    "bypass your",
    "override your",
]

def scan_for_injection(text: str) -> None:
    # Convert to lowercase so we catch "IGNORE PREVIOUS" too
    text_lower = text.lower()

    for pattern in INJECTION_PATTERNS:
        if pattern in text_lower:
            raise HTTPException(
                status_code=400,
                detail=f"Prompt injection detected: '{pattern}'"
            )