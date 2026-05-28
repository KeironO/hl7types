"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PPV_PCA.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from .PPV_PCA_ORDER_DETAIL import PPV_PCA_ORDER_DETAIL

_ORC = ORC
_PPV_PCA_ORDER_DETAIL = PPV_PCA_ORDER_DETAIL


class PPV_PCA_ORDER(BaseModel):
    """HL7 v2 PPV_PCA.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[PPV_PCA_ORDER_DETAIL]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: _PPV_PCA_ORDER_DETAIL | None = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
