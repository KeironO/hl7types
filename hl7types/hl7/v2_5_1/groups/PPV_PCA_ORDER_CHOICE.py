"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPV_PCA.ORDER_CHOICE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class PPV_PCA_ORDER_CHOICE(BaseModel):
    """HL7 v2 PPV_PCA.ORDER_CHOICE group."""

    pass

    model_config = {"populate_by_name": True}
