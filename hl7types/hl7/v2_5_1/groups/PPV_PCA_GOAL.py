"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPV_PCA.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GOL import GOL
from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPV_PCA_GOAL_OBSERVATION import PPV_PCA_GOAL_OBSERVATION
from .PPV_PCA_GOAL_PATHWAY import PPV_PCA_GOAL_PATHWAY
from .PPV_PCA_GOAL_ROLE import PPV_PCA_GOAL_ROLE
from .PPV_PCA_ORDER import PPV_PCA_ORDER
from .PPV_PCA_PROBLEM import PPV_PCA_PROBLEM

_GOL = GOL
_NTE = NTE
_PPV_PCA_GOAL_OBSERVATION = PPV_PCA_GOAL_OBSERVATION
_PPV_PCA_GOAL_PATHWAY = PPV_PCA_GOAL_PATHWAY
_PPV_PCA_GOAL_ROLE = PPV_PCA_GOAL_ROLE
_PPV_PCA_ORDER = PPV_PCA_ORDER
_PPV_PCA_PROBLEM = PPV_PCA_PROBLEM
_VAR = VAR


class PPV_PCA_GOAL(HL7Model):
    """HL7 v2 PPV_PCA.GOAL group.

    Attributes:
        GOL (GOL): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        GOAL_ROLE (Optional[List[PPV_PCA_GOAL_ROLE]]): optional
        GOAL_PATHWAY (Optional[List[PPV_PCA_GOAL_PATHWAY]]): optional
        GOAL_OBSERVATION (Optional[List[PPV_PCA_GOAL_OBSERVATION]]): optional
        PROBLEM (Optional[List[PPV_PCA_PROBLEM]]): optional
        ORDER (Optional[List[PPV_PCA_ORDER]]): optional
    """

    GOL: _GOL = Field(
        default=...,
        title="GOL",
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

    GOAL_ROLE: Optional[List[_PPV_PCA_GOAL_ROLE]] = Field(
        default=None,
        title="GOAL_ROLE",
        description="Optional, repeating",
    )

    GOAL_PATHWAY: Optional[List[_PPV_PCA_GOAL_PATHWAY]] = Field(
        default=None,
        title="GOAL_PATHWAY",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: Optional[List[_PPV_PCA_GOAL_OBSERVATION]] = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    PROBLEM: Optional[List[_PPV_PCA_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
        description="Optional, repeating",
    )

    ORDER: Optional[List[_PPV_PCA_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
