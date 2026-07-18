"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PPV_PCA.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPV_PCA_CHOICE import PPV_PCA_CHOICE
from .PPV_PCA_ORDER_OBSERVATION import PPV_PCA_ORDER_OBSERVATION

_NTE = NTE
_PPV_PCA_CHOICE = PPV_PCA_CHOICE
_PPV_PCA_ORDER_OBSERVATION = PPV_PCA_ORDER_OBSERVATION
_VAR = VAR


class PPV_PCA_ORDER_DETAIL(HL7Model):
    """HL7 v2 PPV_PCA.ORDER_DETAIL group.

    Attributes:
        CHOICE (PPV_PCA_CHOICE): required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        VAR (Optional[List[VAR]]): Variance, optional
        ORDER_OBSERVATION (Optional[List[PPV_PCA_ORDER_OBSERVATION]]): optional
    """

    CHOICE: _PPV_PCA_CHOICE = Field(
        title="CHOICE",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Variance",
    )

    ORDER_OBSERVATION: Optional[List[_PPV_PCA_ORDER_OBSERVATION]] = Field(
        default=None,
        title="ORDER_OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
