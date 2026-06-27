"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PDA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.DR import DR
from ..datatypes.PL import PL
from ..datatypes.XCN import XCN


class PDA(HL7Model):
    """HL7 v2 PDA segment.

    Attributes
    ----------
    pda_1 : list[CWE] | None
        PDA.1 (opt, rep) - Death Cause Code (CWE)

    pda_2 : PL | None
        PDA.2 (opt) - Death Location (PL)

    pda_3 : str | None
        PDA.3 (opt) - Death Certified Indicator (ID)

    pda_4 : str | None
        PDA.4 (opt) - Death Certificate Signed Date/Time (DTM)

    pda_5 : XCN | None
        PDA.5 (opt) - Death Certified By (XCN)

    pda_6 : str | None
        PDA.6 (opt) - Autopsy Indicator (ID)

    pda_7 : DR | None
        PDA.7 (opt) - Autopsy Start and End Date/Time (DR)

    pda_8 : XCN | None
        PDA.8 (opt) - Autopsy Performed By (XCN)

    pda_9 : str | None
        PDA.9 (opt) - Coroner Indicator (ID)
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
        description="Item #1574",
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
        description="Item #1575",
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
        description="Item #1576 | Table HL70136",
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
        description="Item #1577",
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
        description="Item #1578",
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
        description="Item #1579 | Table HL70136",
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
        description="Item #1580",
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
        description="Item #1581",
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
        description="Item #1582 | Table HL70136",
    )

    @field_validator("pda_4", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
