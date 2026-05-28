"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SDD
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class SDD(BaseModel):
    """HL7 v2 SDD segment."""

    sdd_1: EI | None = Field(
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

    sdd_2: EI | None = Field(
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

    sdd_3: str | None = Field(
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

    sdd_4: CWE | None = Field(
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

    sdd_5: CWE | None = Field(
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

    sdd_6: str | None = Field(
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

    sdd_7: str | None = Field(
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

    model_config = {"populate_by_name": True}
