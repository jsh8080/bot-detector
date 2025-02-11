from openai import OpenAI

#harnessing the text file ofyoutibe comments
comment_base = open('comment_base.txt','r',encoding='utf-8')
comment_edits = open('AI_comment_edits','w',encoding='utf-8')
file_content = comment_base.read()

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI()

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
            {"role": "system", "content": "You are a helpful AI that processes text."},
        {"role": "user", "content": f"Here is some text of youtube comments; give me the comments in the same spaced format, but with a statistic next to each comment of the propability that comment is a bot, show the statistic with just the number followed by a percent sign, it does not have to be completely accurate just based on what bots usually comment. Show every comment:\n\n" + file_content},
    ],
)
print(completion.choices[0].message.content)
comment_edits.write(completion.choices[0].message.content)
comment_edits.close()
