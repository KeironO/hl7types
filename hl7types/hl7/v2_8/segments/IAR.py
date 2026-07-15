"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: IAR
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class IAR(HL7Model):
    """allergy reaction (S3.4.8).

    Attributes
    ----------
    iar_1 : CWE
        IAR.1 - Allergy Reaction Code (CWE) R S3.4.8.1

    iar_2 : CWE
        IAR.2 - Allergy Severity Code (CWE) R S3.4.8.2 | 0128 - Allergy Severity

    iar_3 : CWE | None
        IAR.3 - Sensitivity to Causative Agent Code (CWE) O S3.4.8.3 | 0436 - Sensitivity to Causative Agent Code

    iar_4 : str | None
        IAR.4 - Management (ST) O S3.4.8.4
    """

    iar_1: CWE = Field(
        validation_alias=AliasChoices(
            "iar_1",
            "allergy_reaction_code",
            "IAR.1",
        ),
        serialization_alias="IAR.1",
        title="Allergy Reaction Code",
        description="R | Item #03296",
    )

    iar_2: CWE = Field(
        validation_alias=AliasChoices(
            "iar_2",
            "allergy_severity_code",
            "IAR.2",
        ),
        serialization_alias="IAR.2",
        title="Allergy Severity Code",
        description="R | Item #03297 | Table 0128 - Allergy Severity",
    )

    iar_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iar_3",
            "sensitivity_to_causative_agent_code",
            "IAR.3",
        ),
        serialization_alias="IAR.3",
        title="Sensitivity to Causative Agent Code",
        description=(
            "O | Item #03298 | Table 0436 - Sensitivity to Causative Agent Code"
        ),
    )

    iar_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iar_4",
            "management",
            "IAR.4",
        ),
        serialization_alias="IAR.4",
        title="Management",
        description="O | Item #03299",
    )

    model_config = {"populate_by_name": True}
