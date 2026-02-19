from crewai import Agent, Task, Crew
from src.config import Config
from src.tools import TwilioOutreachTool, EmailTool

def run_outreach_campaign(customer_data: dict):
    # 1. Define Agents
    researcher = Agent(
        role='Customer Data Analyst',
        goal='Analyze customer profiles to identify key talking points and product pitches.',
        backstory='You are an expert at reading CRM data and finding the best angle to approach a client.',
        allow_delegation=False,
        llm=Config.llm
    )

    script_writer = Agent(
        role='Persuasive Copywriter',
        goal='Create a natural, personalized call script and email draft.',
        backstory='You write scripts that sound human, empathetic, and professional.',
        allow_delegation=False,
        llm=Config.llm
    )

    outreach_manager = Agent(
        role='Outreach Specialist',
        goal='Execute the communication via Phone and Email tools.',
        backstory='You handle the actual execution of calls and emails using external APIs.',
        allow_delegation=False,
        tools=[TwilioOutreachTool(), EmailTool()],
        llm=Config.llm
    )

    # 2. Define Tasks
    analysis_task = Task(
        description=f"Analyze this customer: {customer_data}. Identify their industry, pain points, and the best angle to pitch a solution.",
        expected_output="A summary of the customer profile and key pitch strategy.",
        agent=researcher
    )

    writing_task = Task(
        description="Using the analysis, write a short phone script (max 3 sentences) and a follow-up email draft.",
        expected_output="A phone script and an email body.",
        agent=script_writer,
        context=[analysis_task]
    )

    execution_task = Task(
        description=f"Use the Twilio Call Tool to contact {customer_data['phone']} with the phone script. Then, use the Email Follow-up Tool to send the email to {customer_data['email']}.",
        expected_output="A confirmation report detailing the execution of the call and email.",
        agent=outreach_manager,
        context=[writing_task]
    )

    # 3. Assemble and Run Crew
    outreach_crew = Crew(
        agents=[researcher, script_writer, outreach_manager],
        tasks=[analysis_task, writing_task, execution_task],
        verbose=True
    )

    result = outreach_crew.kickoff()
    return result