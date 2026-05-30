"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCM_I21.ROLE_CLINICAL_HISTORY_OBJECT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class CCM_I21_ROLE_CLINICAL_HISTORY_OBJECT(HL7Model):
    """HL7 v2 CCM_I21.ROLE_CLINICAL_HISTORY_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}
