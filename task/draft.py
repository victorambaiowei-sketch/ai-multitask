def draft(outline: str) -> str:
    prompt= f"""
    
    Expand the following outline into a complete article
    outline: {outline}

    write a detailed paragraph
    """

    return draft(prompt)