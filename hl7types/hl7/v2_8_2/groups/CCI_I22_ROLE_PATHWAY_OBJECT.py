"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCI_I22.ROLE_PATHWAY_OBJECT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class CCI_I22_ROLE_PATHWAY_OBJECT(BaseModel):
    """HL7 v2 CCI_I22.ROLE_PATHWAY_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}
