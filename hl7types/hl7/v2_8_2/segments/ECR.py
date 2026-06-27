"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ECR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class ECR(HL7Model):
    """HL7 v2 ECR segment.

    Attributes
    ----------
    ecr_1 : CWE
        ECR.1 (req) - Command Response (CWE)

    ecr_2 : str
        ECR.2 (req) - Date/Time Completed (DTM)

    ecr_3 : list[str] | None
        ECR.3 (opt, rep) - Command Response Parameters (TX)
    """

    ecr_1: CWE = Field(
        validation_alias=AliasChoices(
            "ecr_1",
            "command_response",
            "ECR.1",
        ),
        serialization_alias="ECR.1",
        title="Command Response",
        description="Item #1395 | Table HL70387",
    )

    ecr_2: str = Field(
        validation_alias=AliasChoices(
            "ecr_2",
            "date_time_completed",
            "ECR.2",
        ),
        serialization_alias="ECR.2",
        title="Date/Time Completed",
        description="Item #1396",
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
        description="Item #1397",
    )

    @field_validator("ecr_2", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
