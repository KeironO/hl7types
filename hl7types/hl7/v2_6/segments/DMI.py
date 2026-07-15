"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: DMI
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.NR import NR


class DMI(HL7Model):
    """DRG Master File Information (S8.13.2).

    Attributes
    ----------
    dmi_1 : CNE | None
        DMI.1 - Diagnostic Related Group (CNE) O S6.5.3.1 | 0055 - Diagnosis related group

    dmi_2 : CNE | None
        DMI.2 - Major Diagnostic Category (CNE) C S8.13.2.2 | 0118 - Major Diagnostic Category

    dmi_3 : NR | None
        DMI.3 - Lower and Upper Trim Points (NR) C S8.13.2.3

    dmi_4 : str | None
        DMI.4 - Average Length of Stay (NM) C S8.13.2.4

    dmi_5 : str | None
        DMI.5 - Relative Weight (NM) C S8.13.2.5
    """

    dmi_1: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dmi_1",
            "diagnostic_related_group",
            "DMI.1",
        ),
        serialization_alias="DMI.1",
        title="Diagnostic Related Group",
        description="O | Item #00382 | Table 0055 - Diagnosis related group",
    )

    dmi_2: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dmi_2",
            "major_diagnostic_category",
            "DMI.2",
        ),
        serialization_alias="DMI.2",
        title="Major Diagnostic Category",
        description="C | Item #00381 | Table 0118 - Major Diagnostic Category",
    )

    dmi_3: Optional[NR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dmi_3",
            "lower_and_upper_trim_points",
            "DMI.3",
        ),
        serialization_alias="DMI.3",
        title="Lower and Upper Trim Points",
        description="C | Item #02231",
    )

    dmi_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dmi_4",
            "average_length_of_stay",
            "DMI.4",
        ),
        serialization_alias="DMI.4",
        title="Average Length of Stay",
        description="C | Item #02232 | LEN:5",
    )

    dmi_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dmi_5",
            "relative_weight",
            "DMI.5",
        ),
        serialization_alias="DMI.5",
        title="Relative Weight",
        description="C | Item #02233 | LEN:7",
    )

    @field_validator("dmi_4", "dmi_5", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
