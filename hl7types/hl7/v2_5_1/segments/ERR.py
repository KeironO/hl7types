"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ERR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.ELD import ELD
from ..datatypes.ERL import ERL
from ..datatypes.XTN import XTN


class ERR(HL7Model):
    """Error (S2.15.5).

    Attributes
    ----------
    err_1 : list[ELD] | None
        ERR.1 - Error Code and Location (ELD) O rep S2.15.5.1

    err_2 : list[ERL] | None
        ERR.2 - Error Location (ERL) O rep S2.15.5.2

    err_3 : CWE
        ERR.3 - HL7 Error Code (CWE) R S2.15.5.3 | 0357 - Message error condition codes

    err_4 : str
        ERR.4 - Severity (ID) R S2.15.5.4 | 0516 - Error severity

    err_5 : CWE | None
        ERR.5 - Application Error Code (CWE) O S2.15.5.5 | 0533 - Application error code

    err_6 : list[str] | None
        ERR.6 - Application Error Parameter (ST) O rep S2.15.5.6

    err_7 : str | None
        ERR.7 - Diagnostic Information (TX) O S2.15.5.7

    err_8 : str | None
        ERR.8 - User Message (TX) O S2.15.5.8

    err_9 : list[str] | None
        ERR.9 - Inform Person Indicator (IS) O rep S2.15.5.9 | 0517 - Inform person code

    err_10 : CWE | None
        ERR.10 - Override Type (CWE) O S2.15.5.10 | 0518 - Override type

    err_11 : list[CWE] | None
        ERR.11 - Override Reason Code (CWE) O rep S2.15.5.11 | 0519 - Override reason

    err_12 : list[XTN] | None
        ERR.12 - Help Desk Contact Point (XTN) O rep S2.15.5.12
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
        description="O | Item #00024",
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
            "R | Item #01813 | Table 0357 - Message error condition codes"
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
        description="R | Item #01814 | Table 0516 - Error severity | LEN:2",
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
        description="O | Item #01815 | Table 0533 - Application error code",
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
        description="O | Item #01816 | LEN:80",
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

    err_9: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "err_9",
            "inform_person_indicator",
            "ERR.9",
        ),
        serialization_alias="ERR.9",
        title="Inform Person Indicator",
        description=(
            "O | Item #01819 | Table 0517 - Inform person code | LEN:20"
        ),
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
        description="O | Item #01820 | Table 0518 - Override type",
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
        description="O | Item #01821 | Table 0519 - Override reason",
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
