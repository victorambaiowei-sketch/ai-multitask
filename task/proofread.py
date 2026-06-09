def proofread(content, tone):
    prompt=f"""
proofread and improve the content below
content:{content}

fix:
- grammar

- clarity

-readability

-reinforce the tone:
{tone}

Do not change meaning or idea

"""
return proofread(prompt)