"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: PTH
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class PTH(BaseModel):
    """HL7 v2 PTH segment."""

    pth_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pth_1",
            "action_code",
            "PTH.1",
        ),
        serialization_alias="PTH.1",
        title="Action Code",
        description="Item #816 | Table HL70206",
    )

    pth_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "pth_2",
            "pathway_id",
            "PTH.2",
        ),
        serialization_alias="PTH.2",
        title="Pathway ID",
        description="Item #1207",
    )

    pth_3: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "pth_3",
            "pathway_instance_id",
            "PTH.3",
        ),
        serialization_alias="PTH.3",
        title="Pathway Instance ID",
        description="Item #1208",
    )

    pth_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pth_4",
            "pathway_established_date_time",
            "PTH.4",
        ),
        serialization_alias="PTH.4",
        title="Pathway Established Date/Time",
        description="Item #1209",
    )

    pth_5: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pth_5",
            "pathway_life_cycle_status",
            "PTH.5",
        ),
        serialization_alias="PTH.5",
        title="Pathway Life Cycle Status",
        description="Item #1210",
    )

    pth_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pth_6",
            "change_pathway_life_cycle_status_date_time",
            "PTH.6",
        ),
        serialization_alias="PTH.6",
        title="Change Pathway Life Cycle Status Date/Time",
        description="Item #1211",
    )

    pth_7: CNE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pth_7",
            "mood_code",
            "PTH.7",
        ),
        serialization_alias="PTH.7",
        title="Mood Code",
        description="Item #2239 | Table HL70725",
    )

    model_config = {"populate_by_name": True}
