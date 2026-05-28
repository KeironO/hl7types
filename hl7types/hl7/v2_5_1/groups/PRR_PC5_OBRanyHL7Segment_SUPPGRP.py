"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PRR_PC5.OBRanyHL7Segment_SUPPGRP
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class PRR_PC5_OBRanyHL7Segment_SUPPGRP(BaseModel):
    """HL7 v2 PRR_PC5.OBRanyHL7Segment_SUPPGRP group."""

    pass

    model_config = {"populate_by_name": True}
