def apply_tone(content, tone):
    prompt= f"""
rewrite the content below using the tone:
{tone}

content:
{content}

"""

return apply_tone(prompt)

