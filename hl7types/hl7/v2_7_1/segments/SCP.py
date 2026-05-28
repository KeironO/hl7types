"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: SCP
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class SCP(BaseModel):
    """HL7 v2 SCP segment."""

    scp_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_1",
            "number_of_decontamination_sterilization_devices",
            "SCP.1",
        ),
        serialization_alias="SCP.1",
        title="Number Of Decontamination/Sterilization Devices",
        description="Item #2087",
    )

    scp_2: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_2",
            "labor_calculation_type",
            "SCP.2",
        ),
        serialization_alias="SCP.2",
        title="Labor Calculation Type",
        description="Item #2088 | Table HL70651",
    )

    scp_3: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_3",
            "date_format",
            "SCP.3",
        ),
        serialization_alias="SCP.3",
        title="Date Format",
        description="Item #2089 | Table HL70653",
    )

    scp_4: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_4",
            "device_number",
            "SCP.4",
        ),
        serialization_alias="SCP.4",
        title="Device Number",
        description="Item #2090",
    )

    scp_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_5",
            "device_name",
            "SCP.5",
        ),
        serialization_alias="SCP.5",
        title="Device Name",
        description="Item #2279",
    )

    scp_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_6",
            "device_model_name",
            "SCP.6",
        ),
        serialization_alias="SCP.6",
        title="Device Model Name",
        description="Item #2091",
    )

    scp_7: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_7",
            "device_type",
            "SCP.7",
        ),
        serialization_alias="SCP.7",
        title="Device Type",
        description="Item #2092 | Table HL70657",
    )

    scp_8: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_8",
            "lot_control",
            "SCP.8",
        ),
        serialization_alias="SCP.8",
        title="Lot Control",
        description="Item #2093 | Table HL70659",
    )

    model_config = {"populate_by_name": True}
