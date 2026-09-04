import time

with open("week_11_advance_python_for_ai/tokan_streamer.text" , "r" , encoding ="utf-8") as f:
    read_text = f.read()
    # print(read_text)

def stream_response(text):
    for word in text.split():
        time.sleep(0.05)
        yield word

gen_streamer = stream_response(read_text )

for word in gen_streamer:
    print(word , end=" ", flush=True)