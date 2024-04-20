from uagents import Bureau, Agent, Protocol, Context, Model
from uagents.setup import fund_agent_if_low
from message.resume_create import ResumeCreateRequest, ResumeCreateResponse
from message.resume_optimiser import ResumeOptimiseRequest, ResumeOptimiseResponse
from utlis.generate_resume import generate
from protocols import simples
import json
import requests


AGENT_MAILBOX_KEY = "7238038d-75a2-4350-91b5-491fc69985b5"

agent = Agent(
    name="core",
    seed="core's seceret seed",
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
)


agent.include(simples)


class Messages:
    message: str


fund_agent_if_low(agent.wallet.address())


# async def handle_query_request(ctx: Context, sender: str, msg: BookEventRequest):
#     ctx.logger.info(f"Received message from {sender}, session: {ctx.session}")

resume_text = generate()


@agent.on_event("startup")
async def say_hello(ctx: Context):
    ctx.logger.info(f"Hello from Agent! {ctx.name}")
    await ctx.send(
        "agent1qwc6v9jp3jkpxwrphsx5xnkejqpmyu5t734xlmt7s8trupet7e07uddwfps",
        ResumeCreateRequest(
            university="PICT",
            degree="Computer Engineer",
            skills="Networking, Web Development",
        ),
    )


@agent.on_message(model=ResumeCreateResponse)
async def get_resume_text(ctx: Context, sender: str, msg: ResumeCreateResponse):
    ctx.logger.info(f"Received message from {sender} in core, session: {ctx.session}")
    ctx.logger.info(f"{msg}")
    # await ctx.send(
    #     "agent1qfv0hu2g5zhz9ptderhw75dqlnwvs40y463tm0ps486wey74xvej54hzse2",
    #     ResumeOptimiseRequest(resume_text=resume_text),
    # )


if __name__ == "__main__":
    bureau = Bureau(endpoint=["http://127.0.0.1:8005/submit"], port=8005)
    print(f"Adding core agent to Bureau: {agent.address}")

    bureau.add(agent)
    bureau.run()
