"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OBR
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

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

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class OBR(HL7Model):
    """Observation Request (S7.4.1).

    Attributes
    ----------
    obr_1 : str | None
        OBR.1 - Set ID - OBR (SI) O S7.4.1.1

    obr_2 : EI | None
        OBR.2 - Placer Order Number (EI) C S10.6.2.26

    obr_3 : EI | None
        OBR.3 - Filler Order Number (EI) C S10.6.2.27

    obr_4 : CE
        OBR.4 - Universal Service Identifier (CE) R S13.4.10.1

    obr_5 : str | None
        OBR.5 - Priority (ID) O S7.4.1.5

    obr_6 : TS | None
        OBR.6 - Requested Date/Time (TS) O S7.4.1.6

    obr_7 : TS | None
        OBR.7 - Observation Date/Time # (TS) C S7.4.1.7

    obr_8 : TS | None
        OBR.8 - Observation End Date/Time # (TS) O S7.4.1.8

    obr_9 : CQ | None
        OBR.9 - Collection Volume * (CQ) O S7.4.1.9

    obr_10 : list[XCN] | None
        OBR.10 - Collector Identifier * (XCN) O rep S7.4.1.10

    obr_11 : str | None
        OBR.11 - Specimen Action Code * (ID) O S7.4.1.11 | 0065 - Specimen action code

    obr_12 : CE | None
        OBR.12 - Danger Code (CE) O S7.4.1.12

    obr_13 : str | None
        OBR.13 - Relevant Clinical Info. (ST) O S7.4.1.13

    obr_14 : TS | None
        OBR.14 - Specimen Received Date/Time * (TS) C S7.4.1.14

    obr_15 : SPS | None
        OBR.15 - Specimen Source (SPS) O S13.4.9.3 | 0070 - Specimen source codes

    obr_16 : list[XCN] | None
        OBR.16 - Ordering Provider (XCN) O rep S7.4.1.16

    obr_17 : list[XTN] | None
        OBR.17 - Order Callback Phone Number (XTN) O rep S7.4.1.17

    obr_18 : str | None
        OBR.18 - Placer Field 1 (ST) O S7.4.1.18

    obr_19 : str | None
        OBR.19 - Placer Field 2 (ST) O S7.4.1.19

    obr_20 : str | None
        OBR.20 - Filler Field 1 + (ST) O S7.4.1.20

    obr_21 : str | None
        OBR.21 - Filler Field 2 + (ST) O S7.4.1.21

    obr_22 : TS | None
        OBR.22 - Results Rpt/Status Chng - Date/Time + (TS) C S7.4.1.22

    obr_23 : MOC | None
        OBR.23 - Charge to Practice + (MOC) O S7.4.1.23

    obr_24 : str | None
        OBR.24 - Diagnostic Serv Sect ID (ID) O S7.4.1.24 | 0074 - Diagnostic service section ID

    obr_25 : str | None
        OBR.25 - Result Status + (ID) C S7.4.1.25 | 0123 - Result status

    obr_26 : PRL | None
        OBR.26 - Parent Result + (PRL) O S7.4.1.26

    obr_27 : list[TQ] | None
        OBR.27 - Quantity/Timing (TQ) O rep S7.4.1.27

    obr_28 : list[XCN] | None
        OBR.28 - Result Copies To (XCN) O rep S7.4.1.28

    obr_29 : EIP | None
        OBR.29 - Parent (EIP) O S7.4.1.29

    obr_30 : str | None
        OBR.30 - Transportation Mode (ID) O S7.4.1.30 | 0124 - Transportation mode

    obr_31 : list[CE] | None
        OBR.31 - Reason for Study (CE) O rep S7.4.1.31

    obr_32 : NDL | None
        OBR.32 - Principal Result Interpreter + (NDL) O S7.4.1.32

    obr_33 : list[NDL] | None
        OBR.33 - Assistant Result Interpreter + (NDL) O rep S7.4.1.33

    obr_34 : list[NDL] | None
        OBR.34 - Technician + (NDL) O rep S7.4.1.34

    obr_35 : list[NDL] | None
        OBR.35 - Transcriptionist + (NDL) O rep S7.4.1.35

    obr_36 : TS | None
        OBR.36 - Scheduled Date/Time + (TS) O S7.4.1.36

    obr_37 : str | None
        OBR.37 - Number of Sample Containers * (NM) O S7.4.1.37

    obr_38 : list[CE] | None
        OBR.38 - Transport Logistics of Collected Sample * (CE) O rep S7.4.1.38

    obr_39 : list[CE] | None
        OBR.39 - Collector's Comment * (CE) O rep S7.4.1.39

    obr_40 : CE | None
        OBR.40 - Transport Arrangement Responsibility (CE) O S7.4.1.40

    obr_41 : str | None
        OBR.41 - Transport Arranged (ID) O S7.4.1.41 | 0224 - Transport arranged

    obr_42 : str | None
        OBR.42 - Escort Required (ID) O S7.4.1.42 | 0225 - Escort required

    obr_43 : list[CE] | None
        OBR.43 - Planned Patient Transport Comment (CE) O rep S7.4.1.43

    obr_44 : CE | None
        OBR.44 - Procedure Code (CE) O S8.10.2.7 | 0088 - Procedure Code

    obr_45 : list[CE] | None
        OBR.45 - Procedure Code Modifier (CE) O rep S7.4.1.45 | 0340 - Procedure Code modifier

    obr_46 : list[CE] | None
        OBR.46 - Placer Supplemental Service Information (CE) O rep S10.6.4.11 | 0411 - Supplemental service information values

    obr_47 : list[CE] | None
        OBR.47 - Filler Supplemental Service Information (CE) O rep S10.6.4.12 | 0411 - Supplemental service information values
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
        description="O | Item #00237 | LEN:4",
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
        description="C | Item #00216",
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
        description="C | Item #00217",
    )

    obr_4: CE = Field(
        validation_alias=AliasChoices(
            "obr_4",
            "universal_service_identifier",
            "OBR.4",
        ),
        serialization_alias="OBR.4",
        title="Universal Service Identifier",
        description="R | Item #00238",
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
        description="O | Item #00239 | LEN:2",
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
        description="O | Item #00240",
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
        title="Observation End Date/Time #",
        description="O | Item #00242",
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
        description="O | Item #00243",
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
        description="O | Item #00244",
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
        description=(
            "O | Item #00245 | Table 0065 - Specimen action code | LEN:1"
        ),
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
        description="O | Item #00246",
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
        description="O | Item #00247 | LEN:300",
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
        description="C | Item #00248",
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
        description="O | Item #00249 | Table 0070 - Specimen source codes",
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
        description="O | Item #00226",
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
        description="O | Item #00250",
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
        description="O | Item #00251 | LEN:60",
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
        description="O | Item #00252 | LEN:60",
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
        description="O | Item #00253 | LEN:60",
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
        description="O | Item #00254 | LEN:60",
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
        description="C | Item #00255",
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
        description="O | Item #00256",
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
        description=(
            "O | Item #00257 | Table 0074 - Diagnostic service section ID | "
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
        title="Result Status +",
        description="C | Item #00258 | Table 0123 - Result status | LEN:1",
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
        description="O | Item #00259",
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
        description="O | Item #00221",
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
        description="O | Item #00260",
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
        description="O | Item #00261",
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
            "O | Item #00262 | Table 0124 - Transportation mode | LEN:20"
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
        description="O | Item #00263",
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
        description="O | Item #00264",
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
        description="O | Item #00265",
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
        description="O | Item #00266",
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
        description="O | Item #00267",
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
        description="O | Item #00268",
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
        description="O | Item #01028 | LEN:4",
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
        description="O | Item #01029",
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
        description="O | Item #01030",
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
        description="O | Item #01031",
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
        description=(
            "O | Item #01032 | Table 0224 - Transport arranged | LEN:30"
        ),
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
        description="O | Item #01033 | Table 0225 - Escort required | LEN:1",
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
        description="O | Item #01034",
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
        description="O | Item #00393 | Table 0088 - Procedure Code",
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
        description="O | Item #01316 | Table 0340 - Procedure Code modifier",
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
        description=(
            "O | Item #01474 | Table 0411 - Supplemental service information "
            "values"
        ),
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
        description=(
            "O | Item #01475 | Table 0411 - Supplemental service information "
            "values"
        ),
    )

    @field_validator("obr_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("obr_37", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
