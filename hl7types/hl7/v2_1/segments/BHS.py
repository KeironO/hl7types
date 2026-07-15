"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: BHS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class BHS(HL7Model):
    """BATCH HEADER (S2.5.2).

    Attributes
    ----------
    bhs_1 : str
        BHS.1 - BATCH FIELD SEPARATOR (ST) R S2-40

    bhs_2 : str
        BHS.2 - BATCH ENCODING CHARACTERS (ST) R

    bhs_3 : str | None
        BHS.3 - BATCH SENDING APPLICATION (ST) O

    bhs_4 : str | None
        BHS.4 - BATCH SENDING FACILITY (ST) O

    bhs_5 : str | None
        BHS.5 - BATCH RECEIVING APPLICATION (ST) O

    bhs_6 : str | None
        BHS.6 - BATCH RECEIVING FACILITY (ST) O

    bhs_7 : str | None
        BHS.7 - BATCH CREATION DATE/TIME (TS) O

    bhs_8 : str | None
        BHS.8 - BATCH SECURITY (ST) O

    bhs_9 : str | None
        BHS.9 - BATCH NAME/ID/TYPE (ST) O

    bhs_10 : str | None
        BHS.10 - BATCH COMMENT (ST) O

    bhs_11 : str | None
        BHS.11 - BATCH CONTROL ID (ST) O

    bhs_12 : str | None
        BHS.12 - REFERENCE BATCH CONTROL ID (ST) O
    """

    bhs_1: str = Field(
        default="|",
        validation_alias=AliasChoices(
            "bhs_1",
            "batch_field_separator",
            "BHS.1",
        ),
        serialization_alias="BHS.1",
        title="BATCH FIELD SEPARATOR",
        description="R | Item #00685 | LEN:1",
    )

    bhs_2: str = Field(
        default="^~\\&",
        validation_alias=AliasChoices(
            "bhs_2",
            "batch_encoding_characters",
            "BHS.2",
        ),
        serialization_alias="BHS.2",
        title="BATCH ENCODING CHARACTERS",
        description="R | Item #00686 | LEN:3",
    )

    bhs_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_3",
            "batch_sending_application",
            "BHS.3",
        ),
        serialization_alias="BHS.3",
        title="BATCH SENDING APPLICATION",
        description="O | Item #00687 | LEN:15",
    )

    bhs_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_4",
            "batch_sending_facility",
            "BHS.4",
        ),
        serialization_alias="BHS.4",
        title="BATCH SENDING FACILITY",
        description="O | Item #00688 | LEN:20",
    )

    bhs_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_5",
            "batch_receiving_application",
            "BHS.5",
        ),
        serialization_alias="BHS.5",
        title="BATCH RECEIVING APPLICATION",
        description="O | Item #00689 | LEN:15",
    )

    bhs_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_6",
            "batch_receiving_facility",
            "BHS.6",
        ),
        serialization_alias="BHS.6",
        title="BATCH RECEIVING FACILITY",
        description="O | Item #00690 | LEN:20",
    )

    bhs_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_7",
            "batch_creation_date_time",
            "BHS.7",
        ),
        serialization_alias="BHS.7",
        title="BATCH CREATION DATE/TIME",
        description="O | Item #00655 | LEN:19",
    )

    bhs_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_8",
            "batch_security",
            "BHS.8",
        ),
        serialization_alias="BHS.8",
        title="BATCH SECURITY",
        description="O | Item #00691 | LEN:40",
    )

    bhs_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_9",
            "batch_name_id_type",
            "BHS.9",
        ),
        serialization_alias="BHS.9",
        title="BATCH NAME/ID/TYPE",
        description="O | Item #00656 | LEN:20",
    )

    bhs_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_10",
            "batch_comment",
            "BHS.10",
        ),
        serialization_alias="BHS.10",
        title="BATCH COMMENT",
        description="O | Item #00657 | LEN:80",
    )

    bhs_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_11",
            "batch_control_id",
            "BHS.11",
        ),
        serialization_alias="BHS.11",
        title="BATCH CONTROL ID",
        description="O | Item #00658 | LEN:20",
    )

    bhs_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_12",
            "reference_batch_control_id",
            "BHS.12",
        ),
        serialization_alias="BHS.12",
        title="REFERENCE BATCH CONTROL ID",
        description="O | Item #00659 | LEN:20",
    )

    model_config = {"populate_by_name": True}
