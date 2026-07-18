"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ARQ
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.DR import DR
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.RI import RI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class ARQ(HL7Model):
    """ARQ - appointment request segment (S10.5.1).

    Attributes
    ----------
    arq_1 : EI
        ARQ.1 - Placer Appointment ID (EI) R S10.5.2.1

    arq_2 : EI | None
        ARQ.2 - Filler Appointment ID (EI) C S10.5.2.2

    arq_3 : str | None
        ARQ.3 - Occurrence Number (NM) C S10.5.2.3

    arq_4 : EI | None
        ARQ.4 - Placer Group Number (EI) O S10.5.2.4

    arq_5 : CE | None
        ARQ.5 - Schedule ID (CE) O S10.5.2.5

    arq_6 : CE | None
        ARQ.6 - Request Event Reason (CE) O S10.5.1.6

    arq_7 : CE | None
        ARQ.7 - Appointment Reason (CE) O S10.5.2.7 | 0276 - Appointment reason codes

    arq_8 : CE | None
        ARQ.8 - Appointment Type (CE) O S10.5.2.8 | 0277 - Appointment type codes

    arq_9 : str | None
        ARQ.9 - Appointment Duration (NM) O S10.5.2.9

    arq_10 : CE | None
        ARQ.10 - Appointment Duration Units (CE) O S10.5.2.10

    arq_11 : list[DR] | None
        ARQ.11 - Requested Start Date/Time Range (DR) O rep S10.5.1.11

    arq_12 : str | None
        ARQ.12 - Priority-ARQ (ST) O S10.5.1.12

    arq_13 : RI | None
        ARQ.13 - Repeating Interval (RI) O S10.5.1.13

    arq_14 : str | None
        ARQ.14 - Repeating Interval Duration (ST) O S10.5.1.14

    arq_15 : list[XCN]
        ARQ.15 - Placer Contact Person (XCN) R rep S10.5.2.12

    arq_16 : list[XTN] | None
        ARQ.16 - Placer Contact Phone Number (XTN) O rep S10.5.2.13

    arq_17 : list[XAD] | None
        ARQ.17 - Placer Contact Address (XAD) O rep S10.5.2.14

    arq_18 : PL | None
        ARQ.18 - Placer Contact Location (PL) O S10.5.2.15

    arq_19 : list[XCN]
        ARQ.19 - Entered by Person (XCN) R rep S10.5.2.20

    arq_20 : list[XTN] | None
        ARQ.20 - Entered by Phone Number (XTN) O rep S10.5.2.21

    arq_21 : PL | None
        ARQ.21 - Entered by Location (PL) O S10.5.2.22

    arq_22 : EI | None
        ARQ.22 - Parent Placer Appointment ID (EI) O S10.5.2.23

    arq_23 : EI | None
        ARQ.23 - Parent Filler Appointment ID (EI) O S10.5.2.24
    """

    arq_1: EI = Field(
        validation_alias=AliasChoices(
            "arq_1",
            "placer_appointment_id",
            "ARQ.1",
        ),
        serialization_alias="ARQ.1",
        title="Placer Appointment ID",
        description="R | Item #00860",
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
        description="C | Item #00861",
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
        description="C | Item #00862 | LEN:5",
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
        description="O | Item #00218",
    )

    arq_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_5",
            "schedule_id",
            "ARQ.5",
        ),
        serialization_alias="ARQ.5",
        title="Schedule ID",
        description="O | Item #00864",
    )

    arq_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_6",
            "request_event_reason",
            "ARQ.6",
        ),
        serialization_alias="ARQ.6",
        title="Request Event Reason",
        description="O | Item #00865",
    )

    arq_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_7",
            "appointment_reason",
            "ARQ.7",
        ),
        serialization_alias="ARQ.7",
        title="Appointment Reason",
        description="O | Item #00866 | Table 0276 - Appointment reason codes",
    )

    arq_8: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_8",
            "appointment_type",
            "ARQ.8",
        ),
        serialization_alias="ARQ.8",
        title="Appointment Type",
        description="O | Item #00867 | Table 0277 - Appointment type codes",
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
        description="O | Item #00868 | LEN:20",
    )

    arq_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_10",
            "appointment_duration_units",
            "ARQ.10",
        ),
        serialization_alias="ARQ.10",
        title="Appointment Duration Units",
        description="O | Item #00869",
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
        description="O | Item #00870",
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
        description="O | Item #00871 | LEN:5",
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
        description="O | Item #00872",
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
        description="O | Item #00873 | LEN:5",
    )

    arq_15: List[XCN] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "arq_15",
            "placer_contact_person",
            "ARQ.15",
        ),
        serialization_alias="ARQ.15",
        title="Placer Contact Person",
        description="R | Item #00874",
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
        description="O | Item #00875",
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
        description="O | Item #00876",
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
        description="O | Item #00877",
    )

    arq_19: List[XCN] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "arq_19",
            "entered_by_person",
            "ARQ.19",
        ),
        serialization_alias="ARQ.19",
        title="Entered by Person",
        description="R | Item #00878",
    )

    arq_20: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_20",
            "entered_by_phone_number",
            "ARQ.20",
        ),
        serialization_alias="ARQ.20",
        title="Entered by Phone Number",
        description="O | Item #00879",
    )

    arq_21: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "arq_21",
            "entered_by_location",
            "ARQ.21",
        ),
        serialization_alias="ARQ.21",
        title="Entered by Location",
        description="O | Item #00880",
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
        description="O | Item #00881",
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
        description="O | Item #00882",
    )

    @field_validator("arq_3", "arq_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
