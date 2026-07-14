"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DRG
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.MO import MO
from ..datatypes.XPN import XPN


class DRG(HL7Model):
    """Diagnosis Related Group (S6.5.3).

    Attributes
    ----------
    drg_1 : CNE | None
        DRG.1 (opt) - Diagnostic Related Group (CNE) S6.5.3.1 | 0055 - Diagnosis Related Group

    drg_2 : str | None
        DRG.2 (opt) - DRG Assigned Date/Time (DTM) S6.5.3.2

    drg_3 : str | None
        DRG.3 (opt) - DRG Approval Indicator (ID) S6.5.3.3 | 0136 - Yes/no Indicator

    drg_4 : CWE | None
        DRG.4 (opt) - DRG Grouper Review Code (CWE) S6.5.3.4 | 0056 - DRG Grouper Review Code

    drg_5 : CWE | None
        DRG.5 (opt) - Outlier Type (CWE) S6.5.3.5 | 0083 - Outlier Type

    drg_6 : str | None
        DRG.6 (opt) - Outlier Days (NM) S6.5.3.6

    drg_7 : CP | None
        DRG.7 (opt) - Outlier Cost (CP) S6.5.15.5

    drg_8 : CWE | None
        DRG.8 (opt) - DRG Payor (CWE) S6.5.3.8 | 0229 - DRG Payor

    drg_9 : CP | None
        DRG.9 (opt) - Outlier Reimbursement (CP) S6.5.3.9

    drg_10 : str | None
        DRG.10 (opt) - Confidential Indicator (ID) S6.5.2.18 | 0136 - Yes/no Indicator

    drg_11 : CWE | None
        DRG.11 (opt) - DRG Transfer Type (CWE) S6.5.3.11 | 0415 - Transfer Type

    drg_12 : XPN | None
        DRG.12 (opt) - Name of Coder (XPN) S6.5.3.12

    drg_13 : CWE | None
        DRG.13 (opt) - Grouper Status (CWE) S6.5.3.13 | 0734 - Grouper Status

    drg_14 : CWE | None
        DRG.14 (opt) - PCCL Value Code (CWE) S6.5.3.14 | 0728 - CCL Value

    drg_15 : str | None
        DRG.15 (opt) - Effective Weight (NM) S6.5.3.15

    drg_16 : MO | None
        DRG.16 (opt) - Monetary Amount (MO) S6.5.3.16

    drg_17 : CWE | None
        DRG.17 (opt) - Status Patient (CWE) S6.5.3.17 | 0739 - DRG Status Patient

    drg_18 : str | None
        DRG.18 (opt) - Grouper Software Name (ST) S6.5.3.18

    drg_19 : str | None
        DRG.19 (opt) - Grouper Software Version (ST) S6.5.3.19

    drg_20 : CWE | None
        DRG.20 (opt) - Status Financial Calculation (CWE) S6.5.3.20 | 0742 - DRG Status Financial Calculation

    drg_21 : MO | None
        DRG.21 (opt) - Relative Discount/Surcharge (MO) S6.5.3.21

    drg_22 : MO | None
        DRG.22 (opt) - Basic Charge (MO) S6.5.3.22

    drg_23 : MO | None
        DRG.23 (opt) - Total Charge (MO) S6.5.3.23

    drg_24 : MO | None
        DRG.24 (opt) - Discount/Surcharge (MO) S6.5.3.24

    drg_25 : str | None
        DRG.25 (opt) - Calculated Days (NM) S6.5.3.25

    drg_26 : CWE | None
        DRG.26 (opt) - Status Gender (CWE) S6.5.3.26 | 0749 - DRG Grouping Status

    drg_27 : CWE | None
        DRG.27 (opt) - Status Age (CWE) S6.5.3.27 | 0749 - DRG Grouping Status

    drg_28 : CWE | None
        DRG.28 (opt) - Status Length of Stay (CWE) S6.5.3.28 | 0749 - DRG Grouping Status

    drg_29 : CWE | None
        DRG.29 (opt) - Status Same Day Flag (CWE) S6.5.3.29 | 0749 - DRG Grouping Status

    drg_30 : CWE | None
        DRG.30 (opt) - Status Separation Mode (CWE) S6.5.3.30 | 0749 - DRG Grouping Status

    drg_31 : CWE | None
        DRG.31 (opt) - Status Weight at Birth (CWE) S6.5.3.31 | 0755 - Status Weight At Birth

    drg_32 : CWE | None
        DRG.32 (opt) - Status Respiration Minutes (CWE) S6.5.3.32 | 0757 - DRG Status Respiration Minutes

    drg_33 : CWE | None
        DRG.33 (opt) - Status Admission (CWE) S6.5.3.33 | 0759 - Status Admission
    """

    drg_1: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_1",
            "diagnostic_related_group",
            "DRG.1",
        ),
        serialization_alias="DRG.1",
        title="Diagnostic Related Group",
        description="Item #382 | Table HL70055",
    )

    drg_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_2",
            "drg_assigned_date_time",
            "DRG.2",
        ),
        serialization_alias="DRG.2",
        title="DRG Assigned Date/Time",
        description="Item #769",
    )

    drg_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_3",
            "drg_approval_indicator",
            "DRG.3",
        ),
        serialization_alias="DRG.3",
        title="DRG Approval Indicator",
        description="Item #383 | Table HL70136",
    )

    drg_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_4",
            "drg_grouper_review_code",
            "DRG.4",
        ),
        serialization_alias="DRG.4",
        title="DRG Grouper Review Code",
        description="Item #384 | Table HL70056",
    )

    drg_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_5",
            "outlier_type",
            "DRG.5",
        ),
        serialization_alias="DRG.5",
        title="Outlier Type",
        description="Item #385 | Table HL70083",
    )

    drg_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_6",
            "outlier_days",
            "DRG.6",
        ),
        serialization_alias="DRG.6",
        title="Outlier Days",
        description="Item #386",
    )

    drg_7: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_7",
            "outlier_cost",
            "DRG.7",
        ),
        serialization_alias="DRG.7",
        title="Outlier Cost",
        description="Item #387",
    )

    drg_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_8",
            "drg_payor",
            "DRG.8",
        ),
        serialization_alias="DRG.8",
        title="DRG Payor",
        description="Item #770 | Table HL70229",
    )

    drg_9: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_9",
            "outlier_reimbursement",
            "DRG.9",
        ),
        serialization_alias="DRG.9",
        title="Outlier Reimbursement",
        description="Item #771",
    )

    drg_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_10",
            "confidential_indicator",
            "DRG.10",
        ),
        serialization_alias="DRG.10",
        title="Confidential Indicator",
        description="Item #767 | Table HL70136",
    )

    drg_11: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_11",
            "drg_transfer_type",
            "DRG.11",
        ),
        serialization_alias="DRG.11",
        title="DRG Transfer Type",
        description="Item #1500 | Table HL70415",
    )

    drg_12: Optional[XPN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_12",
            "name_of_coder",
            "DRG.12",
        ),
        serialization_alias="DRG.12",
        title="Name of Coder",
        description="Item #2156",
    )

    drg_13: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_13",
            "grouper_status",
            "DRG.13",
        ),
        serialization_alias="DRG.13",
        title="Grouper Status",
        description="Item #2157 | Table HL70734",
    )

    drg_14: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_14",
            "pccl_value_code",
            "DRG.14",
        ),
        serialization_alias="DRG.14",
        title="PCCL Value Code",
        description="Item #2158 | Table HL70728",
    )

    drg_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_15",
            "effective_weight",
            "DRG.15",
        ),
        serialization_alias="DRG.15",
        title="Effective Weight",
        description="Item #2159",
    )

    drg_16: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_16",
            "monetary_amount",
            "DRG.16",
        ),
        serialization_alias="DRG.16",
        title="Monetary Amount",
        description="Item #2160",
    )

    drg_17: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_17",
            "status_patient",
            "DRG.17",
        ),
        serialization_alias="DRG.17",
        title="Status Patient",
        description="Item #2161 | Table HL70739",
    )

    drg_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_18",
            "grouper_software_name",
            "DRG.18",
        ),
        serialization_alias="DRG.18",
        title="Grouper Software Name",
        description="Item #2162",
    )

    drg_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_19",
            "grouper_software_version",
            "DRG.19",
        ),
        serialization_alias="DRG.19",
        title="Grouper Software Version",
        description="Item #2282",
    )

    drg_20: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_20",
            "status_financial_calculation",
            "DRG.20",
        ),
        serialization_alias="DRG.20",
        title="Status Financial Calculation",
        description="Item #2163 | Table HL70742",
    )

    drg_21: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_21",
            "relative_discount_surcharge",
            "DRG.21",
        ),
        serialization_alias="DRG.21",
        title="Relative Discount/Surcharge",
        description="Item #2164",
    )

    drg_22: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_22",
            "basic_charge",
            "DRG.22",
        ),
        serialization_alias="DRG.22",
        title="Basic Charge",
        description="Item #2165",
    )

    drg_23: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_23",
            "total_charge",
            "DRG.23",
        ),
        serialization_alias="DRG.23",
        title="Total Charge",
        description="Item #2166",
    )

    drg_24: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_24",
            "discount_surcharge",
            "DRG.24",
        ),
        serialization_alias="DRG.24",
        title="Discount/Surcharge",
        description="Item #2167",
    )

    drg_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_25",
            "calculated_days",
            "DRG.25",
        ),
        serialization_alias="DRG.25",
        title="Calculated Days",
        description="Item #2168",
    )

    drg_26: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_26",
            "status_gender",
            "DRG.26",
        ),
        serialization_alias="DRG.26",
        title="Status Gender",
        description="Item #2169 | Table HL70749",
    )

    drg_27: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_27",
            "status_age",
            "DRG.27",
        ),
        serialization_alias="DRG.27",
        title="Status Age",
        description="Item #2170 | Table HL70749",
    )

    drg_28: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_28",
            "status_length_of_stay",
            "DRG.28",
        ),
        serialization_alias="DRG.28",
        title="Status Length of Stay",
        description="Item #2171 | Table HL70749",
    )

    drg_29: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_29",
            "status_same_day_flag",
            "DRG.29",
        ),
        serialization_alias="DRG.29",
        title="Status Same Day Flag",
        description="Item #2172 | Table HL70749",
    )

    drg_30: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_30",
            "status_separation_mode",
            "DRG.30",
        ),
        serialization_alias="DRG.30",
        title="Status Separation Mode",
        description="Item #2173 | Table HL70749",
    )

    drg_31: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_31",
            "status_weight_at_birth",
            "DRG.31",
        ),
        serialization_alias="DRG.31",
        title="Status Weight at Birth",
        description="Item #2174 | Table HL70755",
    )

    drg_32: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_32",
            "status_respiration_minutes",
            "DRG.32",
        ),
        serialization_alias="DRG.32",
        title="Status Respiration Minutes",
        description="Item #2175 | Table HL70757",
    )

    drg_33: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_33",
            "status_admission",
            "DRG.33",
        ),
        serialization_alias="DRG.33",
        title="Status Admission",
        description="Item #2176 | Table HL70759",
    )

    @field_validator("drg_2", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("drg_6", "drg_15", "drg_25", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
