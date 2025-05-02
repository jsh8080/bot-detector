from openai import OpenAI

#harnessing the text file ofyoutibe comments
comment_base = open('botDetector/comment_base.txt','r',encoding='utf-8')
comment_edits = open('botDetector/AI_comment_edits.txt','w',encoding='utf-8')
file_content = comment_base.read()

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI()

def make_request():
# Non-streaming:
    comment_base = open('botDetector/comment_base.txt','r',encoding='utf-8')
    comment_edits = open('botDetector/AI_comment_edits.txt','w',encoding='utf-8')
    file_content = comment_base.read()

    print("----- standard request -----")
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
            {"role": "system", "content": "You are a helpful AI that analyzes youtube comments for bot-like behavior"},
            {"role": "user", "content": f"look at these comments and return the full list with percentages next to each of the likelihood they are a bot, fix html syntax" + file_content},
        ],
    )
    comment_edits.write(completion.choices[0].message.content)
    comment_edits.close()
    return completion.choices[0].message.content

#use only to test out the function in this file, otherwise leave commented
#print(make_request())
