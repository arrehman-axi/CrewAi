# Multi CrewAI Project

A comprehensive multi-agent system using CrewAI to demonstrate advanced AI collaboration and task orchestration.

## 🚀 Overview

This project showcases the power of multi-agent systems using CrewAI, where multiple specialized AI agents work together to accomplish complex tasks. Each agent has a specific role and expertise, and they collaborate to produce high-quality results.

## 🤖 Agent Architecture

### Core Agents

#### 1. **Research Agent**
- **Role**: Research Specialist
- **Goal**: Gather comprehensive information on given topics
- **Backstory**: You are an expert researcher with access to vast knowledge databases
- **Responsibilities**:
  - Conduct thorough research on assigned topics
  - Identify key facts, trends, and insights
  - Compile reliable information from multiple sources
  - Provide structured research findings

#### 2. **Writer Agent**
- **Role**: Content Writer
- **Goal**: Create engaging and informative content
- **Backstory**: You are a skilled writer who transforms research into compelling narratives
- **Responsibilities**:
  - Transform research findings into well-structured content
  - Write in clear, engaging language
  - Ensure content flows logically
  - Adapt writing style to target audience

#### 3. **Editor Agent**
- **Role**: Content Editor
- **Goal**: Ensure content quality and accuracy
- **Backstory**: You are an experienced editor with a keen eye for detail and quality
- **Responsibilities**:
  - Review and refine written content
  - Check for grammar, style, and clarity
  - Ensure factual accuracy
  - Optimize content for readability

#### 4. **Fact-Checker Agent**
- **Role**: Fact Verification Specialist
- **Goal**: Verify accuracy of information and claims
- **Backstory**: You are a meticulous fact-checker who ensures all information is accurate
- **Responsibilities**:
  - Verify facts and statistics
  - Cross-reference information
  - Identify potential inaccuracies
  - Provide verification reports

## 🔄 Workflow Process

### Sequential Workflow
1. **Research Phase**: Research Agent gathers information
2. **Writing Phase**: Writer Agent creates content based on research
3. **Editing Phase**: Editor Agent refines the content
4. **Verification Phase**: Fact-Checker Agent verifies accuracy
5. **Final Review**: Collaborative review and finalization

### Parallel Workflow
- Multiple agents can work on different aspects simultaneously
- Research and fact-checking can occur in parallel
- Writing and editing can overlap for efficiency

## 📁 Project Structure

```
Multi Crew Ai/
├── README.md                 # This file
├── main.py                   # Main execution script
├── agents/
│   ├── research_agent.py     # Research agent configuration
│   ├── writer_agent.py       # Writer agent configuration
│   ├── editor_agent.py       # Editor agent configuration
│   └── fact_checker_agent.py # Fact-checker agent configuration
├── tasks/
│   ├── research_task.py      # Research task definitions
│   ├── writing_task.py       # Writing task definitions
│   ├── editing_task.py       # Editing task definitions
│   └── verification_task.py  # Verification task definitions
├── crews/
│   ├── content_creation_crew.py  # Main content creation crew
│   ├── research_crew.py          # Research-focused crew
│   └── quality_assurance_crew.py # Quality assurance crew
├── config/
│   ├── llm_config.py         # LLM configuration
│   └── agent_config.py       # Agent configurations
├── utils/
│   ├── helpers.py            # Utility functions
│   └── validators.py         # Content validation
├── examples/
│   ├── blog_post_example.py  # Blog post creation example
│   ├── report_example.py     # Report generation example
│   └── article_example.py    # Article writing example
├── tests/
│   ├── test_agents.py        # Agent testing
│   ├── test_tasks.py         # Task testing
│   └── test_crews.py         # Crew testing
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables example
└── .gitignore               # Git ignore file
```

## 🛠️ Setup and Installation

### Prerequisites
- Python 3.8+
- Google AI Studio API key (or other LLM provider)
- Virtual environment (recommended)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd "Multi Crew Ai"
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

## 🚀 Usage Examples

### Basic Content Creation
```python
from crews.content_creation_crew import ContentCreationCrew

# Initialize the crew
crew = ContentCreationCrew()

# Create content
result = crew.kickoff(
    inputs={
        "topic": "Artificial Intelligence in Healthcare",
        "content_type": "blog_post",
        "target_audience": "healthcare professionals",
        "word_count": 800
    }
)

print(result)
```

### Research-Only Workflow
```python
from crews.research_crew import ResearchCrew

# Initialize research crew
research_crew = ResearchCrew()

# Conduct research
research_result = research_crew.kickoff(
    inputs={
        "research_topic": "Quantum Computing Applications",
        "depth": "comprehensive",
        "sources_needed": 10
    }
)
```

