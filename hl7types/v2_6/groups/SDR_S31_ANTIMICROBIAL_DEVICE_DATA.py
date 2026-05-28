"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: SDR_S31.ANTIMICROBIAL_DEVICE_DATA
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class SDR_S31_ANTIMICROBIAL_DEVICE_DATA(BaseModel):
    """HL7 v2 SDR_S31.ANTIMICROBIAL_DEVICE_DATA group."""

    pass

    model_config = {"populate_by_name": True}
