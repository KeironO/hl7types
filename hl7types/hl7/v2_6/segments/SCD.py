"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: SCD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CNE import CNE
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.SN import SN
from ..datatypes.XCN import XCN


class SCD(HL7Model):
    """HL7 v2 SCD segment.

    Attributes
    ----------
    scd_1 : str | None
        SCD.1 (opt) - Cycle Start Time (TM)

    scd_2 : str | None
        SCD.2 (opt) - Cycle Count (NM)

    scd_3 : CQ | None
        SCD.3 (opt) - Temp Max (CQ)

    scd_4 : CQ | None
        SCD.4 (opt) - Temp Min (CQ)

    scd_5 : str | None
        SCD.5 (opt) - Load Number (NM)

    scd_6 : CQ | None
        SCD.6 (opt) - Condition Time (CQ)

    scd_7 : CQ | None
        SCD.7 (opt) - Sterilize Time (CQ)

    scd_8 : CQ | None
        SCD.8 (opt) - Exhaust Time (CQ)

    scd_9 : CQ | None
        SCD.9 (opt) - Total Cycle Time (CQ)

    scd_10 : CWE | None
        SCD.10 (opt) - Device Status (CWE)

    scd_11 : str | None
        SCD.11 (opt) - Cycle Start Date/Time (DTM)

    scd_12 : CQ | None
        SCD.12 (opt) - Dry Time (CQ)

    scd_13 : CQ | None
        SCD.13 (opt) - Leak Rate (CQ)

    scd_14 : CQ | None
        SCD.14 (opt) - Control Temperature (CQ)

    scd_15 : CQ | None
        SCD.15 (opt) - Sterilizer Temperature (CQ)

    scd_16 : str | None
        SCD.16 (opt) - Cycle Complete Time (TM)

    scd_17 : CQ | None
        SCD.17 (opt) - Under Temperature (CQ)

    scd_18 : CQ | None
        SCD.18 (opt) - Over Temperature (CQ)

    scd_19 : CNE | None
        SCD.19 (opt) - Abort Cycle (CNE)

    scd_20 : CNE | None
        SCD.20 (opt) - Alarm (CNE)

    scd_21 : CNE | None
        SCD.21 (opt) - Long in Charge Phase (CNE)

    scd_22 : CNE | None
        SCD.22 (opt) - Long in Exhaust Phase (CNE)

    scd_23 : CNE | None
        SCD.23 (opt) - Long in Fast Exhaust Phase (CNE)

    scd_24 : CNE | None
        SCD.24 (opt) - Reset (CNE)

    scd_25 : XCN | None
        SCD.25 (opt) - Operator - Unload (XCN)

    scd_26 : CNE | None
        SCD.26 (opt) - Door Open (CNE)

    scd_27 : CNE | None
        SCD.27 (opt) - Reading Failure (CNE)

    scd_28 : CWE | None
        SCD.28 (opt) - Cycle Type (CWE)

    scd_29 : CQ | None
        SCD.29 (opt) - Thermal Rinse Time (CQ)

    scd_30 : CQ | None
        SCD.30 (opt) - Wash Time (CQ)

    scd_31 : CQ | None
        SCD.31 (opt) - Injection Rate (CQ)

    scd_32 : CNE | None
        SCD.32 (opt) - Procedure Code (CNE)

    scd_33 : list[CX] | None
        SCD.33 (opt, rep) - Patient Identifier List (CX)

    scd_34 : XCN | None
        SCD.34 (opt) - Attending Doctor (XCN)

    scd_35 : SN | None
        SCD.35 (opt) - Dilution Factor (SN)

    scd_36 : CQ | None
        SCD.36 (opt) - Fill Time (CQ)

    scd_37 : CQ | None
        SCD.37 (opt) - Inlet Temperature (CQ)
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
        description="Item #2104",
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
        description="Item #2105",
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
        description="Item #2106",
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
        description="Item #2107",
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
        description="Item #2108",
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
        description="Item #2109",
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
        description="Item #2110",
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
        description="Item #2111",
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
        description="Item #2112",
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
        description="Item #2113 | Table HL70682",
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
        description="Item #2114",
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
        description="Item #2115",
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
        description="Item #2116",
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
        description="Item #2117",
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
        description="Item #2118",
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
        description="Item #2119",
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
        description="Item #2120",
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
        description="Item #2121",
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
        description="Item #2122 | Table HL70532",
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
        description="Item #2123 | Table HL70532",
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
        description="Item #2124 | Table HL70532",
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
        description="Item #2125 | Table HL70532",
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
        description="Item #2126 | Table HL70532",
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
        description="Item #2127 | Table HL70532",
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
        description="Item #2128",
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
        description="Item #2129 | Table HL70532",
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
        description="Item #2130 | Table HL70532",
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
        description="Item #2131 | Table HL70702",
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
        description="Item #2132",
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
        description="Item #2133",
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
        description="Item #2134",
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
        description="Item #393 | Table HL70088",
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
        description="Item #106",
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
        description="Item #137 | Table HL70010",
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
        description="Item #1356",
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
        description="Item #2139",
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
        description="Item #2140",
    )

    @field_validator("scd_1", "scd_16", mode='before')
    @classmethod
    def _validate_tm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 time")
        return v

    @field_validator("scd_2", "scd_5", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("scd_11", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
