api
def query_llm(prompt, query):
    openai.api_key = 'your_openai_api_key'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{query}\n\n{prompt}",
        max_tokens=150
    )
    return response.choices[0].text.strip()
