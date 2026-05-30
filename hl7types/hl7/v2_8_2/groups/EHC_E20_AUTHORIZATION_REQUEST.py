"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EHC_E20.AUTHORIZATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class EHC_E20_AUTHORIZATION_REQUEST(HL7Model):
    """HL7 v2 EHC_E20.AUTHORIZATION_REQUEST group."""

    pass

    model_config = {"populate_by_name": True}
