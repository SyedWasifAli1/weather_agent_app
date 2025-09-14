# import os
# import streamlit as st
# import asyncio
# from agents import Agent, Runner
# from dotenv import load_dotenv

# # Load env
# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# # Create agent
# agent = Agent(
#     name="WeatherAgent",
#     model="gpt-4.1-mini",
#     instructions="You are a helpful weather assistant. Give short, clear weather updates."
# )

# st.title("🌦 Weather Agent App")
# st.write("Ask me about the weather in any city!")

# # Input
# user_input = st.text_input("Enter your question:")

# if st.button("Get Weather"):
#     if user_input.strip():

#         async def run_agent():
#             return await Runner.run(agent, user_input)

#         loop = asyncio.new_event_loop()
#         asyncio.set_event_loop(loop)
#         result = loop.run_until_complete(run_agent())

#         st.success("✅ Response from Agent:")
#         if hasattr(result, "final_output"):
#             st.write(result.final_output)
#         else:
#             st.write("⚠️ No response from agent.")

#     else:
#         st.warning("⚠️ Please enter a question.")















import os
import streamlit as st
import asyncio
from agents import Agent, Runner
from dotenv import load_dotenv
from my_agents import create_weather_agent  # your factory function

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Streamlit page setup
st.set_page_config(page_title="Weather Agent", page_icon="🌤️")
st.title("🌦 Weather Agent App")
st.write("Ask me about the weather in any city!")

# User input
user_input = st.text_input("Enter your question:")

# Run agent when button clicked
if st.button("Get Weather") and user_input.strip():

    # Create the agent
    agent = create_weather_agent()

    async def run_agent():
        result = await Runner.run(agent, user_input)

        # Build debug trace info
        trace_info = {
            "user_input": user_input,
            "final_output": getattr(result, "final_output", None),
            "raw_result": result.__dict__,  # full RunResult object
        }

        return result, trace_info

    # Async event loop for Streamlit
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result, trace = loop.run_until_complete(run_agent())

    # Show final response
    st.success("🤖 Response from Agent:")
    if trace["final_output"]:
        st.write(trace["final_output"])
    else:
        st.write("⚠️ No response from agent.")

    # Debug / Trace panel
    # with st.expander("🔍 Debug Trace"):
        # st.json(trace)

else:
    st.info("⚠️ Enter a question and click 'Get Weather'.")
