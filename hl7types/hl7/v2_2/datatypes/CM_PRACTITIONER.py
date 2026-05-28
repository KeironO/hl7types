"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_PRACTITIONER
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CM_PRACTITIONER(BaseModel):
    """HL7 v2 CM_PRACTITIONER data type."""

    cm_practitioner_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_practitioner_1",
            "procedure_practitioner_id",
            "CM_PRACTITIONER.1",
        ),
        serialization_alias="CM_PRACTITIONER.1",
        title="Procedure Practitioner  ID",
    )

    cm_practitioner_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_practitioner_2",
            "procedure_practitioner_type",
            "CM_PRACTITIONER.2",
        ),
        serialization_alias="CM_PRACTITIONER.2",
        title="procedure practitioner type",
    )

    model_config = {"populate_by_name": True}
