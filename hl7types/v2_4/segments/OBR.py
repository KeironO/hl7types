"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OBR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CQ import CQ
from ..datatypes.EI import EI
from ..datatypes.EIP import EIP
from ..datatypes.MOC import MOC
from ..datatypes.NDL import NDL
from ..datatypes.PRL import PRL
from ..datatypes.SPS import SPS
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class OBR(BaseModel):
    """HL7 v2 OBR segment."""

    obr_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_1",
            "set_id_obr",
            "OBR.1",
        ),
        serialization_alias="OBR.1",
        title="Set ID - OBR",
        description="Item #237",
    )

    obr_2: Optional[EI] = Field(
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

    obr_3: Optional[EI] = Field(
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
            "universal_service_identifier",
            "OBR.4",
        ),
        serialization_alias="OBR.4",
        title="Universal Service Identifier",
        description="Item #238",
    )

    obr_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_5",
            "priority",
            "OBR.5",
        ),
        serialization_alias="OBR.5",
        title="Priority",
        description="Item #239",
    )

    obr_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_6",
            "requested_date_time",
            "OBR.6",
        ),
        serialization_alias="OBR.6",
        title="Requested Date/Time",
        description="Item #240",
    )

    obr_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_7",
            "observation_date_time",
            "OBR.7",
        ),
        serialization_alias="OBR.7",
        title="Observation Date/Time #",
        description="Item #241",
    )

    obr_8: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_8",
            "observation_end_date_time",
            "OBR.8",
        ),
        serialization_alias="OBR.8",
        title="Observation End Date/Time #",
        description="Item #242",
    )

    obr_9: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_9",
            "collection_volume",
            "OBR.9",
        ),
        serialization_alias="OBR.9",
        title="Collection Volume *",
        description="Item #243",
    )

    obr_10: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_10",
            "collector_identifier",
            "OBR.10",
        ),
        serialization_alias="OBR.10",
        title="Collector Identifier *",
        description="Item #244",
    )

    obr_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_11",
            "specimen_action_code",
            "OBR.11",
        ),
        serialization_alias="OBR.11",
        title="Specimen Action Code *",
        description="Item #245 | Table HL70065",
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
        description="Item #246",
    )

    obr_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_13",
            "relevant_clinical_info",
            "OBR.13",
        ),
        serialization_alias="OBR.13",
        title="Relevant Clinical Info.",
        description="Item #247",
    )

    obr_14: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_14",
            "specimen_received_date_time",
            "OBR.14",
        ),
        serialization_alias="OBR.14",
        title="Specimen Received Date/Time *",
        description="Item #248",
    )

    obr_15: Optional[SPS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_15",
            "specimen_source",
            "OBR.15",
        ),
        serialization_alias="OBR.15",
        title="Specimen Source",
        description="Item #249 | Table HL70070",
    )

    obr_16: Optional[List[XCN]] = Field(
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

    obr_17: Optional[List[XTN]] = Field(
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

    obr_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_18",
            "placer_field_1",
            "OBR.18",
        ),
        serialization_alias="OBR.18",
        title="Placer Field 1",
        description="Item #251",
    )

    obr_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_19",
            "placer_field_2",
            "OBR.19",
        ),
        serialization_alias="OBR.19",
        title="Placer Field 2",
        description="Item #252",
    )

    obr_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_20",
            "filler_field_1",
            "OBR.20",
        ),
        serialization_alias="OBR.20",
        title="Filler Field 1 +",
        description="Item #253",
    )

    obr_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_21",
            "filler_field_2",
            "OBR.21",
        ),
        serialization_alias="OBR.21",
        title="Filler Field 2 +",
        description="Item #254",
    )

    obr_22: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_22",
            "results_rpt_status_chng_date_time",
            "OBR.22",
        ),
        serialization_alias="OBR.22",
        title="Results Rpt/Status Chng - Date/Time +",
        description="Item #255",
    )

    obr_23: Optional[MOC] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_23",
            "charge_to_practice",
            "OBR.23",
        ),
        serialization_alias="OBR.23",
        title="Charge to Practice +",
        description="Item #256",
    )

    obr_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_24",
            "diagnostic_serv_sect_id",
            "OBR.24",
        ),
        serialization_alias="OBR.24",
        title="Diagnostic Serv Sect ID",
        description="Item #257 | Table HL70074",
    )

    obr_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_25",
            "result_status",
            "OBR.25",
        ),
        serialization_alias="OBR.25",
        title="Result Status +",
        description="Item #258 | Table HL70123",
    )

    obr_26: Optional[PRL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_26",
            "parent_result",
            "OBR.26",
        ),
        serialization_alias="OBR.26",
        title="Parent Result +",
        description="Item #259",
    )

    obr_27: Optional[List[TQ]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_27",
            "quantity_timing",
            "OBR.27",
        ),
        serialization_alias="OBR.27",
        title="Quantity/Timing",
        description="Item #221",
    )

    obr_28: Optional[List[XCN]] = Field(
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

    obr_29: Optional[EIP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_29",
            "parent",
            "OBR.29",
        ),
        serialization_alias="OBR.29",
        title="Parent",
        description="Item #261",
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
        description="Item #262 | Table HL70124",
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
        description="Item #263",
    )

    obr_32: Optional[NDL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_32",
            "principal_result_interpreter",
            "OBR.32",
        ),
        serialization_alias="OBR.32",
        title="Principal Result Interpreter +",
        description="Item #264",
    )

    obr_33: Optional[List[NDL]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_33",
            "assistant_result_interpreter",
            "OBR.33",
        ),
        serialization_alias="OBR.33",
        title="Assistant Result Interpreter +",
        description="Item #265",
    )

    obr_34: Optional[List[NDL]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_34",
            "technician",
            "OBR.34",
        ),
        serialization_alias="OBR.34",
        title="Technician +",
        description="Item #266",
    )

    obr_35: Optional[List[NDL]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_35",
            "transcriptionist",
            "OBR.35",
        ),
        serialization_alias="OBR.35",
        title="Transcriptionist +",
        description="Item #267",
    )

    obr_36: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_36",
            "scheduled_date_time",
            "OBR.36",
        ),
        serialization_alias="OBR.36",
        title="Scheduled Date/Time +",
        description="Item #268",
    )

    obr_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_37",
            "number_of_sample_containers",
            "OBR.37",
        ),
        serialization_alias="OBR.37",
        title="Number of Sample Containers *",
        description="Item #1028",
    )

    obr_38: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_38",
            "transport_logistics_of_collected_sample",
            "OBR.38",
        ),
        serialization_alias="OBR.38",
        title="Transport Logistics of Collected Sample *",
        description="Item #1029",
    )

    obr_39: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_39",
            "collector_s_comment",
            "OBR.39",
        ),
        serialization_alias="OBR.39",
        title="Collector's Comment *",
        description="Item #1030",
    )

    obr_40: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_40",
            "transport_arrangement_responsibility",
            "OBR.40",
        ),
        serialization_alias="OBR.40",
        title="Transport Arrangement Responsibility",
        description="Item #1031",
    )

    obr_41: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_41",
            "transport_arranged",
            "OBR.41",
        ),
        serialization_alias="OBR.41",
        title="Transport Arranged",
        description="Item #1032 | Table HL70224",
    )

    obr_42: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_42",
            "escort_required",
            "OBR.42",
        ),
        serialization_alias="OBR.42",
        title="Escort Required",
        description="Item #1033 | Table HL70225",
    )

    obr_43: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_43",
            "planned_patient_transport_comment",
            "OBR.43",
        ),
        serialization_alias="OBR.43",
        title="Planned Patient Transport Comment",
        description="Item #1034",
    )

    obr_44: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_44",
            "procedure_code",
            "OBR.44",
        ),
        serialization_alias="OBR.44",
        title="Procedure Code",
        description="Item #393 | Table HL70088",
    )

    obr_45: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_45",
            "procedure_code_modifier",
            "OBR.45",
        ),
        serialization_alias="OBR.45",
        title="Procedure Code Modifier",
        description="Item #1316 | Table HL70340",
    )

    obr_46: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_46",
            "placer_supplemental_service_information",
            "OBR.46",
        ),
        serialization_alias="OBR.46",
        title="Placer Supplemental Service Information",
        description="Item #1474 | Table HL70411",
    )

    obr_47: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_47",
            "filler_supplemental_service_information",
            "OBR.47",
        ),
        serialization_alias="OBR.47",
        title="Filler Supplemental Service Information",
        description="Item #1475 | Table HL70411",
    )

    model_config = {"populate_by_name": True}
