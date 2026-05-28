"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: PV2
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class PV2(BaseModel):
    """HL7 v2 PV2 segment."""

    pv2_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_1",
            "prior_pending_location",
            "PV2.1",
        ),
        serialization_alias="PV2.1",
        title="Prior Pending Location",
        description="Item #181",
    )

    pv2_2: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_2",
            "accommodation_code",
            "PV2.2",
        ),
        serialization_alias="PV2.2",
        title="Accommodation Code",
        description="Item #182 | Table HL70129",
    )

    pv2_3: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_3",
            "admit_reason",
            "PV2.3",
        ),
        serialization_alias="PV2.3",
        title="Admit Reason",
        description="Item #183",
    )

    pv2_4: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_4",
            "transfer_reason",
            "PV2.4",
        ),
        serialization_alias="PV2.4",
        title="Transfer Reason",
        description="Item #184",
    )

    pv2_5: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_5",
            "patient_valuables",
            "PV2.5",
        ),
        serialization_alias="PV2.5",
        title="Patient Valuables",
        description="Item #185",
    )

    pv2_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_6",
            "patient_valuables_location",
            "PV2.6",
        ),
        serialization_alias="PV2.6",
        title="Patient Valuables Location",
        description="Item #186",
    )

    pv2_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_7",
            "visit_user_code",
            "PV2.7",
        ),
        serialization_alias="PV2.7",
        title="Visit User Code",
        description="Item #187 | Table HL70130",
    )

    pv2_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_8",
            "expected_admit_date",
            "PV2.8",
        ),
        serialization_alias="PV2.8",
        title="Expected Admit Date",
        description="Item #188",
    )

    pv2_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_9",
            "expected_discharge_date",
            "PV2.9",
        ),
        serialization_alias="PV2.9",
        title="Expected Discharge Date",
        description="Item #189",
    )

    model_config = {"populate_by_name": True}
