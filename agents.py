from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv
load_dotenv()
import os
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4-0125-preview'

## Create a senior blog content researcher
blog_researcher = Agent(
    role = 'Blog Researcher from Youtube Videos',
    goal = 'Get the relevant video content for the topic {topic} from Youtube channel',
    verbose = True,
    memory = True,
    backstory = (
        'Expert in understanding video in AI, Data Science, Machine Learning and Generative AI and providing suggestion'
    ),
    tools = [yt_tool],
    allow_delegation = True # permite passar o que foi feito por esse agente para outro
)

## Create a senior blog writer agente with Youtube tools
blog_writer = Agent(
    role = 'Blog Writer',
    goal = 'Narrate compelling tech stories abaout the video {topic} from Youtube channel',
    verbose = True,
    memory = True,
    backstory = (
        'With a flair fot simplifying complex topics, you craft',
        'engaging narratives that captivate and educate, bringing new',
        'discoveries to light in an accessible manner'
    ),
    tools=[],
    allow_delegation = False
)