"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CCP import CCP
from .CSU import CSU
from .NR import NR
from .WVI import WVI
from .WVS import WVS


class CD(HL7Model):
    """HL7 v2 CD data type.

    Attributes
    ----------
    cd_1 : WVI | None
        CD.1 (opt) - Channel Identifier (WVI)

    cd_2 : WVS | None
        CD.2 (opt) - Waveform Source (WVS)

    cd_3 : CSU | None
        CD.3 (opt) - Channel Sensitivity and Units (CSU)

    cd_4 : CCP | None
        CD.4 (opt) - Channel Calibration Parameters (CCP)

    cd_5 : str | None
        CD.5 (opt) - Channel Sampling Frequency (NM)

    cd_6 : NR | None
        CD.6 (opt) - Minimum and Maximum Data Values (NR)
    """

    cd_1: Optional[WVI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_1",
            "channel_identifier",
            "CD.1",
        ),
        serialization_alias="CD.1",
        title="Channel Identifier",
    )

    cd_2: Optional[WVS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_2",
            "waveform_source",
            "CD.2",
        ),
        serialization_alias="CD.2",
        title="Waveform Source",
    )

    cd_3: Optional[CSU] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_3",
            "channel_sensitivity_and_units",
            "CD.3",
        ),
        serialization_alias="CD.3",
        title="Channel Sensitivity and Units",
    )

    cd_4: Optional[CCP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_4",
            "channel_calibration_parameters",
            "CD.4",
        ),
        serialization_alias="CD.4",
        title="Channel Calibration Parameters",
    )

    cd_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_5",
            "channel_sampling_frequency",
            "CD.5",
        ),
        serialization_alias="CD.5",
        title="Channel Sampling Frequency",
    )

    cd_6: Optional[NR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_6",
            "minimum_and_maximum_data_values",
            "CD.6",
        ),
        serialization_alias="CD.6",
        title="Minimum and Maximum Data Values",
    )

    model_config = {"populate_by_name": True}
