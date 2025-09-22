from uagents import Context, Model, Protocol
from ai_engine import UAgentResponse, UAgentResponseType
from .firebase import upload_base64_docx_to_firebase
from pydantic import Field
import json
import requests


class Request(Model):
    resume_text: str = Field(description="Enter the resume text which you want to optimise")


simples = Protocol(name="Resume optimiser", version="1.1")


async def fetch_data_from_rapidapi(
    name, email, phone, address, skills, certifications, awards, experiences
):
    try:
        url = "https://resumeoptimizerpro.p.rapidapi.com/optimize"

        payload = {
            "ResumeText": "",
            "WritingStyle": "Professional",
            "FormattingOptions": { "TemplateStyle": "1" }
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "bd321abc3bmsh17add886c4e711dp1faf16jsn8a94214d70e2",
            "X-RapidAPI-Host": "resumeoptimizerpro.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)
    except:
        print(f"An error occurred")
        return "An error occured"


@simples.on_message(model=Request, replies={UAgentResponse})
async def handle_message(ctx: Context, sender: str, msg: Request):
    response = await fetch_data_from_rapidapi(
        msg.name,
        msg.email,
        msg.phone,
        msg.address,
        msg.skills,
        msg.certifications,
        msg.awards,
        msg.experiences,
    )
    await ctx.send(
        sender, UAgentResponse(message=response, type=UAgentResponseType.FINAL)
    )


agent.include(simples)


# async def handle_query_request(ctx: Context, sender: str, msg: BookEventRequest):
#     ctx.logger.info(f"Received message from {sender}, session: {ctx.session}")
