"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ECR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class ECR(HL7Model):
    """Equipment Command Response (S13.4.6).

    Attributes
    ----------
    ecr_1 : CWE
        ECR.1 - Command Response (CWE) R S13.4.6.1 | 0387 - Command Response

    ecr_2 : str
        ECR.2 - Date/Time Completed (DTM) R S13.4.6.2

    ecr_3 : list[str] | None
        ECR.3 - Command Response Parameters (TX) O rep S13.4.6.3
    """

    ecr_1: CWE = Field(
        validation_alias=AliasChoices(
            "ecr_1",
            "command_response",
            "ECR.1",
        ),
        serialization_alias="ECR.1",
        title="Command Response",
        description="R | Item #01395 | Table 0387 - Command Response",
    )

    ecr_2: str = Field(
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
