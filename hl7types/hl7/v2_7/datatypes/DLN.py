"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: DLN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CWE import CWE


class DLN(HL7Model):
    """HL7 v2 DLN data type.

    Attributes
    ----------
    dln_1 : str
        DLN.1 (req) - License Number (ST)

    dln_2 : CWE | None
        DLN.2 (opt) - Issuing State, Province, Country (CWE)

    dln_3 : str | None
        DLN.3 (opt) - Expiration Date (DT)
    """

    dln_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "dln_1",
            "license_number",
            "DLN.1",
        ),
        serialization_alias="DLN.1",
        title="License Number",
    )

    dln_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dln_2",
            "issuing_state_province_country",
            "DLN.2",
        ),
        serialization_alias="DLN.2",
        title="Issuing State, Province, Country",
    )

    dln_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dln_3",
            "expiration_date",
            "DLN.3",
        ),
        serialization_alias="DLN.3",
        title="Expiration Date",
    )

    model_config = {"populate_by_name": True}
