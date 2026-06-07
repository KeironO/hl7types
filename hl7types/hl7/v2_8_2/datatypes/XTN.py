"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: XTN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from .CWE import CWE
from .EI import EI


class XTN(HL7Model):
    """HL7 v2 XTN data type.

    Attributes
    ----------
    xtn_2 : str | None
        XTN.2 (opt) - Telecommunication Use Code (ID)

    xtn_3 : str
        XTN.3 (req) - Telecommunication Equipment Type (ID)

    xtn_4 : str | None
        XTN.4 (opt) - Communication Address (ST)

    xtn_5 : str | None
        XTN.5 (opt) - Country Code (SNM)

    xtn_6 : str | None
        XTN.6 (opt) - Area/City Code (SNM)

    xtn_7 : str | None
        XTN.7 (opt) - Local Number (SNM)

    xtn_8 : str | None
        XTN.8 (opt) - Extension (SNM)

    xtn_9 : str | None
        XTN.9 (opt) - Any Text (ST)

    xtn_10 : str | None
        XTN.10 (opt) - Extension Prefix (ST)

    xtn_11 : str | None
        XTN.11 (opt) - Speed Dial Code (ST)

    xtn_12 : str | None
        XTN.12 (opt) - Unformatted Telephone number (ST)

    xtn_13 : str | None
        XTN.13 (opt) - Effective Start Date (DTM)

    xtn_14 : str | None
        XTN.14 (opt) - Expiration Date (DTM)

    xtn_15 : CWE | None
        XTN.15 (opt) - Expiration Reason (CWE)

    xtn_16 : CWE | None
        XTN.16 (opt) - Protection Code (CWE)

    xtn_17 : EI | None
        XTN.17 (opt) - Shared Telecommunication Identifier (EI)

    xtn_18 : str | None
        XTN.18 (opt) - Preference Order (NM)
    """

    xtn_2: Optional[str] = Field(
        default=None,
        max_length=3,
        validation_alias=AliasChoices(
            "xtn_2",
            "telecommunication_use_code",
            "XTN.2",
        ),
        serialization_alias="XTN.2",
        title="Telecommunication Use Code",
    )

    xtn_3: str = Field(
        max_length=8,
        validation_alias=AliasChoices(
            "xtn_3",
            "telecommunication_equipment_type",
            "XTN.3",
        ),
        serialization_alias="XTN.3",
        title="Telecommunication Equipment Type",
    )

    xtn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_4",
            "communication_address",
            "XTN.4",
        ),
        serialization_alias="XTN.4",
        title="Communication Address",
    )

    xtn_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_5",
            "country_code",
            "XTN.5",
        ),
        serialization_alias="XTN.5",
        title="Country Code",
    )

    xtn_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_6",
            "area_city_code",
            "XTN.6",
        ),
        serialization_alias="XTN.6",
        title="Area/City Code",
    )

    xtn_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_7",
            "local_number",
            "XTN.7",
        ),
        serialization_alias="XTN.7",
        title="Local Number",
    )

    xtn_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_8",
            "extension",
            "XTN.8",
        ),
        serialization_alias="XTN.8",
        title="Extension",
    )

    xtn_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_9",
            "any_text",
            "XTN.9",
        ),
        serialization_alias="XTN.9",
        title="Any Text",
    )

    xtn_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_10",
            "extension_prefix",
            "XTN.10",
        ),
        serialization_alias="XTN.10",
        title="Extension Prefix",
    )

    xtn_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_11",
            "speed_dial_code",
            "XTN.11",
        ),
        serialization_alias="XTN.11",
        title="Speed Dial Code",
    )

    xtn_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_12",
            "unformatted_telephone_number",
            "XTN.12",
        ),
        serialization_alias="XTN.12",
        title="Unformatted Telephone number",
    )

    xtn_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_13",
            "effective_start_date",
            "XTN.13",
        ),
        serialization_alias="XTN.13",
        title="Effective Start Date",
    )

    xtn_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_14",
            "expiration_date",
            "XTN.14",
        ),
        serialization_alias="XTN.14",
        title="Expiration Date",
    )

    xtn_15: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_15",
            "expiration_reason",
            "XTN.15",
        ),
        serialization_alias="XTN.15",
        title="Expiration Reason",
    )

    xtn_16: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_16",
            "protection_code",
            "XTN.16",
        ),
        serialization_alias="XTN.16",
        title="Protection Code",
    )

    xtn_17: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_17",
            "shared_telecommunication_identifier",
            "XTN.17",
        ),
        serialization_alias="XTN.17",
        title="Shared Telecommunication Identifier",
    )

    xtn_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_18",
            "preference_order",
            "XTN.18",
        ),
        serialization_alias="XTN.18",
        title="Preference Order",
    )

    @field_validator("xtn_13", "xtn_14", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    @field_validator("xtn_18", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
