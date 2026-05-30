"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCI_I22.ROLE_PROBLEM_OBJECT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class CCI_I22_ROLE_PROBLEM_OBJECT(HL7Model):
    """HL7 v2 CCI_I22.ROLE_PROBLEM_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}
