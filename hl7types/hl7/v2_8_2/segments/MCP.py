"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MCP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.MO import MO


class MCP(HL7Model):
    """Master File Coverage (S8.8.18).

    Attributes
    ----------
    mcp_1 : str
        MCP.1 - Set ID - MCP (SI) R S8.8.18.1

    mcp_2 : CWE
        MCP.2 - Producer's Service/Test/Observation ID (CWE) R S8.8.18.2

    mcp_3 : MO | None
        MCP.3 - Universal Service Price Range - Low Value (MO) O S8.8.18.3

    mcp_4 : MO | None
        MCP.4 - Universal Service Price Range - High Value (MO) O S8.8.18.4

    mcp_5 : str | None
        MCP.5 - Reason for Universal Service Cost Range (ST) C S8.8.18.5
    """

    mcp_1: str = Field(
        validation_alias=AliasChoices(
            "mcp_1",
            "set_id_mcp",
            "MCP.1",
        ),
        serialization_alias="MCP.1",
        title="Set ID - MCP",
        description="R | Item #03468 | LEN:4",
    )

    mcp_2: CWE = Field(
        validation_alias=AliasChoices(
            "mcp_2",
            "producer_s_service_test_observation_id",
            "MCP.2",
        ),
        serialization_alias="MCP.2",
        title="Producer's Service/Test/Observation ID",
        description="R | Item #00587",
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
        description="O | Item #03469",
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
        description="O | Item #03470",
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
        description="C | Item #03471",
    )

    @field_validator("mcp_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
