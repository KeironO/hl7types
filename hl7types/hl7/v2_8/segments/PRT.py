"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: PRT
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN


class PRT(BaseModel):
    """HL7 v2 PRT segment."""

    prt_1: Optional[EI] = Field(
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

    prt_3: Optional[CWE] = Field(
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

    prt_5: Optional[List[XCN]] = Field(
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

    prt_6: Optional[CWE] = Field(
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

    prt_7: Optional[CWE] = Field(
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

    prt_8: Optional[List[XON]] = Field(
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

    prt_9: Optional[List[PL]] = Field(
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

    prt_10: Optional[List[EI]] = Field(
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

    prt_11: Optional[str] = Field(
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

    prt_12: Optional[str] = Field(
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

    prt_13: Optional[CWE] = Field(
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

    prt_14: Optional[List[XAD]] = Field(
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

    prt_15: Optional[List[XTN]] = Field(
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

    model_config = {"populate_by_name": True}
