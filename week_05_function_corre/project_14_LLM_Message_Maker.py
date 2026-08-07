# Project 14 — LLM Message Maker (default + real AI shape)
# EN: Write make_message(text, role="user") that returns a dict {"role": role, "content": text}. Make a normal user message and a role="system" message. (This is exactly how AI chat messages look!)
# हिंदी: make_message(text, role="user") बनाओ जो dict {"role": role, "content": text} return करे। एक normal user message और एक role="system" message बनाओ। (AI chat messages बिल्कुल ऐसे ही दिखते हैं!)
# Concepts: default value, returning a dict, agentic link
# Hint: return {"role": role, "content": text}.

'''
restate1=this program is simple just make meaasge in any 
example2=just role of the massage and content of the massage.
psuedocode3=1.create the def make_message(text, role="user")
            2.return the  {"role": role, "content": text}
            3.print the make_message("abc","add item")
translate4=
dry run5=

'''
print("===========LLM Message Maker (default + real AI shape)=========")

def make_message(text, role="user"):

    return {"role": role, "content": text}


print(make_message("HR is the human resourse this post is the best and higher of the empoyee!","HR"))
