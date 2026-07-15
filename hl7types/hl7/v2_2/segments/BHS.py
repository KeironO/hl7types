"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: BHS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS


class BHS(HL7Model):
    """BATCH HEADER (S2.10.13).

    Attributes
    ----------
    bhs_1 : str
        BHS.1 - Batch Field Separator (ST) R S2.10.13.1

    bhs_2 : str
        BHS.2 - Batch Encoding Characters (ST) R S2.10.13.2

    bhs_3 : str | None
        BHS.3 - Batch Sending Application (ST) NA S2.10.13.3

    bhs_4 : str | None
        BHS.4 - Batch Sending Facility (ST) NA S2.10.13.4

    bhs_5 : str | None
        BHS.5 - Batch Receiving Application (ST) NA S2.10.13.5

    bhs_6 : str | None
        BHS.6 - Batch Receiving Facility (ST) NA S2.10.13.6

    bhs_7 : TS | None
        BHS.7 - Batch creation date / time (TS) NA S2.10.13.7

    bhs_8 : str | None
        BHS.8 - Batch Security (ST) NA S2.10.13.8

    bhs_9 : str | None
        BHS.9 - Batch name / ID / type (ST) NA S2.10.13.9

    bhs_10 : str | None
        BHS.10 - Batch Comment (ST) NA S2.10.13.10

    bhs_11 : str | None
        BHS.11 - Batch Control ID (ST) NA S2.10.13.11

    bhs_12 : str | None
        BHS.12 - Reference Batch Control ID (ST) NA S2.10.13.12
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
        description="R | Item #00082 | LEN:4",
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
        description="NA | Item #00083 | LEN:15",
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
        description="NA | Item #00084 | LEN:20",
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
        description="NA | Item #00085 | LEN:30",
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
        description="NA | Item #00086 | LEN:30",
    )

    bhs_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_7",
            "batch_creation_date_time",
            "BHS.7",
        ),
        serialization_alias="BHS.7",
        title="Batch creation date / time",
        description="NA | Item #00087",
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
        description="NA | Item #00088 | LEN:40",
    )

    bhs_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bhs_9",
            "batch_name_id_type",
            "BHS.9",
        ),
        serialization_alias="BHS.9",
        title="Batch name / ID / type",
        description="NA | Item #00089 | LEN:20",
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
        description="NA | Item #00090 | LEN:80",
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
        description="NA | Item #00091 | LEN:20",
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
        description="NA | Item #00092 | LEN:20",
    )

    model_config = {"populate_by_name": True}
