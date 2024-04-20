from uagents import Model
from enum import Enum
from typing import Optional, List
from pydantic import Field


class ResumeCreateRequest(Model):
    university: str
    degree: str
    skills: str


class ResumeCreateResponse(Model):
    resume_text: str
