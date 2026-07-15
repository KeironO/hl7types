"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
    """Pathway (S12.3.4).

    Attributes
    ----------
    pth_1 : str
        PTH.1 - Action Code (ID) R S12.3.4.1 | 0287 - Problem/Goal Action code

    pth_2 : CE
        PTH.2 - Pathway ID (CE) R S12.3.4.2

    pth_3 : EI
        PTH.3 - Pathway Instance ID (EI) R S12.3.4.3

    pth_4 : TS
        PTH.4 - Pathway Established Date/Time (TS) R S12.3.4.4

    pth_5 : CE | None
        PTH.5 - Pathway Life Cycle Status (CE) O S12.3.4.5

    pth_6 : TS | None
        PTH.6 - Change Pathway Life Cycle Status Date/Time (TS) C S12.3.4.6
    """

    pth_1: str = Field(
        validation_alias=AliasChoices(
            "pth_1",
            "action_code",
            "PTH.1",
        ),
        serialization_alias="PTH.1",
        title="Action Code",
        description=(
            "R | Item #00816 | Table 0287 - Problem/Goal Action code | LEN:2"
        ),
    )

    pth_2: CE = Field(
        validation_alias=AliasChoices(
            "pth_2",
            "pathway_id",
            "PTH.2",
        ),
        serialization_alias="PTH.2",
        title="Pathway ID",
        description="R | Item #01207",
    )

    pth_3: EI = Field(
        validation_alias=AliasChoices(
            "pth_3",
            "pathway_instance_id",
            "PTH.3",
        ),
        serialization_alias="PTH.3",
        title="Pathway Instance ID",
        description="R | Item #01208",
    )

    pth_4: TS = Field(
        validation_alias=AliasChoices(
            "pth_4",
            "pathway_established_date_time",
            "PTH.4",
        ),
        serialization_alias="PTH.4",
        title="Pathway Established Date/Time",
        description="R | Item #01209",
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
        description="O | Item #01210",
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
        description="C | Item #01211",
    )

    model_config = {"populate_by_name": True}
