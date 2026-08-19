# Upar wale Agent project mein ek teesra tool add karo: ReverseTool jo string ulta kare.


# 1= restate=Upar wale Agent project mein ek teesra tool add karo: ReverseTool jo string ulta kare.
# 2=example=from agent_tools import Tool,CalculatorTool,GreeterTool,ReverseTool,Agent
#           class ReverseTool(Tool):
# 3=psuedocode=1.from agent_tools import Tool,CalculatorTool,GreeterTool,ReverseTool,Agent
#              2.create the call with parent ,class ReverseTool(Tool):
#              3 call the super() method super().__init__("reverse","a tool for reverseing string")
#              4.method def run(self,*args): check condition word = args[0], return word[::-1]
#              5.agent =Agent("MY first Agent"),agent.add_tool(ReverseTool())
#              6.reverse_word  = agent.use_tool("reverse","Arti")
#              7.print("Reverse word is : ",reverse_word )

# 4=translate to python =


from agent_tools import Tool,CalculatorTool,GreeterTool,ReverseTool,Agent


print('------------homework1-----------')

class ReverseTool(Tool):

    def __init__(self):

        super().__init__("reverse","a tool for reverseing string")


    def run(self,*args):

        word = args[0]

        return word[::-1]




agent =Agent("MY first Agent")

agent.add_tool(ReverseTool())

reverse_word  = agent.use_tool("reverse","Arti")


print("Reverse word is : ",reverse_word )

# 5=dry run=