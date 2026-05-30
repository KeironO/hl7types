"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ARQ
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.DR import DR
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.RI import RI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class ARQ(HL7Model):
    """HL7 v2 ARQ segment.

    Attributes
    ----------
    arq_1 : EI
        ARQ.1 (req) - Placer Appointment ID (EI)

    arq_2 : EI | None
        ARQ.2 (opt) - Filler Appointment ID (EI)

    arq_3 : str | None
        ARQ.3 (opt) - Occurrence Number (NM)

    arq_4 : EI | None
        ARQ.4 (opt) - Placer Group Number (EI)

    arq_5 : CWE | None
        ARQ.5 (opt) - Schedule ID (CWE)

    arq_6 : CWE | None
        ARQ.6 (opt) - Request Event Reason (CWE)

    arq_7 : CWE | None
        ARQ.7 (opt) - Appointment Reason (CWE)

    arq_8 : CWE | None
        ARQ.8 (opt) - Appointment Type (CWE)

    arq_9 : str | None
        ARQ.9 (opt) - Appointment Duration (NM)

    arq_10 : CNE | None
        ARQ.10 (opt) - Appointment Duration Units (CNE)

    arq_11 : list[DR] | None
        ARQ.11 (opt, rep) - Requested Start Date/Time Range (DR)

    arq_12 : str | None
        ARQ.12 (opt) - Priority-ARQ (ST)

    arq_13 : RI | None
        ARQ.13 (opt) - Repeating Interval (RI)

    arq_14 : str | None
        ARQ.14 (opt) - Repeating Interval Duration (ST)

    arq_15 : list[XCN]
        ARQ.15 (req, rep) - Placer Contact Person (XCN)

    arq_16 : list[XTN] | None
        ARQ.16 (opt, rep) - Placer Contact Phone Number (XTN)

    arq_17 : list[XAD] | None
        ARQ.17 (opt, rep) - Placer Contact Address (XAD)

    arq_18 : PL | None
        ARQ.18 (opt) - Placer Contact Location (PL)

    arq_19 : list[XCN]
        ARQ.19 (req, rep) - Entered By Person (XCN)

    arq_20 : list[XTN] | None
        ARQ.20 (opt, rep) - Entered By Phone Number (XTN)

    arq_21 : PL | None
        ARQ.21 (opt) - Entered By Location (PL)

    arq_22 : EI | None
        ARQ.22 (opt) - Parent Placer Appointment ID (EI)

    arq_23 : EI | None
        ARQ.23 (opt) - Parent Filler Appointment ID (EI)

    arq_24 : list[EI] | None
        ARQ.24 (opt, rep) - Placer Order Number (EI)

    arq_25 : list[EI] | None
        ARQ.25 (opt, rep) - Filler Order Number (EI)
    """

    arq_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "arq_1",
            "placer_appointment_id",
            "ARQ.1",
        ),
        serialization_alias="ARQ.1",
        title="Placer Appointment ID",
        description="Item #860",
    )

    arq_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_2",
            "filler_appointment_id",
            "ARQ.2",
        ),
        serialization_alias="ARQ.2",
        title="Filler Appointment ID",
        description="Item #861",
    )

    arq_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_3",
            "occurrence_number",
            "ARQ.3",
        ),
        serialization_alias="ARQ.3",
        title="Occurrence Number",
        description="Item #862",
    )

    arq_4: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_4",
            "placer_group_number",
            "ARQ.4",
        ),
        serialization_alias="ARQ.4",
        title="Placer Group Number",
        description="Item #218",
    )

    arq_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_5",
            "schedule_id",
            "ARQ.5",
        ),
        serialization_alias="ARQ.5",
        title="Schedule ID",
        description="Item #864",
    )

    arq_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_6",
            "request_event_reason",
            "ARQ.6",
        ),
        serialization_alias="ARQ.6",
        title="Request Event Reason",
        description="Item #865",
    )

    arq_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_7",
            "appointment_reason",
            "ARQ.7",
        ),
        serialization_alias="ARQ.7",
        title="Appointment Reason",
        description="Item #866 | Table HL70276",
    )

    arq_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_8",
            "appointment_type",
            "ARQ.8",
        ),
        serialization_alias="ARQ.8",
        title="Appointment Type",
        description="Item #867 | Table HL70277",
    )

    arq_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_9",
            "appointment_duration",
            "ARQ.9",
        ),
        serialization_alias="ARQ.9",
        title="Appointment Duration",
        description="Item #868",
    )

    arq_10: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_10",
            "appointment_duration_units",
            "ARQ.10",
        ),
        serialization_alias="ARQ.10",
        title="Appointment Duration Units",
        description="Item #869",
    )

    arq_11: Optional[List[DR]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_11",
            "requested_start_date_time_range",
            "ARQ.11",
        ),
        serialization_alias="ARQ.11",
        title="Requested Start Date/Time Range",
        description="Item #870",
    )

    arq_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_12",
            "priority_arq",
            "ARQ.12",
        ),
        serialization_alias="ARQ.12",
        title="Priority-ARQ",
        description="Item #871",
    )

    arq_13: Optional[RI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_13",
            "repeating_interval",
            "ARQ.13",
        ),
        serialization_alias="ARQ.13",
        title="Repeating Interval",
        description="Item #872",
    )

    arq_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_14",
            "repeating_interval_duration",
            "ARQ.14",
        ),
        serialization_alias="ARQ.14",
        title="Repeating Interval Duration",
        description="Item #873",
    )

    arq_15: List[XCN] = Field(
        default=...,
        validation_alias=AliasChoices(
            "arq_15",
            "placer_contact_person",
            "ARQ.15",
        ),
        serialization_alias="ARQ.15",
        title="Placer Contact Person",
        description="Item #874",
    )

    arq_16: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_16",
            "placer_contact_phone_number",
            "ARQ.16",
        ),
        serialization_alias="ARQ.16",
        title="Placer Contact Phone Number",
        description="Item #875",
    )

    arq_17: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_17",
            "placer_contact_address",
            "ARQ.17",
        ),
        serialization_alias="ARQ.17",
        title="Placer Contact Address",
        description="Item #876",
    )

    arq_18: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_18",
            "placer_contact_location",
            "ARQ.18",
        ),
        serialization_alias="ARQ.18",
        title="Placer Contact Location",
        description="Item #877",
    )

    arq_19: List[XCN] = Field(
        default=...,
        validation_alias=AliasChoices(
            "arq_19",
            "entered_by_person",
            "ARQ.19",
        ),
        serialization_alias="ARQ.19",
        title="Entered By Person",
        description="Item #878",
    )

    arq_20: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_20",
            "entered_by_phone_number",
            "ARQ.20",
        ),
        serialization_alias="ARQ.20",
        title="Entered By Phone Number",
        description="Item #879",
    )

    arq_21: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_21",
            "entered_by_location",
            "ARQ.21",
        ),
        serialization_alias="ARQ.21",
        title="Entered By Location",
        description="Item #880",
    )

    arq_22: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_22",
            "parent_placer_appointment_id",
            "ARQ.22",
        ),
        serialization_alias="ARQ.22",
        title="Parent Placer Appointment ID",
        description="Item #881",
    )

    arq_23: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_23",
            "parent_filler_appointment_id",
            "ARQ.23",
        ),
        serialization_alias="ARQ.23",
        title="Parent Filler Appointment ID",
        description="Item #882",
    )

    arq_24: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_24",
            "placer_order_number",
            "ARQ.24",
        ),
        serialization_alias="ARQ.24",
        title="Placer Order Number",
        description="Item #216",
    )

    arq_25: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_25",
            "filler_order_number",
            "ARQ.25",
        ),
        serialization_alias="ARQ.25",
        title="Filler Order Number",
        description="Item #217",
    )

    model_config = {"populate_by_name": True}
