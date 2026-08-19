# Use agent mein add karke use_tool("reverse", "hello") test karo.

# 1=restate=Use agent mein add karke use_tool("reverse", "hello") test karo.
# 2=example=from agent_tools import Tool,CalculatorTool,GreeterTool,ReverseTool,Agent
            # class ReverseTool(Tool):,
# 3=psuedocode=1.from agent_tools import Tool,CalculatorTool,GreeterTool,ReverseTool,Agent
#              2.class is class ReverseTool(Tool):, method run(self , *args):
#              3.check the text is text = args[0],return text[::-1]
#              4.create object agent=Agent("My first Agent"),call method agent.add_tool(ReverseTool()),
#              5.print(agent.use_tool("reverse","hello"))
# 4=translate to python =


from agent_tools import Tool,CalculatorTool,GreeterTool,ReverseTool,Agent

print("--------homework 2-----------")

class ReverseTool(Tool):

    def __init__(self):
        super().__init__("reverse","A tool reverseing the string")

    def run(self , *args):
        text = args[0]
        return text[::-1]

agent=Agent("My first Agent")

agent.add_tool(ReverseTool())

print(agent.use_tool("reverse","hello"))

# 5=dry run=