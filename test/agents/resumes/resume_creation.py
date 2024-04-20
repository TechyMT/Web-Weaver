from uagents import Bureau, Agent, Protocol, Context, Model
from uagents.setup import fund_agent_if_low
import json
import requests
import os
import sys

# set the message directory path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from message import ResumeCreateRequest, ResumeCreateResponse


resume_agent = Agent(
    "resume resume_agent",
    seed="this is a good secret",
    endpoint=["http://127.0.0.1:8004/submit"],
)


fund_agent_if_low(resume_agent.wallet.address())


async def fetch_data_from_rapidapi(university, degree, skills):
    try:

        # api_url = "https://ai-resume-generator.p.rapidapi.com/Documents/GenerateResume"
        # querystring = {
        #     "university": university,
        #     "degree": degree,
        #     "skills": skills,
        # }

        # headers = {
        #     "X-RapidAPI-Key": "bd321abc3bmsh17add886c4e711dp1faf16jsn8a94214d70e2",
        #     "X-RapidAPI-Host": "ai-resume-generator.p.rapidapi.com",
        # }

        # response = await requests.get(api_url, headers=headers, params=querystring)

        # print(response.json())
        url = "https://facts-by-api-ninjas.p.rapidapi.com/v1/facts"

        headers = {
            "X-RapidAPI-Key": "bd321abc3bmsh17add886c4e711dp1faf16jsn8a94214d70e2",
            "X-RapidAPI-Host": "facts-by-api-ninjas.p.rapidapi.com",
        }

        response = requests.get(url, headers=headers)

        fact = response.json()[0]["fact"]
        print(fact)
        return fact
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


@resume_agent.on_message(model=ResumeCreateRequest)
async def get_resume_text(ctx: Context, sender: str, msg: ResumeCreateRequest):
    ctx.logger.info(f"Received message from {sender} in core, session: {sender}")
    ctx.logger.info(f"Received message from {sender} in core, session: {ctx.session}")
    ctx.logger.info(f"{msg}")
    # await ctx.send("agent1qttrpd7ngt8q4pf2htrf52ms5jqtslmch3cv4h5u9g8z8kyh4ddh6ned3q9", BookEventRequest(title="Cab booked", location="XYZ", start_date_time="2023-12-28T09:13:00+05:30",end_date_time="2023-12-28T10:14:00+05:30"))

    response = await fetch_data_from_rapidapi(msg.university, msg.degree, msg.skills)
    if response:
        await ctx.send(
            sender,
            ResumeCreateResponse(resume_text=str(response)),
        )
    else:
        await ctx.send(
            sender,
            ResumeCreateResponse(resume_text="Error in fetching data"),
        )


if __name__ == "__main__":
    bureau = Bureau(endpoint=["http://127.0.0.1:8004/submit"], port=8004)
    print(f"Adding resume_agent to Bureau: {resume_agent.address}")
    bureau.add(resume_agent)
    bureau.run()
