"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: DRG
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.MO import MO
from ..datatypes.XPN import XPN


class DRG(BaseModel):
    """HL7 v2 DRG segment."""

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

    model_config = {"populate_by_name": True}
