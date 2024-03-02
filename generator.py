# generator.py

# This module contains functions for generating and customizing prompts for customer service chatbots.

def generate_prompt(query_type: str) -> str:
    default_prompts = {
        "welcome": "Hello! How can I assist you today?",
        "order_status": "Please provide your order number for a status update.",
        "product_inquiry": "What product information can I assist you with?"
    }

    return default_prompts.get(query_type, "How can I assist you today?")

def customize_prompt(base_prompt: str, customizations: dict) -> str:
    for placeholder, replacement in customizations.items():
        base_prompt = base_prompt.replace(f"[{placeholder}]", replacement)
    return base_prompt

def prompt_suggestions(base_prompt: str) -> list:
    suggestions = [
        f"Could you please {base_prompt.lower()}?",
        f"To assist you better, {base_prompt.lower()}",
        f"For a faster response, {base_prompt.lower()}"
    ]
    return suggestions


if __name__ == "__main__":
    # Test generate_prompt
    print(generate_prompt("welcome"))

    # Test customize_prompt
    print(customize_prompt("Hello, [name]! How can I assist you today?", {"name": "Edward"}))

    # Test prompt_suggestions
    print(prompt_suggestions("please provide your order number"))

