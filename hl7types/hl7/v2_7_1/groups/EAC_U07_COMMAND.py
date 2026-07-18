"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EAC_U07.COMMAND
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CNS import CNS
from ..segments.ECD import ECD
from ..segments.TQ1 import TQ1

from .EAC_U07_SPECIMEN_CONTAINER import EAC_U07_SPECIMEN_CONTAINER

_CNS = CNS
_EAC_U07_SPECIMEN_CONTAINER = EAC_U07_SPECIMEN_CONTAINER
_ECD = ECD
_TQ1 = TQ1


class EAC_U07_COMMAND(HL7Model):
    """HL7 v2 EAC_U07.COMMAND group.

    Attributes:
        ECD (ECD): Equipment Command, required
        TQ1 (Optional[TQ1]): Timing/Quantity, optional
        SPECIMEN_CONTAINER (Optional[EAC_U07_SPECIMEN_CONTAINER]): optional
        CNS (Optional[CNS]): Clear Notification, optional
    """

    ECD: _ECD = Field(
        title="ECD",
        description="Equipment Command",
    )

    TQ1: Optional[_TQ1] = Field(
        default=None,
        title="TQ1",
        description="Timing/Quantity",
    )

    SPECIMEN_CONTAINER: Optional[_EAC_U07_SPECIMEN_CONTAINER] = Field(
        default=None,
        title="SPECIMEN_CONTAINER",
    )

    CNS: Optional[_CNS] = Field(
        default=None,
        title="CNS",
        description="Clear Notification",
    )

    model_config = ConfigDict(populate_by_name=True)
