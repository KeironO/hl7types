"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PPV_PCA.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .PPV_PCA_ORDER_DETAIL import PPV_PCA_ORDER_DETAIL

_ORC = ORC
_PPV_PCA_ORDER_DETAIL = PPV_PCA_ORDER_DETAIL


class PPV_PCA_ORDER(HL7Model):
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

    ORDER_DETAIL: Optional[_PPV_PCA_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
