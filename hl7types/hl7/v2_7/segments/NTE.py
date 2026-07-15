"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: NTE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.XCN import XCN


class NTE(HL7Model):
    """Notes and Comments (S2.14.10).

    Attributes
    ----------
    nte_1 : str | None
        NTE.1 - Set ID - NTE (SI) O S2.14.10.1

    nte_2 : str | None
        NTE.2 - Source of Comment (ID) O S2.14.10.2 | 0105 - Source of Comment

    nte_3 : list[str] | None
        NTE.3 - Comment (FT) O rep S2.14.10.3

    nte_4 : CWE | None
        NTE.4 - Comment Type (CWE) O S2.14.10.4 | 0364 - Comment Type

    nte_5 : XCN | None
        NTE.5 - Entered By (XCN) O S2.14.10.5

    nte_6 : str | None
        NTE.6 - Entered Date/Time (DTM) O S2.14.10.6

    nte_7 : str | None
        NTE.7 - Effective Start Date (DTM) O S2.14.10.7

    nte_8 : str | None
        NTE.8 - Expiration Date (DTM) O S2.14.10.8
    """

    nte_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_1",
            "set_id_nte",
            "NTE.1",
        ),
        serialization_alias="NTE.1",
        title="Set ID - NTE",
        description="O | Item #00096",
    )

    nte_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_2",
            "source_of_comment",
            "NTE.2",
        ),
        serialization_alias="NTE.2",
        title="Source of Comment",
        description="O | Item #00097 | Table 0105 - Source of Comment | LEN:1",
    )

    nte_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_3",
            "comment",
            "NTE.3",
        ),
        serialization_alias="NTE.3",
        title="Comment",
        description="O | Item #00098",
    )

    nte_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_4",
            "comment_type",
            "NTE.4",
        ),
        serialization_alias="NTE.4",
        title="Comment Type",
        description="O | Item #01318 | Table 0364 - Comment Type",
    )

    nte_5: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_5",
            "entered_by",
            "NTE.5",
        ),
        serialization_alias="NTE.5",
        title="Entered By",
        description="O | Item #00224",
    )

    nte_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_6",
            "entered_date_time",
            "NTE.6",
        ),
        serialization_alias="NTE.6",
        title="Entered Date/Time",
        description="O | Item #00661",
    )

    nte_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_7",
            "effective_start_date",
            "NTE.7",
        ),
        serialization_alias="NTE.7",
        title="Effective Start Date",
        description="O | Item #01004",
    )

    nte_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_8",
            "expiration_date",
            "NTE.8",
        ),
        serialization_alias="NTE.8",
        title="Expiration Date",
        description="O | Item #02185",
    )

    @field_validator("nte_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("nte_6", "nte_7", "nte_8", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
