"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: BPO
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD


class BPO(BaseModel):
    """HL7 v2 BPO segment."""

    bpo_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "bpo_1",
            "set_id_bpo",
            "BPO.1",
        ),
        serialization_alias="BPO.1",
        title="Set ID - BPO",
        description="Item #1700",
    )

    bpo_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "bpo_2",
            "bp_universal_service_identifier",
            "BPO.2",
        ),
        serialization_alias="BPO.2",
        title="BP Universal Service Identifier",
        description="Item #1701 | Table HL79999",
    )

    bpo_3: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpo_3",
            "bp_processing_requirements",
            "BPO.3",
        ),
        serialization_alias="BPO.3",
        title="BP  Processing Requirements",
        description="Item #1702 | Table HL70508",
    )

    bpo_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "bpo_4",
            "bp_quantity",
            "BPO.4",
        ),
        serialization_alias="BPO.4",
        title="BP Quantity",
        description="Item #1703",
    )

    bpo_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpo_5",
            "bp_amount",
            "BPO.5",
        ),
        serialization_alias="BPO.5",
        title="BP Amount",
        description="Item #1704",
    )

    bpo_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpo_6",
            "bp_units",
            "BPO.6",
        ),
        serialization_alias="BPO.6",
        title="BP Units",
        description="Item #1705 | Table HL79999",
    )

    bpo_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpo_7",
            "bp_intended_use_date_time",
            "BPO.7",
        ),
        serialization_alias="BPO.7",
        title="BP Intended Use Date/Time",
        description="Item #1706",
    )

    bpo_8: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpo_8",
            "bp_intended_dispense_from_location",
            "BPO.8",
        ),
        serialization_alias="BPO.8",
        title="BP Intended Dispense From Location",
        description="Item #1707",
    )

    bpo_9: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpo_9",
            "bp_intended_dispense_from_address",
            "BPO.9",
        ),
        serialization_alias="BPO.9",
        title="BP Intended Dispense From Address",
        description="Item #1708",
    )

    bpo_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpo_10",
            "bp_requested_dispense_date_time",
            "BPO.10",
        ),
        serialization_alias="BPO.10",
        title="BP Requested Dispense Date/Time",
        description="Item #1709",
    )

    bpo_11: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpo_11",
            "bp_requested_dispense_to_location",
            "BPO.11",
        ),
        serialization_alias="BPO.11",
        title="BP Requested Dispense To Location",
        description="Item #1710",
    )

    bpo_12: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpo_12",
            "bp_requested_dispense_to_address",
            "BPO.12",
        ),
        serialization_alias="BPO.12",
        title="BP Requested Dispense To Address",
        description="Item #1711",
    )

    bpo_13: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpo_13",
            "bp_indication_for_use",
            "BPO.13",
        ),
        serialization_alias="BPO.13",
        title="BP Indication for Use",
        description="Item #1712 | Table HL70509",
    )

    bpo_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpo_14",
            "bp_informed_consent_indicator",
            "BPO.14",
        ),
        serialization_alias="BPO.14",
        title="BP Informed Consent Indicator",
        description="Item #1713 | Table HL70136",
    )

    model_config = {"populate_by_name": True}
