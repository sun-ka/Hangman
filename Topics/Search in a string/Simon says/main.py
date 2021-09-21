def what_to_do(instructions):
    condition = instructions.endswith("Simon says") or instructions.startswith("Simon says")

    if condition:
        action = instructions.replace("Simon says", "").strip()
        return f"I {action}"

    return "I won't do it!"
