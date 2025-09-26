#!/usr/bin/env python3
"""
CrewAI script with a Writer agent that creates blog posts about AI.
Uses Google Gemini via AI Studio API key (not Vertex).
"""

from crewai import Agent, Task, Crew, Process, LLM

# 🔑 Hardcode Gemini API Key


# ✅ Use AI Studio provider in litellm
llm = LLM(
    model="gemini/gemini-1.5-pro",
    api_key=GEMINI_API_KEY,
    temperature=0.7
)


# Writer Agent
writer_agent = Agent(
    role="Writer",
    goal="Write a short blog post about AI",
    backstory="You are a tech writer who explains AI in simple words",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Task
blog_task = Task(
    description="Write a 3-sentence blogpost about AI in education",
    agent=writer_agent,
    expected_output="A concise 3-sentence blog post about AI in education"
)

# Crew
crew = Crew(
    agents=[writer_agent],
    tasks=[blog_task],
    process=Process.sequential,
    verbose=True,
    memory=False
)

if __name__ == "__main__":
    print("🚀 Starting CrewAI blog writer with Gemini (AI Studio)...")
    result = crew.kickoff()
    print("📝 BLOG POST OUTPUT:")
    print(result)
