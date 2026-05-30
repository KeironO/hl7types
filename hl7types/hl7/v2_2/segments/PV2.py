"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: PV2
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class PV2(HL7Model):
    """HL7 v2 PV2 segment.

    Attributes
    ----------
    pv2_1 : str | None
        PV2.1 (opt) - Prior Pending Location (CM)

    pv2_2 : CE | None
        PV2.2 (opt) - Accommodation Code (CE)

    pv2_3 : CE | None
        PV2.3 (opt) - Admit Reason (CE)

    pv2_4 : CE | None
        PV2.4 (opt) - Transfer Reason (CE)

    pv2_5 : list[str] | None
        PV2.5 (opt, rep) - Patient Valuables (ST)

    pv2_6 : str | None
        PV2.6 (opt) - Patient Valuables Location (ST)

    pv2_7 : str | None
        PV2.7 (opt) - Visit User Code (ID)

    pv2_8 : str | None
        PV2.8 (opt) - Expected Admit Date (DT)

    pv2_9 : str | None
        PV2.9 (opt) - Expected Discharge Date (DT)
    """

    pv2_1: Optional[str] = Field(
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

    pv2_2: Optional[CE] = Field(
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

    pv2_3: Optional[CE] = Field(
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

    pv2_4: Optional[CE] = Field(
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

    pv2_5: Optional[List[str]] = Field(
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

    pv2_6: Optional[str] = Field(
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

    pv2_7: Optional[str] = Field(
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

    pv2_8: Optional[str] = Field(
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

    pv2_9: Optional[str] = Field(
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
