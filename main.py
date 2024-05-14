import openai
import environ

# Load environment variables
env = environ.Env.read_env()

# Set OpenAI API key
openai.api_key = env("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="text-davinci-003",  # You can choose a different model if you prefer
            messages=[{"role":"user","content":prompt}]
        )
        return response.choices[0].message['content'].strip()
    except openai.error.RateLimitError as e:
        print("Rate limit exceeded. Please try again later.")
    except Exception as e:
        print("An error occurred:", e)
        return None

if __name__ == "__main__":
    print("Chat with the GPT-3 powered chatbot. Type 'quit', 'exit', or 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        response = chat_with_gpt(user_input)
        if response:
            print("Chatbot:", response)
