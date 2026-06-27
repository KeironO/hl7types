"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: XAD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator, ValidationInfo
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from .CWE import CWE
from .EI import EI
from .SAD import SAD


class XAD(HL7Model):
    """HL7 v2 XAD data type.

    Attributes
    ----------
    xad_1 : SAD | None
        XAD.1 (opt) - Street Address (SAD)

    xad_2 : str | None
        XAD.2 (opt) - Other Designation (ST)

    xad_3 : str | None
        XAD.3 (opt) - City (ST)

    xad_4 : str | None
        XAD.4 (opt) - State or Province (ST)

    xad_5 : str | None
        XAD.5 (opt) - Zip or Postal Code (ST)

    xad_6 : str | None
        XAD.6 (opt) - Country (ID)

    xad_7 : str | None
        XAD.7 (opt) - Address Type (ID)

    xad_8 : str | None
        XAD.8 (opt) - Other Geographic Designation (ST)

    xad_9 : CWE | None
        XAD.9 (opt) - County/Parish Code (CWE)

    xad_10 : CWE | None
        XAD.10 (opt) - Census Tract (CWE)

    xad_11 : str | None
        XAD.11 (opt) - Address Representation Code (ID)

    xad_13 : str | None
        XAD.13 (opt) - Effective Date (DTM)

    xad_14 : str | None
        XAD.14 (opt) - Expiration Date (DTM)

    xad_15 : CWE | None
        XAD.15 (opt) - Expiration Reason (CWE)

    xad_16 : str | None
        XAD.16 (opt) - Temporary Indicator (ID)

    xad_17 : str | None
        XAD.17 (opt) - Bad Address Indicator (ID)

    xad_18 : str | None
        XAD.18 (opt) - Address Usage (ID)

    xad_19 : str | None
        XAD.19 (opt) - Addressee (ST)

    xad_20 : str | None
        XAD.20 (opt) - Comment (ST)

    xad_21 : str | None
        XAD.21 (opt) - Preference Order (NM)

    xad_22 : CWE | None
        XAD.22 (opt) - Protection Code (CWE)

    xad_23 : EI | None
        XAD.23 (opt) - Address Identifier (EI)
    """

    xad_1: Optional[SAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_1",
            "street_address",
            "XAD.1",
        ),
        serialization_alias="XAD.1",
        title="Street Address",
    )

    xad_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_2",
            "other_designation",
            "XAD.2",
        ),
        serialization_alias="XAD.2",
        title="Other Designation",
    )

    xad_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_3",
            "city",
            "XAD.3",
        ),
        serialization_alias="XAD.3",
        title="City",
    )

    xad_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_4",
            "state_or_province",
            "XAD.4",
        ),
        serialization_alias="XAD.4",
        title="State or Province",
    )

    xad_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_5",
            "zip_or_postal_code",
            "XAD.5",
        ),
        serialization_alias="XAD.5",
        title="Zip or Postal Code",
    )

    xad_6: Optional[str] = Field(
        default=None,
        max_length=3,
        validation_alias=AliasChoices(
            "xad_6",
            "country",
            "XAD.6",
        ),
        serialization_alias="XAD.6",
        title="Country",
    )

    xad_7: Optional[str] = Field(
        default=None,
        max_length=3,
        validation_alias=AliasChoices(
            "xad_7",
            "address_type",
            "XAD.7",
        ),
        serialization_alias="XAD.7",
        title="Address Type",
    )

    xad_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_8",
            "other_geographic_designation",
            "XAD.8",
        ),
        serialization_alias="XAD.8",
        title="Other Geographic Designation",
    )

    xad_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_9",
            "county_parish_code",
            "XAD.9",
        ),
        serialization_alias="XAD.9",
        title="County/Parish Code",
    )

    xad_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_10",
            "census_tract",
            "XAD.10",
        ),
        serialization_alias="XAD.10",
        title="Census Tract",
    )

    xad_11: Optional[str] = Field(
        default=None,
        max_length=1,
        validation_alias=AliasChoices(
            "xad_11",
            "address_representation_code",
            "XAD.11",
        ),
        serialization_alias="XAD.11",
        title="Address Representation Code",
    )

    xad_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_13",
            "effective_date",
            "XAD.13",
        ),
        serialization_alias="XAD.13",
        title="Effective Date",
    )

    xad_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_14",
            "expiration_date",
            "XAD.14",
        ),
        serialization_alias="XAD.14",
        title="Expiration Date",
    )

    xad_15: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_15",
            "expiration_reason",
            "XAD.15",
        ),
        serialization_alias="XAD.15",
        title="Expiration Reason",
    )

    xad_16: Optional[str] = Field(
        default=None,
        max_length=1,
        validation_alias=AliasChoices(
            "xad_16",
            "temporary_indicator",
            "XAD.16",
        ),
        serialization_alias="XAD.16",
        title="Temporary Indicator",
    )

    xad_17: Optional[str] = Field(
        default=None,
        max_length=1,
        validation_alias=AliasChoices(
            "xad_17",
            "bad_address_indicator",
            "XAD.17",
        ),
        serialization_alias="XAD.17",
        title="Bad Address Indicator",
    )

    xad_18: Optional[str] = Field(
        default=None,
        max_length=1,
        validation_alias=AliasChoices(
            "xad_18",
            "address_usage",
            "XAD.18",
        ),
        serialization_alias="XAD.18",
        title="Address Usage",
    )

    xad_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_19",
            "addressee",
            "XAD.19",
        ),
        serialization_alias="XAD.19",
        title="Addressee",
    )

    xad_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_20",
            "comment",
            "XAD.20",
        ),
        serialization_alias="XAD.20",
        title="Comment",
    )

    xad_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_21",
            "preference_order",
            "XAD.21",
        ),
        serialization_alias="XAD.21",
        title="Preference Order",
    )

    xad_22: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_22",
            "protection_code",
            "XAD.22",
        ),
        serialization_alias="XAD.22",
        title="Protection Code",
    )

    xad_23: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_23",
            "address_identifier",
            "XAD.23",
        ),
        serialization_alias="XAD.23",
        title="Address Identifier",
    )

    @field_validator("xad_13", "xad_14", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("xad_21", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
