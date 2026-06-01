"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: SCH
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.EIP import EIP
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class SCH(HL7Model):
    """HL7 v2 SCH segment.

    Attributes
    ----------
    sch_1 : EI | None
        SCH.1 (opt) - Placer Appointment ID (EI)

    sch_2 : EI | None
        SCH.2 (opt) - Filler Appointment ID (EI)

    sch_3 : str | None
        SCH.3 (opt) - Occurrence Number (NM)

    sch_4 : EIP | None
        SCH.4 (opt) - Placer Group Number (EIP)

    sch_5 : CWE | None
        SCH.5 (opt) - Schedule ID (CWE)

    sch_6 : CWE
        SCH.6 (req) - Event Reason (CWE)

    sch_7 : CWE | None
        SCH.7 (opt) - Appointment Reason (CWE)

    sch_8 : CWE | None
        SCH.8 (opt) - Appointment Type (CWE)

    sch_10 : CNE | None
        SCH.10 (opt) - Appointment Duration Units (CNE)

    sch_12 : list[XCN] | None
        SCH.12 (opt, rep) - Placer Contact Person (XCN)

    sch_13 : XTN | None
        SCH.13 (opt) - Placer Contact Phone Number (XTN)

    sch_14 : list[XAD] | None
        SCH.14 (opt, rep) - Placer Contact Address (XAD)

    sch_15 : PL | None
        SCH.15 (opt) - Placer Contact Location (PL)

    sch_16 : list[XCN] | None
        SCH.16 (req, rep) - Filler Contact Person (XCN) [optional: XCN has no required components]

    sch_17 : XTN | None
        SCH.17 (opt) - Filler Contact Phone Number (XTN)

    sch_18 : list[XAD] | None
        SCH.18 (opt, rep) - Filler Contact Address (XAD)

    sch_19 : PL | None
        SCH.19 (opt) - Filler Contact Location (PL)

    sch_20 : list[XCN] | None
        SCH.20 (req, rep) - Entered By Person (XCN) [optional: XCN has no required components]

    sch_21 : list[XTN] | None
        SCH.21 (opt, rep) - Entered By Phone Number (XTN)

    sch_22 : PL | None
        SCH.22 (opt) - Entered By Location (PL)

    sch_23 : EI | None
        SCH.23 (opt) - Parent Placer Appointment ID (EI)

    sch_24 : EI | None
        SCH.24 (opt) - Parent Filler Appointment ID (EI)

    sch_25 : CWE | None
        SCH.25 (opt) - Filler Status Code (CWE)

    sch_26 : list[EI] | None
        SCH.26 (opt, rep) - Placer Order Number (EI)

    sch_27 : list[EI] | None
        SCH.27 (opt, rep) - Filler Order Number (EI)
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
        description="Item #860",
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
        description="Item #861",
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
        description="Item #862",
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
        description="Item #218",
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
        description="Item #864",
    )

    sch_6: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "sch_6",
            "event_reason",
            "SCH.6",
        ),
        serialization_alias="SCH.6",
        title="Event Reason",
        description="Item #883",
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
        description="Item #866 | Table HL70276",
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
        description="Item #867 | Table HL70277",
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
        description="Item #869",
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
        description="Item #874",
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
        description="Item #875",
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
        description="Item #876",
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
        description="Item #877",
    )

    sch_16: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_16",
            "filler_contact_person",
            "SCH.16",
        ),
        serialization_alias="SCH.16",
        title="Filler Contact Person",
        description="Item #885",
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
        description="Item #886",
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
        description="Item #887",
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
        description="Item #888",
    )

    sch_20: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sch_20",
            "entered_by_person",
            "SCH.20",
        ),
        serialization_alias="SCH.20",
        title="Entered By Person",
        description="Item #878",
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
        description="Item #879",
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
        description="Item #880",
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
        description="Item #881",
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
        description="Item #882",
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
        description="Item #889 | Table HL70278",
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
        description="Item #216",
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
        description="Item #217",
    )

    @field_validator("sch_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
