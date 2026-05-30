"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPR_PC1.OBR_SUPPGRP
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class PPR_PC1_OBR_SUPPGRP(HL7Model):
    """HL7 v2 PPR_PC1.OBR_SUPPGRP group."""

    pass

    model_config = {"populate_by_name": True}
