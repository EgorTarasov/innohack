import openai


def is_ticket_clear(ticket_description: str) -> bool:
    api_key = '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'

    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose different engines depending on your needs
        prompt="is ticket description clear? Answer yes, if you have information on what to do. Evaluate lite. More yes, than no  (answer only one word: yes/no) \description {}",
        max_tokens=50  # You can adjust the max_tokens to limit the response length
    )

    return "yes" in response.choices[0].text.lower()