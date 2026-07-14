"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PRC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CP import CP
from ..datatypes.EI import EI
from ..datatypes.MO import MO
from ..datatypes.TS import TS


class PRC(HL7Model):
    """Pricing (S8.9.3).

    Attributes
    ----------
    prc_1 : CE
        PRC.1 (req) - Primary Key Value (CE) S8.9.3.1 | 0132 - Transaction Code

    prc_2 : list[EI]
        PRC.2 (req, rep) - Facility ID (EI) S7.11.6.1

    prc_3 : list[CE] | None
        PRC.3 (opt, rep) - Department (CE) S8.9.3.3

    prc_4 : list[str] | None
        PRC.4 (opt, rep) - Valid Patient Classes (ID) S8.8.5.5 | 0004 - Patient Class

    prc_5 : list[CP] | None
        PRC.5 (opt, rep) - Price (CP) S8.9.3.5

    prc_6 : list[str] | None
        PRC.6 (opt, rep) - Formula (ST) S8.9.3.6

    prc_7 : str | None
        PRC.7 (opt) - Minimum Quantity (NM) S8.9.3.7

    prc_8 : str | None
        PRC.8 (opt) - Maximum Quantity (NM) S8.9.3.8

    prc_9 : MO | None
        PRC.9 (opt) - Minimum Price (MO) S8.9.3.9

    prc_10 : MO | None
        PRC.10 (opt) - Maximum Price (MO) S8.9.3.10

    prc_11 : TS | None
        PRC.11 (opt) - Effective Start Date (TS) S8.9.3.11

    prc_12 : TS | None
        PRC.12 (opt) - Effective End Date (TS) S8.9.3.12

    prc_13 : str | None
        PRC.13 (opt) - Price Override Flag (ID) S8.9.3.13 | 0268 - Override

    prc_14 : list[CE] | None
        PRC.14 (opt, rep) - Billing Category (CE) S8.9.3.14 | 0293 - Billing Category

    prc_15 : str | None
        PRC.15 (opt) - Chargeable Flag (ID) S8.9.3.15 | 0136 - Yes/No Indicator

    prc_16 : str | None
        PRC.16 (opt) - Active/Inactive Flag (ID) S8.6.2 | 0183 - Active/Inactive

    prc_17 : MO | None
        PRC.17 (opt) - Cost (MO) S8.9.3.17

    prc_18 : str | None
        PRC.18 (opt) - Charge On Indicator (ID) S8.9.3.18 | 0269 - Charge on Indicator
    """

    prc_1: CE = Field(
        validation_alias=AliasChoices(
            "prc_1",
            "primary_key_value",
            "PRC.1",
        ),
        serialization_alias="PRC.1",
        title="Primary Key Value",
        description="Item #982 | Table HL70132",
    )

    prc_2: List[EI] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "prc_2",
            "facility_id",
            "PRC.2",
        ),
        serialization_alias="PRC.2",
        title="Facility ID",
        description="Item #1262",
    )

    prc_3: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_3",
            "department",
            "PRC.3",
        ),
        serialization_alias="PRC.3",
        title="Department",
        description="Item #996",
    )

    prc_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_4",
            "valid_patient_classes",
            "PRC.4",
        ),
        serialization_alias="PRC.4",
        title="Valid Patient Classes",
        description="Item #967 | Table HL70004",
    )

    prc_5: Optional[List[CP]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_5",
            "price",
            "PRC.5",
        ),
        serialization_alias="PRC.5",
        title="Price",
        description="Item #998",
    )

    prc_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_6",
            "formula",
            "PRC.6",
        ),
        serialization_alias="PRC.6",
        title="Formula",
        description="Item #999",
    )

    prc_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_7",
            "minimum_quantity",
            "PRC.7",
        ),
        serialization_alias="PRC.7",
        title="Minimum Quantity",
        description="Item #1000",
    )

    prc_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_8",
            "maximum_quantity",
            "PRC.8",
        ),
        serialization_alias="PRC.8",
        title="Maximum Quantity",
        description="Item #1001",
    )

    prc_9: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_9",
            "minimum_price",
            "PRC.9",
        ),
        serialization_alias="PRC.9",
        title="Minimum Price",
        description="Item #1002",
    )

    prc_10: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_10",
            "maximum_price",
            "PRC.10",
        ),
        serialization_alias="PRC.10",
        title="Maximum Price",
        description="Item #1003",
    )

    prc_11: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_11",
            "effective_start_date",
            "PRC.11",
        ),
        serialization_alias="PRC.11",
        title="Effective Start Date",
        description="Item #1004",
    )

    prc_12: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_12",
            "effective_end_date",
            "PRC.12",
        ),
        serialization_alias="PRC.12",
        title="Effective End Date",
        description="Item #1005",
    )

    prc_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_13",
            "price_override_flag",
            "PRC.13",
        ),
        serialization_alias="PRC.13",
        title="Price Override Flag",
        description="Item #1006 | Table HL70268",
    )

    prc_14: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_14",
            "billing_category",
            "PRC.14",
        ),
        serialization_alias="PRC.14",
        title="Billing Category",
        description="Item #1007 | Table HL70293",
    )

    prc_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_15",
            "chargeable_flag",
            "PRC.15",
        ),
        serialization_alias="PRC.15",
        title="Chargeable Flag",
        description="Item #1008 | Table HL70136",
    )

    prc_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_16",
            "active_inactive_flag",
            "PRC.16",
        ),
        serialization_alias="PRC.16",
        title="Active/Inactive Flag",
        description="Item #675 | Table HL70183",
    )

    prc_17: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_17",
            "cost",
            "PRC.17",
        ),
        serialization_alias="PRC.17",
        title="Cost",
        description="Item #989",
    )

    prc_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_18",
            "charge_on_indicator",
            "PRC.18",
        ),
        serialization_alias="PRC.18",
        title="Charge On Indicator",
        description="Item #1009 | Table HL70269",
    )

    @field_validator("prc_7", "prc_8", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
