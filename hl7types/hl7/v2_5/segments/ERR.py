"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ERR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.ELD import ELD
from ..datatypes.ERL import ERL
from ..datatypes.TX import TX
from ..datatypes.XTN import XTN


class ERR(HL7Model):
    """HL7 v2 ERR segment.

    Attributes
    ----------
    err_1 : list[ELD] | None
        ERR.1 (opt, rep) - Error Code and Location (ELD)

    err_2 : list[ERL] | None
        ERR.2 (opt, rep) - Error Location (ERL)

    err_3 : CWE
        ERR.3 (req) - HL7 Error Code (CWE)

    err_4 : str
        ERR.4 (req) - Severity (ID)

    err_5 : CWE | None
        ERR.5 (opt) - Application Error Code (CWE)

    err_6 : list[str] | None
        ERR.6 (opt, rep) - Application Error Parameter (ST)

    err_7 : TX | None
        ERR.7 (opt) - Diagnostic Information (TX)

    err_8 : TX | None
        ERR.8 (opt) - User Message (TX)

    err_9 : list[str] | None
        ERR.9 (opt, rep) - Inform Person Indicator (IS)

    err_10 : CWE | None
        ERR.10 (opt) - Override Type (CWE)

    err_11 : list[CWE] | None
        ERR.11 (opt, rep) - Override Reason Code (CWE)

    err_12 : list[XTN] | None
        ERR.12 (opt, rep) - Help Desk Contact Point (XTN)
    """

    err_1: Optional[List[ELD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_1",
            "error_code_and_location",
            "ERR.1",
        ),
        serialization_alias="ERR.1",
        title="Error Code and Location",
        description="Item #24",
    )

    err_2: Optional[List[ERL]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_2",
            "error_location",
            "ERR.2",
        ),
        serialization_alias="ERR.2",
        title="Error Location",
        description="Item #1812",
    )

    err_3: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "err_3",
            "hl7_error_code",
            "ERR.3",
        ),
        serialization_alias="ERR.3",
        title="HL7 Error Code",
        description="Item #1813 | Table HL70357",
    )

    err_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "err_4",
            "severity",
            "ERR.4",
        ),
        serialization_alias="ERR.4",
        title="Severity",
        description="Item #1814 | Table HL70516",
    )

    err_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_5",
            "application_error_code",
            "ERR.5",
        ),
        serialization_alias="ERR.5",
        title="Application Error Code",
        description="Item #1815 | Table HL70533",
    )

    err_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_6",
            "application_error_parameter",
            "ERR.6",
        ),
        serialization_alias="ERR.6",
        title="Application Error Parameter",
        description="Item #1816",
    )

    err_7: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_7",
            "diagnostic_information",
            "ERR.7",
        ),
        serialization_alias="ERR.7",
        title="Diagnostic Information",
        description="Item #1817",
    )

    err_8: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_8",
            "user_message",
            "ERR.8",
        ),
        serialization_alias="ERR.8",
        title="User Message",
        description="Item #1818",
    )

    err_9: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_9",
            "inform_person_indicator",
            "ERR.9",
        ),
        serialization_alias="ERR.9",
        title="Inform Person Indicator",
        description="Item #1819 | Table HL70517",
    )

    err_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_10",
            "override_type",
            "ERR.10",
        ),
        serialization_alias="ERR.10",
        title="Override Type",
        description="Item #1820 | Table HL70518",
    )

    err_11: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_11",
            "override_reason_code",
            "ERR.11",
        ),
        serialization_alias="ERR.11",
        title="Override Reason Code",
        description="Item #1821 | Table HL70519",
    )

    err_12: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_12",
            "help_desk_contact_point",
            "ERR.12",
        ),
        serialization_alias="ERR.12",
        title="Help Desk Contact Point",
        description="Item #1822",
    )

    model_config = {"populate_by_name": True}
