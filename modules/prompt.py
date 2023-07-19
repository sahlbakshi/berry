def getPrompt(name, info):
    prompt = '''
    Use the relevant information from the text below to generate 1 to 4 for the following {name}
    {info}
    1. Company name 
    2. Refund policy 
    3. Time frame of Refund Policy 
    4. What's not covered in the refund policy? 
    '''.format(name=name, info=info)
    return prompt