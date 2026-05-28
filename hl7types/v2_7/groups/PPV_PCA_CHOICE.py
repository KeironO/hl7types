"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PPV_PCA.CHOICE
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class PPV_PCA_CHOICE(BaseModel):
    """HL7 v2 PPV_PCA.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}
