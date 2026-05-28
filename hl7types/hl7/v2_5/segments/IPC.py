"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: IPC
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.EI import EI


class IPC(BaseModel):
    """HL7 v2 IPC segment."""

    ipc_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "ipc_1",
            "accession_identifier",
            "IPC.1",
        ),
        serialization_alias="IPC.1",
        title="Accession Identifier",
        description="Item #1330",
    )

    ipc_2: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "ipc_2",
            "requested_procedure_id",
            "IPC.2",
        ),
        serialization_alias="IPC.2",
        title="Requested Procedure ID",
        description="Item #1658",
    )

    ipc_3: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "ipc_3",
            "study_instance_uid",
            "IPC.3",
        ),
        serialization_alias="IPC.3",
        title="Study Instance UID",
        description="Item #1659",
    )

    ipc_4: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "ipc_4",
            "scheduled_procedure_step_id",
            "IPC.4",
        ),
        serialization_alias="IPC.4",
        title="Scheduled Procedure Step ID",
        description="Item #1660",
    )

    ipc_5: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipc_5",
            "modality",
            "IPC.5",
        ),
        serialization_alias="IPC.5",
        title="Modality",
        description="Item #1661",
    )

    ipc_6: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipc_6",
            "protocol_code",
            "IPC.6",
        ),
        serialization_alias="IPC.6",
        title="Protocol Code",
        description="Item #1662",
    )

    ipc_7: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipc_7",
            "scheduled_station_name",
            "IPC.7",
        ),
        serialization_alias="IPC.7",
        title="Scheduled Station Name",
        description="Item #1663",
    )

    ipc_8: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipc_8",
            "scheduled_procedure_step_location",
            "IPC.8",
        ),
        serialization_alias="IPC.8",
        title="Scheduled Procedure Step Location",
        description="Item #1664",
    )

    ipc_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipc_9",
            "scheduled_ae_title",
            "IPC.9",
        ),
        serialization_alias="IPC.9",
        title="Scheduled AE Title",
        description="Item #1665",
    )

    model_config = {"populate_by_name": True}
