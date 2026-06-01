"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DPS
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE


class DPS(HL7Model):
    """HL7 v2 DPS segment.

    Attributes
    ----------
    dps_1 : CWE
        DPS.1 (req) - Diagnosis Code - MCP (CWE)

    dps_2 : list[CWE] | None
        DPS.2 (req, rep) - Procedure Code (CWE) [optional: CWE has no required components]

    dps_3 : str | None
        DPS.3 (opt) - Effective Date/Time (DTM)

    dps_4 : str | None
        DPS.4 (opt) - Expiration Date/Time (DTM)

    dps_5 : CNE | None
        DPS.5 (opt) - Type of Limitation (CNE)
    """

    dps_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "dps_1",
            "diagnosis_code_mcp",
            "DPS.1",
        ),
        serialization_alias="DPS.1",
        title="Diagnosis Code - MCP",
        description="Item #3472 | Table HL70051",
    )

    dps_2: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dps_2",
            "procedure_code",
            "DPS.2",
        ),
        serialization_alias="DPS.2",
        title="Procedure Code",
        description="Item #3484 | Table HL70941",
    )

    dps_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dps_3",
            "effective_date_time",
            "DPS.3",
        ),
        serialization_alias="DPS.3",
        title="Effective Date/Time",
        description="Item #662",
    )

    dps_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dps_4",
            "expiration_date_time",
            "DPS.4",
        ),
        serialization_alias="DPS.4",
        title="Expiration Date/Time",
        description="Item #3473",
    )

    dps_5: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dps_5",
            "type_of_limitation",
            "DPS.5",
        ),
        serialization_alias="DPS.5",
        title="Type of Limitation",
        description="Item #3474 | Table HL70940",
    )

    @field_validator("dps_3", "dps_4", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
