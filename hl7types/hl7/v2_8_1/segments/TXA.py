"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: TXA
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PPN import PPN
from ..datatypes.XCN import XCN


class TXA(BaseModel):
    """HL7 v2 TXA segment."""

    txa_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "txa_1",
            "set_id_txa",
            "TXA.1",
        ),
        serialization_alias="TXA.1",
        title="Set ID- TXA",
        description="Item #914",
    )

    txa_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "txa_2",
            "document_type",
            "TXA.2",
        ),
        serialization_alias="TXA.2",
        title="Document Type",
        description="Item #915 | Table HL70270",
    )

    txa_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_3",
            "document_content_presentation",
            "TXA.3",
        ),
        serialization_alias="TXA.3",
        title="Document Content Presentation",
        description="Item #916 | Table HL70191",
    )

    txa_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_4",
            "activity_date_time",
            "TXA.4",
        ),
        serialization_alias="TXA.4",
        title="Activity Date/Time",
        description="Item #917",
    )

    txa_5: list[XCN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_5",
            "primary_activity_provider_code_name",
            "TXA.5",
        ),
        serialization_alias="TXA.5",
        title="Primary Activity Provider Code/Name",
        description="Item #918",
    )

    txa_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_6",
            "origination_date_time",
            "TXA.6",
        ),
        serialization_alias="TXA.6",
        title="Origination Date/Time",
        description="Item #919",
    )

    txa_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_7",
            "transcription_date_time",
            "TXA.7",
        ),
        serialization_alias="TXA.7",
        title="Transcription Date/Time",
        description="Item #920",
    )

    txa_8: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_8",
            "edit_date_time",
            "TXA.8",
        ),
        serialization_alias="TXA.8",
        title="Edit Date/Time",
        description="Item #921",
    )

    txa_9: list[XCN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_9",
            "originator_code_name",
            "TXA.9",
        ),
        serialization_alias="TXA.9",
        title="Originator Code/Name",
        description="Item #922",
    )

    txa_10: list[XCN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_10",
            "assigned_document_authenticator",
            "TXA.10",
        ),
        serialization_alias="TXA.10",
        title="Assigned Document Authenticator",
        description="Item #923",
    )

    txa_11: list[XCN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_11",
            "transcriptionist_code_name",
            "TXA.11",
        ),
        serialization_alias="TXA.11",
        title="Transcriptionist Code/Name",
        description="Item #924",
    )

    txa_12: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "txa_12",
            "unique_document_number",
            "TXA.12",
        ),
        serialization_alias="TXA.12",
        title="Unique Document Number",
        description="Item #925",
    )

    txa_13: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_13",
            "parent_document_number",
            "TXA.13",
        ),
        serialization_alias="TXA.13",
        title="Parent Document Number",
        description="Item #926",
    )

    txa_14: list[EI] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_14",
            "placer_order_number",
            "TXA.14",
        ),
        serialization_alias="TXA.14",
        title="Placer Order Number",
        description="Item #216",
    )

    txa_15: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_15",
            "filler_order_number",
            "TXA.15",
        ),
        serialization_alias="TXA.15",
        title="Filler Order Number",
        description="Item #217",
    )

    txa_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_16",
            "unique_document_file_name",
            "TXA.16",
        ),
        serialization_alias="TXA.16",
        title="Unique Document File Name",
        description="Item #927",
    )

    txa_17: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "txa_17",
            "document_completion_status",
            "TXA.17",
        ),
        serialization_alias="TXA.17",
        title="Document Completion Status",
        description="Item #928 | Table HL70271",
    )

    txa_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_18",
            "document_confidentiality_status",
            "TXA.18",
        ),
        serialization_alias="TXA.18",
        title="Document Confidentiality Status",
        description="Item #929 | Table HL70272",
    )

    txa_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_19",
            "document_availability_status",
            "TXA.19",
        ),
        serialization_alias="TXA.19",
        title="Document Availability Status",
        description="Item #930 | Table HL70273",
    )

    txa_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_20",
            "document_storage_status",
            "TXA.20",
        ),
        serialization_alias="TXA.20",
        title="Document Storage Status",
        description="Item #932 | Table HL70275",
    )

    txa_21: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_21",
            "document_change_reason",
            "TXA.21",
        ),
        serialization_alias="TXA.21",
        title="Document Change Reason",
        description="Item #933",
    )

    txa_22: list[PPN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_22",
            "authentication_person_time_stamp_set",
            "TXA.22",
        ),
        serialization_alias="TXA.22",
        title="Authentication Person, Time Stamp (set)",
        description="Item #934",
    )

    txa_23: list[XCN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_23",
            "distributed_copies_code_and_name_of_recipient_s",
            "TXA.23",
        ),
        serialization_alias="TXA.23",
        title="Distributed Copies (Code and Name of Recipient(s) )",
        description="Item #935",
    )

    txa_24: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_24",
            "folder_assignment",
            "TXA.24",
        ),
        serialization_alias="TXA.24",
        title="Folder Assignment",
        description="Item #2378",
    )

    txa_25: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_25",
            "document_title",
            "TXA.25",
        ),
        serialization_alias="TXA.25",
        title="Document Title",
        description="Item #3301",
    )

    txa_26: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_26",
            "agreed_due_date_time",
            "TXA.26",
        ),
        serialization_alias="TXA.26",
        title="Agreed Due Date/Time",
        description="Item #3302",
    )

    model_config = {"populate_by_name": True}
