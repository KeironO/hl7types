"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCU_I20.ROLE_GOAL_OBJECT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class CCU_I20_ROLE_GOAL_OBJECT(HL7Model):
    """HL7 v2 CCU_I20.ROLE_GOAL_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}
