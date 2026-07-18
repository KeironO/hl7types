"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ARV
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.DR import DR

_RE_SI = re.compile(r'\d*')


class ARV(HL7Model):
    """Access Restriction (S3.4.14).

    Attributes
    ----------
    arv_1 : str | None
        ARV.1 - Set ID (SI) O S3.4.14.1

    arv_2 : CNE
        ARV.2 - Access Restriction Action Code (CNE) R S3.4.14.2 | 0206 - Segment Action Code

    arv_3 : CWE
        ARV.3 - Access Restriction Value (CWE) R S3.4.14.3 | 0717 - Access Restriction Value

    arv_4 : list[CWE] | None
        ARV.4 - Access Restriction Reason (CWE) O rep S3.4.14.4 | 0719 - Access Restriction Reason Code

    arv_5 : list[str] | None
        ARV.5 - Special Access Restriction Instructions (ST) O rep S3.4.14.5

    arv_6 : DR | None
        ARV.6 - Access Restriction Date Range (DR) O S3.4.14.6
    """

    arv_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arv_1",
            "set_id",
            "ARV.1",
        ),
        serialization_alias="ARV.1",
        title="Set ID",
        description="O | Item #02143 | LEN:4",
    )

    arv_2: CNE = Field(
        validation_alias=AliasChoices(
            "arv_2",
            "access_restriction_action_code",
            "ARV.2",
        ),
        serialization_alias="ARV.2",
        title="Access Restriction Action Code",
        description="R | Item #02144 | Table 0206 - Segment Action Code",
    )

    arv_3: CWE = Field(
        validation_alias=AliasChoices(
            "arv_3",
            "access_restriction_value",
            "ARV.3",
        ),
        serialization_alias="ARV.3",
        title="Access Restriction Value",
        description="R | Item #02145 | Table 0717 - Access Restriction Value",
    )

    arv_4: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arv_4",
            "access_restriction_reason",
            "ARV.4",
        ),
        serialization_alias="ARV.4",
        title="Access Restriction Reason",
        description=(
            "O | Item #02146 | Table 0719 - Access Restriction Reason Code"
        ),
    )

    arv_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arv_5",
            "special_access_restriction_instructions",
            "ARV.5",
        ),
        serialization_alias="ARV.5",
        title="Special Access Restriction Instructions",
        description="O | Item #02147",
    )

    arv_6: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arv_6",
            "access_restriction_date_range",
            "ARV.6",
        ),
        serialization_alias="ARV.6",
        title="Access Restriction Date Range",
        description="O | Item #02148",
    )

    @field_validator("arv_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
