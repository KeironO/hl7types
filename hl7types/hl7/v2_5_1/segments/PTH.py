"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PTH
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TS import TS


class PTH(HL7Model):
    """HL7 v2 PTH segment.

    Attributes
    ----------
    pth_1 : str
        PTH.1 (req) - Action Code (ID)

    pth_2 : CE
        PTH.2 (req) - Pathway ID (CE)

    pth_3 : EI
        PTH.3 (req) - Pathway Instance ID (EI)

    pth_4 : TS
        PTH.4 (req) - Pathway Established Date/Time (TS)

    pth_5 : CE | None
        PTH.5 (opt) - Pathway Life Cycle Status (CE)

    pth_6 : TS | None
        PTH.6 (opt) - Change Pathway Life Cycle Status Date/Time (TS)
    """

    pth_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pth_1",
            "action_code",
            "PTH.1",
        ),
        serialization_alias="PTH.1",
        title="Action Code",
        description="Item #816 | Table HL70287",
    )

    pth_2: CE = Field(
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

    pth_4: TS = Field(
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

    pth_5: Optional[CE] = Field(
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

    pth_6: Optional[TS] = Field(
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

    model_config = {"populate_by_name": True}
