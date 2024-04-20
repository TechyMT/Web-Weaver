from uagents import Bureau, Agent, Protocol, Context, Model
from uagents.setup import fund_agent_if_low
import json
import requests
import os
import sys
import base64

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utlis.constant import data
from message.resume_optimiser import ResumeOptimiseRequest, ResumeOptimiseResponse
from message.resume_analyzer import ResumeAnalyzeRequest


resume_agent = Agent(
    "resume optimiser_agent",
    seed="let me think of a secret",
    endpoint=["http://127.0.0.1:8002/submit"],
)


fund_agent_if_low(resume_agent.wallet.address())


async def fetch_data_from_rapidapi(resume_text):
    try:

        url = "https://resumeoptimizerpro.p.rapidapi.com/optimize"

        payload = {
            "ResumeText": resume_text,
            "WritingStyle": "Professional",
            "FormattingOptions": {"TemplateStyle": "1"},
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "bd321abc3bmsh17add886c4e711dp1faf16jsn8a94214d70e2",
            "X-RapidAPI-Host": "resumeoptimizerpro.p.rapidapi.com",
        }

        # response = await requests.post(url, json=payload, headers=headers)
        file_data = base64.b64decode(data)

        current_dir = os.getcwd()

        # File name you want to write to
        file_name = "output_file.docx"

        # Complete path
        file_path = os.path.join(current_dir, file_name)

        # Write the bytes to a file
        with open(file_path, "wb") as file:
            file.write(file_data)

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


@resume_agent.on_message(model=ResumeOptimiseRequest)
async def get_resume_text(ctx: Context, sender: str, msg: ResumeOptimiseRequest):
    ctx.logger.info(f"Received message from {sender} in core, session: {sender}")
    ctx.logger.info(f"Received message from {sender} in core, session: {ctx.session}")
    ctx.logger.info(f"{msg}")
    # await ctx.send("agent1qttrpd7ngt8q4pf2htrf52ms5jqtslmch3cv4h5u9g8z8kyh4ddh6ned3q9", BookEventRequest(title="Cab booked", location="XYZ", start_date_time="2023-12-28T09:13:00+05:30",end_date_time="2023-12-28T10:14:00+05:30"))

    response = await fetch_data_from_rapidapi(msg.resume_text)
    await ctx.send(
        "agent1qwnykg3mgxvhua0dyk3s0ac6mnjy3mlgadjmcdakhvd8d4j3vqvp2j6skf0",
        ResumeAnalyzeRequest(
            file_path="/home/mustafa/coding/Web_Weaver/test/agents/resumes/report.pdf"
        ),
    )


if __name__ == "__main__":
    bureau = Bureau(endpoint=["http://127.0.0.1:8002/submit"], port=8002)
    print(f"Adding resume_agent to Bureau: {resume_agent.address}")
    bureau.add(resume_agent)
    bureau.run()
