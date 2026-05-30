"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OBR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.EI import EI
from ..datatypes.EIP import EIP
from ..datatypes.MOC import MOC
from ..datatypes.NDL import NDL
from ..datatypes.PRL import PRL
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class OBR(HL7Model):
    """HL7 v2 OBR segment.

    Attributes
    ----------
    obr_1 : str | None
        OBR.1 (opt) - Set ID - OBR (SI)

    obr_2 : EI | None
        OBR.2 (opt) - Placer Order Number (EI)

    obr_3 : EI | None
        OBR.3 (opt) - Filler Order Number (EI)

    obr_4 : CWE
        OBR.4 (req) - Universal Service Identifier (CWE)

    obr_7 : str | None
        OBR.7 (opt) - Observation Date/Time # (DTM)

    obr_8 : str | None
        OBR.8 (opt) - Observation End Date/Time # (DTM)

    obr_9 : CQ | None
        OBR.9 (opt) - Collection Volume * (CQ)

    obr_10 : list[XCN] | None
        OBR.10 (opt, rep) - Collector Identifier * (XCN)

    obr_11 : str | None
        OBR.11 (opt) - Specimen Action Code * (ID)

    obr_12 : CWE | None
        OBR.12 (opt) - Danger Code (CWE)

    obr_13 : str | None
        OBR.13 (opt) - Relevant Clinical Information (ST)

    obr_16 : list[XCN] | None
        OBR.16 (opt, rep) - Ordering Provider (XCN)

    obr_17 : list[XTN] | None
        OBR.17 (opt, rep) - Order Callback Phone Number (XTN)

    obr_18 : str | None
        OBR.18 (opt) - Placer Field 1 (ST)

    obr_19 : str | None
        OBR.19 (opt) - Placer Field 2 (ST)

    obr_20 : str | None
        OBR.20 (opt) - Filler Field 1 + (ST)

    obr_21 : str | None
        OBR.21 (opt) - Filler Field 2 + (ST)

    obr_22 : str | None
        OBR.22 (opt) - Results Rpt/Status Chng - Date/Time + (DTM)

    obr_23 : MOC | None
        OBR.23 (opt) - Charge to Practice + (MOC)

    obr_24 : str | None
        OBR.24 (opt) - Diagnostic Serv Sect ID (ID)

    obr_25 : str | None
        OBR.25 (opt) - Result Status + (ID)

    obr_26 : PRL | None
        OBR.26 (opt) - Parent Result + (PRL)

    obr_28 : list[XCN] | None
        OBR.28 (opt, rep) - Result Copies To (XCN)

    obr_29 : EIP | None
        OBR.29 (opt) - Parent (EIP)

    obr_30 : str | None
        OBR.30 (opt) - Transportation Mode (ID)

    obr_31 : list[CWE] | None
        OBR.31 (opt, rep) - Reason for Study (CWE)

    obr_32 : NDL | None
        OBR.32 (opt) - Principal Result Interpreter + (NDL)

    obr_33 : list[NDL] | None
        OBR.33 (opt, rep) - Assistant Result Interpreter + (NDL)

    obr_34 : list[NDL] | None
        OBR.34 (opt, rep) - Technician + (NDL)

    obr_35 : list[NDL] | None
        OBR.35 (opt, rep) - Transcriptionist + (NDL)

    obr_36 : str | None
        OBR.36 (opt) - Scheduled Date/Time + (DTM)

    obr_37 : str | None
        OBR.37 (opt) - Number of Sample Containers * (NM)

    obr_38 : list[CWE] | None
        OBR.38 (opt, rep) - Transport Logistics of Collected Sample * (CWE)

    obr_39 : list[CWE] | None
        OBR.39 (opt, rep) - Collector's Comment * (CWE)

    obr_40 : CWE | None
        OBR.40 (opt) - Transport Arrangement Responsibility (CWE)

    obr_41 : str | None
        OBR.41 (opt) - Transport Arranged (ID)

    obr_42 : str | None
        OBR.42 (opt) - Escort Required (ID)

    obr_43 : list[CWE] | None
        OBR.43 (opt, rep) - Planned Patient Transport Comment (CWE)

    obr_44 : CNE | None
        OBR.44 (opt) - Procedure Code (CNE)

    obr_45 : list[CNE] | None
        OBR.45 (opt, rep) - Procedure Code Modifier (CNE)

    obr_46 : list[CWE] | None
        OBR.46 (opt, rep) - Placer Supplemental Service Information (CWE)

    obr_47 : list[CWE] | None
        OBR.47 (opt, rep) - Filler Supplemental Service Information (CWE)

    obr_48 : CWE | None
        OBR.48 (opt) - Medically Necessary Duplicate Procedure Reason (CWE)

    obr_49 : CWE | None
        OBR.49 (opt) - Result Handling (CWE)

    obr_50 : CWE | None
        OBR.50 (opt) - Parent Universal Service Identifier (CWE)

    obr_51 : EI | None
        OBR.51 (opt) - Observation Group ID (EI)

    obr_52 : EI | None
        OBR.52 (opt) - Parent Observation Group ID (EI)

    obr_53 : list[CX] | None
        OBR.53 (opt, rep) - Alternate Placer Order Number (CX)
    """

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

    obr_4: CWE = Field(
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

    obr_7: Optional[str] = Field(
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

    obr_8: Optional[str] = Field(
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

    obr_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_12",
            "danger_code",
            "OBR.12",
        ),
        serialization_alias="OBR.12",
        title="Danger Code",
        description="Item #246 | Table HL79999",
    )

    obr_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_13",
            "relevant_clinical_information",
            "OBR.13",
        ),
        serialization_alias="OBR.13",
        title="Relevant Clinical Information",
        description="Item #247",
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

    obr_22: Optional[str] = Field(
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

    obr_31: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_31",
            "reason_for_study",
            "OBR.31",
        ),
        serialization_alias="OBR.31",
        title="Reason for Study",
        description="Item #263 | Table HL79999",
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

    obr_36: Optional[str] = Field(
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

    obr_38: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_38",
            "transport_logistics_of_collected_sample",
            "OBR.38",
        ),
        serialization_alias="OBR.38",
        title="Transport Logistics of Collected Sample *",
        description="Item #1029 | Table HL79999",
    )

    obr_39: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_39",
            "collector_s_comment",
            "OBR.39",
        ),
        serialization_alias="OBR.39",
        title="Collector's Comment *",
        description="Item #1030 | Table HL79999",
    )

    obr_40: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_40",
            "transport_arrangement_responsibility",
            "OBR.40",
        ),
        serialization_alias="OBR.40",
        title="Transport Arrangement Responsibility",
        description="Item #1031 | Table HL79999",
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

    obr_43: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_43",
            "planned_patient_transport_comment",
            "OBR.43",
        ),
        serialization_alias="OBR.43",
        title="Planned Patient Transport Comment",
        description="Item #1034 | Table HL79999",
    )

    obr_44: Optional[CNE] = Field(
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

    obr_45: Optional[List[CNE]] = Field(
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

    obr_46: Optional[List[CWE]] = Field(
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

    obr_47: Optional[List[CWE]] = Field(
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

    obr_48: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_48",
            "medically_necessary_duplicate_procedure_reason",
            "OBR.48",
        ),
        serialization_alias="OBR.48",
        title="Medically Necessary Duplicate Procedure Reason",
        description="Item #1646 | Table HL70476",
    )

    obr_49: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_49",
            "result_handling",
            "OBR.49",
        ),
        serialization_alias="OBR.49",
        title="Result Handling",
        description="Item #1647 | Table HL70507",
    )

    obr_50: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_50",
            "parent_universal_service_identifier",
            "OBR.50",
        ),
        serialization_alias="OBR.50",
        title="Parent Universal Service Identifier",
        description="Item #2286",
    )

    obr_51: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_51",
            "observation_group_id",
            "OBR.51",
        ),
        serialization_alias="OBR.51",
        title="Observation Group ID",
        description="Item #2307",
    )

    obr_52: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_52",
            "parent_observation_group_id",
            "OBR.52",
        ),
        serialization_alias="OBR.52",
        title="Parent Observation Group ID",
        description="Item #2308",
    )

    obr_53: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obr_53",
            "alternate_placer_order_number",
            "OBR.53",
        ),
        serialization_alias="OBR.53",
        title="Alternate Placer Order Number",
        description="Item #3303",
    )

    model_config = {"populate_by_name": True}
