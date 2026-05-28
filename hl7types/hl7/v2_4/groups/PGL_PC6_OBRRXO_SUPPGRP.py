"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PGL_PC6.OBRRXO_SUPPGRP
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class PGL_PC6_OBRRXO_SUPPGRP(BaseModel):
    """HL7 v2 PGL_PC6.OBRRXO_SUPPGRP group."""

    pass

    model_config = {"populate_by_name": True}
