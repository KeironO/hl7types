"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: PCR
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE


class PCR(BaseModel):
    """HL7 v2 PCR segment."""

    pcr_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "pcr_1",
            "implicated_product",
            "PCR.1",
        ),
        serialization_alias="PCR.1",
        title="Implicated Product",
        description="Item #1098 | Table HL79999",
    )

    pcr_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_2",
            "generic_product",
            "PCR.2",
        ),
        serialization_alias="PCR.2",
        title="Generic Product",
        description="Item #1099 | Table HL70249",
    )

    pcr_3: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_3",
            "product_class",
            "PCR.3",
        ),
        serialization_alias="PCR.3",
        title="Product Class",
        description="Item #1100 | Table HL79999",
    )

    pcr_4: CQ | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_4",
            "total_duration_of_therapy",
            "PCR.4",
        ),
        serialization_alias="PCR.4",
        title="Total Duration Of Therapy",
        description="Item #1101",
    )

    pcr_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_5",
            "product_manufacture_date",
            "PCR.5",
        ),
        serialization_alias="PCR.5",
        title="Product Manufacture Date",
        description="Item #1102",
    )

    pcr_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_6",
            "product_expiration_date",
            "PCR.6",
        ),
        serialization_alias="PCR.6",
        title="Product Expiration Date",
        description="Item #1103",
    )

    pcr_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_7",
            "product_implantation_date",
            "PCR.7",
        ),
        serialization_alias="PCR.7",
        title="Product Implantation Date",
        description="Item #1104",
    )

    pcr_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_8",
            "product_explantation_date",
            "PCR.8",
        ),
        serialization_alias="PCR.8",
        title="Product Explantation Date",
        description="Item #1105",
    )

    pcr_9: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_9",
            "single_use_device",
            "PCR.9",
        ),
        serialization_alias="PCR.9",
        title="Single Use Device",
        description="Item #1106 | Table HL70244",
    )

    pcr_10: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_10",
            "indication_for_product_use",
            "PCR.10",
        ),
        serialization_alias="PCR.10",
        title="Indication For Product Use",
        description="Item #1107 | Table HL79999",
    )

    pcr_11: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_11",
            "product_problem",
            "PCR.11",
        ),
        serialization_alias="PCR.11",
        title="Product Problem",
        description="Item #1108 | Table HL70245",
    )

    pcr_12: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_12",
            "product_serial_lot_number",
            "PCR.12",
        ),
        serialization_alias="PCR.12",
        title="Product Serial/Lot Number",
        description="Item #1109",
    )

    pcr_13: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_13",
            "product_available_for_inspection",
            "PCR.13",
        ),
        serialization_alias="PCR.13",
        title="Product Available For Inspection",
        description="Item #1110 | Table HL70246",
    )

    pcr_14: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_14",
            "product_evaluation_performed",
            "PCR.14",
        ),
        serialization_alias="PCR.14",
        title="Product Evaluation Performed",
        description="Item #1111 | Table HL79999",
    )

    pcr_15: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_15",
            "product_evaluation_status",
            "PCR.15",
        ),
        serialization_alias="PCR.15",
        title="Product Evaluation Status",
        description="Item #1112 | Table HL70247",
    )

    pcr_16: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_16",
            "product_evaluation_results",
            "PCR.16",
        ),
        serialization_alias="PCR.16",
        title="Product Evaluation Results",
        description="Item #1113 | Table HL79999",
    )

    pcr_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_17",
            "evaluated_product_source",
            "PCR.17",
        ),
        serialization_alias="PCR.17",
        title="Evaluated Product Source",
        description="Item #1114 | Table HL70248",
    )

    pcr_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_18",
            "date_product_returned_to_manufacturer",
            "PCR.18",
        ),
        serialization_alias="PCR.18",
        title="Date Product Returned To Manufacturer",
        description="Item #1115",
    )

    pcr_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_19",
            "device_operator_qualifications",
            "PCR.19",
        ),
        serialization_alias="PCR.19",
        title="Device Operator Qualifications",
        description="Item #1116 | Table HL70242",
    )

    pcr_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_20",
            "relatedness_assessment",
            "PCR.20",
        ),
        serialization_alias="PCR.20",
        title="Relatedness Assessment",
        description="Item #1117 | Table HL70250",
    )

    pcr_21: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_21",
            "action_taken_in_response_to_the_event",
            "PCR.21",
        ),
        serialization_alias="PCR.21",
        title="Action Taken In Response To The Event",
        description="Item #1118 | Table HL70251",
    )

    pcr_22: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_22",
            "event_causality_observations",
            "PCR.22",
        ),
        serialization_alias="PCR.22",
        title="Event Causality Observations",
        description="Item #1119 | Table HL70252",
    )

    pcr_23: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_23",
            "indirect_exposure_mechanism",
            "PCR.23",
        ),
        serialization_alias="PCR.23",
        title="Indirect Exposure Mechanism",
        description="Item #1120 | Table HL70253",
    )

    model_config = {"populate_by_name": True}
