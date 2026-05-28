"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORS_O06.RSPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .ORS_O06_ORDER import ORS_O06_ORDER
from .ORS_O06_PATIENT import ORS_O06_PATIENT

_ORS_O06_ORDER = ORS_O06_ORDER
_ORS_O06_PATIENT = ORS_O06_PATIENT


class ORS_O06_RSPONSE(BaseModel):
    """HL7 v2 ORS_O06.RSPONSE group.

    Attributes:
        PATIENT (Optional[ORS_O06_PATIENT]): optional
        ORDER (List[ORS_O06_ORDER]): required
    """

    PATIENT: _ORS_O06_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_ORS_O06_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
