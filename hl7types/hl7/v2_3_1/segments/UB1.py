"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: UB1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.OCD import OCD
from ..datatypes.UVC import UVC


class UB1(BaseModel):
    """HL7 v2 UB1 segment."""

    ub1_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_1",
            "set_id_ub1",
            "UB1.1",
        ),
        serialization_alias="UB1.1",
        title="Set ID - UB1",
        description="Item #530",
    )

    ub1_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_2",
            "blood_deductible_43",
            "UB1.2",
        ),
        serialization_alias="UB1.2",
        title="Blood Deductible  (43)",
        description="Item #531",
    )

    ub1_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_3",
            "blood_furnished_pints_of_40",
            "UB1.3",
        ),
        serialization_alias="UB1.3",
        title="Blood Furnished-Pints Of (40)",
        description="Item #532",
    )

    ub1_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_4",
            "blood_replaced_pints_41",
            "UB1.4",
        ),
        serialization_alias="UB1.4",
        title="Blood Replaced-Pints (41)",
        description="Item #533",
    )

    ub1_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_5",
            "blood_not_replaced_pints_42",
            "UB1.5",
        ),
        serialization_alias="UB1.5",
        title="Blood Not Replaced-Pints(42)",
        description="Item #534",
    )

    ub1_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_6",
            "co_insurance_days_25",
            "UB1.6",
        ),
        serialization_alias="UB1.6",
        title="Co-Insurance Days (25)",
        description="Item #535",
    )

    ub1_7: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_7",
            "condition_code_35_39",
            "UB1.7",
        ),
        serialization_alias="UB1.7",
        title="Condition Code (35-39)",
        description="Item #536 | Table HL70043",
    )

    ub1_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_8",
            "covered_days_23",
            "UB1.8",
        ),
        serialization_alias="UB1.8",
        title="Covered Days - (23)",
        description="Item #537",
    )

    ub1_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_9",
            "non_covered_days_24",
            "UB1.9",
        ),
        serialization_alias="UB1.9",
        title="Non Covered Days - (24)",
        description="Item #538",
    )

    ub1_10: list[UVC] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_10",
            "value_amount_code_46_49",
            "UB1.10",
        ),
        serialization_alias="UB1.10",
        title="Value Amount & Code (46-49)",
        description="Item #539 | Table HL70153",
    )

    ub1_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_11",
            "number_of_grace_days_90",
            "UB1.11",
        ),
        serialization_alias="UB1.11",
        title="Number Of Grace Days (90)",
        description="Item #540",
    )

    ub1_12: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_12",
            "special_program_indicator_44",
            "UB1.12",
        ),
        serialization_alias="UB1.12",
        title="Special Program Indicator (44)",
        description="Item #541 | Table HL70348",
    )

    ub1_13: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_13",
            "psro_ur_approval_indicator_87",
            "UB1.13",
        ),
        serialization_alias="UB1.13",
        title="PSRO/UR Approval Indicator (87)",
        description="Item #542 | Table HL70349",
    )

    ub1_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_14",
            "psro_ur_approved_stay_fm_88",
            "UB1.14",
        ),
        serialization_alias="UB1.14",
        title="PSRO/UR Approved Stay-Fm (88)",
        description="Item #543",
    )

    ub1_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_15",
            "psro_ur_approved_stay_to_89",
            "UB1.15",
        ),
        serialization_alias="UB1.15",
        title="PSRO/UR Approved Stay-To (89)",
        description="Item #544",
    )

    ub1_16: list[OCD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_16",
            "occurrence_28_32",
            "UB1.16",
        ),
        serialization_alias="UB1.16",
        title="Occurrence (28-32)",
        description="Item #545 | Table HL70350",
    )

    ub1_17: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_17",
            "occurrence_span_33",
            "UB1.17",
        ),
        serialization_alias="UB1.17",
        title="Occurrence Span (33)",
        description="Item #546 | Table HL70351",
    )

    ub1_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_18",
            "occur_span_start_date_33",
            "UB1.18",
        ),
        serialization_alias="UB1.18",
        title="Occur Span Start Date(33)",
        description="Item #547",
    )

    ub1_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_19",
            "occur_span_end_date_33",
            "UB1.19",
        ),
        serialization_alias="UB1.19",
        title="Occur Span End Date (33)",
        description="Item #548",
    )

    ub1_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_20",
            "ub_82_locator_2",
            "UB1.20",
        ),
        serialization_alias="UB1.20",
        title="UB-82 Locator 2",
        description="Item #549",
    )

    ub1_21: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_21",
            "ub_82_locator_9",
            "UB1.21",
        ),
        serialization_alias="UB1.21",
        title="UB-82 Locator 9",
        description="Item #550",
    )

    ub1_22: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_22",
            "ub_82_locator_27",
            "UB1.22",
        ),
        serialization_alias="UB1.22",
        title="UB-82 Locator 27",
        description="Item #551",
    )

    ub1_23: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_23",
            "ub_82_locator_45",
            "UB1.23",
        ),
        serialization_alias="UB1.23",
        title="UB-82 Locator 45",
        description="Item #552",
    )

    model_config = {"populate_by_name": True}
