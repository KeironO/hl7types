"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CQU_I19.ROLE_PATHWAY_OBJECT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class CQU_I19_ROLE_PATHWAY_OBJECT(BaseModel):
    """HL7 v2 CQU_I19.ROLE_PATHWAY_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}
