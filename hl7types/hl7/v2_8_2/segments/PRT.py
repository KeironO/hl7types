"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PRT
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN


class PRT(BaseModel):
    """HL7 v2 PRT segment."""

    prt_1: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_1",
            "participation_instance_id",
            "PRT.1",
        ),
        serialization_alias="PRT.1",
        title="Participation Instance ID",
        description="Item #2379",
    )

    prt_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "prt_2",
            "action_code",
            "PRT.2",
        ),
        serialization_alias="PRT.2",
        title="Action Code",
        description="Item #816 | Table HL70206",
    )

    prt_3: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_3",
            "action_reason",
            "PRT.3",
        ),
        serialization_alias="PRT.3",
        title="Action Reason",
        description="Item #2380",
    )

    prt_4: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "prt_4",
            "participation",
            "PRT.4",
        ),
        serialization_alias="PRT.4",
        title="Participation",
        description="Item #2381 | Table HL70912",
    )

    prt_5: list[XCN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_5",
            "participation_person",
            "PRT.5",
        ),
        serialization_alias="PRT.5",
        title="Participation Person",
        description="Item #2382",
    )

    prt_6: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_6",
            "participation_person_provider_type",
            "PRT.6",
        ),
        serialization_alias="PRT.6",
        title="Participation Person Provider Type",
        description="Item #2383",
    )

    prt_7: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_7",
            "participant_organization_unit_type",
            "PRT.7",
        ),
        serialization_alias="PRT.7",
        title="Participant Organization Unit Type",
        description="Item #2384 | Table HL70406",
    )

    prt_8: list[XON] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_8",
            "participation_organization",
            "PRT.8",
        ),
        serialization_alias="PRT.8",
        title="Participation Organization",
        description="Item #2385",
    )

    prt_9: list[PL] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_9",
            "participant_location",
            "PRT.9",
        ),
        serialization_alias="PRT.9",
        title="Participant Location",
        description="Item #2386",
    )

    prt_10: list[EI] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_10",
            "participation_device",
            "PRT.10",
        ),
        serialization_alias="PRT.10",
        title="Participation Device",
        description="Item #2348",
    )

    prt_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_11",
            "participation_begin_date_time_arrival_time",
            "PRT.11",
        ),
        serialization_alias="PRT.11",
        title="Participation Begin Date/Time (arrival time)",
        description="Item #2387",
    )

    prt_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_12",
            "participation_end_date_time_departure_time",
            "PRT.12",
        ),
        serialization_alias="PRT.12",
        title="Participation End Date/Time (departure time)",
        description="Item #2388",
    )

    prt_13: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_13",
            "participation_qualitative_duration",
            "PRT.13",
        ),
        serialization_alias="PRT.13",
        title="Participation Qualitative Duration",
        description="Item #2389",
    )

    prt_14: list[XAD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_14",
            "participation_address",
            "PRT.14",
        ),
        serialization_alias="PRT.14",
        title="Participation Address",
        description="Item #2390",
    )

    prt_15: list[XTN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_15",
            "participant_telecommunication_address",
            "PRT.15",
        ),
        serialization_alias="PRT.15",
        title="Participant Telecommunication Address",
        description="Item #2391",
    )

    prt_16: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_16",
            "participant_device_identifier",
            "PRT.16",
        ),
        serialization_alias="PRT.16",
        title="Participant Device Identifier",
        description="Item #3476",
    )

    prt_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_17",
            "participant_device_manufacture_date",
            "PRT.17",
        ),
        serialization_alias="PRT.17",
        title="Participant Device Manufacture Date",
        description="Item #3477",
    )

    prt_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_18",
            "participant_device_expiry_date",
            "PRT.18",
        ),
        serialization_alias="PRT.18",
        title="Participant Device Expiry Date",
        description="Item #3478",
    )

    prt_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_19",
            "participant_device_lot_number",
            "PRT.19",
        ),
        serialization_alias="PRT.19",
        title="Participant Device Lot Number",
        description="Item #3479",
    )

    prt_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_20",
            "participant_device_serial_number",
            "PRT.20",
        ),
        serialization_alias="PRT.20",
        title="Participant Device Serial Number",
        description="Item #3480",
    )

    prt_21: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_21",
            "participant_device_donation_identification",
            "PRT.21",
        ),
        serialization_alias="PRT.21",
        title="Participant Device Donation Identification",
        description="Item #3481",
    )

    prt_22: CNE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_22",
            "participation_device_type",
            "PRT.22",
        ),
        serialization_alias="PRT.22",
        title="Participation Device Type",
        description="Item #3483",
    )

    model_config = {"populate_by_name": True}
