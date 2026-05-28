"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EAR_U08.COMMAND_RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ECD import ECD
from ..segments.ECR import ECR
from .EAR_U08_SPECIMEN_CONTAINER import EAR_U08_SPECIMEN_CONTAINER

_EAR_U08_SPECIMEN_CONTAINER = EAR_U08_SPECIMEN_CONTAINER
_ECD = ECD
_ECR = ECR


class EAR_U08_COMMAND_RESPONSE(BaseModel):
    """HL7 v2 EAR_U08.COMMAND_RESPONSE group.

    Attributes:
        ECD (ECD): required
        SPECIMEN_CONTAINER (Optional[EAR_U08_SPECIMEN_CONTAINER]): optional
        ECR (ECR): required
    """

    ECD: _ECD = Field(
        default=...,
        title="ECD",
        description="Required",
    )

    SPECIMEN_CONTAINER: _EAR_U08_SPECIMEN_CONTAINER | None = Field(
        default=None,
        title="SPECIMEN_CONTAINER",
        description="Optional",
    )

    ECR: _ECR = Field(
        default=...,
        title="ECR",
        description="Required",
    )

    model_config = {"populate_by_name": True}
