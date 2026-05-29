"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: DMI
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.NR import NR


class DMI(BaseModel):
    """HL7 v2 DMI segment.

    Attributes
    ----------
    dmi_1 : CNE | None
        DMI.1 (opt) - Diagnostic Related Group (CNE)

    dmi_2 : CNE | None
        DMI.2 (opt) - Major Diagnostic Category (CNE)

    dmi_3 : NR | None
        DMI.3 (opt) - Lower and Upper Trim Points (NR)

    dmi_4 : str | None
        DMI.4 (opt) - Average Length of Stay (NM)

    dmi_5 : str | None
        DMI.5 (opt) - Relative Weight (NM)
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
        description="Item #382 | Table HL70055",
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
        description="Item #381 | Table HL70118",
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
        description="Item #2231",
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
        description="Item #2232",
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
        description="Item #2233",
    )

    model_config = {"populate_by_name": True}