### Quality Assurance Workflow
```python
from crews.quality_assurance_crew import QualityAssuranceCrew

# Initialize QA crew
qa_crew = QualityAssuranceCrew()

# Review content
qa_result = qa_crew.kickoff(
    inputs={
        "content_to_review": "Your content here",
        "review_type": "comprehensive",
        "fact_check_required": True
    }
)
```

## ⚙️ Configuration

### LLM Configuration
```python
# config/llm_config.py
from crewai.llm import LLM

def get_llm():
    return LLM(
        model="gemini/gemini-2.0-flash",
        api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0.7
    )
```

### Agent Configuration
```python
# config/agent_config.py
def get_research_agent():
    return Agent(
        role="Research Specialist",
        goal="Gather comprehensive information on given topics",
        backstory="You are an expert researcher with access to vast knowledge databases",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )
```

## 🔧 Customization

### Adding New Agents
1. Create agent configuration in `agents/`
2. Define tasks in `tasks/`
3. Update crew configuration in `crews/`
4. Test the new agent

### Modifying Workflows
1. Edit crew configurations in `crews/`
2. Adjust task dependencies
3. Update process type (sequential/parallel)
4. Test the modified workflow

### Custom Tasks
1. Define new tasks in `tasks/`
2. Specify input/output requirements
3. Configure task dependencies
4. Integrate with existing agents

## 📊 Performance Optimization

### Parallel Processing
- Use `Process.parallel` for independent tasks
- Implement task dependencies carefully
- Monitor resource usage

### Memory Management
- Disable memory for simple workflows
- Use memory strategically for complex tasks
- Monitor memory consumption

### Error Handling
- Implement robust error handling
- Add retry mechanisms
- Log errors for debugging

## 🧪 Testing

### Running Tests
```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_agents.py

# Run with coverage
python -m pytest --cov=. tests/
```

### Test Structure
- **Unit Tests**: Test individual agents and tasks
- **Integration Tests**: Test crew workflows
- **End-to-End Tests**: Test complete processes

## 📈 Monitoring and Logging

### Logging Configuration
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('crewai.log'),
        logging.StreamHandler()
    ]
)
```

### Performance Metrics
- Track execution time
- Monitor API usage
- Measure content quality
- Analyze agent collaboration

## 🔒 Security and Best Practices

### API Key Management
- Use environment variables
- Never commit API keys
- Rotate keys regularly
- Monitor API usage

### Content Validation
- Implement fact-checking
- Validate sources
- Review for bias
- Ensure accuracy

### Error Handling
- Graceful failure handling
- Retry mechanisms
- Fallback strategies
- User-friendly error messages

## 🚀 Advanced Features

### Dynamic Agent Creation
```python
def create_custom_agent(role, goal, backstory):
    return Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )
```

### Conditional Workflows
```python
def conditional_workflow(content_quality):
    if content_quality < 0.8:
        return "additional_review_workflow"
    else:
        return "finalization_workflow"
```

### Multi-Model Support
```python
def get_llm_for_agent(agent_type):
    if agent_type == "research":
        return LLM(model="gemini/gemini-2.0-flash")
    elif agent_type == "writing":
        return LLM(model="gemini/gemini-2.0-flash")
    # Add more models as needed
```

## 📚 Examples and Use Cases

### 1. Blog Post Creation
- Research trending topics
- Write engaging content
- Edit for clarity
- Fact-check information

### 2. Technical Documentation
- Research technical concepts
- Write clear documentation
- Review for accuracy
- Verify technical details

### 3. Content Marketing
- Research target audience
- Create marketing content
- Optimize for engagement
- Ensure brand consistency

### 4. Academic Writing
- Conduct literature review
- Write research papers
- Peer review process
- Fact-check citations

## 🤝 Contributing

### Development Workflow
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

### Code Standards
- Follow PEP 8
- Add docstrings
- Write tests
- Update documentation

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support and Troubleshooting

### Common Issues
1. **API Key Errors**: Verify API key configuration
2. **Model Not Found**: Check model availability
3. **Memory Issues**: Optimize workflow complexity
4. **Performance Issues**: Use parallel processing

### Getting Help
- Check the documentation
- Review example code
- Open an issue
- Join the community

## 🔮 Future Enhancements

### Planned Features
- [ ] Web interface for crew management
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Integration with external APIs
- [ ] Automated testing framework
- [ ] Performance optimization tools
- [ ] Content quality metrics
- [ ] Real-time collaboration features

### Research Areas
- Agent communication protocols
- Dynamic workflow adaptation
- Quality assurance automation
- Performance optimization
- Scalability improvements

---

**Built with ❤️ using CrewAI**

*This multi-agent system demonstrates the power of AI collaboration and showcases advanced CrewAI capabilities.*
