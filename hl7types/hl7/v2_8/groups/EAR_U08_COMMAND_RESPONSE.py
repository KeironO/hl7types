"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EAR_U08.COMMAND_RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ECD import ECD
from ..segments.ECR import ECR

from .EAR_U08_SPECIMEN_CONTAINER import EAR_U08_SPECIMEN_CONTAINER

_EAR_U08_SPECIMEN_CONTAINER = EAR_U08_SPECIMEN_CONTAINER
_ECD = ECD
_ECR = ECR


class EAR_U08_COMMAND_RESPONSE(HL7Model):
    """HL7 v2 EAR_U08.COMMAND_RESPONSE group.

    Attributes:
        ECD (ECD): Equipment Command, required
        SPECIMEN_CONTAINER (Optional[EAR_U08_SPECIMEN_CONTAINER]): optional
        ECR (ECR): Equipment Command Response, required
    """

    ECD: _ECD = Field(
        title="ECD",
        description="Equipment Command",
    )

    SPECIMEN_CONTAINER: Optional[_EAR_U08_SPECIMEN_CONTAINER] = Field(
        default=None,
        title="SPECIMEN_CONTAINER",
    )

    ECR: _ECR = Field(
        title="ECR",
        description="Equipment Command Response",
    )

    model_config = {"populate_by_name": True}
