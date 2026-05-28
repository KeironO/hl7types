"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PPV_PCA.CHOICE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class PPV_PCA_CHOICE(BaseModel):
    """HL7 v2 PPV_PCA.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}
