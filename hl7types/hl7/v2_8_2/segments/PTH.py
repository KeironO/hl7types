"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PTH
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class PTH(HL7Model):
    """Pathway (S12.4.3).

    Attributes
    ----------
    pth_1 : str
        PTH.1 - Action Code (ID) R S4.A.9.2 | 0206 - Segment Action Code

    pth_2 : CWE
        PTH.2 - Pathway ID (CWE) R S12.4.3.2

    pth_3 : EI
        PTH.3 - Pathway Instance ID (EI) R S12.4.3.3

    pth_4 : str
        PTH.4 - Pathway Established Date/Time (DTM) R S12.4.3.4

    pth_5 : CWE | None
        PTH.5 - Pathway Life Cycle Status (CWE) O S12.4.3.5

    pth_6 : str | None
        PTH.6 - Change Pathway Life Cycle Status Date/Time (DTM) C S12.4.3.6

    pth_7 : CNE | None
        PTH.7 - Mood Code (CNE) C S12.4.3.7 | 0725 - Mood Codes
    """

    pth_1: str = Field(
        validation_alias=AliasChoices(
            "pth_1",
            "action_code",
            "PTH.1",
        ),
        serialization_alias="PTH.1",
        title="Action Code",
        description="R | Item #00816 | Table 0206 - Segment Action Code",
    )

    pth_2: CWE = Field(
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

    pth_4: str = Field(
        validation_alias=AliasChoices(
            "pth_4",
            "pathway_established_date_time",
            "PTH.4",
        ),
        serialization_alias="PTH.4",
        title="Pathway Established Date/Time",
        description="R | Item #01209",
    )

    pth_5: Optional[CWE] = Field(
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

    pth_6: Optional[str] = Field(
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

    pth_7: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pth_7",
            "mood_code",
            "PTH.7",
        ),
        serialization_alias="PTH.7",
        title="Mood Code",
        description="C | Item #02239 | Table 0725 - Mood Codes",
    )

    @field_validator("pth_4", "pth_6", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
