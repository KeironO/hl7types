"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: SCH
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.EIP import EIP
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class SCH(HL7Model):
    """Scheduling Activity Information (S10.6.2).

    Attributes
    ----------
    sch_1 : EI | None
        SCH.1 - Placer Appointment ID (EI) C S10.6.1.1

    sch_2 : EI | None
        SCH.2 - Filler Appointment ID (EI) C S10.6.1.2

    sch_3 : str | None
        SCH.3 - Occurrence Number (NM) C S10.6.1.3

    sch_4 : EIP | None
        SCH.4 - Placer Group Number (EIP) O S10.6.1.4

    sch_5 : CWE | None
        SCH.5 - Schedule ID (CWE) O S10.6.1.5

    sch_6 : CWE
        SCH.6 - Event Reason (CWE) R S10.6.2.6

    sch_7 : CWE | None
        SCH.7 - Appointment Reason (CWE) O S10.6.1.7 | 0276 - Appointment reason codes

    sch_8 : CWE | None
        SCH.8 - Appointment Type (CWE) O S10.6.1.8 | 0277 - Appointment Type Codes

    sch_10 : CNE | None
        SCH.10 - Appointment Duration Units (CNE) O S10.6.1.10

    sch_12 : list[XCN] | None
        SCH.12 - Placer Contact Person (XCN) O rep S10.6.1.15

    sch_13 : XTN | None
        SCH.13 - Placer Contact Phone Number (XTN) O S10.6.1.16

    sch_14 : list[XAD] | None
        SCH.14 - Placer Contact Address (XAD) O rep S10.6.1.17

    sch_15 : PL | None
        SCH.15 - Placer Contact Location (PL) O S10.6.1.18

    sch_16 : list[XCN]
        SCH.16 - Filler Contact Person (XCN) R rep S10.6.2.16

    sch_17 : XTN | None
        SCH.17 - Filler Contact Phone Number (XTN) O S10.6.2.17

    sch_18 : list[XAD] | None
        SCH.18 - Filler Contact Address (XAD) O rep S10.6.2.18

    sch_19 : PL | None
        SCH.19 - Filler Contact Location (PL) O S10.6.2.19

    sch_20 : list[XCN]
        SCH.20 - Entered By Person (XCN) R rep S10.6.1.19

    sch_21 : list[XTN] | None
        SCH.21 - Entered By Phone Number (XTN) O rep S10.6.1.20

    sch_22 : PL | None
        SCH.22 - Entered By Location (PL) O S10.6.1.21

    sch_23 : EI | None
        SCH.23 - Parent Placer Appointment ID (EI) O S10.6.1.22

    sch_24 : EI | None
        SCH.24 - Parent Filler Appointment ID (EI) C S10.6.1.23

    sch_25 : CWE | None
        SCH.25 - Filler Status Code (CWE) O S10.6.2.25 | 0278 - Filler status codes

    sch_26 : list[EI] | None
        SCH.26 - Placer Order Number (EI) C rep S10.6.1.24

    sch_27 : list[EI] | None
        SCH.27 - Filler Order Number (EI) C rep S10.6.1.25
    """

    sch_1: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_1",
            "placer_appointment_id",
            "SCH.1",
        ),
        serialization_alias="SCH.1",
        title="Placer Appointment ID",
        description="C | Item #00860",
    )

    sch_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_2",
            "filler_appointment_id",
            "SCH.2",
        ),
        serialization_alias="SCH.2",
        title="Filler Appointment ID",
        description="C | Item #00861",
    )

    sch_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_3",
            "occurrence_number",
            "SCH.3",
        ),
        serialization_alias="SCH.3",
        title="Occurrence Number",
        description="C | Item #00862",
    )

    sch_4: Optional[EIP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_4",
            "placer_group_number",
            "SCH.4",
        ),
        serialization_alias="SCH.4",
        title="Placer Group Number",
        description="O | Item #00218",
    )

    sch_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_5",
            "schedule_id",
            "SCH.5",
        ),
        serialization_alias="SCH.5",
        title="Schedule ID",
        description="O | Item #00864",
    )

    sch_6: CWE = Field(
        validation_alias=AliasChoices(
            "sch_6",
            "event_reason",
            "SCH.6",
        ),
        serialization_alias="SCH.6",
        title="Event Reason",
        description="R | Item #00883",
    )

    sch_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_7",
            "appointment_reason",
            "SCH.7",
        ),
        serialization_alias="SCH.7",
        title="Appointment Reason",
        description="O | Item #00866 | Table 0276 - Appointment reason codes",
    )

    sch_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_8",
            "appointment_type",
            "SCH.8",
        ),
        serialization_alias="SCH.8",
        title="Appointment Type",
        description="O | Item #00867 | Table 0277 - Appointment Type Codes",
    )

    sch_10: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_10",
            "appointment_duration_units",
            "SCH.10",
        ),
        serialization_alias="SCH.10",
        title="Appointment Duration Units",
        description="O | Item #00869",
    )

    sch_12: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_12",
            "placer_contact_person",
            "SCH.12",
        ),
        serialization_alias="SCH.12",
        title="Placer Contact Person",
        description="O | Item #00874",
    )

    sch_13: Optional[XTN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_13",
            "placer_contact_phone_number",
            "SCH.13",
        ),
        serialization_alias="SCH.13",
        title="Placer Contact Phone Number",
        description="O | Item #00875",
    )

    sch_14: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_14",
            "placer_contact_address",
            "SCH.14",
        ),
        serialization_alias="SCH.14",
        title="Placer Contact Address",
        description="O | Item #00876",
    )

    sch_15: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_15",
            "placer_contact_location",
            "SCH.15",
        ),
        serialization_alias="SCH.15",
        title="Placer Contact Location",
        description="O | Item #00877",
    )

    sch_16: List[XCN] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "sch_16",
            "filler_contact_person",
            "SCH.16",
        ),
        serialization_alias="SCH.16",
        title="Filler Contact Person",
        description="R | Item #00885",
    )

    sch_17: Optional[XTN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_17",
            "filler_contact_phone_number",
            "SCH.17",
        ),
        serialization_alias="SCH.17",
        title="Filler Contact Phone Number",
        description="O | Item #00886",
    )

    sch_18: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_18",
            "filler_contact_address",
            "SCH.18",
        ),
        serialization_alias="SCH.18",
        title="Filler Contact Address",
        description="O | Item #00887",
    )

    sch_19: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_19",
            "filler_contact_location",
            "SCH.19",
        ),
        serialization_alias="SCH.19",
        title="Filler Contact Location",
        description="O | Item #00888",
    )

    sch_20: List[XCN] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "sch_20",
            "entered_by_person",
            "SCH.20",
        ),
        serialization_alias="SCH.20",
        title="Entered By Person",
        description="R | Item #00878",
    )

    sch_21: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_21",
            "entered_by_phone_number",
            "SCH.21",
        ),
        serialization_alias="SCH.21",
        title="Entered By Phone Number",
        description="O | Item #00879",
    )

    sch_22: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_22",
            "entered_by_location",
            "SCH.22",
        ),
        serialization_alias="SCH.22",
        title="Entered By Location",
        description="O | Item #00880",
    )

    sch_23: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_23",
            "parent_placer_appointment_id",
            "SCH.23",
        ),
        serialization_alias="SCH.23",
        title="Parent Placer Appointment ID",
        description="O | Item #00881",
    )

    sch_24: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_24",
            "parent_filler_appointment_id",
            "SCH.24",
        ),
        serialization_alias="SCH.24",
        title="Parent Filler Appointment ID",
        description="C | Item #00882",
    )

    sch_25: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_25",
            "filler_status_code",
            "SCH.25",
        ),
        serialization_alias="SCH.25",
        title="Filler Status Code",
        description="O | Item #00889 | Table 0278 - Filler status codes",
    )

    sch_26: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_26",
            "placer_order_number",
            "SCH.26",
        ),
        serialization_alias="SCH.26",
        title="Placer Order Number",
        description="C | Item #00216",
    )

    sch_27: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_27",
            "filler_order_number",
            "SCH.27",
        ),
        serialization_alias="SCH.27",
        title="Filler Order Number",
        description="C | Item #00217",
    )

    @field_validator("sch_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
