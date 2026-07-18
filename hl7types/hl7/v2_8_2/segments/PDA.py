"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PDA
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.DR import DR
from ..datatypes.PL import PL
from ..datatypes.XCN import XCN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class PDA(HL7Model):
    """Patient Death and Autopsy (S3.4.13).

    Attributes
    ----------
    pda_1 : list[CWE] | None
        PDA.1 - Death Cause Code (CWE) O rep S3.4.13.1

    pda_2 : PL | None
        PDA.2 - Death Location (PL) O S3.4.13.2

    pda_3 : str | None
        PDA.3 - Death Certified Indicator (ID) O S3.4.13.3 | 0136 - Yes/no Indicator

    pda_4 : str | None
        PDA.4 - Death Certificate Signed Date/Time (DTM) O S3.4.13.4

    pda_5 : XCN | None
        PDA.5 - Death Certified By (XCN) O S3.4.13.5

    pda_6 : str | None
        PDA.6 - Autopsy Indicator (ID) O S3.4.13.6 | 0136 - Yes/no Indicator

    pda_7 : DR | None
        PDA.7 - Autopsy Start and End Date/Time (DR) O S3.4.13.7

    pda_8 : XCN | None
        PDA.8 - Autopsy Performed By (XCN) O S3.4.13.8

    pda_9 : str | None
        PDA.9 - Coroner Indicator (ID) O S3.4.13.9 | 0136 - Yes/no Indicator
    """

    pda_1: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pda_1",
            "death_cause_code",
            "PDA.1",
        ),
        serialization_alias="PDA.1",
        title="Death Cause Code",
        description="O | Item #01574",
    )

    pda_2: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pda_2",
            "death_location",
            "PDA.2",
        ),
        serialization_alias="PDA.2",
        title="Death Location",
        description="O | Item #01575",
    )

    pda_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pda_3",
            "death_certified_indicator",
            "PDA.3",
        ),
        serialization_alias="PDA.3",
        title="Death Certified Indicator",
        description="O | Item #01576 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    pda_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pda_4",
            "death_certificate_signed_date_time",
            "PDA.4",
        ),
        serialization_alias="PDA.4",
        title="Death Certificate Signed Date/Time",
        description="O | Item #01577",
    )

    pda_5: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pda_5",
            "death_certified_by",
            "PDA.5",
        ),
        serialization_alias="PDA.5",
        title="Death Certified By",
        description="O | Item #01578",
    )

    pda_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pda_6",
            "autopsy_indicator",
            "PDA.6",
        ),
        serialization_alias="PDA.6",
        title="Autopsy Indicator",
        description="O | Item #01579 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    pda_7: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pda_7",
            "autopsy_start_and_end_date_time",
            "PDA.7",
        ),
        serialization_alias="PDA.7",
        title="Autopsy Start and End Date/Time",
        description="O | Item #01580",
    )

    pda_8: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pda_8",
            "autopsy_performed_by",
            "PDA.8",
        ),
        serialization_alias="PDA.8",
        title="Autopsy Performed By",
        description="O | Item #01581",
    )

    pda_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pda_9",
            "coroner_indicator",
            "PDA.9",
        ),
        serialization_alias="PDA.9",
        title="Coroner Indicator",
        description="O | Item #01582 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    @field_validator("pda_4", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
