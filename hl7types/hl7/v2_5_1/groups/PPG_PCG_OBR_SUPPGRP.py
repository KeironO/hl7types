"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPG_PCG.OBR_SUPPGRP
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class PPG_PCG_OBR_SUPPGRP(BaseModel):
    """HL7 v2 PPG_PCG.OBR_SUPPGRP group."""

    pass

    model_config = {"populate_by_name": True}
