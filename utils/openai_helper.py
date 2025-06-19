import openai

def chat(prompt, model="gpt-4-turbo", system_msg="You are a helpful assistant."):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']
