from uagents import Model
from enum import Enum
from typing import Optional, List
from pydantic import Field


class ResumeAnalyzeRequest(Model):
    file_path: str


class ResumeOptimiseResponse(Model):
    optimised_resume_text: str
