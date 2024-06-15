from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

## Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents = [blog_researcher, blog_writer],
    tasks = [research_task, write_task],
    process = Process.sequential, # optional: sequential task exection is default
    memory = True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

## Start the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': 'AI vs ML vs DL vs Data Science'})
print(result)