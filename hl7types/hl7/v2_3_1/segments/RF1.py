"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RF1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TS import TS


class RF1(HL7Model):
    """HL7 v2 RF1 segment.

    Attributes
    ----------
    rf1_1 : CE | None
        RF1.1 (opt) - Referral Status (CE)

    rf1_2 : CE | None
        RF1.2 (opt) - Referral Priority (CE)

    rf1_3 : CE | None
        RF1.3 (opt) - Referral Type (CE)

    rf1_4 : list[CE] | None
        RF1.4 (opt, rep) - Referral Disposition (CE)

    rf1_5 : CE | None
        RF1.5 (opt) - Referral Category (CE)

    rf1_6 : EI
        RF1.6 (req) - Originating Referral Identifier (EI)

    rf1_7 : TS | None
        RF1.7 (opt) - Effective Date (TS)

    rf1_8 : TS | None
        RF1.8 (opt) - Expiration Date (TS)

    rf1_9 : TS | None
        RF1.9 (opt) - Process Date (TS)

    rf1_10 : list[CE] | None
        RF1.10 (opt, rep) - Referral Reason (CE)

    rf1_11 : list[EI] | None
        RF1.11 (opt, rep) - External Referral Identifier (EI)
    """

    rf1_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_1",
            "referral_status",
            "RF1.1",
        ),
        serialization_alias="RF1.1",
        title="Referral Status",
        description="Item #1137 | Table HL70283",
    )

    rf1_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_2",
            "referral_priority",
            "RF1.2",
        ),
        serialization_alias="RF1.2",
        title="Referral Priority",
        description="Item #1138 | Table HL70280",
    )

    rf1_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_3",
            "referral_type",
            "RF1.3",
        ),
        serialization_alias="RF1.3",
        title="Referral Type",
        description="Item #1139 | Table HL70281",
    )

    rf1_4: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_4",
            "referral_disposition",
            "RF1.4",
        ),
        serialization_alias="RF1.4",
        title="Referral Disposition",
        description="Item #1140 | Table HL70282",
    )

    rf1_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_5",
            "referral_category",
            "RF1.5",
        ),
        serialization_alias="RF1.5",
        title="Referral Category",
        description="Item #1141 | Table HL70284",
    )

    rf1_6: EI = Field(
        validation_alias=AliasChoices(
            "rf1_6",
            "originating_referral_identifier",
            "RF1.6",
        ),
        serialization_alias="RF1.6",
        title="Originating Referral Identifier",
        description="Item #1142",
    )

    rf1_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_7",
            "effective_date",
            "RF1.7",
        ),
        serialization_alias="RF1.7",
        title="Effective Date",
        description="Item #1143",
    )

    rf1_8: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_8",
            "expiration_date",
            "RF1.8",
        ),
        serialization_alias="RF1.8",
        title="Expiration Date",
        description="Item #1144",
    )

    rf1_9: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_9",
            "process_date",
            "RF1.9",
        ),
        serialization_alias="RF1.9",
        title="Process Date",
        description="Item #1145",
    )

    rf1_10: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_10",
            "referral_reason",
            "RF1.10",
        ),
        serialization_alias="RF1.10",
        title="Referral Reason",
        description="Item #1228 | Table HL70336",
    )

    rf1_11: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_11",
            "external_referral_identifier",
            "RF1.11",
        ),
        serialization_alias="RF1.11",
        title="External Referral Identifier",
        description="Item #1300",
    )

    model_config = {"populate_by_name": True}
