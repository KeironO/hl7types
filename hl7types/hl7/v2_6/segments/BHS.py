"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: BHS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.HD import HD


class BHS(HL7Model):
    """HL7 v2 BHS segment.

    Attributes
    ----------
    bhs_1 : str
        BHS.1 (req) - Batch Field Separator (ST)

    bhs_2 : str
        BHS.2 (req) - Batch Encoding Characters (ST)

    bhs_3 : HD | None
        BHS.3 (opt) - Batch Sending Application (HD)

    bhs_4 : HD | None
        BHS.4 (opt) - Batch Sending Facility (HD)

    bhs_5 : HD | None
        BHS.5 (opt) - Batch Receiving Application (HD)

    bhs_6 : HD | None
        BHS.6 (opt) - Batch Receiving Facility (HD)

    bhs_7 : str | None
        BHS.7 (opt) - Batch Creation Date/Time (DTM)

    bhs_8 : str | None
        BHS.8 (opt) - Batch Security (ST)

    bhs_9 : str | None
        BHS.9 (opt) - Batch Name/ID/Type (ST)

    bhs_10 : str | None
        BHS.10 (opt) - Batch Comment (ST)

    bhs_11 : str | None
        BHS.11 (opt) - Batch Control ID (ST)

    bhs_12 : str | None
        BHS.12 (opt) - Reference Batch Control ID (ST)

    bhs_13 : HD | None
        BHS.13 (opt) - Batch Sending Network Address (HD)

    bhs_14 : HD | None
        BHS.14 (opt) - Batch Receiving Network Address (HD)
    """

    bhs_1: str = Field(
        default="|",
        validation_alias=AliasChoices(
            "bhs_1",
            "batch_field_separator",
            "BHS.1",
        ),
        serialization_alias="BHS.1",
        title="Batch Field Separator",
        description="Item #81",
    )

    bhs_2: str = Field(
        default="^~\\&",
        validation_alias=AliasChoices(
            "bhs_2",
            "batch_encoding_characters",
            "BHS.2",
        ),
        serialization_alias="BHS.2",
        title="Batch Encoding Characters",
        description="Item #82",
    )

    bhs_3: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_3",
            "batch_sending_application",
            "BHS.3",
        ),
        serialization_alias="BHS.3",
        title="Batch Sending Application",
        description="Item #83",
    )

    bhs_4: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_4",
            "batch_sending_facility",
            "BHS.4",
        ),
        serialization_alias="BHS.4",
        title="Batch Sending Facility",
        description="Item #84",
    )

    bhs_5: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_5",
            "batch_receiving_application",
            "BHS.5",
        ),
        serialization_alias="BHS.5",
        title="Batch Receiving Application",
        description="Item #85",
    )

    bhs_6: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_6",
            "batch_receiving_facility",
            "BHS.6",
        ),
        serialization_alias="BHS.6",
        title="Batch Receiving Facility",
        description="Item #86",
    )

    bhs_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_7",
            "batch_creation_date_time",
            "BHS.7",
        ),
        serialization_alias="BHS.7",
        title="Batch Creation Date/Time",
        description="Item #87",
    )

    bhs_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_8",
            "batch_security",
            "BHS.8",
        ),
        serialization_alias="BHS.8",
        title="Batch Security",
        description="Item #88",
    )

    bhs_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_9",
            "batch_name_id_type",
            "BHS.9",
        ),
        serialization_alias="BHS.9",
        title="Batch Name/ID/Type",
        description="Item #89",
    )

    bhs_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_10",
            "batch_comment",
            "BHS.10",
        ),
        serialization_alias="BHS.10",
        title="Batch Comment",
        description="Item #90",
    )

    bhs_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_11",
            "batch_control_id",
            "BHS.11",
        ),
        serialization_alias="BHS.11",
        title="Batch Control ID",
        description="Item #91",
    )

    bhs_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_12",
            "reference_batch_control_id",
            "BHS.12",
        ),
        serialization_alias="BHS.12",
        title="Reference Batch Control ID",
        description="Item #92",
    )

    bhs_13: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_13",
            "batch_sending_network_address",
            "BHS.13",
        ),
        serialization_alias="BHS.13",
        title="Batch Sending Network Address",
        description="Item #2271",
    )

    bhs_14: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_14",
            "batch_receiving_network_address",
            "BHS.14",
        ),
        serialization_alias="BHS.14",
        title="Batch Receiving Network Address",
        description="Item #2272",
    )

    @field_validator("bhs_7", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
