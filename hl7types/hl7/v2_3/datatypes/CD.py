"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CD(BaseModel):
    """HL7 v2 CD data type.

    Attributes
    ----------
    cd_1 : str | None
        CD.1 (opt) - channel identifier (CM)

    cd_2 : str | None
        CD.2 (opt) - electrode names (CM)

    cd_3 : str | None
        CD.3 (opt) - channel sensitivity/units (CM)

    cd_4 : str | None
        CD.4 (opt) - calibration parameters (CM)

    cd_5 : str | None
        CD.5 (opt) - sampling frequency (NM)

    cd_6 : str | None
        CD.6 (opt) - minimum/maximum data values (CM)
    """

    cd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_1",
            "channel_identifier",
            "CD.1",
        ),
        serialization_alias="CD.1",
        title="channel identifier",
    )

    cd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_2",
            "electrode_names",
            "CD.2",
        ),
        serialization_alias="CD.2",
        title="electrode names",
    )

    cd_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_3",
            "channel_sensitivity_units",
            "CD.3",
        ),
        serialization_alias="CD.3",
        title="channel sensitivity/units",
    )

    cd_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_4",
            "calibration_parameters",
            "CD.4",
        ),
        serialization_alias="CD.4",
        title="calibration parameters",
    )

    cd_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_5",
            "sampling_frequency",
            "CD.5",
        ),
        serialization_alias="CD.5",
        title="sampling frequency",
    )

    cd_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_6",
            "minimum_maximum_data_values",
            "CD.6",
        ),
        serialization_alias="CD.6",
        title="minimum/maximum data values",
    )

    model_config = {"populate_by_name": True}
