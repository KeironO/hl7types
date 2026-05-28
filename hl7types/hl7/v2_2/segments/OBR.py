"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: OBR
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS


class OBR(BaseModel):
    """HL7 v2 OBR segment."""

    obr_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_1",
            "set_id_observation_request",
            "OBR.1",
        ),
        serialization_alias="OBR.1",
        title="Set ID - Observation Request",
        description="Item #237",
    )

    obr_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_2",
            "placer_order_number",
            "OBR.2",
        ),
        serialization_alias="OBR.2",
        title="Placer Order Number",
        description="Item #216",
    )

    obr_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_3",
            "filler_order_number",
            "OBR.3",
        ),
        serialization_alias="OBR.3",
        title="Filler Order Number",
        description="Item #217",
    )

    obr_4: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "obr_4",
            "universal_service_id",
            "OBR.4",
        ),
        serialization_alias="OBR.4",
        title="Universal Service ID",
        description="Item #238",
    )

    obr_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_5",
            "priority_not_used",
            "OBR.5",
        ),
        serialization_alias="OBR.5",
        title="Priority (not used)",
        description="Item #239",
    )

    obr_6: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_6",
            "requested_date_time_not_used",
            "OBR.6",
        ),
        serialization_alias="OBR.6",
        title="Requested date / time (not used)",
        description="Item #240",
    )

    obr_7: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_7",
            "observation_date_time",
            "OBR.7",
        ),
        serialization_alias="OBR.7",
        title="Observation date / time",
        description="Item #241",
    )

    obr_8: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_8",
            "observation_end_date_time",
            "OBR.8",
        ),
        serialization_alias="OBR.8",
        title="Observation end date / time",
        description="Item #242",
    )

    obr_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_9",
            "collection_volume",
            "OBR.9",
        ),
        serialization_alias="OBR.9",
        title="Collection Volume",
        description="Item #243",
    )

    obr_10: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_10",
            "collector_identifier",
            "OBR.10",
        ),
        serialization_alias="OBR.10",
        title="Collector Identifier",
        description="Item #244",
    )

    obr_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_11",
            "specimen_action_code",
            "OBR.11",
        ),
        serialization_alias="OBR.11",
        title="Specimen action code",
        description="Item #245 | Table HL70065",
    )

    obr_12: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_12",
            "danger_code",
            "OBR.12",
        ),
        serialization_alias="OBR.12",
        title="Danger Code",
        description="Item #246",
    )

    obr_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_13",
            "relevant_clinical_information",
            "OBR.13",
        ),
        serialization_alias="OBR.13",
        title="Relevant clinical information",
        description="Item #247",
    )

    obr_14: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_14",
            "specimen_received_date_time",
            "OBR.14",
        ),
        serialization_alias="OBR.14",
        title="Specimen received date / time",
        description="Item #248",
    )

    obr_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_15",
            "specimen_source",
            "OBR.15",
        ),
        serialization_alias="OBR.15",
        title="Specimen source",
        description="Item #249 | Table HL70070",
    )

    obr_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_16",
            "ordering_provider",
            "OBR.16",
        ),
        serialization_alias="OBR.16",
        title="Ordering Provider",
        description="Item #226",
    )

    obr_17: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_17",
            "order_callback_phone_number",
            "OBR.17",
        ),
        serialization_alias="OBR.17",
        title="Order Callback Phone Number",
        description="Item #250",
    )

    obr_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_18",
            "placer_field_1",
            "OBR.18",
        ),
        serialization_alias="OBR.18",
        title="Placer field 1",
        description="Item #251",
    )

    obr_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_19",
            "placer_field_2",
            "OBR.19",
        ),
        serialization_alias="OBR.19",
        title="Placer field 2",
        description="Item #252",
    )

    obr_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_20",
            "filler_field_1",
            "OBR.20",
        ),
        serialization_alias="OBR.20",
        title="Filler Field 1",
        description="Item #253",
    )

    obr_21: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_21",
            "filler_field_2",
            "OBR.21",
        ),
        serialization_alias="OBR.21",
        title="Filler Field 2",
        description="Item #254",
    )

    obr_22: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_22",
            "results_report_status_change_date_time",
            "OBR.22",
        ),
        serialization_alias="OBR.22",
        title="Results report / status change - date / time",
        description="Item #255",
    )

    obr_23: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_23",
            "charge_to_practice",
            "OBR.23",
        ),
        serialization_alias="OBR.23",
        title="Charge to Practice",
        description="Item #256",
    )

    obr_24: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_24",
            "diagnostic_service_section_id",
            "OBR.24",
        ),
        serialization_alias="OBR.24",
        title="Diagnostic service section ID",
        description="Item #257 | Table HL70074",
    )

    obr_25: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_25",
            "result_status",
            "OBR.25",
        ),
        serialization_alias="OBR.25",
        title="Result Status",
        description="Item #258 | Table HL70123",
    )

    obr_26: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_26",
            "parent_result",
            "OBR.26",
        ),
        serialization_alias="OBR.26",
        title="Parent Result",
        description="Item #259",
    )

    obr_27: list[TQ] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_27",
            "quantity_timing",
            "OBR.27",
        ),
        serialization_alias="OBR.27",
        title="Quantity / timing",
        description="Item #221",
    )

    obr_28: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_28",
            "result_copies_to",
            "OBR.28",
        ),
        serialization_alias="OBR.28",
        title="Result Copies To",
        description="Item #260",
    )

    obr_29: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_29",
            "parent_number",
            "OBR.29",
        ),
        serialization_alias="OBR.29",
        title="Parent Number",
        description="Item #261",
    )

    obr_30: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_30",
            "transportation_mode",
            "OBR.30",
        ),
        serialization_alias="OBR.30",
        title="Transportation Mode",
        description="Item #262 | Table HL70124",
    )

    obr_31: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_31",
            "reason_for_study",
            "OBR.31",
        ),
        serialization_alias="OBR.31",
        title="Reason for Study",
        description="Item #263",
    )

    obr_32: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_32",
            "principal_result_interpreter",
            "OBR.32",
        ),
        serialization_alias="OBR.32",
        title="Principal Result Interpreter",
        description="Item #264",
    )

    obr_33: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_33",
            "assistant_result_interpreter",
            "OBR.33",
        ),
        serialization_alias="OBR.33",
        title="Assistant Result Interpreter",
        description="Item #265",
    )

    obr_34: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_34",
            "technician",
            "OBR.34",
        ),
        serialization_alias="OBR.34",
        title="Technician",
        description="Item #266",
    )

    obr_35: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_35",
            "transcriptionist",
            "OBR.35",
        ),
        serialization_alias="OBR.35",
        title="Transcriptionist",
        description="Item #267",
    )

    obr_36: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_36",
            "scheduled_date_time",
            "OBR.36",
        ),
        serialization_alias="OBR.36",
        title="Scheduled date / time",
        description="Item #268",
    )

    model_config = {"populate_by_name": True}
