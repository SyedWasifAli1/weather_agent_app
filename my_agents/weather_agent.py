from agents import Agent
from .tools import get_weather_data

def create_weather_agent() -> Agent:
    """Factory function to create and return a Weather Agent."""
    return Agent(
        name="WeatherAgent",
        instructions="You are a helpful weather agent. Always answer with weather info.",
        tools=[get_weather_data],
        model="gpt-4o-mini",
    )
