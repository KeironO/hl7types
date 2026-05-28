"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_PTA
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CM_PTA(BaseModel):
    """HL7 v2 CM_PTA data type."""

    cm_pta_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pta_1",
            "policy_type",
            "CM_PTA.1",
        ),
        serialization_alias="CM_PTA.1",
        title="policy type",
    )

    cm_pta_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pta_2",
            "amount_class",
            "CM_PTA.2",
        ),
        serialization_alias="CM_PTA.2",
        title="amount class",
    )

    cm_pta_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pta_3",
            "amount",
            "CM_PTA.3",
        ),
        serialization_alias="CM_PTA.3",
        title="amount",
    )

    model_config = {"populate_by_name": True}
