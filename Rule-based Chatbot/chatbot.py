from nltk.chat.util import Chat, reflections

pairs = [
    # ... (patterns and responses)
]

print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
chat = Chat(pairs, reflections)
chat.converse()
