"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: OBR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS


class OBR(HL7Model):
    """OBSERVATION REQUEST (S7.3.1).

    Attributes
    ----------
    obr_1 : str | None
        OBR.1 - Set ID - Observation Request (SI) NA S4.5.1.1

    obr_2 : str | None
        OBR.2 - Placer Order Number (CM) C S4.5.1.2

    obr_3 : str | None
        OBR.3 - Filler Order Number (CM) C S6.4.1.23

    obr_4 : CE
        OBR.4 - Universal Service ID (CE) R S4.5.1.4

    obr_5 : str | None
        OBR.5 - Priority (not used) (ID) NA S4.5.1.5

    obr_6 : TS | None
        OBR.6 - Requested date / time (not used) (TS) NA S4.5.1.6

    obr_7 : TS | None
        OBR.7 - Observation date / time (TS) C S4.5.1.7

    obr_8 : TS | None
        OBR.8 - Observation end date / time (TS) C S4.5.1.8

    obr_9 : str | None
        OBR.9 - Collection Volume (CQ) C S4.5.1.9

    obr_10 : list[str] | None
        OBR.10 - Collector Identifier (CN) NA rep S4.5.1.10

    obr_11 : str | None
        OBR.11 - Specimen action code (ID) NA S4.5.1.11 | 0065 - ACTION CODE

    obr_12 : CE | None
        OBR.12 - Danger Code (CE) NA S4-30

    obr_13 : str | None
        OBR.13 - Relevant clinical information (ST) NA S4.5.1.13

    obr_14 : TS | None
        OBR.14 - Specimen received date / time (TS) C S4.5.1.14

    obr_15 : str | None
        OBR.15 - Specimen source (CM) NA S4.5.1.15 | 0070 - SOURCE OF SPECIMEN

    obr_16 : str | None
        OBR.16 - Ordering Provider (CN) NA S4.5.1.16

    obr_17 : list[str] | None
        OBR.17 - Order Callback Phone Number (TN) NA rep S4.5.1.17

    obr_18 : str | None
        OBR.18 - Placer field 1 (ST) NA S4.5.1.18

    obr_19 : str | None
        OBR.19 - Placer field 2 (ST) NA S4.5.1.19

    obr_20 : str | None
        OBR.20 - Filler Field 1 (ST) NA S4.5.1.20

    obr_21 : str | None
        OBR.21 - Filler Field 2 (ST) NA S4.5.1.21

    obr_22 : TS | None
        OBR.22 - Results report / status change - date / time (TS) C S4.5.1.22

    obr_23 : str | None
        OBR.23 - Charge to Practice (CM) NA S4.5.1.23

    obr_24 : str | None
        OBR.24 - Diagnostic service section ID (ID) NA S4.5.1.24 | 0074 - DIAGNOSTIC SERVICE SECTION ID

    obr_25 : str | None
        OBR.25 - Result Status (ID) C S4.5.1.25 | 0123 - RESULT STATUS - OBR

    obr_26 : str | None
        OBR.26 - Parent Result (CM) NA S4.5.1.26

    obr_27 : list[TQ] | None
        OBR.27 - Quantity / timing (TQ) NA rep S4.8.12.3

    obr_28 : list[str] | None
        OBR.28 - Result Copies To (CN) NA rep S4.5.1.28

    obr_29 : str | None
        OBR.29 - Parent Number (CM) NA S4.5.1.29

    obr_30 : str | None
        OBR.30 - Transportation Mode (ID) NA S4.5.1.30 | 0124 - TRANSPORTATION MODE

    obr_31 : list[CE] | None
        OBR.31 - Reason for Study (CE) NA rep S4.5.1.31

    obr_32 : str | None
        OBR.32 - Principal Result Interpreter (CM) NA S4.5.1.32

    obr_33 : list[str] | None
        OBR.33 - Assistant Result Interpreter (CM) NA rep S4.5.1.33

    obr_34 : list[str] | None
        OBR.34 - Technician (CM) NA rep S4.5.1.34

    obr_35 : list[str] | None
        OBR.35 - Transcriptionist (CM) NA rep S4.5.1.35

    obr_36 : TS | None
        OBR.36 - Scheduled date / time (TS) NA S4.5.1.36
    """

    obr_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_1",
            "set_id_observation_request",
            "OBR.1",
        ),
        serialization_alias="OBR.1",
        title="Set ID - Observation Request",
        description="NA | Item #00237 | LEN:4",
    )

    obr_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_2",
            "placer_order_number",
            "OBR.2",
        ),
        serialization_alias="OBR.2",
        title="Placer Order Number",
        description="C | Item #00216",
    )

    obr_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_3",
            "filler_order_number",
            "OBR.3",
        ),
        serialization_alias="OBR.3",
        title="Filler Order Number",
        description="C | Item #00217",
    )

    obr_4: CE = Field(
        validation_alias=AliasChoices(
            "obr_4",
            "universal_service_id",
            "OBR.4",
        ),
        serialization_alias="OBR.4",
        title="Universal Service ID",
        description="R | Item #00238",
    )

    obr_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_5",
            "priority_not_used",
            "OBR.5",
        ),
        serialization_alias="OBR.5",
        title="Priority (not used)",
        description="NA | Item #00239 | LEN:2",
    )

    obr_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_6",
            "requested_date_time_not_used",
            "OBR.6",
        ),
        serialization_alias="OBR.6",
        title="Requested date / time (not used)",
        description="NA | Item #00240",
    )

    obr_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_7",
            "observation_date_time",
            "OBR.7",
        ),
        serialization_alias="OBR.7",
        title="Observation date / time",
        description="C | Item #00241",
    )

    obr_8: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_8",
            "observation_end_date_time",
            "OBR.8",
        ),
        serialization_alias="OBR.8",
        title="Observation end date / time",
        description="C | Item #00242",
    )

    obr_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_9",
            "collection_volume",
            "OBR.9",
        ),
        serialization_alias="OBR.9",
        title="Collection Volume",
        description="C | Item #00243",
    )

    obr_10: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_10",
            "collector_identifier",
            "OBR.10",
        ),
        serialization_alias="OBR.10",
        title="Collector Identifier",
        description="NA | Item #00244",
    )

    obr_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_11",
            "specimen_action_code",
            "OBR.11",
        ),
        serialization_alias="OBR.11",
        title="Specimen action code",
        description="NA | Item #00245 | Table 0065 - ACTION CODE | LEN:1",
    )

    obr_12: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_12",
            "danger_code",
            "OBR.12",
        ),
        serialization_alias="OBR.12",
        title="Danger Code",
        description="NA | Item #00246",
    )

    obr_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_13",
            "relevant_clinical_information",
            "OBR.13",
        ),
        serialization_alias="OBR.13",
        title="Relevant clinical information",
        description="NA | Item #00247 | LEN:300",
    )

    obr_14: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_14",
            "specimen_received_date_time",
            "OBR.14",
        ),
        serialization_alias="OBR.14",
        title="Specimen received date / time",
        description="C | Item #00248",
    )

    obr_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_15",
            "specimen_source",
            "OBR.15",
        ),
        serialization_alias="OBR.15",
        title="Specimen source",
        description="NA | Item #00249 | Table 0070 - SOURCE OF SPECIMEN",
    )

    obr_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_16",
            "ordering_provider",
            "OBR.16",
        ),
        serialization_alias="OBR.16",
        title="Ordering Provider",
        description="NA | Item #00226",
    )

    obr_17: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_17",
            "order_callback_phone_number",
            "OBR.17",
        ),
        serialization_alias="OBR.17",
        title="Order Callback Phone Number",
        description="NA | Item #00250 | LEN:40",
    )

    obr_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_18",
            "placer_field_1",
            "OBR.18",
        ),
        serialization_alias="OBR.18",
        title="Placer field 1",
        description="NA | Item #00251 | LEN:60",
    )

    obr_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_19",
            "placer_field_2",
            "OBR.19",
        ),
        serialization_alias="OBR.19",
        title="Placer field 2",
        description="NA | Item #00252 | LEN:60",
    )

    obr_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_20",
            "filler_field_1",
            "OBR.20",
        ),
        serialization_alias="OBR.20",
        title="Filler Field 1",
        description="NA | Item #00253 | LEN:60",
    )

    obr_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_21",
            "filler_field_2",
            "OBR.21",
        ),
        serialization_alias="OBR.21",
        title="Filler Field 2",
        description="NA | Item #00254 | LEN:60",
    )

    obr_22: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_22",
            "results_report_status_change_date_time",
            "OBR.22",
        ),
        serialization_alias="OBR.22",
        title="Results report / status change - date / time",
        description="C | Item #00255",
    )

    obr_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_23",
            "charge_to_practice",
            "OBR.23",
        ),
        serialization_alias="OBR.23",
        title="Charge to Practice",
        description="NA | Item #00256",
    )

    obr_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_24",
            "diagnostic_service_section_id",
            "OBR.24",
        ),
        serialization_alias="OBR.24",
        title="Diagnostic service section ID",
        description=(
            "NA | Item #00257 | Table 0074 - DIAGNOSTIC SERVICE SECTION ID | "
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
        title="Result Status",
        description=(
            "C | Item #00258 | Table 0123 - RESULT STATUS - OBR | LEN:1"
        ),
    )

    obr_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_26",
            "parent_result",
            "OBR.26",
        ),
        serialization_alias="OBR.26",
        title="Parent Result",
        description="NA | Item #00259",
    )

    obr_27: Optional[List[TQ]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_27",
            "quantity_timing",
            "OBR.27",
        ),
        serialization_alias="OBR.27",
        title="Quantity / timing",
        description="NA | Item #00221",
    )

    obr_28: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_28",
            "result_copies_to",
            "OBR.28",
        ),
        serialization_alias="OBR.28",
        title="Result Copies To",
        description="NA | Item #00260",
    )

    obr_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_29",
            "parent_number",
            "OBR.29",
        ),
        serialization_alias="OBR.29",
        title="Parent Number",
        description="NA | Item #00261",
    )

    obr_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_30",
            "transportation_mode",
            "OBR.30",
        ),
        serialization_alias="OBR.30",
        title="Transportation Mode",
        description=(
            "NA | Item #00262 | Table 0124 - TRANSPORTATION MODE | LEN:20"
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
        title="Reason for Study",
        description="NA | Item #00263",
    )

    obr_32: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_32",
            "principal_result_interpreter",
            "OBR.32",
        ),
        serialization_alias="OBR.32",
        title="Principal Result Interpreter",
        description="NA | Item #00264",
    )

    obr_33: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_33",
            "assistant_result_interpreter",
            "OBR.33",
        ),
        serialization_alias="OBR.33",
        title="Assistant Result Interpreter",
        description="NA | Item #00265",
    )

    obr_34: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_34",
            "technician",
            "OBR.34",
        ),
        serialization_alias="OBR.34",
        title="Technician",
        description="NA | Item #00266",
    )

    obr_35: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_35",
            "transcriptionist",
            "OBR.35",
        ),
        serialization_alias="OBR.35",
        title="Transcriptionist",
        description="NA | Item #00267",
    )

    obr_36: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_36",
            "scheduled_date_time",
            "OBR.36",
        ),
        serialization_alias="OBR.36",
        title="Scheduled date / time",
        description="NA | Item #00268",
    )

    @field_validator("obr_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
