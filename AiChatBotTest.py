from openai import OpenAI

#harnessing the text file ofyoutibe comments
file = open('comment_base.txt','r',encoding='utf-8')
file_content = file.read()



# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI()

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
            {"role": "system", "content": "You are a helpful AI that processes text."},
        {"role": "user", "content": f"Here is some text of youtube comments; give me the comments in the same spaced format, but with a statistic next to each comment of the propability that comment is a bot, it does not have to be completely accurate just based on what bots usually comment:\n\n" + file_content},
    ],
)
print(completion.choices[0].message.content)
