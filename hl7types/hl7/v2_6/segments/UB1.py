"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: UB1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.OCD import OCD
from ..datatypes.UVC import UVC


class UB1(BaseModel):
    """HL7 v2 UB1 segment.

    Attributes
    ----------
    ub1_1 : str | None
        UB1.1 (opt) - Set ID - UB1 (SI)

    ub1_3 : str | None
        UB1.3 (opt) - Blood Furnished-Pints (NM)

    ub1_4 : str | None
        UB1.4 (opt) - Blood Replaced-Pints (NM)

    ub1_5 : str | None
        UB1.5 (opt) - Blood Not Replaced-Pints (NM)

    ub1_6 : str | None
        UB1.6 (opt) - Co-Insurance Days (NM)

    ub1_7 : list[str] | None
        UB1.7 (opt, rep) - Condition Code (IS)

    ub1_8 : str | None
        UB1.8 (opt) - Covered Days (NM)

    ub1_9 : str | None
        UB1.9 (opt) - Non Covered Days (NM)

    ub1_10 : list[UVC] | None
        UB1.10 (opt, rep) - Value Amount & Code (UVC)

    ub1_11 : str | None
        UB1.11 (opt) - Number Of Grace Days (NM)

    ub1_12 : CWE | None
        UB1.12 (opt) - Special Program Indicator (CWE)

    ub1_13 : CWE | None
        UB1.13 (opt) - PSRO/UR Approval Indicator (CWE)

    ub1_14 : str | None
        UB1.14 (opt) - PSRO/UR Approved Stay-Fm (DT)

    ub1_15 : str | None
        UB1.15 (opt) - PSRO/UR Approved Stay-To (DT)

    ub1_16 : list[OCD] | None
        UB1.16 (opt, rep) - Occurrence (OCD)

    ub1_17 : CWE | None
        UB1.17 (opt) - Occurrence Span (CWE)

    ub1_18 : str | None
        UB1.18 (opt) - Occur Span Start Date (DT)

    ub1_19 : str | None
        UB1.19 (opt) - Occur Span End Date (DT)

    ub1_20 : str | None
        UB1.20 (opt) - UB-82 Locator 2 (ST)

    ub1_21 : str | None
        UB1.21 (opt) - UB-82 Locator 9 (ST)

    ub1_22 : str | None
        UB1.22 (opt) - UB-82 Locator 27 (ST)

    ub1_23 : str | None
        UB1.23 (opt) - UB-82 Locator 45 (ST)
    """

    ub1_1: Optional[str] = Field(
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

    ub1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_3",
            "blood_furnished_pints",
            "UB1.3",
        ),
        serialization_alias="UB1.3",
        title="Blood Furnished-Pints",
        description="Item #532",
    )

    ub1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_4",
            "blood_replaced_pints",
            "UB1.4",
        ),
        serialization_alias="UB1.4",
        title="Blood Replaced-Pints",
        description="Item #533",
    )

    ub1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_5",
            "blood_not_replaced_pints",
            "UB1.5",
        ),
        serialization_alias="UB1.5",
        title="Blood Not Replaced-Pints",
        description="Item #534",
    )

    ub1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_6",
            "co_insurance_days",
            "UB1.6",
        ),
        serialization_alias="UB1.6",
        title="Co-Insurance Days",
        description="Item #535",
    )

    ub1_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_7",
            "condition_code",
            "UB1.7",
        ),
        serialization_alias="UB1.7",
        title="Condition Code",
        description="Item #536 | Table HL70043",
    )

    ub1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_8",
            "covered_days",
            "UB1.8",
        ),
        serialization_alias="UB1.8",
        title="Covered Days",
        description="Item #537",
    )

    ub1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_9",
            "non_covered_days",
            "UB1.9",
        ),
        serialization_alias="UB1.9",
        title="Non Covered Days",
        description="Item #538",
    )

    ub1_10: Optional[List[UVC]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_10",
            "value_amount_code",
            "UB1.10",
        ),
        serialization_alias="UB1.10",
        title="Value Amount & Code",
        description="Item #539",
    )

    ub1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_11",
            "number_of_grace_days",
            "UB1.11",
        ),
        serialization_alias="UB1.11",
        title="Number Of Grace Days",
        description="Item #540",
    )

    ub1_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_12",
            "special_program_indicator",
            "UB1.12",
        ),
        serialization_alias="UB1.12",
        title="Special Program Indicator",
        description="Item #541 | Table HL70348",
    )

    ub1_13: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_13",
            "psro_ur_approval_indicator",
            "UB1.13",
        ),
        serialization_alias="UB1.13",
        title="PSRO/UR Approval Indicator",
        description="Item #542 | Table HL70349",
    )

    ub1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_14",
            "psro_ur_approved_stay_fm",
            "UB1.14",
        ),
        serialization_alias="UB1.14",
        title="PSRO/UR Approved Stay-Fm",
        description="Item #543",
    )

    ub1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_15",
            "psro_ur_approved_stay_to",
            "UB1.15",
        ),
        serialization_alias="UB1.15",
        title="PSRO/UR Approved Stay-To",
        description="Item #544",
    )

    ub1_16: Optional[List[OCD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_16",
            "occurrence",
            "UB1.16",
        ),
        serialization_alias="UB1.16",
        title="Occurrence",
        description="Item #545",
    )

    ub1_17: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_17",
            "occurrence_span",
            "UB1.17",
        ),
        serialization_alias="UB1.17",
        title="Occurrence Span",
        description="Item #546 | Table HL70351",
    )

    ub1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_18",
            "occur_span_start_date",
            "UB1.18",
        ),
        serialization_alias="UB1.18",
        title="Occur Span Start Date",
        description="Item #547",
    )

    ub1_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_19",
            "occur_span_end_date",
            "UB1.19",
        ),
        serialization_alias="UB1.19",
        title="Occur Span End Date",
        description="Item #548",
    )

    ub1_20: Optional[str] = Field(
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

    ub1_21: Optional[str] = Field(
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

    ub1_22: Optional[str] = Field(
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

    ub1_23: Optional[str] = Field(
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
