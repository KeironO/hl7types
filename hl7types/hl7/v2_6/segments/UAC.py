"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: UAC
Type: Segment
"""
from __future__ import annotations

from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.ED import ED


class UAC(HL7Model):
    """User Authentication Credential Segment (S2.14.13).

    Attributes
    ----------
    uac_1 : CWE
        UAC.1 - User Authentication Credential Type Code (CWE) R S2.14.13.1 | 0615 - User Authentication Credential Type Code

    uac_2 : ED
        UAC.2 - User Authentication Credential (ED) R S2.14.13.2
    """

    uac_1: CWE = Field(
        validation_alias=AliasChoices(
            "uac_1",
            "user_authentication_credential_type_code",
            "UAC.1",
        ),
        serialization_alias="UAC.1",
        title="User Authentication Credential Type Code",
        description=(
            "R | Item #02267 | Table 0615 - User Authentication Credential Type "
            "Code"
        ),
    )

    uac_2: ED = Field(
        validation_alias=AliasChoices(
            "uac_2",
            "user_authentication_credential",
            "UAC.2",
        ),
        serialization_alias="UAC.2",
        title="User Authentication Credential",
        description="R | Item #02268",
    )

    model_config = ConfigDict(populate_by_name=True)
