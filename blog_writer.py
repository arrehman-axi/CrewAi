#!/usr/bin/env python3
"""
Simple CrewAI script with a Writer agent that creates blog posts about AI.
Uses Google Gemini API via Google AI Studio.
"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai.llm import LLM

# Load environment variables from .env file
load_dotenv()

# Create LLM instance for Gemini using the correct model name
llm = LLM(
    model="gemini/gemini-2.0-flash",  # Using available model
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)

# Define the Writer agent
writer_agent = Agent(
    role="Writer",
    goal="Write a short blog post about AI",
    backstory="You are a tech writer who explains AI in simple words",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Define the task
blog_task = Task(
    description="Write a 3-sentence blogpost about AI in education",
    agent=writer_agent,
    expected_output="A concise 3-sentence blog post about AI in education"
)

# Create the crew
crew = Crew(
    agents=[writer_agent],
    tasks=[blog_task],
    process=Process.sequential,
    verbose=True,
    memory=False  # Disable memory to prevent additional API calls
)

# Run the crew
if __name__ == "__main__":
    print("🚀 Starting CrewAI blog writer with Gemini (Google AI Studio)...")
    print("=" * 60)
    
    # Execute the crew
    result = crew.kickoff()
    
    print("=" * 60)
    print("📝 BLOG POST OUTPUT:")
    print("=" * 60)
    print(result)