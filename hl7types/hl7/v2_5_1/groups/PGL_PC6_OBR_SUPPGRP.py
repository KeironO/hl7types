"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PGL_PC6.OBR_SUPPGRP
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class PGL_PC6_OBR_SUPPGRP(BaseModel):
    """HL7 v2 PGL_PC6.OBR_SUPPGRP group."""

    pass

    model_config = {"populate_by_name": True}
