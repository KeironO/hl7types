"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_JOB_CODE
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class CM_JOB_CODE(HL7Model):
    """HL7 v2 CM_JOB_CODE data type.

    Attributes
    ----------
    cm_job_code_1 : str | None
        CM_JOB_CODE.1 (opt) - job code (ID)

    cm_job_code_2 : str | None
        CM_JOB_CODE.2 (opt) - employee classification (ID)
    """

    cm_job_code_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_job_code_1",
            "job_code",
            "CM_JOB_CODE.1",
        ),
        serialization_alias="CM_JOB_CODE.1",
        title="job code",
    )

    cm_job_code_2: Optional[str] = Field(
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
