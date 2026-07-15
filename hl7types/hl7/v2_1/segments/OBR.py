"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: OBR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class OBR(HL7Model):
    """OBSERVATION REQUEST.

    Attributes
    ----------
    obr_1 : str | None
        OBR.1 - SET ID - OBSERVATION REQUEST (SI) O S7-4

    obr_2 : str | None
        OBR.2 - PLACER ORDER # (CM) O

    obr_3 : str | None
        OBR.3 - FILLER ORDER # (CM) O

    obr_4 : CE
        OBR.4 - UNIVERSAL SERVICE IDENT. (CE) R

    obr_5 : str | None
        OBR.5 - PRIORITY (ST) O

    obr_6 : str | None
        OBR.6 - REQUESTED DATE-TIME (TS) O

    obr_7 : str
        OBR.7 - OBSERVATION DATE/TIME (TS) R

    obr_8 : str
        OBR.8 - OBSERVATION END DATE/TIME (TS) R

    obr_9 : str
        OBR.9 - COLLECTION VOLUME (CQ) R | 0036 - UNITS OF MEASURE - ISO528,1977

    obr_10 : list[str] | None
        OBR.10 - COLLECTOR IDENTIFIER (CN) O rep

    obr_11 : str | None
        OBR.11 - SPECIMEN ACTION CODE (ST) O | 0065 - ACTION CODE

    obr_12 : str | None
        OBR.12 - DANGER CODE (CM) O | 0047 - DANGER CODE

    obr_13 : str | None
        OBR.13 - RELEVANT CLINICAL INFO. (ST) O

    obr_14 : str
        OBR.14 - SPECIMEN RECEIVED DATE/TIME (TS) R

    obr_15 : str | None
        OBR.15 - SPECIMEN SOURCE (CM) O | 0070 - SOURCE OF SPECIMEN

    obr_16 : list[str] | None
        OBR.16 - ORDERING PROVIDER (CN) O rep | 0010 - PHYSICIAN ID

    obr_17 : list[str] | None
        OBR.17 - ORDER CALL-BACK PHONE NUM (TN) O rep

    obr_18 : str | None
        OBR.18 - PLACERS FIELD #1 (ST) O

    obr_19 : str | None
        OBR.19 - PLACERS FIELD #2 (ST) O

    obr_20 : str | None
        OBR.20 - FILLERS FIELD #1 (ST) O

    obr_21 : str | None
        OBR.21 - FILLERS FIELD #2 (ST) O

    obr_22 : str
        OBR.22 - RESULTS RPT/STATUS CHNG - DATE/T (TS) R

    obr_23 : str | None
        OBR.23 - CHARGE TO PRACTICE (CM) O

    obr_24 : str | None
        OBR.24 - DIAGNOSTIC SERV SECT ID (ID) O | 0074 - DIAGNOSTIC SERVICE SECTION ID

    obr_25 : str | None
        OBR.25 - RESULT STATUS (ID) O | 0123 - RESULT STATUS - OBR

    obr_26 : CE | None
        OBR.26 - LINKED RESULTS (CE) O

    obr_27 : list[str] | None
        OBR.27 - QUANTITY/TIMING (CM) O rep

    obr_28 : list[str] | None
        OBR.28 - RESULT COPIES TO (CN) O rep

    obr_29 : str | None
        OBR.29 - PARENT ACCESSION # (CM) O

    obr_30 : str | None
        OBR.30 - TRANSPORTATION MODE (ID) O | 0124 - TRANSPORTATION MODE

    obr_31 : list[CE] | None
        OBR.31 - REASON FOR STUDY (CE) O rep

    obr_32 : str | None
        OBR.32 - PRINCIPAL RESULT INTERPRETER (CN) O

    obr_33 : str | None
        OBR.33 - ASSISTANT RESULT INTERPRETER (CN) O

    obr_34 : str | None
        OBR.34 - TECHNICIAN (CN) O

    obr_35 : str | None
        OBR.35 - TRANSCRIPTIONIST (CN) O

    obr_36 : str | None
        OBR.36 - SCHEDULED - DATE/TIME (TS) O
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
        description="O | Item #00520 | LEN:4",
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
        description="O | Item #00732 | LEN:75",
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
        description="O | Item #00733 | LEN:75",
    )

    obr_4: CE = Field(
        validation_alias=AliasChoices(
            "obr_4",
            "universal_service_ident",
            "OBR.4",
        ),
        serialization_alias="OBR.4",
        title="UNIVERSAL SERVICE IDENT.",
        description="R | Item #00523",
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
        description="O | Item #00524 | LEN:2",
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
        description="O | Item #00529 | LEN:19",
    )

    obr_7: str = Field(
        validation_alias=AliasChoices(
            "obr_7",
            "observation_date_time",
            "OBR.7",
        ),
        serialization_alias="OBR.7",
        title="OBSERVATION DATE/TIME",
        description="R | Item #00530 | LEN:19",
    )

    obr_8: str = Field(
        validation_alias=AliasChoices(
            "obr_8",
            "observation_end_date_time",
            "OBR.8",
        ),
        serialization_alias="OBR.8",
        title="OBSERVATION END DATE/TIME",
        description="R | Item #00531 | LEN:19",
    )

    obr_9: str = Field(
        validation_alias=AliasChoices(
            "obr_9",
            "collection_volume",
            "OBR.9",
        ),
        serialization_alias="OBR.9",
        title="COLLECTION VOLUME",
        description=(
            "R | Item #00532 | Table 0036 - UNITS OF MEASURE - ISO528,1977 | "
            "LEN:20"
        ),
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
        description="O | Item #00533 | LEN:60",
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
        description="O | Item #00534 | Table 0065 - ACTION CODE | LEN:1",
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
        description="O | Item #00535 | Table 0047 - DANGER CODE | LEN:60",
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
        description="O | Item #00536 | LEN:300",
    )

    obr_14: str = Field(
        validation_alias=AliasChoices(
            "obr_14",
            "specimen_received_date_time",
            "OBR.14",
        ),
        serialization_alias="OBR.14",
        title="SPECIMEN RECEIVED DATE/TIME",
        description="R | Item #00537 | LEN:19",
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
        description=(
            "O | Item #00538 | Table 0070 - SOURCE OF SPECIMEN | LEN:300"
        ),
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
        description="O | Item #00539 | Table 0010 - PHYSICIAN ID | LEN:60",
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
        description="O | Item #00540 | LEN:40",
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
        description="O | Item #00541 | LEN:60",
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
        description="O | Item #00542 | LEN:60",
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
        description="O | Item #00543 | LEN:60",
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
        description="O | Item #00544 | LEN:60",
    )

    obr_22: str = Field(
        validation_alias=AliasChoices(
            "obr_22",
            "results_rpt_status_chng_date_t",
            "OBR.22",
        ),
        serialization_alias="OBR.22",
        title="RESULTS RPT/STATUS CHNG - DATE/T",
        description="R | Item #00546 | LEN:19",
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
        description="O | Item #00547 | LEN:40",
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
        description=(
            "O | Item #00548 | Table 0074 - DIAGNOSTIC SERVICE SECTION ID | "
            "LEN:10"
        ),
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
        description=(
            "O | Item #00734 | Table 0123 - RESULT STATUS - OBR | LEN:1"
        ),
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
        description="O | Item #00550",
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
        description="O | Item #00735 | LEN:200",
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
        description="O | Item #00551 | LEN:80",
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
        description="O | Item #00737 | LEN:150",
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
        description=(
            "O | Item #00625 | Table 0124 - TRANSPORTATION MODE | LEN:20"
        ),
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
        description="O | Item #00626",
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
        description="O | Item #00627 | LEN:60",
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
        description="O | Item #00628 | LEN:60",
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
        description="O | Item #00630 | LEN:60",
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
        description="O | Item #00629 | LEN:60",
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
        description="O | Item #00736 | LEN:19",
    )

    @field_validator("obr_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
