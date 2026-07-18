"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: TXA
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PPN import PPN
from ..datatypes.XCN import XCN

_RE_SI = re.compile(r'\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class TXA(HL7Model):
    """Transcription Document Header (S9.7.3).

    Attributes
    ----------
    txa_1 : str
        TXA.1 - Set ID- TXA (SI) R S9.7.3.1

    txa_2 : CWE
        TXA.2 - Document Type (CWE) R S9.7.3.2 | 0270 - Document Type

    txa_3 : str | None
        TXA.3 - Document Content Presentation (ID) C S9.7.3.3 | 0191 - Type of Referenced Data

    txa_4 : str | None
        TXA.4 - Activity Date/Time (DTM) O S9.7.3.4

    txa_5 : list[XCN] | None
        TXA.5 - Primary Activity Provider Code/Name (XCN) C rep S9.7.3.5

    txa_6 : str | None
        TXA.6 - Origination Date/Time (DTM) O S9.7.3.6

    txa_7 : str | None
        TXA.7 - Transcription Date/Time (DTM) C S9.7.3.7

    txa_8 : list[str] | None
        TXA.8 - Edit Date/Time (DTM) O rep S9.7.3.8

    txa_9 : list[XCN] | None
        TXA.9 - Originator Code/Name (XCN) O rep S9.7.3.9

    txa_10 : list[XCN] | None
        TXA.10 - Assigned Document Authenticator (XCN) O rep S9.7.3.10

    txa_11 : list[XCN] | None
        TXA.11 - Transcriptionist Code/Name (XCN) C rep S9.7.3.11

    txa_12 : EI
        TXA.12 - Unique Document Number (EI) R S9.7.3.12

    txa_13 : EI | None
        TXA.13 - Parent Document Number (EI) C S9.7.3.13

    txa_14 : list[EI] | None
        TXA.14 - Placer Order Number (EI) O rep S10.6.1.24

    txa_15 : EI | None
        TXA.15 - Filler Order Number (EI) O S10.6.1.25

    txa_16 : str | None
        TXA.16 - Unique Document File Name (ST) O S9.7.3.16

    txa_17 : str
        TXA.17 - Document Completion Status (ID) R S9.7.3.17 | 0271 - Document Completion Status

    txa_18 : str | None
        TXA.18 - Document Confidentiality Status (ID) O S9.7.3.18 | 0272 - Document Confidentiality Status

    txa_19 : str | None
        TXA.19 - Document Availability Status (ID) O S9.7.3.19 | 0273 - Document Availability Status

    txa_20 : str | None
        TXA.20 - Document Storage Status (ID) O S9.7.3.20 | 0275 - Document Storage Status

    txa_21 : str | None
        TXA.21 - Document Change Reason (ST) O S9.7.3.21

    txa_22 : list[PPN] | None
        TXA.22 - Authentication Person, Time Stamp (set) (PPN) C rep S9.7.3.22

    txa_23 : list[XCN] | None
        TXA.23 - Distributed Copies (Code and Name of Recipient(s) ) (XCN) O rep S9.7.3.23

    txa_24 : list[CWE] | None
        TXA.24 - Folder Assignment (CWE) O rep S9.7.3.24

    txa_25 : list[str] | None
        TXA.25 - Document Title (ST) O rep S9.7.3.25

    txa_26 : str | None
        TXA.26 - Agreed Due Date/Time (DTM) O S9.7.3.26
    """

    txa_1: str = Field(
        validation_alias=AliasChoices(
            "txa_1",
            "set_id_txa",
            "TXA.1",
        ),
        serialization_alias="TXA.1",
        title="Set ID- TXA",
        description="R | Item #00914 | LEN:4",
    )

    txa_2: CWE = Field(
        validation_alias=AliasChoices(
            "txa_2",
            "document_type",
            "TXA.2",
        ),
        serialization_alias="TXA.2",
        title="Document Type",
        description="R | Item #00915 | Table 0270 - Document Type",
    )

    txa_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_3",
            "document_content_presentation",
            "TXA.3",
        ),
        serialization_alias="TXA.3",
        title="Document Content Presentation",
        description="C | Item #00916 | Table 0191 - Type of Referenced Data",
    )

    txa_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_4",
            "activity_date_time",
            "TXA.4",
        ),
        serialization_alias="TXA.4",
        title="Activity Date/Time",
        description="O | Item #00917",
    )

    txa_5: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_5",
            "primary_activity_provider_code_name",
            "TXA.5",
        ),
        serialization_alias="TXA.5",
        title="Primary Activity Provider Code/Name",
        description="C | Item #00918",
    )

    txa_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_6",
            "origination_date_time",
            "TXA.6",
        ),
        serialization_alias="TXA.6",
        title="Origination Date/Time",
        description="O | Item #00919",
    )

    txa_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_7",
            "transcription_date_time",
            "TXA.7",
        ),
        serialization_alias="TXA.7",
        title="Transcription Date/Time",
        description="C | Item #00920",
    )

    txa_8: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_8",
            "edit_date_time",
            "TXA.8",
        ),
        serialization_alias="TXA.8",
        title="Edit Date/Time",
        description="O | Item #00921",
    )

    txa_9: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_9",
            "originator_code_name",
            "TXA.9",
        ),
        serialization_alias="TXA.9",
        title="Originator Code/Name",
        description="O | Item #00922",
    )

    txa_10: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_10",
            "assigned_document_authenticator",
            "TXA.10",
        ),
        serialization_alias="TXA.10",
        title="Assigned Document Authenticator",
        description="O | Item #00923",
    )

    txa_11: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_11",
            "transcriptionist_code_name",
            "TXA.11",
        ),
        serialization_alias="TXA.11",
        title="Transcriptionist Code/Name",
        description="C | Item #00924",
    )

    txa_12: EI = Field(
        validation_alias=AliasChoices(
            "txa_12",
            "unique_document_number",
            "TXA.12",
        ),
        serialization_alias="TXA.12",
        title="Unique Document Number",
        description="R | Item #00925",
    )

    txa_13: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_13",
            "parent_document_number",
            "TXA.13",
        ),
        serialization_alias="TXA.13",
        title="Parent Document Number",
        description="C | Item #00926",
    )

    txa_14: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_14",
            "placer_order_number",
            "TXA.14",
        ),
        serialization_alias="TXA.14",
        title="Placer Order Number",
        description="O | Item #00216",
    )

    txa_15: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_15",
            "filler_order_number",
            "TXA.15",
        ),
        serialization_alias="TXA.15",
        title="Filler Order Number",
        description="O | Item #00217",
    )

    txa_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_16",
            "unique_document_file_name",
            "TXA.16",
        ),
        serialization_alias="TXA.16",
        title="Unique Document File Name",
        description="O | Item #00927",
    )

    txa_17: str = Field(
        validation_alias=AliasChoices(
            "txa_17",
            "document_completion_status",
            "TXA.17",
        ),
        serialization_alias="TXA.17",
        title="Document Completion Status",
        description=(
            "R | Item #00928 | Table 0271 - Document Completion Status | LEN:2"
        ),
    )

    txa_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_18",
            "document_confidentiality_status",
            "TXA.18",
        ),
        serialization_alias="TXA.18",
        title="Document Confidentiality Status",
        description=(
            "O | Item #00929 | Table 0272 - Document Confidentiality Status | "
            "LEN:1"
        ),
    )

    txa_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_19",
            "document_availability_status",
            "TXA.19",
        ),
        serialization_alias="TXA.19",
        title="Document Availability Status",
        description=(
            "O | Item #00930 | Table 0273 - Document Availability Status | LEN:2"
        ),
    )

    txa_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_20",
            "document_storage_status",
            "TXA.20",
        ),
        serialization_alias="TXA.20",
        title="Document Storage Status",
        description=(
            "O | Item #00932 | Table 0275 - Document Storage Status | LEN:2"
        ),
    )

    txa_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_21",
            "document_change_reason",
            "TXA.21",
        ),
        serialization_alias="TXA.21",
        title="Document Change Reason",
        description="O | Item #00933",
    )

    txa_22: Optional[List[PPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_22",
            "authentication_person_time_stamp_set",
            "TXA.22",
        ),
        serialization_alias="TXA.22",
        title="Authentication Person, Time Stamp (set)",
        description="C | Item #00934",
    )

    txa_23: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_23",
            "distributed_copies_code_and_name_of_recipient_s",
            "TXA.23",
        ),
        serialization_alias="TXA.23",
        title="Distributed Copies (Code and Name of Recipient(s) )",
        description="O | Item #00935",
    )

    txa_24: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_24",
            "folder_assignment",
            "TXA.24",
        ),
        serialization_alias="TXA.24",
        title="Folder Assignment",
        description="O | Item #02378",
    )

    txa_25: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_25",
            "document_title",
            "TXA.25",
        ),
        serialization_alias="TXA.25",
        title="Document Title",
        description="O | Item #03301",
    )

    txa_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "txa_26",
            "agreed_due_date_time",
            "TXA.26",
        ),
        serialization_alias="TXA.26",
        title="Agreed Due Date/Time",
        description="O | Item #03302",
    )

    @field_validator("txa_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("txa_4", "txa_6", "txa_7", "txa_8", "txa_26", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
