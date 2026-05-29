"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: BHS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.TS import TS


class BHS(BaseModel):
    """HL7 v2 BHS segment.

    Attributes
    ----------
    bhs_1 : str
        BHS.1 (req) - Batch Field Separator (ST)

    bhs_2 : str
        BHS.2 (req) - Batch Encoding Characters (ST)

    bhs_3 : str | None
        BHS.3 (opt) - Batch Sending Application (ST)

    bhs_4 : str | None
        BHS.4 (opt) - Batch Sending Facility (ST)

    bhs_5 : str | None
        BHS.5 (opt) - Batch Receiving Application (ST)

    bhs_6 : str | None
        BHS.6 (opt) - Batch Receiving Facility (ST)

    bhs_7 : TS | None
        BHS.7 (opt) - Batch Creation Date/Time (TS)

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

    bhs_3: Optional[str] = Field(
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

    bhs_4: Optional[str] = Field(
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

    bhs_5: Optional[str] = Field(
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

    bhs_6: Optional[str] = Field(
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

    bhs_7: Optional[TS] = Field(
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

    model_config = {"populate_by_name": True}
