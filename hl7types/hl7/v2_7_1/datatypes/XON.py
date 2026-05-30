"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: XON
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CWE import CWE
from .HD import HD


class XON(HL7Model):
    """HL7 v2 XON data type.

    Attributes
    ----------
    xon_1 : str | None
        XON.1 (opt) - Organization Name (ST)

    xon_2 : CWE | None
        XON.2 (opt) - Organization Name Type Code (CWE)

    xon_4 : str | None
        XON.4 (opt) - Identifier Check Digit (NM)

    xon_5 : str | None
        XON.5 (opt) - Check Digit Scheme (ID)

    xon_6 : HD | None
        XON.6 (opt) - Assigning Authority (HD)

    xon_7 : str | None
        XON.7 (opt) - Identifier Type Code (ID)

    xon_8 : HD | None
        XON.8 (opt) - Assigning Facility (HD)

    xon_9 : str | None
        XON.9 (opt) - Name Representation Code (ID)

    xon_10 : str | None
        XON.10 (opt) - Organization Identifier (ST)
    """

    xon_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_1",
            "organization_name",
            "XON.1",
        ),
        serialization_alias="XON.1",
        title="Organization Name",
    )

    xon_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_2",
            "organization_name_type_code",
            "XON.2",
        ),
        serialization_alias="XON.2",
        title="Organization Name Type Code",
    )

    xon_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_4",
            "identifier_check_digit",
            "XON.4",
        ),
        serialization_alias="XON.4",
        title="Identifier Check Digit",
    )

    xon_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_5",
            "check_digit_scheme",
            "XON.5",
        ),
        serialization_alias="XON.5",
        title="Check Digit Scheme",
    )

    xon_6: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_6",
            "assigning_authority",
            "XON.6",
        ),
        serialization_alias="XON.6",
        title="Assigning Authority",
    )

    xon_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_7",
            "identifier_type_code",
            "XON.7",
        ),
        serialization_alias="XON.7",
        title="Identifier Type Code",
    )

    xon_8: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_8",
            "assigning_facility",
            "XON.8",
        ),
        serialization_alias="XON.8",
        title="Assigning Facility",
    )

    xon_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_9",
            "name_representation_code",
            "XON.9",
        ),
        serialization_alias="XON.9",
        title="Name Representation Code",
    )

    xon_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_10",
            "organization_identifier",
            "XON.10",
        ),
        serialization_alias="XON.10",
        title="Organization Identifier",
    )

    model_config = {"populate_by_name": True}
