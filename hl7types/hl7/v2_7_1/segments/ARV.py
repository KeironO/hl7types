"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ARV
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.DR import DR


class ARV(HL7Model):
    """HL7 v2 ARV segment.

    Attributes
    ----------
    arv_1 : str | None
        ARV.1 (opt) - Set ID (SI)

    arv_2 : CNE
        ARV.2 (req) - Access Restriction Action Code (CNE)

    arv_3 : CWE
        ARV.3 (req) - Access Restriction Value (CWE)

    arv_4 : list[CWE] | None
        ARV.4 (opt, rep) - Access Restriction Reason (CWE)

    arv_5 : list[str] | None
        ARV.5 (opt, rep) - Special Access Restriction Instructions (ST)

    arv_6 : DR | None
        ARV.6 (opt) - Access Restriction Date Range (DR)
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
        description="Item #2143",
    )

    arv_2: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "arv_2",
            "access_restriction_action_code",
            "ARV.2",
        ),
        serialization_alias="ARV.2",
        title="Access Restriction Action Code",
        description="Item #2144 | Table HL70206",
    )

    arv_3: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "arv_3",
            "access_restriction_value",
            "ARV.3",
        ),
        serialization_alias="ARV.3",
        title="Access Restriction Value",
        description="Item #2145 | Table HL70717",
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
        description="Item #2146 | Table HL70719",
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
        description="Item #2147",
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
        description="Item #2148",
    )

    model_config = {"populate_by_name": True}
