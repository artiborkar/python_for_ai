# Project 16 — Chat History Appender (no data leak)
# EN: Write add_message(text, history=None) that appends {"role": "user", "content": text} to the history and returns it. Start two SEPARATE conversations and prove their histories do not mix.
# हिंदी: add_message(text, history=None) बनाओ जो {"role": "user", "content": text} को history में जोड़ कर उसे return करे। दो अलग बातचीत शुरू करके साबित करो कि उनकी history आपस में नहीं मिलती।
# Concepts: None default, list of dicts, .append()
# Hint: if history is None: history = [] — otherwise both chats share one list (a privacy bug!).

print("====== Chat History Appender========")

def add_message(text, history=None):

    if history is None:
        history=[]
    history.append(
                    {"role": "user", 
                    "content": text}
                  )
    return history

message1=add_message("hello")
message1=add_message("how are you", message1)

print(message1)
