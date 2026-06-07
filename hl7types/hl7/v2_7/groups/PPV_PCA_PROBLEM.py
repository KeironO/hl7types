"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PPV_PCA.PROBLEM
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PRB import PRB
from ..segments.VAR import VAR

from .PPV_PCA_PROBLEM_OBSERVATION import PPV_PCA_PROBLEM_OBSERVATION
from .PPV_PCA_PROBLEM_ROLE import PPV_PCA_PROBLEM_ROLE

_NTE = NTE
_PPV_PCA_PROBLEM_OBSERVATION = PPV_PCA_PROBLEM_OBSERVATION
_PPV_PCA_PROBLEM_ROLE = PPV_PCA_PROBLEM_ROLE
_PRB = PRB
_VAR = VAR


class PPV_PCA_PROBLEM(HL7Model):
    """HL7 v2 PPV_PCA.PROBLEM group.

    Attributes:
        PRB (PRB): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        PROBLEM_ROLE (Optional[List[PPV_PCA_PROBLEM_ROLE]]): optional
        PROBLEM_OBSERVATION (Optional[List[PPV_PCA_PROBLEM_OBSERVATION]]): optional
    """

    PRB: _PRB = Field(
        title="PRB",
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

    PROBLEM_ROLE: Optional[List[_PPV_PCA_PROBLEM_ROLE]] = Field(
        default=None,
        title="PROBLEM_ROLE",
        description="Optional, repeating",
    )

    PROBLEM_OBSERVATION: Optional[List[_PPV_PCA_PROBLEM_OBSERVATION]] = Field(
        default=None,
        title="PROBLEM_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
