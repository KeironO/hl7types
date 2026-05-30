"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PRC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.MO import MO


class PRC(HL7Model):
    """HL7 v2 PRC segment.

    Attributes
    ----------
    prc_1 : CWE
        PRC.1 (req) - Primary Key Value - PRC (CWE)

    prc_2 : list[CWE] | None
        PRC.2 (opt, rep) - Facility ID - PRC (CWE)

    prc_3 : list[CWE] | None
        PRC.3 (opt, rep) - Department (CWE)

    prc_4 : list[CWE] | None
        PRC.4 (opt, rep) - Valid Patient Classes (CWE)

    prc_5 : list[CP] | None
        PRC.5 (opt, rep) - Price (CP)

    prc_6 : list[str] | None
        PRC.6 (opt, rep) - Formula (ST)

    prc_7 : str | None
        PRC.7 (opt) - Minimum Quantity (NM)

    prc_8 : str | None
        PRC.8 (opt) - Maximum Quantity (NM)

    prc_9 : MO | None
        PRC.9 (opt) - Minimum Price (MO)

    prc_10 : MO | None
        PRC.10 (opt) - Maximum Price (MO)

    prc_11 : str | None
        PRC.11 (opt) - Effective Start Date (DTM)

    prc_12 : str | None
        PRC.12 (opt) - Effective End Date (DTM)

    prc_13 : CWE | None
        PRC.13 (opt) - Price Override Flag (CWE)

    prc_14 : list[CWE] | None
        PRC.14 (opt, rep) - Billing Category (CWE)

    prc_15 : str | None
        PRC.15 (opt) - Chargeable Flag (ID)

    prc_16 : str | None
        PRC.16 (opt) - Active/Inactive Flag (ID)

    prc_17 : MO | None
        PRC.17 (opt) - Cost (MO)

    prc_18 : CWE | None
        PRC.18 (opt) - Charge on Indicator (CWE)
    """

    prc_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "prc_1",
            "primary_key_value_prc",
            "PRC.1",
        ),
        serialization_alias="PRC.1",
        title="Primary Key Value - PRC",
        description="Item #982 | Table HL70132",
    )

    prc_2: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_2",
            "facility_id_prc",
            "PRC.2",
        ),
        serialization_alias="PRC.2",
        title="Facility ID - PRC",
        description="Item #995 | Table HL70464",
    )

    prc_3: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_3",
            "department",
            "PRC.3",
        ),
        serialization_alias="PRC.3",
        title="Department",
        description="Item #676 | Table HL70184",
    )

    prc_4: Optional[List[CWE]] = Field(
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

    prc_11: Optional[str] = Field(
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

    prc_12: Optional[str] = Field(
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

    prc_13: Optional[CWE] = Field(
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

    prc_14: Optional[List[CWE]] = Field(
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

    prc_18: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prc_18",
            "charge_on_indicator",
            "PRC.18",
        ),
        serialization_alias="PRC.18",
        title="Charge on Indicator",
        description="Item #1009 | Table HL70269",
    )

    model_config = {"populate_by_name": True}
