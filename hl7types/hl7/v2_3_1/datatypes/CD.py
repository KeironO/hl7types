"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CCP import CCP
from .CSU import CSU
from .NR import NR
from .WVI import WVI
from .WVS import WVS


class CD(BaseModel):
    """HL7 v2 CD data type."""

    cd_1: WVI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_1",
            "channel_identifier",
            "CD.1",
        ),
        serialization_alias="CD.1",
        title="channel identifier",
    )

    cd_2: WVS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_2",
            "electrode_names",
            "CD.2",
        ),
        serialization_alias="CD.2",
        title="electrode names",
    )

    cd_3: CSU | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_3",
            "channel_sensitivity_units",
            "CD.3",
        ),
        serialization_alias="CD.3",
        title="channel sensitivity/units",
    )

    cd_4: CCP | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_4",
            "calibration_parameters",
            "CD.4",
        ),
        serialization_alias="CD.4",
        title="calibration parameters",
    )

    cd_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_5",
            "sampling_frequency",
            "CD.5",
        ),
        serialization_alias="CD.5",
        title="sampling frequency",
    )

    cd_6: NR | None = Field(
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
