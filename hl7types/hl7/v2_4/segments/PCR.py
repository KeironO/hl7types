"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PCR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CQ import CQ
from ..datatypes.TS import TS


class PCR(HL7Model):
    """Possible Causal Relationship (S7.12.3).

    Attributes
    ----------
    pcr_1 : CE
        PCR.1 - Implicated Product (CE) R S7.12.3.1

    pcr_2 : str | None
        PCR.2 - Generic Product (IS) O S7.12.3.2 | 0249 - Generic product

    pcr_3 : CE | None
        PCR.3 - Product Class (CE) O S7.12.3.3

    pcr_4 : CQ | None
        PCR.4 - Total Duration Of Therapy (CQ) O S7.12.3.4

    pcr_5 : TS | None
        PCR.5 - Product Manufacture Date (TS) O S7.12.3.5

    pcr_6 : TS | None
        PCR.6 - Product Expiration Date (TS) O S7.12.3.6

    pcr_7 : TS | None
        PCR.7 - Product Implantation Date (TS) O S7.12.3.7

    pcr_8 : TS | None
        PCR.8 - Product Explantation Date (TS) O S7.12.3.8

    pcr_9 : str | None
        PCR.9 - Single Use Device (IS) O S7.12.3.9 | 0244 - Single use device

    pcr_10 : CE | None
        PCR.10 - Indication For Product Use (CE) O S7.12.3.10

    pcr_11 : str | None
        PCR.11 - Product Problem (IS) O S7.12.3.11 | 0245 - Product problem

    pcr_12 : list[str] | None
        PCR.12 - Product Serial/Lot Number (ST) O rep S7.12.3.12

    pcr_13 : str | None
        PCR.13 - Product Available For Inspection (IS) O S7.12.3.13 | 0246 - Product available for inspection

    pcr_14 : CE | None
        PCR.14 - Product Evaluation Performed (CE) O S7.12.3.14

    pcr_15 : CE | None
        PCR.15 - Product Evaluation Status (CE) O S7.12.3.15 | 0247 - Status of evaluation

    pcr_16 : CE | None
        PCR.16 - Product Evaluation Results (CE) O S7.12.3.16

    pcr_17 : str | None
        PCR.17 - Evaluated Product Source (ID) O S7.12.3.17 | 0248 - Product source

    pcr_18 : TS | None
        PCR.18 - Date Product Returned To Manufacturer (TS) O S7.12.3.18

    pcr_19 : str | None
        PCR.19 - Device Operator Qualifications (ID) O S7.12.3.19 | 0242 - Primary observer's qualification

    pcr_20 : str | None
        PCR.20 - Relatedness Assessment (ID) O S7.12.3.20 | 0250 - Relatedness assessment

    pcr_21 : list[str] | None
        PCR.21 - Action Taken In Response To The Event (ID) O rep S7.12.3.21 | 0251 - Action taken in response to the event

    pcr_22 : list[str] | None
        PCR.22 - Event Causality Observations (ID) O rep S7.12.3.22 | 0252 - Causality observations

    pcr_23 : list[str] | None
        PCR.23 - Indirect Exposure Mechanism (ID) O rep S7.12.3.23 | 0253 - Indirect exposure mechanism
    """

    pcr_1: CE = Field(
        validation_alias=AliasChoices(
            "pcr_1",
            "implicated_product",
            "PCR.1",
        ),
        serialization_alias="PCR.1",
        title="Implicated Product",
        description="R | Item #01098",
    )

    pcr_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_2",
            "generic_product",
            "PCR.2",
        ),
        serialization_alias="PCR.2",
        title="Generic Product",
        description="O | Item #01099 | Table 0249 - Generic product | LEN:1",
    )

    pcr_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_3",
            "product_class",
            "PCR.3",
        ),
        serialization_alias="PCR.3",
        title="Product Class",
        description="O | Item #01100",
    )

    pcr_4: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_4",
            "total_duration_of_therapy",
            "PCR.4",
        ),
        serialization_alias="PCR.4",
        title="Total Duration Of Therapy",
        description="O | Item #01101",
    )

    pcr_5: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_5",
            "product_manufacture_date",
            "PCR.5",
        ),
        serialization_alias="PCR.5",
        title="Product Manufacture Date",
        description="O | Item #01102",
    )

    pcr_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_6",
            "product_expiration_date",
            "PCR.6",
        ),
        serialization_alias="PCR.6",
        title="Product Expiration Date",
        description="O | Item #01103",
    )

    pcr_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_7",
            "product_implantation_date",
            "PCR.7",
        ),
        serialization_alias="PCR.7",
        title="Product Implantation Date",
        description="O | Item #01104",
    )

    pcr_8: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_8",
            "product_explantation_date",
            "PCR.8",
        ),
        serialization_alias="PCR.8",
        title="Product Explantation Date",
        description="O | Item #01105",
    )

    pcr_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_9",
            "single_use_device",
            "PCR.9",
        ),
        serialization_alias="PCR.9",
        title="Single Use Device",
        description="O | Item #01106 | Table 0244 - Single use device | LEN:8",
    )

    pcr_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_10",
            "indication_for_product_use",
            "PCR.10",
        ),
        serialization_alias="PCR.10",
        title="Indication For Product Use",
        description="O | Item #01107",
    )

    pcr_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_11",
            "product_problem",
            "PCR.11",
        ),
        serialization_alias="PCR.11",
        title="Product Problem",
        description="O | Item #01108 | Table 0245 - Product problem | LEN:8",
    )

    pcr_12: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_12",
            "product_serial_lot_number",
            "PCR.12",
        ),
        serialization_alias="PCR.12",
        title="Product Serial/Lot Number",
        description="O | Item #01109 | LEN:30",
    )

    pcr_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_13",
            "product_available_for_inspection",
            "PCR.13",
        ),
        serialization_alias="PCR.13",
        title="Product Available For Inspection",
        description=(
            "O | Item #01110 | Table 0246 - Product available for inspection | "
            "LEN:1"
        ),
    )

    pcr_14: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_14",
            "product_evaluation_performed",
            "PCR.14",
        ),
        serialization_alias="PCR.14",
        title="Product Evaluation Performed",
        description="O | Item #01111",
    )

    pcr_15: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_15",
            "product_evaluation_status",
            "PCR.15",
        ),
        serialization_alias="PCR.15",
        title="Product Evaluation Status",
        description="O | Item #01112 | Table 0247 - Status of evaluation",
    )

    pcr_16: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_16",
            "product_evaluation_results",
            "PCR.16",
        ),
        serialization_alias="PCR.16",
        title="Product Evaluation Results",
        description="O | Item #01113",
    )

    pcr_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_17",
            "evaluated_product_source",
            "PCR.17",
        ),
        serialization_alias="PCR.17",
        title="Evaluated Product Source",
        description="O | Item #01114 | Table 0248 - Product source | LEN:8",
    )

    pcr_18: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_18",
            "date_product_returned_to_manufacturer",
            "PCR.18",
        ),
        serialization_alias="PCR.18",
        title="Date Product Returned To Manufacturer",
        description="O | Item #01115",
    )

    pcr_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_19",
            "device_operator_qualifications",
            "PCR.19",
        ),
        serialization_alias="PCR.19",
        title="Device Operator Qualifications",
        description=(
            "O | Item #01116 | Table 0242 - Primary observer's qualification | "
            "LEN:1"
        ),
    )

    pcr_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_20",
            "relatedness_assessment",
            "PCR.20",
        ),
        serialization_alias="PCR.20",
        title="Relatedness Assessment",
        description=(
            "O | Item #01117 | Table 0250 - Relatedness assessment | LEN:1"
        ),
    )

    pcr_21: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_21",
            "action_taken_in_response_to_the_event",
            "PCR.21",
        ),
        serialization_alias="PCR.21",
        title="Action Taken In Response To The Event",
        description=(
            "O | Item #01118 | Table 0251 - Action taken in response to the event "
            "| LEN:2"
        ),
    )

    pcr_22: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_22",
            "event_causality_observations",
            "PCR.22",
        ),
        serialization_alias="PCR.22",
        title="Event Causality Observations",
        description=(
            "O | Item #01119 | Table 0252 - Causality observations | LEN:2"
        ),
    )

    pcr_23: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcr_23",
            "indirect_exposure_mechanism",
            "PCR.23",
        ),
        serialization_alias="PCR.23",
        title="Indirect Exposure Mechanism",
        description=(
            "O | Item #01120 | Table 0253 - Indirect exposure mechanism | LEN:1"
        ),
    )

    model_config = ConfigDict(populate_by_name=True)
