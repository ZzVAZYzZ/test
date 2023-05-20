import openai

# import os

openai.organization = 'org-AjTmCQ65Mt7m97gU3ZB8Gw6k'
openai.api_key = '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'

data2 = None

def execute_data(data):
    global data2
    data2 = data
    return data2

def inputText():
    global data2
    return data2

def prompt():
    x = inputText()
    main = f'As a Python expert, can you teach me about {x}'
    return main


def generate_response():
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt(),
        max_tokens=500,
        temperature=0.7
    )
    response = completion.choices[0].text
    return response


def get_response():
    response = generate_response()
    return response