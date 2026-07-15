"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SCP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class SCP(HL7Model):
    """Sterilizer Configuration (Anti-Microbial Devices) (S17.7.1).

    Attributes
    ----------
    scp_1 : str | None
        SCP.1 - Number Of Decontamination/Sterilization Devices (NM) O S17.7.1.1

    scp_2 : CWE | None
        SCP.2 - Labor Calculation Type (CWE) O S17.7.1.2 | 0651 - Labor Calculation Type

    scp_3 : CWE | None
        SCP.3 - Date Format (CWE) O S17.7.1.3 | 0653 - Date Format

    scp_4 : EI | None
        SCP.4 - Device Number (EI) O S17.7.1.4

    scp_5 : str | None
        SCP.5 - Device Name (ST) O S17.7.1.5

    scp_6 : str | None
        SCP.6 - Device Model Name (ST) O S17.7.1.6

    scp_7 : CWE | None
        SCP.7 - Device Type (CWE) O S17.7.1.7 | 0657 - Device Type

    scp_8 : CWE | None
        SCP.8 - Lot Control (CWE) O S17.7.1.8 | 0659 - Lot Control
    """

    scp_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_1",
            "number_of_decontamination_sterilization_devices",
            "SCP.1",
        ),
        serialization_alias="SCP.1",
        title="Number Of Decontamination/Sterilization Devices",
        description="O | Item #02087",
    )

    scp_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_2",
            "labor_calculation_type",
            "SCP.2",
        ),
        serialization_alias="SCP.2",
        title="Labor Calculation Type",
        description="O | Item #02088 | Table 0651 - Labor Calculation Type",
    )

    scp_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_3",
            "date_format",
            "SCP.3",
        ),
        serialization_alias="SCP.3",
        title="Date Format",
        description="O | Item #02089 | Table 0653 - Date Format",
    )

    scp_4: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_4",
            "device_number",
            "SCP.4",
        ),
        serialization_alias="SCP.4",
        title="Device Number",
        description="O | Item #02090",
    )

    scp_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_5",
            "device_name",
            "SCP.5",
        ),
        serialization_alias="SCP.5",
        title="Device Name",
        description="O | Item #02279",
    )

    scp_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_6",
            "device_model_name",
            "SCP.6",
        ),
        serialization_alias="SCP.6",
        title="Device Model Name",
        description="O | Item #02091",
    )

    scp_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_7",
            "device_type",
            "SCP.7",
        ),
        serialization_alias="SCP.7",
        title="Device Type",
        description="O | Item #02092 | Table 0657 - Device Type",
    )

    scp_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scp_8",
            "lot_control",
            "SCP.8",
        ),
        serialization_alias="SCP.8",
        title="Lot Control",
        description="O | Item #02093 | Table 0659 - Lot Control",
    )

    @field_validator("scp_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
