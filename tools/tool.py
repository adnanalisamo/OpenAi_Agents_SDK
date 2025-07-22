from agents import Agent, Runner, function_tool
from main import config  # make sure your config is set correctly


# Tools
@function_tool
def calculator(a: float, b: float):
    return f'The result of the calculator is {a - b}'

@function_tool
def usd_to_pkr():
    return 'USD to PKR conversion rate is 1 USD = 280 PKR as of today.'

@function_tool
def get_weather(city: str):
    return f'Weather of {city} is cloudy.'

# Agent
agent = Agent(
    name="Query Agent",
    instructions="You are a helpful assistant. Your task is to help the user with their queries.",
    tools=[usd_to_pkr, get_weather, calculator]
)

# 🧑‍💻 Take user input from terminal
if __name__ == "__main__":
    user_input = input("Ask your question: ")

    result = Runner.run_sync(
        agent,
        user_input,
        run_config=config
    )

    print("\n🤖 Agent Response:")
    print(result.final_output)
