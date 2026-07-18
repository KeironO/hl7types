"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ERR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.ERL import ERL
from ..datatypes.XTN import XTN


class ERR(HL7Model):
    """Error (S2.14.5).

    Attributes
    ----------
    err_2 : list[ERL] | None
        ERR.2 - Error Location (ERL) O rep S2.14.5.2

    err_3 : CWE
        ERR.3 - HL7 Error Code (CWE) R S2.14.5.3 | 0357 - Message Error Condition Codes

    err_4 : str
        ERR.4 - Severity (ID) R S2.14.5.4 | 0516 - Error Severity

    err_5 : CWE | None
        ERR.5 - Application Error Code (CWE) O S2.14.5.5 | 0533 - Application Error Code

    err_6 : list[str] | None
        ERR.6 - Application Error Parameter (ST) O rep S2.14.5.6

    err_7 : str | None
        ERR.7 - Diagnostic Information (TX) O S2.14.5.7

    err_8 : str | None
        ERR.8 - User Message (TX) O S2.14.5.8

    err_9 : list[CWE] | None
        ERR.9 - Inform Person Indicator (CWE) O rep S2.14.5.9 | 0517 - Inform Person Code

    err_10 : CWE | None
        ERR.10 - Override Type (CWE) O S2.14.5.10 | 0518 - Override Type

    err_11 : list[CWE] | None
        ERR.11 - Override Reason Code (CWE) O rep S2.14.5.11 | 0519 - Override Reason

    err_12 : list[XTN] | None
        ERR.12 - Help Desk Contact Point (XTN) O rep S2.14.5.12
    """

    err_2: Optional[List[ERL]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_2",
            "error_location",
            "ERR.2",
        ),
        serialization_alias="ERR.2",
        title="Error Location",
        description="O | Item #01812",
    )

    err_3: CWE = Field(
        validation_alias=AliasChoices(
            "err_3",
            "hl7_error_code",
            "ERR.3",
        ),
        serialization_alias="ERR.3",
        title="HL7 Error Code",
        description=(
            "R | Item #01813 | Table 0357 - Message Error Condition Codes"
        ),
    )

    err_4: str = Field(
        validation_alias=AliasChoices(
            "err_4",
            "severity",
            "ERR.4",
        ),
        serialization_alias="ERR.4",
        title="Severity",
        description="R | Item #01814 | Table 0516 - Error Severity | LEN:1",
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
        description="O | Item #01815 | Table 0533 - Application Error Code",
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
        description="O | Item #01816",
    )

    err_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_7",
            "diagnostic_information",
            "ERR.7",
        ),
        serialization_alias="ERR.7",
        title="Diagnostic Information",
        description="O | Item #01817",
    )

    err_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_8",
            "user_message",
            "ERR.8",
        ),
        serialization_alias="ERR.8",
        title="User Message",
        description="O | Item #01818",
    )

    err_9: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_9",
            "inform_person_indicator",
            "ERR.9",
        ),
        serialization_alias="ERR.9",
        title="Inform Person Indicator",
        description="O | Item #01819 | Table 0517 - Inform Person Code",
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
        description="O | Item #01820 | Table 0518 - Override Type",
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
        description="O | Item #01821 | Table 0519 - Override Reason",
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
        description="O | Item #01822",
    )

    model_config = ConfigDict(populate_by_name=True)
