# CrewAI Blog Writer

A simple Python script using CrewAI to generate blog posts about AI using Google Gemini.

## Overview

This project demonstrates how to use CrewAI with Google's Gemini API to create a multi-agent system for content generation. The system includes a Writer agent that specializes in creating educational blog posts about AI.

## Features

- 🤖 **Writer Agent**: Creates educational blog posts about AI
- 🔑 **Secure API Key Management**: Uses `.env` file for API key storage
- 🚀 **Google Gemini Integration**: Uses Google AI Studio API
- 📝 **Customizable Content**: Easy to modify prompts and topics

## Prerequisites

- Python 3.8+
- Google AI Studio API key
- Virtual environment (recommended)

## Setup

### 1. Clone or Download the Project
```bash
git clone <your-repo-url>
cd CrewAi
```

### 2. Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
Create a `.env` file in the project root:
```bash
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
```

Replace `your_actual_api_key_here` with your actual Google AI Studio API key.

## Usage

### Basic Usage
```bash
python blog_writer.py
```

### Expected Output
The script will generate a 3-sentence blog post about AI in education, for example:

> "AI is transforming education by personalizing learning experiences for students. It provides tools for automated grading, intelligent tutoring, and creating customized content. This technology helps educators focus on individual student needs and fosters a more engaging and effective learning environment."

## Project Structure

```
CrewAi/
├── .env                    # API key (not in git)
├── .gitignore             # Git ignore file
├── blog_writer.py         # Main script
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── simple_gemini_test.py # API test script
└── check_models.py       # Model availability checker
```

## Configuration

### Agent Configuration
The Writer agent is configured with:
- **Role**: Writer
- **Goal**: Write a short blog post about AI
- **Backstory**: You are a tech writer who explains AI in simple words

### Task Configuration
The blog task is set to:
- **Description**: Write a 3-sentence blogpost about AI in education
- **Expected Output**: A concise 3-sentence blog post about AI in education

### Model Configuration
- **Model**: `gemini-2.0-flash`
- **Temperature**: 0.7
- **Memory**: Disabled

## Customization

### Changing the Topic
Modify the task description in `blog_writer.py`:
```python
blog_task = Task(
    description="Write a 3-sentence blogpost about [YOUR TOPIC HERE]",
    agent=writer_agent,
    expected_output="A concise 3-sentence blog post about [YOUR TOPIC HERE]"
)
```

### Adding More Agents
You can extend the system by adding more agents:
```python
# Add a new agent
editor_agent = Agent(
    role="Editor",
    goal="Review and improve blog posts",
    backstory="You are an experienced editor who ensures content quality",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Add to crew
crew = Crew(
    agents=[writer_agent, editor_agent],
    tasks=[blog_task, edit_task],
    process=Process.sequential,
    verbose=True,
    memory=False
)
```

## Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your `.env` file contains the correct API key
   - Verify the API key is active in Google AI Studio

2. **Model Not Found**
   - The script uses `gemini-2.0-flash` which should be available
   - Run `python check_models.py` to see available models

3. **Network Issues**
   - Check your internet connection
   - Ensure you can access Google's APIs

### Testing the API
Run the test script to verify your API key works:
```bash
python simple_gemini_test.py
```

## Dependencies

- `crewai>=0.1.0` - Multi-agent framework
- `langchain-google-genai>=0.0.5` - Google Gemini integration
- `python-dotenv>=1.0.0` - Environment variable management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues:
1. Check the troubleshooting section
2. Verify your API key and model availability
3. Check the CrewAI documentation
4. Open an issue in the repository

## Next Steps

- Add more specialized agents (researcher, fact-checker, etc.)
- Implement different content types (news articles, tutorials, etc.)
- Add content validation and quality checks
- Integrate with content management systems
- Add support for multiple languages

---

**Happy coding with CrewAI! 🚀**