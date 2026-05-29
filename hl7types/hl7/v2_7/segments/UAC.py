"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: UAC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.ED import ED


class UAC(BaseModel):
    """HL7 v2 UAC segment.

    Attributes
    ----------
    uac_1 : CWE
        UAC.1 (req) - User Authentication Credential Type Code (CWE)

    uac_2 : ED
        UAC.2 (req) - User Authentication Credential (ED)
    """

    uac_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "uac_1",
            "user_authentication_credential_type_code",
            "UAC.1",
        ),
        serialization_alias="UAC.1",
        title="User Authentication Credential Type Code",
        description="Item #2267 | Table HL70615",
    )

    uac_2: ED = Field(
        default=...,
        validation_alias=AliasChoices(
            "uac_2",
            "user_authentication_credential",
            "UAC.2",
        ),
        serialization_alias="UAC.2",
        title="User Authentication Credential",
        description="Item #2268",
    )

    model_config = {"populate_by_name": True}
