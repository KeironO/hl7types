"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
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
    """Referral Information (S11.6.1).

    Attributes
    ----------
    rf1_1 : CE | None
        RF1.1 - Referral Status (CE) O S11.6.1.1 | 0283 - Referral status

    rf1_2 : CE | None
        RF1.2 - Referral Priority (CE) O S11.6.1.2 | 0280 - Referral priority

    rf1_3 : CE | None
        RF1.3 - Referral Type (CE) O S11.6.1.3 | 0281 - Referral type

    rf1_4 : list[CE] | None
        RF1.4 - Referral Disposition (CE) O rep S11.6.1.4 | 0282 - Referral disposition

    rf1_5 : CE | None
        RF1.5 - Referral Category (CE) O S11.6.1.5 | 0284 - Referral category

    rf1_6 : EI
        RF1.6 - Originating Referral Identifier (EI) R S11.6.1.6

    rf1_7 : TS | None
        RF1.7 - Effective Date (TS) O S11.6.1.7

    rf1_8 : TS | None
        RF1.8 - Expiration Date (TS) O S11.6.1.8

    rf1_9 : TS | None
        RF1.9 - Process Date (TS) O S11.6.2.10

    rf1_10 : list[CE] | None
        RF1.10 - Referral Reason (CE) O rep S11.6.1.10 | 0336 - Referral reason

    rf1_11 : list[EI] | None
        RF1.11 - External Referral Identifier (EI) O rep S11.6.1.11
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
        description="O | Item #01137 | Table 0283 - Referral status",
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
        description="O | Item #01138 | Table 0280 - Referral priority",
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
        description="O | Item #01139 | Table 0281 - Referral type",
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
        description="O | Item #01140 | Table 0282 - Referral disposition",
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
        description="O | Item #01141 | Table 0284 - Referral category",
    )

    rf1_6: EI = Field(
        validation_alias=AliasChoices(
            "rf1_6",
            "originating_referral_identifier",
            "RF1.6",
        ),
        serialization_alias="RF1.6",
        title="Originating Referral Identifier",
        description="R | Item #01142",
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
        description="O | Item #01143",
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
        description="O | Item #01144",
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
        description="O | Item #01145",
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
        description="O | Item #01228 | Table 0336 - Referral reason",
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
        description="O | Item #01300",
    )

    model_config = {"populate_by_name": True}
