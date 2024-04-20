from uagents import Bureau, Agent, Protocol, Context, Model
from uagents.setup import fund_agent_if_low
import json
import requests
import os
import sys
import aiohttp


# set the message directory path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from message import ResumeCreateRequest, ResumeCreateResponse
from message.resume_analyzer import ResumeAnalyzeRequest

resume_agent = Agent(
    "analyzer agent",
    seed="wow a good secret",
    endpoint=["http://127.0.0.1:8001/submit"],
)


fund_agent_if_low(resume_agent.wallet.address())


def is_file_open(file):
    try:
        file.tell()  # Performs a harmless operation that needs the file to be open.
        return True
    except ValueError:
        return False


async def fetch_data_from_rapidapi(file_path):
    try:
        url = "https://resume-parser-and-analyzer.p.rapidapi.com/api/v1/cv/"

        # Open the file in binary mode within a context manager to ensure it closes properly
        files = {"file": open(file_path, "rb")}
        headers = {
            "X-RapidAPI-Key": "bd321abc3bmsh17add886c4e711dp1faf16jsn8a94214d70e2",
            "X-RapidAPI-Host": "resume-parser-and-analyzer.p.rapidapi.com",
            "Content-Type": "application/pdf",
        }

        response = requests.post(url, files=files, headers=headers)
        print(response.json())

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


@resume_agent.on_message(model=ResumeAnalyzeRequest)
async def get_resume_text(ctx: Context, sender: str, msg: ResumeCreateRequest):
    ctx.logger.info(f"Received message from {sender} in core, session: {sender}")
    ctx.logger.info(f"Received message from {sender} in core, session: {ctx.session}")
    ctx.logger.info(f"{msg}")
    # await ctx.send("agent1qttrpd7ngt8q4pf2htrf52ms5jqtslmch3cv4h5u9g8z8kyh4ddh6ned3q9", BookEventRequest(title="Cab booked", location="XYZ", start_date_time="2023-12-28T09:13:00+05:30",end_date_time="2023-12-28T10:14:00+05:30"))

    response = await fetch_data_from_rapidapi(msg.file_path)


if __name__ == "__main__":
    bureau = Bureau(endpoint=["http://127.0.0.1:8001/submit"], port=8001)
    print(f"Adding resume_agent to Bureau: {resume_agent.address}")
    bureau.add(resume_agent)
    bureau.run()
