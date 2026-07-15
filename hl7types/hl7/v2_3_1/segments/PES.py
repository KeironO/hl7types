"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PES
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.EI import EI
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN


class PES(HL7Model):
    """PES - product experience sender segment (S7.11.1).

    Attributes
    ----------
    pes_1 : list[XON] | None
        PES.1 - Sender Organization Name (XON) O rep S7.11.1.1

    pes_2 : list[XCN] | None
        PES.2 - Sender Individual Name (XCN) O rep S7.11.1.2

    pes_3 : list[XAD] | None
        PES.3 - Sender Address (XAD) O rep S7.11.1.3

    pes_4 : list[XTN] | None
        PES.4 - Sender Telephone (XTN) O rep S7.11.1.4

    pes_5 : EI | None
        PES.5 - Sender Event Identifier (EI) O S7.11.1.5

    pes_6 : str | None
        PES.6 - Sender Sequence Number (NM) O S7.11.1.6

    pes_7 : list[str] | None
        PES.7 - Sender Event Description (FT) O rep S7.11.1.7

    pes_8 : str | None
        PES.8 - Sender Comment (FT) O S7.11.1.8

    pes_9 : TS | None
        PES.9 - Sender Aware Date/Time (TS) O S7.11.1.9

    pes_10 : TS
        PES.10 - Event Report Date (TS) R S7.11.1.10

    pes_11 : list[str] | None
        PES.11 - Event Report Timing/Type (ID) O rep S7.11.1.11 | 0234 - Report timing

    pes_12 : str | None
        PES.12 - Event Report Source (ID) O S7.11.1.12 | 0235 - Report source

    pes_13 : list[str] | None
        PES.13 - Event Reported To (ID) O rep S7.11.1.13 | 0236 - Event reported to
    """

    pes_1: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_1",
            "sender_organization_name",
            "PES.1",
        ),
        serialization_alias="PES.1",
        title="Sender Organization Name",
        description="O | Item #01059",
    )

    pes_2: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_2",
            "sender_individual_name",
            "PES.2",
        ),
        serialization_alias="PES.2",
        title="Sender Individual Name",
        description="O | Item #01060",
    )

    pes_3: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_3",
            "sender_address",
            "PES.3",
        ),
        serialization_alias="PES.3",
        title="Sender Address",
        description="O | Item #01062",
    )

    pes_4: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_4",
            "sender_telephone",
            "PES.4",
        ),
        serialization_alias="PES.4",
        title="Sender Telephone",
        description="O | Item #01063",
    )

    pes_5: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_5",
            "sender_event_identifier",
            "PES.5",
        ),
        serialization_alias="PES.5",
        title="Sender Event Identifier",
        description="O | Item #01064",
    )

    pes_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_6",
            "sender_sequence_number",
            "PES.6",
        ),
        serialization_alias="PES.6",
        title="Sender Sequence Number",
        description="O | Item #01065 | LEN:2",
    )

    pes_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_7",
            "sender_event_description",
            "PES.7",
        ),
        serialization_alias="PES.7",
        title="Sender Event Description",
        description="O | Item #01066",
    )

    pes_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_8",
            "sender_comment",
            "PES.8",
        ),
        serialization_alias="PES.8",
        title="Sender Comment",
        description="O | Item #01067",
    )

    pes_9: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_9",
            "sender_aware_date_time",
            "PES.9",
        ),
        serialization_alias="PES.9",
        title="Sender Aware Date/Time",
        description="O | Item #01068",
    )

    pes_10: TS = Field(
        validation_alias=AliasChoices(
            "pes_10",
            "event_report_date",
            "PES.10",
        ),
        serialization_alias="PES.10",
        title="Event Report Date",
        description="R | Item #01069",
    )

    pes_11: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_11",
            "event_report_timing_type",
            "PES.11",
        ),
        serialization_alias="PES.11",
        title="Event Report Timing/Type",
        description="O | Item #01070 | Table 0234 - Report timing | LEN:3",
    )

    pes_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_12",
            "event_report_source",
            "PES.12",
        ),
        serialization_alias="PES.12",
        title="Event Report Source",
        description="O | Item #01071 | Table 0235 - Report source | LEN:1",
    )

    pes_13: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_13",
            "event_reported_to",
            "PES.13",
        ),
        serialization_alias="PES.13",
        title="Event Reported To",
        description="O | Item #01072 | Table 0236 - Event reported to | LEN:1",
    )

    @field_validator("pes_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
