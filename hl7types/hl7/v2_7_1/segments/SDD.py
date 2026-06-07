"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: SDD
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class SDD(HL7Model):
    """HL7 v2 SDD segment.

    Attributes
    ----------
    sdd_1 : EI | None
        SDD.1 (opt) - Lot Number (EI)

    sdd_2 : EI | None
        SDD.2 (opt) - Device Number (EI)

    sdd_3 : str | None
        SDD.3 (opt) - Device Name (ST)

    sdd_4 : CWE | None
        SDD.4 (opt) - Device Data State (CWE)

    sdd_5 : CWE | None
        SDD.5 (opt) - Load Status (CWE)

    sdd_6 : str | None
        SDD.6 (opt) - Control Code (NM)

    sdd_7 : str | None
        SDD.7 (opt) - Operator Name (ST)
    """

    sdd_1: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sdd_1",
            "lot_number",
            "SDD.1",
        ),
        serialization_alias="SDD.1",
        title="Lot Number",
        description="Item #2098",
    )

    sdd_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sdd_2",
            "device_number",
            "SDD.2",
        ),
        serialization_alias="SDD.2",
        title="Device Number",
        description="Item #2099",
    )

    sdd_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sdd_3",
            "device_name",
            "SDD.3",
        ),
        serialization_alias="SDD.3",
        title="Device Name",
        description="Item #2281",
    )

    sdd_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sdd_4",
            "device_data_state",
            "SDD.4",
        ),
        serialization_alias="SDD.4",
        title="Device Data State",
        description="Item #2100 | Table HL70667",
    )

    sdd_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sdd_5",
            "load_status",
            "SDD.5",
        ),
        serialization_alias="SDD.5",
        title="Load Status",
        description="Item #2101 | Table HL70669",
    )

    sdd_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sdd_6",
            "control_code",
            "SDD.6",
        ),
        serialization_alias="SDD.6",
        title="Control Code",
        description="Item #2102",
    )

    sdd_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sdd_7",
            "operator_name",
            "SDD.7",
        ),
        serialization_alias="SDD.7",
        title="Operator Name",
        description="Item #2103",
    )

    @field_validator("sdd_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
