"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MCP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CWE import CWE
from ..datatypes.MO import MO


class MCP(HL7Model):
    """HL7 v2 MCP segment.

    Attributes
    ----------
    mcp_1 : str
        MCP.1 (req) - Set ID - MCP (SI)

    mcp_2 : CWE
        MCP.2 (req) - Producer's Service/Test/Observation ID (CWE)

    mcp_3 : MO | None
        MCP.3 (opt) - Universal Service Price Range - Low Value (MO)

    mcp_4 : MO | None
        MCP.4 (opt) - Universal Service Price Range - High Value (MO)

    mcp_5 : str | None
        MCP.5 (opt) - Reason for Universal Service Cost Range (ST)
    """

    mcp_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "mcp_1",
            "set_id_mcp",
            "MCP.1",
        ),
        serialization_alias="MCP.1",
        title="Set ID - MCP",
        description="Item #3468",
    )

    mcp_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "mcp_2",
            "producer_s_service_test_observation_id",
            "MCP.2",
        ),
        serialization_alias="MCP.2",
        title="Producer's Service/Test/Observation ID",
        description="Item #587",
    )

    mcp_3: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mcp_3",
            "universal_service_price_range_low_value",
            "MCP.3",
        ),
        serialization_alias="MCP.3",
        title="Universal Service Price Range - Low Value",
        description="Item #3469",
    )

    mcp_4: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mcp_4",
            "universal_service_price_range_high_value",
            "MCP.4",
        ),
        serialization_alias="MCP.4",
        title="Universal Service Price Range - High Value",
        description="Item #3470",
    )

    mcp_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mcp_5",
            "reason_for_universal_service_cost_range",
            "MCP.5",
        ),
        serialization_alias="MCP.5",
        title="Reason for Universal Service Cost Range",
        description="Item #3471",
    )

    @field_validator("mcp_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
