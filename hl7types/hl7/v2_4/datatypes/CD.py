"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
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
        CD.1 (opt) - channel identifier (WVI)

    cd_2 : WVS | None
        CD.2 (opt) - waveform source (WVS)

    cd_3 : CSU | None
        CD.3 (opt) - channel sensitivity/units (CSU)

    cd_4 : CCP | None
        CD.4 (opt) - channel calibration parameters (CCP)

    cd_5 : str | None
        CD.5 (opt) - channel sampling frequency (NM)

    cd_6 : NR | None
        CD.6 (opt) - minimum/maximum data values (NR)
    """

    cd_1: Optional[WVI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_1",
            "channel_identifier",
            "CD.1",
        ),
        serialization_alias="CD.1",
        title="channel identifier",
    )

    cd_2: Optional[WVS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_2",
            "waveform_source",
            "CD.2",
        ),
        serialization_alias="CD.2",
        title="waveform source",
    )

    cd_3: Optional[CSU] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_3",
            "channel_sensitivity_units",
            "CD.3",
        ),
        serialization_alias="CD.3",
        title="channel sensitivity/units",
    )

    cd_4: Optional[CCP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_4",
            "channel_calibration_parameters",
            "CD.4",
        ),
        serialization_alias="CD.4",
        title="channel calibration parameters",
    )

    cd_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_5",
            "channel_sampling_frequency",
            "CD.5",
        ),
        serialization_alias="CD.5",
        title="channel sampling frequency",
    )

    cd_6: Optional[NR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cd_6",
            "minimum_maximum_data_values",
            "CD.6",
        ),
        serialization_alias="CD.6",
        title="minimum/maximum data values",
    )

    @field_validator("cd_5", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
