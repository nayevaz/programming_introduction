# You should not modify this file
import os
import openai


def _call(prompt):
    pre = "k-9"
    KEY = "gbIuWdqMEPTMJOtHYG0T"
    path = os.path.dirname(os.path.abspath(__file__))

    with open(path + "/post.txt") as f:
        lines = f.readlines()

    post = lines[0].strip()
    openai.api_key = "s" + pre + KEY + post

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=300,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response

def recipe(ingredients, instructions):
    if type(ingredients) is not list:
        raise Exception("Provide a list of ingredients.")

    if type(instructions) is not str:
        raise Exception("Provide instructions as text.")

    header = "Write a recipe based on these ingredients and instructions:\nIngredient: "

    ingredient_str = ""
    for ingredient in ingredients:
        ingredient_str = ingredient_str + ingredient + ","

    instruction_str = "\nInstructions: " + instructions
    prompt = header + ingredient_str + instruction_str
    return _call(prompt)
