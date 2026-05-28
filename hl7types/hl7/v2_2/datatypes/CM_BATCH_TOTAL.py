"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_BATCH_TOTAL
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CM_BATCH_TOTAL(BaseModel):
    """HL7 v2 CM_BATCH_TOTAL data type."""

    cm_batch_total_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_batch_total_1",
            "batch_total_1",
            "CM_BATCH_TOTAL.1",
        ),
        serialization_alias="CM_BATCH_TOTAL.1",
        title="Batch total 1",
    )

    cm_batch_total_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_batch_total_2",
            "batch_total_2",
            "CM_BATCH_TOTAL.2",
        ),
        serialization_alias="CM_BATCH_TOTAL.2",
        title="Batch total 2",
    )

    model_config = {"populate_by_name": True}
