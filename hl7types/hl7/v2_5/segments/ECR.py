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
from ..datatypes.TX import TX


class ECR(HL7Model):
    """HL7 v2 ECR segment.

    Attributes
    ----------
    ecr_1 : CE
        ECR.1 (req) - Command Response (CE)

    ecr_2 : TS
        ECR.2 (req) - Date/Time Completed (TS)

    ecr_3 : list[TX] | None
        ECR.3 (opt, rep) - Command Response Parameters (TX)
    """

    ecr_1: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "ecr_1",
            "command_response",
            "ECR.1",
        ),
        serialization_alias="ECR.1",
        title="Command Response",
        description="Item #1395 | Table HL70387",
    )

    ecr_2: TS = Field(
        default=...,
        validation_alias=AliasChoices(
            "ecr_2",
            "date_time_completed",
            "ECR.2",
        ),
        serialization_alias="ECR.2",
        title="Date/Time Completed",
        description="Item #1396",
    )

    ecr_3: Optional[List[TX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ecr_3",
            "command_response_parameters",
            "ECR.3",
        ),
        serialization_alias="ECR.3",
        title="Command Response Parameters",
        description="Item #1397",
    )

    model_config = {"populate_by_name": True}
