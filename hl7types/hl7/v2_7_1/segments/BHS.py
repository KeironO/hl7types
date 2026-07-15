"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: BHS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.HD import HD


class BHS(HL7Model):
    """Batch Header (S2.14.2).

    Attributes
    ----------
    bhs_1 : str
        BHS.1 - Batch Field Separator (ST) R S2.14.2.1

    bhs_2 : str
        BHS.2 - Batch Encoding Characters (ST) R S2.14.2.2

    bhs_3 : HD | None
        BHS.3 - Batch Sending Application (HD) O S2.14.2.3

    bhs_4 : HD | None
        BHS.4 - Batch Sending Facility (HD) O S2.14.2.4

    bhs_5 : HD | None
        BHS.5 - Batch Receiving Application (HD) O S2.14.2.5

    bhs_6 : HD | None
        BHS.6 - Batch Receiving Facility (HD) O S2.14.2.6

    bhs_7 : str | None
        BHS.7 - Batch Creation Date/Time (DTM) O S2.14.2.7

    bhs_8 : str | None
        BHS.8 - Batch Security (ST) O S2.14.2.8

    bhs_9 : str | None
        BHS.9 - Batch Name/ID/Type (ST) O S2.14.2.9

    bhs_10 : str | None
        BHS.10 - Batch Comment (ST) O S2.14.2.10

    bhs_11 : str | None
        BHS.11 - Batch Control ID (ST) O S2.14.2.11

    bhs_12 : str | None
        BHS.12 - Reference Batch Control ID (ST) O S2.14.2.12

    bhs_13 : HD | None
        BHS.13 - Batch Sending Network Address (HD) O S2.14.2.13

    bhs_14 : HD | None
        BHS.14 - Batch Receiving Network Address (HD) O S2.14.2.14
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
        description="R | Item #00081 | LEN:1",
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
        description="R | Item #00082 | LEN:5",
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
        description="O | Item #00083",
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
        description="O | Item #00084",
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
        description="O | Item #00085",
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
        description="O | Item #00086",
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
        description="O | Item #00087",
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
        description="O | Item #00088",
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
        description="O | Item #00089",
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
        description="O | Item #00090",
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
        description="O | Item #00091",
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
        description="O | Item #00092",
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
        description="O | Item #02271",
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
        description="O | Item #02272",
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
