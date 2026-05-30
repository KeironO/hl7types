"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCR_I16.CLINICAL_ORDER_OBJECT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class CCR_I16_CLINICAL_ORDER_OBJECT(HL7Model):
    """HL7 v2 CCR_I16.CLINICAL_ORDER_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}
