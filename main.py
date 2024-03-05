import os
from crewai import Agent, Task, Crew, Process

from langchain_community.llms import Ollama


model_name = os.getenv("OLLAMA_MODEL", "llama2")
base_url = os.getenv("OLLAMA_BASE_URL", "http://llm:11434")

# Initialize the Ollama model with the specified model and base URL
ollama_model = Ollama(model=model_name, base_url=base_url)

### OPENAI
# os.environ["OPENAI_API_KEY"] = "Your Key"
#export OPENAI_API_KEY=sk-blablabla # on Linux/Mac


# Define your agents with roles and goals
researcher = Agent(
      role='Researcher',
      goal='Discover new insights',
      backstory="You're a world class researcher working on a major data science company",
      verbose=True,
      allow_delegation=False,
      llm=ollama_model, ### OLLAMA VERSION!!
      # llm=OpenAI(temperature=0.7, model_name="gpt-4"). It uses langchain.chat_models, default is GPT4 ### OPENAI VERSION!!

)
writer = Agent(
      role='Writer',
      goal='Create engaging content',
      backstory="You're a famous technical writer, specialized on writing data related content",
      verbose=True,
      allow_delegation=False,
      llm=ollama_model ### OLLAMA VERSION!!

)

# Create tasks for your agents
task1 = Task(
        description='Investigate the latest AI trends',
        agent=researcher,
        expected_output='Some relevant findings or insights'
)

task2 = Task(
        description='Write a science article about future of the crew ai',
        agent=writer,
        expected_output='A science article with references'
)

# Instantiate your crew with a sequential process - TWO AGENTS!
crew = Crew(
      agents=[researcher, writer],
      tasks=[task1, task2],
      llm=ollama_model, ### OLLAMA VERSION!!
      verbose=2, # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
      process=Process.sequential # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.

)

# Get your crew to work!
result = crew.kickoff()

