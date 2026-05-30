"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: XON
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .HD import HD


class XON(HL7Model):
    """HL7 v2 XON data type.

    Attributes
    ----------
    xon_1 : str | None
        XON.1 (opt) - organization name (ST)

    xon_2 : str | None
        XON.2 (opt) - organization name type code (IS)

    xon_3 : str | None
        XON.3 (opt) - ID number (NM) (NM)

    xon_4 : str | None
        XON.4 (opt) - check digit (NM)

    xon_5 : str | None
        XON.5 (opt) - code identifying the check digit scheme employed (ID)

    xon_6 : HD | None
        XON.6 (opt) - assigning authority (HD)

    xon_7 : str | None
        XON.7 (opt) - identifier type code (IS)

    xon_8 : HD | None
        XON.8 (opt) - assigning facility ID (HD)

    xon_9 : str | None
        XON.9 (opt) - Name Representation code (ID)
    """

    xon_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_1",
            "organization_name",
            "XON.1",
        ),
        serialization_alias="XON.1",
        title="organization name",
    )

    xon_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_2",
            "organization_name_type_code",
            "XON.2",
        ),
        serialization_alias="XON.2",
        title="organization name type code",
    )

    xon_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_3",
            "id_number_nm",
            "XON.3",
        ),
        serialization_alias="XON.3",
        title="ID number (NM)",
    )

    xon_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_4",
            "check_digit",
            "XON.4",
        ),
        serialization_alias="XON.4",
        title="check digit",
    )

    xon_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_5",
            "code_identifying_the_check_digit_scheme_employed",
            "XON.5",
        ),
        serialization_alias="XON.5",
        title="code identifying the check digit scheme employed",
    )

    xon_6: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_6",
            "assigning_authority",
            "XON.6",
        ),
        serialization_alias="XON.6",
        title="assigning authority",
    )

    xon_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_7",
            "identifier_type_code",
            "XON.7",
        ),
        serialization_alias="XON.7",
        title="identifier type code",
    )

    xon_8: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_8",
            "assigning_facility_id",
            "XON.8",
        ),
        serialization_alias="XON.8",
        title="assigning facility ID",
    )

    xon_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_9",
            "name_representation_code",
            "XON.9",
        ),
        serialization_alias="XON.9",
        title="Name Representation code",
    )

    model_config = {"populate_by_name": True}
