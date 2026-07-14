"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFN_M08.MF_NUMERIC_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OM2 import OM2
from ..segments.OM3 import OM3
from ..segments.OM4 import OM4

_OM2 = OM2
_OM3 = OM3
_OM4 = OM4


class MFN_M08_MF_NUMERIC_OBSERVATION(HL7Model):
    """HL7 v2 MFN_M08.MF_NUMERIC_OBSERVATION group.

    Attributes:
        OM2 (Optional[OM2]): OM2 - numeric observation segment, optional
        OM3 (Optional[OM3]): OM3 - categorical test/observation segment, optional
        OM4 (Optional[OM4]): OM4 - observations that require specimens segment, optional
    """

    OM2: Optional[_OM2] = Field(
        default=None,
        title="OM2",
        description="OM2 - numeric observation segment",
    )

    OM3: Optional[_OM3] = Field(
        default=None,
        title="OM3",
        description="OM3 - categorical test/observation segment",
    )

    OM4: Optional[_OM4] = Field(
        default=None,
        title="OM4",
        description="OM4 - observations that require specimens segment",
    )

    model_config = {"populate_by_name": True}
