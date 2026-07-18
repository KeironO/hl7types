"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: SCD
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CNE import CNE
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.SN import SN
from ..datatypes.XCN import XCN

_RE_TM = re.compile(r'([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class SCD(HL7Model):
    """Anti-Microbial Cycle Data (S17.7.4).

    Attributes
    ----------
    scd_1 : str | None
        SCD.1 - Cycle Start Time (TM) O S17.7.4.1

    scd_2 : str | None
        SCD.2 - Cycle Count (NM) O S17.7.4.2

    scd_3 : CQ | None
        SCD.3 - Temp Max (CQ) O S17.7.4.3

    scd_4 : CQ | None
        SCD.4 - Temp Min (CQ) O S17.7.4.4

    scd_5 : str | None
        SCD.5 - Load Number (NM) O S17.7.4.5

    scd_6 : CQ | None
        SCD.6 - Condition Time (CQ) O S17.7.4.6

    scd_7 : CQ | None
        SCD.7 - Sterilize Time (CQ) O S17.7.4.7

    scd_8 : CQ | None
        SCD.8 - Exhaust Time (CQ) O S17.7.4.8

    scd_9 : CQ | None
        SCD.9 - Total Cycle Time (CQ) O S17.7.4.9

    scd_10 : CWE | None
        SCD.10 - Device Status (CWE) O S17.7.4.10 | 0682 - Device Status

    scd_11 : str | None
        SCD.11 - Cycle Start Date/Time (DTM) O S17.7.4.11

    scd_12 : CQ | None
        SCD.12 - Dry Time (CQ) O S17.7.4.12

    scd_13 : CQ | None
        SCD.13 - Leak Rate (CQ) O S17.7.4.13

    scd_14 : CQ | None
        SCD.14 - Control Temperature (CQ) O S17.7.4.14

    scd_15 : CQ | None
        SCD.15 - Sterilizer Temperature (CQ) O S17.7.4.15

    scd_16 : str | None
        SCD.16 - Cycle Complete Time (TM) O S17.7.4.16

    scd_17 : CQ | None
        SCD.17 - Under Temperature (CQ) O S17.7.4.17

    scd_18 : CQ | None
        SCD.18 - Over Temperature (CQ) O S17.7.4.18

    scd_19 : CNE | None
        SCD.19 - Abort Cycle (CNE) O S17.7.4.19 | 0532 - Expanded Yes/no Indicator

    scd_20 : CNE | None
        SCD.20 - Alarm (CNE) O S17.7.4.20 | 0532 - Expanded Yes/no Indicator

    scd_21 : CNE | None
        SCD.21 - Long in Charge Phase (CNE) O S17.7.4.21 | 0532 - Expanded Yes/no Indicator

    scd_22 : CNE | None
        SCD.22 - Long in Exhaust Phase (CNE) O S17.7.4.22 | 0532 - Expanded Yes/no Indicator

    scd_23 : CNE | None
        SCD.23 - Long in Fast Exhaust Phase (CNE) O S17.7.4.23 | 0532 - Expanded Yes/no Indicator

    scd_24 : CNE | None
        SCD.24 - Reset (CNE) O S17.7.4.24 | 0532 - Expanded Yes/no Indicator

    scd_25 : XCN | None
        SCD.25 - Operator - Unload (XCN) O S17.7.4.25

    scd_26 : CNE | None
        SCD.26 - Door Open (CNE) O S17.7.4.26 | 0532 - Expanded Yes/no Indicator

    scd_27 : CNE | None
        SCD.27 - Reading Failure (CNE) O S17.7.4.27 | 0532 - Expanded Yes/no Indicator

    scd_28 : CWE | None
        SCD.28 - Cycle Type (CWE) O S17.7.4.28 | 0702 - Cycle Type

    scd_29 : CQ | None
        SCD.29 - Thermal Rinse Time (CQ) O S17.7.4.29

    scd_30 : CQ | None
        SCD.30 - Wash Time (CQ) O S17.7.4.30

    scd_31 : CQ | None
        SCD.31 - Injection Rate (CQ) O S17.7.4.31

    scd_32 : CNE | None
        SCD.32 - Procedure Code (CNE) O S17.4.1.14 | 0088 - Procedure Code

    scd_33 : list[CX] | None
        SCD.33 - Patient Identifier List (CX) O rep S17.7.4.33

    scd_34 : XCN | None
        SCD.34 - Attending Doctor (XCN) O S17.7.4.34 | 0010 - Physician ID

    scd_35 : SN | None
        SCD.35 - Dilution Factor (SN) O S13.4.3.29

    scd_36 : CQ | None
        SCD.36 - Fill Time (CQ) O S17.7.4.36

    scd_37 : CQ | None
        SCD.37 - Inlet Temperature (CQ) O S17.7.4.37
    """

    scd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_1",
            "cycle_start_time",
            "SCD.1",
        ),
        serialization_alias="SCD.1",
        title="Cycle Start Time",
        description="O | Item #02104",
    )

    scd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_2",
            "cycle_count",
            "SCD.2",
        ),
        serialization_alias="SCD.2",
        title="Cycle Count",
        description="O | Item #02105",
    )

    scd_3: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_3",
            "temp_max",
            "SCD.3",
        ),
        serialization_alias="SCD.3",
        title="Temp Max",
        description="O | Item #02106",
    )

    scd_4: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_4",
            "temp_min",
            "SCD.4",
        ),
        serialization_alias="SCD.4",
        title="Temp Min",
        description="O | Item #02107",
    )

    scd_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_5",
            "load_number",
            "SCD.5",
        ),
        serialization_alias="SCD.5",
        title="Load Number",
        description="O | Item #02108",
    )

    scd_6: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_6",
            "condition_time",
            "SCD.6",
        ),
        serialization_alias="SCD.6",
        title="Condition Time",
        description="O | Item #02109",
    )

    scd_7: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_7",
            "sterilize_time",
            "SCD.7",
        ),
        serialization_alias="SCD.7",
        title="Sterilize Time",
        description="O | Item #02110",
    )

    scd_8: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_8",
            "exhaust_time",
            "SCD.8",
        ),
        serialization_alias="SCD.8",
        title="Exhaust Time",
        description="O | Item #02111",
    )

    scd_9: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_9",
            "total_cycle_time",
            "SCD.9",
        ),
        serialization_alias="SCD.9",
        title="Total Cycle Time",
        description="O | Item #02112",
    )

    scd_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_10",
            "device_status",
            "SCD.10",
        ),
        serialization_alias="SCD.10",
        title="Device Status",
        description="O | Item #02113 | Table 0682 - Device Status",
    )

    scd_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_11",
            "cycle_start_date_time",
            "SCD.11",
        ),
        serialization_alias="SCD.11",
        title="Cycle Start Date/Time",
        description="O | Item #02114",
    )

    scd_12: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_12",
            "dry_time",
            "SCD.12",
        ),
        serialization_alias="SCD.12",
        title="Dry Time",
        description="O | Item #02115",
    )

    scd_13: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_13",
            "leak_rate",
            "SCD.13",
        ),
        serialization_alias="SCD.13",
        title="Leak Rate",
        description="O | Item #02116",
    )

    scd_14: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_14",
            "control_temperature",
            "SCD.14",
        ),
        serialization_alias="SCD.14",
        title="Control Temperature",
        description="O | Item #02117",
    )

    scd_15: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_15",
            "sterilizer_temperature",
            "SCD.15",
        ),
        serialization_alias="SCD.15",
        title="Sterilizer Temperature",
        description="O | Item #02118",
    )

    scd_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_16",
            "cycle_complete_time",
            "SCD.16",
        ),
        serialization_alias="SCD.16",
        title="Cycle Complete Time",
        description="O | Item #02119",
    )

    scd_17: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_17",
            "under_temperature",
            "SCD.17",
        ),
        serialization_alias="SCD.17",
        title="Under Temperature",
        description="O | Item #02120",
    )

    scd_18: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_18",
            "over_temperature",
            "SCD.18",
        ),
        serialization_alias="SCD.18",
        title="Over Temperature",
        description="O | Item #02121",
    )

    scd_19: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_19",
            "abort_cycle",
            "SCD.19",
        ),
        serialization_alias="SCD.19",
        title="Abort Cycle",
        description="O | Item #02122 | Table 0532 - Expanded Yes/no Indicator",
    )

    scd_20: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_20",
            "alarm",
            "SCD.20",
        ),
        serialization_alias="SCD.20",
        title="Alarm",
        description="O | Item #02123 | Table 0532 - Expanded Yes/no Indicator",
    )

    scd_21: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_21",
            "long_in_charge_phase",
            "SCD.21",
        ),
        serialization_alias="SCD.21",
        title="Long in Charge Phase",
        description="O | Item #02124 | Table 0532 - Expanded Yes/no Indicator",
    )

    scd_22: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_22",
            "long_in_exhaust_phase",
            "SCD.22",
        ),
        serialization_alias="SCD.22",
        title="Long in Exhaust Phase",
        description="O | Item #02125 | Table 0532 - Expanded Yes/no Indicator",
    )

    scd_23: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_23",
            "long_in_fast_exhaust_phase",
            "SCD.23",
        ),
        serialization_alias="SCD.23",
        title="Long in Fast Exhaust Phase",
        description="O | Item #02126 | Table 0532 - Expanded Yes/no Indicator",
    )

    scd_24: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_24",
            "reset",
            "SCD.24",
        ),
        serialization_alias="SCD.24",
        title="Reset",
        description="O | Item #02127 | Table 0532 - Expanded Yes/no Indicator",
    )

    scd_25: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_25",
            "operator_unload",
            "SCD.25",
        ),
        serialization_alias="SCD.25",
        title="Operator - Unload",
        description="O | Item #02128",
    )

    scd_26: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_26",
            "door_open",
            "SCD.26",
        ),
        serialization_alias="SCD.26",
        title="Door Open",
        description="O | Item #02129 | Table 0532 - Expanded Yes/no Indicator",
    )

    scd_27: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_27",
            "reading_failure",
            "SCD.27",
        ),
        serialization_alias="SCD.27",
        title="Reading Failure",
        description="O | Item #02130 | Table 0532 - Expanded Yes/no Indicator",
    )

    scd_28: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_28",
            "cycle_type",
            "SCD.28",
        ),
        serialization_alias="SCD.28",
        title="Cycle Type",
        description="O | Item #02131 | Table 0702 - Cycle Type",
    )

    scd_29: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_29",
            "thermal_rinse_time",
            "SCD.29",
        ),
        serialization_alias="SCD.29",
        title="Thermal Rinse Time",
        description="O | Item #02132",
    )

    scd_30: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_30",
            "wash_time",
            "SCD.30",
        ),
        serialization_alias="SCD.30",
        title="Wash Time",
        description="O | Item #02133",
    )

    scd_31: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_31",
            "injection_rate",
            "SCD.31",
        ),
        serialization_alias="SCD.31",
        title="Injection Rate",
        description="O | Item #02134",
    )

    scd_32: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_32",
            "procedure_code",
            "SCD.32",
        ),
        serialization_alias="SCD.32",
        title="Procedure Code",
        description="O | Item #00393 | Table 0088 - Procedure Code",
    )

    scd_33: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_33",
            "patient_identifier_list",
            "SCD.33",
        ),
        serialization_alias="SCD.33",
        title="Patient Identifier List",
        description="O | Item #00106",
    )

    scd_34: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_34",
            "attending_doctor",
            "SCD.34",
        ),
        serialization_alias="SCD.34",
        title="Attending Doctor",
        description="O | Item #00137 | Table 0010 - Physician ID",
    )

    scd_35: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_35",
            "dilution_factor",
            "SCD.35",
        ),
        serialization_alias="SCD.35",
        title="Dilution Factor",
        description="O | Item #01356",
    )

    scd_36: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_36",
            "fill_time",
            "SCD.36",
        ),
        serialization_alias="SCD.36",
        title="Fill Time",
        description="O | Item #02139",
    )

    scd_37: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scd_37",
            "inlet_temperature",
            "SCD.37",
        ),
        serialization_alias="SCD.37",
        title="Inlet Temperature",
        description="O | Item #02140",
    )

    @field_validator("scd_1", "scd_16", mode='before')
    @classmethod
    def _validate_tm(cls, v: str) -> str:
        if not _RE_TM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 time")
        return v

    @field_validator("scd_2", "scd_5", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("scd_11", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
