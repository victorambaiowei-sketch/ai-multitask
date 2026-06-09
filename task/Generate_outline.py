from gemini_client import Ask_gemini
def generate_outline(topic: str) -> str:
    prompt= f"""
    create a detailed outline for
    {topic}

    include:
    - introduction
    - Main sections
    - conclusion

    return only outline
    """

    return ask_gemini(prompt)
     