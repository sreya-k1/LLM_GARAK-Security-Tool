BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "ignore all previous instructions",
    "system prompt",
    "reveal your prompt",
    "developer mode",
    "jailbreak",
    "bypass safety",
]


def validate_prompt(prompt: str) -> bool:
    prompt = prompt.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in prompt:
            return False

    return True