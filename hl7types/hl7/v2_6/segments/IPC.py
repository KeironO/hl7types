"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: IPC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class IPC(HL7Model):
    """Imaging Procedure Control Segment (S4.5.6).

    Attributes
    ----------
    ipc_1 : EI
        IPC.1 - Accession Identifier (EI) R S13.4.3.2

    ipc_2 : EI
        IPC.2 - Requested Procedure ID (EI) R S4.5.6.2

    ipc_3 : EI
        IPC.3 - Study Instance UID (EI) R S4.5.6.3

    ipc_4 : EI
        IPC.4 - Scheduled Procedure Step ID (EI) R S4.5.6.4

    ipc_5 : CWE | None
        IPC.5 - Modality (CWE) O S4.5.6.5 | 9999 - no table for CE

    ipc_6 : list[CWE] | None
        IPC.6 - Protocol Code (CWE) O rep S4.5.6.6 | 9999 - no table for CE

    ipc_7 : EI | None
        IPC.7 - Scheduled Station Name (EI) O S4.5.6.7

    ipc_8 : list[CWE] | None
        IPC.8 - Scheduled Procedure Step Location (CWE) O rep S4.5.6.8 | 9999 - no table for CE

    ipc_9 : str | None
        IPC.9 - Scheduled Station AE Title (ST) O S4.5.6.9
    """

    ipc_1: EI = Field(
        validation_alias=AliasChoices(
            "ipc_1",
            "accession_identifier",
            "IPC.1",
        ),
        serialization_alias="IPC.1",
        title="Accession Identifier",
        description="R | Item #01330",
    )

    ipc_2: EI = Field(
        validation_alias=AliasChoices(
            "ipc_2",
            "requested_procedure_id",
            "IPC.2",
        ),
        serialization_alias="IPC.2",
        title="Requested Procedure ID",
        description="R | Item #01658",
    )

    ipc_3: EI = Field(
        validation_alias=AliasChoices(
            "ipc_3",
            "study_instance_uid",
            "IPC.3",
        ),
        serialization_alias="IPC.3",
        title="Study Instance UID",
        description="R | Item #01659",
    )

    ipc_4: EI = Field(
        validation_alias=AliasChoices(
            "ipc_4",
            "scheduled_procedure_step_id",
            "IPC.4",
        ),
        serialization_alias="IPC.4",
        title="Scheduled Procedure Step ID",
        description="R | Item #01660",
    )

    ipc_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipc_5",
            "modality",
            "IPC.5",
        ),
        serialization_alias="IPC.5",
        title="Modality",
        description="O | Item #01661 | Table 9999 - no table for CE",
    )

    ipc_6: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipc_6",
            "protocol_code",
            "IPC.6",
        ),
        serialization_alias="IPC.6",
        title="Protocol Code",
        description="O | Item #01662 | Table 9999 - no table for CE",
    )

    ipc_7: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipc_7",
            "scheduled_station_name",
            "IPC.7",
        ),
        serialization_alias="IPC.7",
        title="Scheduled Station Name",
        description="O | Item #01663",
    )

    ipc_8: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipc_8",
            "scheduled_procedure_step_location",
            "IPC.8",
        ),
        serialization_alias="IPC.8",
        title="Scheduled Procedure Step Location",
        description="O | Item #01664 | Table 9999 - no table for CE",
    )

    ipc_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipc_9",
            "scheduled_station_ae_title",
            "IPC.9",
        ),
        serialization_alias="IPC.9",
        title="Scheduled Station AE Title",
        description="O | Item #01665 | LEN:16",
    )

    model_config = ConfigDict(populate_by_name=True)
