"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: CSU
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CSU(BaseModel):
    """HL7 v2 CSU data type.

    Attributes
    ----------
    csu_1 : str | None
        CSU.1 (opt) - Channel Sensitivity (NM)

    csu_2 : str | None
        CSU.2 (opt) - Unit of Measure Identifier (ST)

    csu_3 : str | None
        CSU.3 (opt) - Unit of Measure Description (ST)

    csu_4 : str | None
        CSU.4 (opt) - Unit of Measure Coding System (ID)

    csu_5 : str | None
        CSU.5 (opt) - Alternate Unit of Measure Identifier (ST)

    csu_6 : str | None
        CSU.6 (opt) - Alternate Unit of Measure Description (ST)

    csu_7 : str | None
        CSU.7 (opt) - Alternate Unit of Measure Coding System (ID)
    """

    csu_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_1",
            "channel_sensitivity",
            "CSU.1",
        ),
        serialization_alias="CSU.1",
        title="Channel Sensitivity",
    )

    csu_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_2",
            "unit_of_measure_identifier",
            "CSU.2",
        ),
        serialization_alias="CSU.2",
        title="Unit of Measure Identifier",
    )

    csu_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_3",
            "unit_of_measure_description",
            "CSU.3",
        ),
        serialization_alias="CSU.3",
        title="Unit of Measure Description",
    )

    csu_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_4",
            "unit_of_measure_coding_system",
            "CSU.4",
        ),
        serialization_alias="CSU.4",
        title="Unit of Measure Coding System",
    )

    csu_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_5",
            "alternate_unit_of_measure_identifier",
            "CSU.5",
        ),
        serialization_alias="CSU.5",
        title="Alternate Unit of Measure Identifier",
    )

    csu_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_6",
            "alternate_unit_of_measure_description",
            "CSU.6",
        ),
        serialization_alias="CSU.6",
        title="Alternate Unit of Measure Description",
    )

    csu_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_7",
            "alternate_unit_of_measure_coding_system",
            "CSU.7",
        ),
        serialization_alias="CSU.7",
        title="Alternate Unit of Measure Coding System",
    )

    model_config = {"populate_by_name": True}
