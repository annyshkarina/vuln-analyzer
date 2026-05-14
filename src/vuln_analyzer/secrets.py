import re

def detect_secrets(code: str):
    issues = []

    patterns = {
        "Password": r"(?i)password\s*=\s*['\"].+?['\"]",
        "API Key": r"(?i)api[_-]?key\s*=\s*['\"][A-Za-z0-9_\-]{10,}['\"]",
        "AWS Key": r"AKIA[0-9A-Z]{16}",
        "Token": r"(?i)token\s*=\s*['\"][A-Za-z0-9_\-]{10,}['\"]",
        "Secret": r"(?i)secret\s*=\s*['\"].+?['\"]",
    }

    for name, pattern in patterns.items():
        if re.search(pattern, code):
            issues.append(f"Possible {name} detected")

    return issues if issues else ["No secrets detected"]
