from uagents import Model
from enum import Enum
from typing import Optional, List
from pydantic import Field


class ResumeOptimiseRequest(Model):
    resume_text: str


class ResumeOptimiseResponse(Model):
    optimised_resume_text: str
