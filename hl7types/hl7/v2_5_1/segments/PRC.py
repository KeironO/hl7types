"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PRC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CP import CP
from ..datatypes.MO import MO
from ..datatypes.TS import TS


class PRC(HL7Model):
    """Pricing (S8.10.3).

    Attributes
    ----------
    prc_1 : CE
        PRC.1 - Primary Key Value - PRC (CE) R S8.10.3.1 | 0132 - Transaction Code

    prc_2 : list[CE] | None
        PRC.2 - Facility ID - PRC (CE) O rep S8.10.3.2 | 0464 - Facility ID

    prc_3 : list[CE] | None
        PRC.3 - Department (CE) O rep S15.4.8.8 | 0184 - Department

    prc_4 : list[str] | None
        PRC.4 - Valid Patient Classes (IS) O rep S8.10.3.4 | 0004 - Patient Class

    prc_5 : list[CP] | None
        PRC.5 - Price (CP) C rep S8.10.3.5

    prc_6 : list[str] | None
        PRC.6 - Formula (ST) O rep S8.10.3.6

    prc_7 : str | None
        PRC.7 - Minimum Quantity (NM) O S8.10.3.7

    prc_8 : str | None
        PRC.8 - Maximum Quantity (NM) O S8.10.3.8

    prc_9 : MO | None
        PRC.9 - Minimum Price (MO) O S8.10.3.9

    prc_10 : MO | None
        PRC.10 - Maximum Price (MO) O S8.10.3.10

    prc_11 : TS | None
        PRC.11 - Effective Start Date (TS) O S8.10.3.11

    prc_12 : TS | None
        PRC.12 - Effective End Date (TS) O S8.10.3.12

    prc_13 : str | None
        PRC.13 - Price Override Flag (IS) O S8.10.3.13 | 0268 - Override

    prc_14 : list[CE] | None
        PRC.14 - Billing Category (CE) O rep S8.10.3.14 | 0293 - Billing Category

    prc_15 : str | None
        PRC.15 - Chargeable Flag (ID) O S8.10.3.15 | 0136 - Yes/no indicator

    prc_16 : str | None
        PRC.16 - Active/Inactive Flag (ID) O S15.4.8.7 | 0183 - Active/Inactive

    prc_17 : MO | None
        PRC.17 - Cost (MO) O S8.10.3.17

    prc_18 : str | None
        PRC.18 - Charge On Indicator (IS) O S8.10.3.18 | 0269 - Charge On Indicator
    """

    prc_1: CE = Field(
        validation_alias=AliasChoices(
            "prc_1",
            "primary_key_value_prc",
            "PRC.1",
        ),
        serialization_alias="PRC.1",
        title="Primary Key Value - PRC",
        description="R | Item #00982 | Table 0132 - Transaction Code",
    )

    prc_2: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_2",
            "facility_id_prc",
            "PRC.2",
        ),
        serialization_alias="PRC.2",
        title="Facility ID - PRC",
        description="O | Item #00995 | Table 0464 - Facility ID",
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
        description="O | Item #00676 | Table 0184 - Department",
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
        description="O | Item #00967 | Table 0004 - Patient Class | LEN:1",
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
        description="C | Item #00998",
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
        description="O | Item #00999 | LEN:200",
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
        description="O | Item #01000 | LEN:4",
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
        description="O | Item #01001 | LEN:4",
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
        description="O | Item #01002",
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
        description="O | Item #01003",
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
        description="O | Item #01004",
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
        description="O | Item #01005",
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
        description="O | Item #01006 | Table 0268 - Override | LEN:1",
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
        description="O | Item #01007 | Table 0293 - Billing Category",
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
        description="O | Item #01008 | Table 0136 - Yes/no indicator | LEN:1",
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
        description="O | Item #00675 | Table 0183 - Active/Inactive | LEN:1",
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
        description="O | Item #00989",
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
        description=(
            "O | Item #01009 | Table 0269 - Charge On Indicator | LEN:1"
        ),
    )

    @field_validator("prc_7", "prc_8", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
