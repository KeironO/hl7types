"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_JOB_CODE
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CM_JOB_CODE(BaseModel):
    """HL7 v2 CM_JOB_CODE data type."""

    cm_job_code_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_job_code_1",
            "job_code",
            "CM_JOB_CODE.1",
        ),
        serialization_alias="CM_JOB_CODE.1",
        title="job code",
    )

    cm_job_code_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_job_code_2",
            "employee_classification",
            "CM_JOB_CODE.2",
        ),
        serialization_alias="CM_JOB_CODE.2",
        title="employee classification",
    )

    model_config = {"populate_by_name": True}
