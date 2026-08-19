from abc import ABC, abstractmethod 

class Tool(ABC):
    def __init__(self,name,description):
        self.name = name
        self.description = description


    @abstractmethod
    def run(self,*args):
        ...

class CalculatorTool(Tool):
    def __init__(self):
        super().__init__("calculator","A tool for adding and multiplying number")

    def add(self,a,b):
        return a + b

    def mul(self,a,b):
        return a * b

    def run (self,*args):
        a, b, name = args     ##1,3,,"add"
        if name == "add" :
            return self.add(a,b)
        elif name == "mul":
            return self.mul(a,b)
        else:
            raise ValueError(f"Invalied opreation :(name)")

class GreeterTool(Tool):
    def __init__(self):
        super().__init__("greeter","A tool for greetering people")

    def run (self,*args):
        name = args[0]
        return f"Hello , {name} !"


class ReverseTool(Tool):

    def __init__(self):
        super().__init__("Reverse","A tool for reverse the string")

        
    def run(self , *args):
        word = args[0]
        return word[::-1]




class Agent:
    def __init__(self,name):
        self.name=name
        self.tools=[]

    def add_tool(self,tool:Tool):
        self.tools.append(tool)

    def list_tool(self):
        for tool in self.tools:
            print(f"{tool.name},{tool.description}")
            

    def use_tool (self,tool_name:str,*args):
        for tool in self.tools:
            if tool.name == tool_name:
                return tool.run(*args)

        return f"Tool {tool_name} not  found"

    

agent =Agent("MY first Agent")

agent.add_tool(CalculatorTool())

agent.add_tool(GreeterTool())

agent.add_tool(ReverseTool())

agent.list_tool()


add_result = agent.use_tool("calculator",3,7,"add")

mul_result = agent.use_tool("calculator",3,3,"mul")

greet_result = agent.use_tool("greeter" ,"artii")

reverse_result = agent.use_tool("Reverse","arti")



print("Addition result : ",add_result)

print("Multification Result : ",mul_result)

print("greeting result :",greet_result)

print("Reverse the text",reverse_result)