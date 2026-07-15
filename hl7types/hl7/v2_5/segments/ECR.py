"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ECR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class ECR(HL7Model):
    """Equipment Command Response (S13.4.6).

    Attributes
    ----------
    ecr_1 : CE
        ECR.1 - Command Response (CE) R S13.4.6.1 | 0387 - Command response

    ecr_2 : TS
        ECR.2 - Date/Time Completed (TS) R S13.4.6.2

    ecr_3 : list[str] | None
        ECR.3 - Command Response Parameters (TX) O rep S13.4.6.3
    """

    ecr_1: CE = Field(
        validation_alias=AliasChoices(
            "ecr_1",
            "command_response",
            "ECR.1",
        ),
        serialization_alias="ECR.1",
        title="Command Response",
        description="R | Item #01395 | Table 0387 - Command response",
    )

    ecr_2: TS = Field(
        validation_alias=AliasChoices(
            "ecr_2",
            "date_time_completed",
            "ECR.2",
        ),
        serialization_alias="ECR.2",
        title="Date/Time Completed",
        description="R | Item #01396",
    )

    ecr_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ecr_3",
            "command_response_parameters",
            "ECR.3",
        ),
        serialization_alias="ECR.3",
        title="Command Response Parameters",
        description="O | Item #01397",
    )

    model_config = {"populate_by_name": True}
