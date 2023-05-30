import openai

API_KEY = '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'


class ChatBot:

    def get_response(self, query):
        openai.api_key = API_KEY
        reply = openai.Completion.create(
            engine='text-davinci-002',
            prompt=query,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return reply


if __name__ == '__main__':
    chatbot = ChatBot()
    answer = chatbot.get_response('Write a Dad joke')
    print(answer)
