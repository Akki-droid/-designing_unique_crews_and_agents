from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import os

@CrewBase
class DesigningUniqueCrewsAndAgentsCrew():
    """DesigningUniqueCrewsAndAgents crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    @agent
    def MarketDataCollector(self) -> Agent:
        return Agent(
            config=self.agents_config['MarketDataCollector'],
            llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="anthropic/claude-3-haiku-20240307", )
        )

    @agent
    def MarketInsightsAnalyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['MarketInsightsAnalyzer'],
            llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="anthropic/claude-3-haiku-20240307", )
        )


    @task
    def collect_market_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['collect_market_data_task']
        )

    @task
    def analyze_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_insights_task']
        )


    @crew
    def crew(self) -> Crew:
        """Creates the DesigningUniqueCrewsAndAgents crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

@CrewBase
class DesignCrew():
    """DesigningUniqueCrewsAndAgents crew"""
    agents_config = 'config/agents1.yaml'
    tasks_config = 'config/tasks1.yaml'

    @agent
    def DataCollector1(self) -> Agent:
        return Agent(
            config=self.agents_config['DataCollector1'],
            llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="anthropic/claude-3-haiku-20240307", ),
        )

    @agent
    def DataAnalyser1(self) -> Agent:
        return Agent(
            config=self.agents_config['DataAnalyser1'],
            llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="anthropic/claude-3-haiku-20240307", ),
        )

    @agent
    def DataOutput1(self) -> Agent:
        return Agent(
            config=self.agents_config['DataOutput1'],
            llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="anthropic/claude-3-haiku-20240307", ),
        )


    @task
    def collect_market_data_task1(self) -> Task:
        return Task(
            config=self.tasks_config['collect_market_data_task1'],
        )

    @task
    def analyze_insights_task1(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_insights_task1'],
        )

    @task
    def data_output_task1(self) -> Task:
        return Task(
            config=self.tasks_config['data_output_task1'],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the DesigningUniqueCrewsAndAgents crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )