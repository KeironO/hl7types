"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: OBR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CE import CE


class OBR(HL7Model):
    """HL7 v2 OBR segment.

    Attributes
    ----------
    obr_1 : str | None
        OBR.1 (opt) - SET ID - OBSERVATION REQUEST (SI)

    obr_2 : str | None
        OBR.2 (opt) - PLACER ORDER # (CM)

    obr_3 : str | None
        OBR.3 (opt) - FILLER ORDER # (CM)

    obr_4 : CE
        OBR.4 (req) - UNIVERSAL SERVICE IDENT. (CE)

    obr_5 : str | None
        OBR.5 (opt) - PRIORITY (ST)

    obr_6 : str | None
        OBR.6 (opt) - REQUESTED DATE-TIME (TS)

    obr_7 : str
        OBR.7 (req) - OBSERVATION DATE/TIME (TS)

    obr_8 : str
        OBR.8 (req) - OBSERVATION END DATE/TIME (TS)

    obr_9 : str
        OBR.9 (req) - COLLECTION VOLUME (CQ)

    obr_10 : list[str] | None
        OBR.10 (opt, rep) - COLLECTOR IDENTIFIER (CN)

    obr_11 : str | None
        OBR.11 (opt) - SPECIMEN ACTION CODE (ST)

    obr_12 : str | None
        OBR.12 (opt) - DANGER CODE (CM)

    obr_13 : str | None
        OBR.13 (opt) - RELEVANT CLINICAL INFO. (ST)

    obr_14 : str
        OBR.14 (req) - SPECIMEN RECEIVED DATE/TIME (TS)

    obr_15 : str | None
        OBR.15 (opt) - SPECIMEN SOURCE (CM)

    obr_16 : list[str] | None
        OBR.16 (opt, rep) - ORDERING PROVIDER (CN)

    obr_17 : list[str] | None
        OBR.17 (opt, rep) - ORDER CALL-BACK PHONE NUM (TN)

    obr_18 : str | None
        OBR.18 (opt) - PLACERS FIELD #1 (ST)

    obr_19 : str | None
        OBR.19 (opt) - PLACERS FIELD #2 (ST)

    obr_20 : str | None
        OBR.20 (opt) - FILLERS FIELD #1 (ST)

    obr_21 : str | None
        OBR.21 (opt) - FILLERS FIELD #2 (ST)

    obr_22 : str
        OBR.22 (req) - RESULTS RPT/STATUS CHNG - DATE/T (TS)

    obr_23 : str | None
        OBR.23 (opt) - CHARGE TO PRACTICE (CM)

    obr_24 : str | None
        OBR.24 (opt) - DIAGNOSTIC SERV SECT ID (ID)

    obr_25 : str | None
        OBR.25 (opt) - RESULT STATUS (ID)

    obr_26 : CE | None
        OBR.26 (opt) - LINKED RESULTS (CE)

    obr_27 : list[str] | None
        OBR.27 (opt, rep) - QUANTITY/TIMING (CM)

    obr_28 : list[str] | None
        OBR.28 (opt, rep) - RESULT COPIES TO (CN)

    obr_29 : str | None
        OBR.29 (opt) - PARENT ACCESSION # (CM)

    obr_30 : str | None
        OBR.30 (opt) - TRANSPORTATION MODE (ID)

    obr_31 : list[CE] | None
        OBR.31 (opt, rep) - REASON FOR STUDY (CE)

    obr_32 : str | None
        OBR.32 (opt) - PRINCIPAL RESULT INTERPRETER (CN)

    obr_33 : str | None
        OBR.33 (opt) - ASSISTANT RESULT INTERPRETER (CN)

    obr_34 : str | None
        OBR.34 (opt) - TECHNICIAN (CN)

    obr_35 : str | None
        OBR.35 (opt) - TRANSCRIPTIONIST (CN)

    obr_36 : str | None
        OBR.36 (opt) - SCHEDULED - DATE/TIME (TS)
    """

    obr_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_1",
            "set_id_observation_request",
            "OBR.1",
        ),
        serialization_alias="OBR.1",
        title="SET ID - OBSERVATION REQUEST",
        description="Item #520",
    )

    obr_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_2",
            "placer_order",
            "OBR.2",
        ),
        serialization_alias="OBR.2",
        title="PLACER ORDER #",
        description="Item #732",
    )

    obr_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_3",
            "filler_order",
            "OBR.3",
        ),
        serialization_alias="OBR.3",
        title="FILLER ORDER #",
        description="Item #733",
    )

    obr_4: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "obr_4",
            "universal_service_ident",
            "OBR.4",
        ),
        serialization_alias="OBR.4",
        title="UNIVERSAL SERVICE IDENT.",
        description="Item #523",
    )

    obr_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_5",
            "priority",
            "OBR.5",
        ),
        serialization_alias="OBR.5",
        title="PRIORITY",
        description="Item #524",
    )

    obr_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_6",
            "requested_date_time",
            "OBR.6",
        ),
        serialization_alias="OBR.6",
        title="REQUESTED DATE-TIME",
        description="Item #529",
    )

    obr_7: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "obr_7",
            "observation_date_time",
            "OBR.7",
        ),
        serialization_alias="OBR.7",
        title="OBSERVATION DATE/TIME",
        description="Item #530",
    )

    obr_8: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "obr_8",
            "observation_end_date_time",
            "OBR.8",
        ),
        serialization_alias="OBR.8",
        title="OBSERVATION END DATE/TIME",
        description="Item #531",
    )

    obr_9: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "obr_9",
            "collection_volume",
            "OBR.9",
        ),
        serialization_alias="OBR.9",
        title="COLLECTION VOLUME",
        description="Item #532 | Table HL70036",
    )

    obr_10: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_10",
            "collector_identifier",
            "OBR.10",
        ),
        serialization_alias="OBR.10",
        title="COLLECTOR IDENTIFIER",
        description="Item #533",
    )

    obr_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_11",
            "specimen_action_code",
            "OBR.11",
        ),
        serialization_alias="OBR.11",
        title="SPECIMEN ACTION CODE",
        description="Item #534 | Table HL70065",
    )

    obr_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_12",
            "danger_code",
            "OBR.12",
        ),
        serialization_alias="OBR.12",
        title="DANGER CODE",
        description="Item #535 | Table HL70047",
    )

    obr_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_13",
            "relevant_clinical_info",
            "OBR.13",
        ),
        serialization_alias="OBR.13",
        title="RELEVANT CLINICAL INFO.",
        description="Item #536",
    )

    obr_14: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "obr_14",
            "specimen_received_date_time",
            "OBR.14",
        ),
        serialization_alias="OBR.14",
        title="SPECIMEN RECEIVED DATE/TIME",
        description="Item #537",
    )

    obr_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_15",
            "specimen_source",
            "OBR.15",
        ),
        serialization_alias="OBR.15",
        title="SPECIMEN SOURCE",
        description="Item #538 | Table HL70070",
    )

    obr_16: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_16",
            "ordering_provider",
            "OBR.16",
        ),
        serialization_alias="OBR.16",
        title="ORDERING PROVIDER",
        description="Item #539 | Table HL70010",
    )

    obr_17: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_17",
            "order_call_back_phone_num",
            "OBR.17",
        ),
        serialization_alias="OBR.17",
        title="ORDER CALL-BACK PHONE NUM",
        description="Item #540",
    )

    obr_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_18",
            "placers_field_1",
            "OBR.18",
        ),
        serialization_alias="OBR.18",
        title="PLACERS FIELD #1",
        description="Item #541",
    )

    obr_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_19",
            "placers_field_2",
            "OBR.19",
        ),
        serialization_alias="OBR.19",
        title="PLACERS FIELD #2",
        description="Item #542",
    )

    obr_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_20",
            "fillers_field_1",
            "OBR.20",
        ),
        serialization_alias="OBR.20",
        title="FILLERS FIELD #1",
        description="Item #543",
    )

    obr_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_21",
            "fillers_field_2",
            "OBR.21",
        ),
        serialization_alias="OBR.21",
        title="FILLERS FIELD #2",
        description="Item #544",
    )

    obr_22: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "obr_22",
            "results_rpt_status_chng_date_t",
            "OBR.22",
        ),
        serialization_alias="OBR.22",
        title="RESULTS RPT/STATUS CHNG - DATE/T",
        description="Item #546",
    )

    obr_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_23",
            "charge_to_practice",
            "OBR.23",
        ),
        serialization_alias="OBR.23",
        title="CHARGE TO PRACTICE",
        description="Item #547",
    )

    obr_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_24",
            "diagnostic_serv_sect_id",
            "OBR.24",
        ),
        serialization_alias="OBR.24",
        title="DIAGNOSTIC SERV SECT ID",
        description="Item #548 | Table HL70074",
    )

    obr_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_25",
            "result_status",
            "OBR.25",
        ),
        serialization_alias="OBR.25",
        title="RESULT STATUS",
        description="Item #734 | Table HL70123",
    )

    obr_26: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_26",
            "linked_results",
            "OBR.26",
        ),
        serialization_alias="OBR.26",
        title="LINKED RESULTS",
        description="Item #550",
    )

    obr_27: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_27",
            "quantity_timing",
            "OBR.27",
        ),
        serialization_alias="OBR.27",
        title="QUANTITY/TIMING",
        description="Item #735",
    )

    obr_28: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_28",
            "result_copies_to",
            "OBR.28",
        ),
        serialization_alias="OBR.28",
        title="RESULT COPIES TO",
        description="Item #551",
    )

    obr_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_29",
            "parent_accession",
            "OBR.29",
        ),
        serialization_alias="OBR.29",
        title="PARENT ACCESSION #",
        description="Item #737",
    )

    obr_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_30",
            "transportation_mode",
            "OBR.30",
        ),
        serialization_alias="OBR.30",
        title="TRANSPORTATION MODE",
        description="Item #625 | Table HL70124",
    )

    obr_31: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_31",
            "reason_for_study",
            "OBR.31",
        ),
        serialization_alias="OBR.31",
        title="REASON FOR STUDY",
        description="Item #626",
    )

    obr_32: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_32",
            "principal_result_interpreter",
            "OBR.32",
        ),
        serialization_alias="OBR.32",
        title="PRINCIPAL RESULT INTERPRETER",
        description="Item #627",
    )

    obr_33: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_33",
            "assistant_result_interpreter",
            "OBR.33",
        ),
        serialization_alias="OBR.33",
        title="ASSISTANT RESULT INTERPRETER",
        description="Item #628",
    )

    obr_34: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_34",
            "technician",
            "OBR.34",
        ),
        serialization_alias="OBR.34",
        title="TECHNICIAN",
        description="Item #630",
    )

    obr_35: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_35",
            "transcriptionist",
            "OBR.35",
        ),
        serialization_alias="OBR.35",
        title="TRANSCRIPTIONIST",
        description="Item #629",
    )

    obr_36: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_36",
            "scheduled_date_time",
            "OBR.36",
        ),
        serialization_alias="OBR.36",
        title="SCHEDULED - DATE/TIME",
        description="Item #736",
    )

    @field_validator("obr_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
