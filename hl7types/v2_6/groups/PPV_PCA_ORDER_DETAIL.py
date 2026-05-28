"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PPV_PCA.ORDER_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPV_PCA_CHOICE import PPV_PCA_CHOICE
from .PPV_PCA_ORDER_OBSERVATION import PPV_PCA_ORDER_OBSERVATION

_NTE = NTE
_PPV_PCA_CHOICE = PPV_PCA_CHOICE
_PPV_PCA_ORDER_OBSERVATION = PPV_PCA_ORDER_OBSERVATION
_VAR = VAR


class PPV_PCA_ORDER_DETAIL(BaseModel):
    """HL7 v2 PPV_PCA.ORDER_DETAIL group.

    Attributes:
        CHOICE (PPV_PCA_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PPV_PCA_ORDER_OBSERVATION]]): optional
    """

    CHOICE: _PPV_PCA_CHOICE = Field(
        default=...,
        title="CHOICE",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ORDER_OBSERVATION: Optional[List[_PPV_PCA_ORDER_OBSERVATION]] = Field(
        default=None,
        title="ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
