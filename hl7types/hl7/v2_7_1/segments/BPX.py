"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: BPX
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON


class BPX(HL7Model):
    """HL7 v2 BPX segment.

    Attributes
    ----------
    bpx_1 : str
        BPX.1 (req) - Set ID - BPX (SI)

    bpx_2 : CWE
        BPX.2 (req) - BP Dispense Status (CWE)

    bpx_3 : str
        BPX.3 (req) - BP Status (ID)

    bpx_4 : str
        BPX.4 (req) - BP Date/Time of Status (DTM)

    bpx_5 : EI | None
        BPX.5 (opt) - BC Donation ID (EI)

    bpx_6 : CNE | None
        BPX.6 (opt) - BC Component (CNE)

    bpx_7 : CNE | None
        BPX.7 (opt) - BC Donation Type / Intended Use (CNE)

    bpx_8 : CWE | None
        BPX.8 (opt) - CP Commercial Product (CWE)

    bpx_9 : XON | None
        BPX.9 (opt) - CP Manufacturer (XON)

    bpx_10 : EI | None
        BPX.10 (opt) - CP Lot Number (EI)

    bpx_11 : CNE | None
        BPX.11 (opt) - BP Blood Group (CNE)

    bpx_12 : list[CNE] | None
        BPX.12 (opt, rep) - BC Special Testing (CNE)

    bpx_13 : str | None
        BPX.13 (opt) - BP Expiration Date/Time (DTM)

    bpx_14 : str
        BPX.14 (req) - BP Quantity (NM)

    bpx_15 : str | None
        BPX.15 (opt) - BP Amount (NM)

    bpx_16 : CWE | None
        BPX.16 (opt) - BP Units (CWE)

    bpx_17 : EI | None
        BPX.17 (opt) - BP Unique ID (EI)

    bpx_18 : PL | None
        BPX.18 (opt) - BP Actual Dispensed To Location (PL)

    bpx_19 : XAD | None
        BPX.19 (opt) - BP Actual Dispensed To Address (XAD)

    bpx_20 : XCN | None
        BPX.20 (opt) - BP Dispensed to Receiver (XCN)

    bpx_21 : XCN | None
        BPX.21 (opt) - BP Dispensing Individual (XCN)
    """

    bpx_1: str = Field(
        validation_alias=AliasChoices(
            "bpx_1",
            "set_id_bpx",
            "BPX.1",
        ),
        serialization_alias="BPX.1",
        title="Set ID - BPX",
        description="Item #1714",
    )

    bpx_2: CWE = Field(
        validation_alias=AliasChoices(
            "bpx_2",
            "bp_dispense_status",
            "BPX.2",
        ),
        serialization_alias="BPX.2",
        title="BP Dispense Status",
        description="Item #1715 | Table HL70510",
    )

    bpx_3: str = Field(
        validation_alias=AliasChoices(
            "bpx_3",
            "bp_status",
            "BPX.3",
        ),
        serialization_alias="BPX.3",
        title="BP Status",
        description="Item #1716 | Table HL70511",
    )

    bpx_4: str = Field(
        validation_alias=AliasChoices(
            "bpx_4",
            "bp_date_time_of_status",
            "BPX.4",
        ),
        serialization_alias="BPX.4",
        title="BP Date/Time of Status",
        description="Item #1717",
    )

    bpx_5: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_5",
            "bc_donation_id",
            "BPX.5",
        ),
        serialization_alias="BPX.5",
        title="BC Donation ID",
        description="Item #1718",
    )

    bpx_6: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_6",
            "bc_component",
            "BPX.6",
        ),
        serialization_alias="BPX.6",
        title="BC Component",
        description="Item #1719 | Table HL79999",
    )

    bpx_7: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_7",
            "bc_donation_type_intended_use",
            "BPX.7",
        ),
        serialization_alias="BPX.7",
        title="BC Donation Type / Intended Use",
        description="Item #1720 | Table HL79999",
    )

    bpx_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_8",
            "cp_commercial_product",
            "BPX.8",
        ),
        serialization_alias="BPX.8",
        title="CP Commercial Product",
        description="Item #1721 | Table HL70512",
    )

    bpx_9: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_9",
            "cp_manufacturer",
            "BPX.9",
        ),
        serialization_alias="BPX.9",
        title="CP Manufacturer",
        description="Item #1722",
    )

    bpx_10: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_10",
            "cp_lot_number",
            "BPX.10",
        ),
        serialization_alias="BPX.10",
        title="CP Lot Number",
        description="Item #1723",
    )

    bpx_11: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_11",
            "bp_blood_group",
            "BPX.11",
        ),
        serialization_alias="BPX.11",
        title="BP Blood Group",
        description="Item #1724 | Table HL79999",
    )

    bpx_12: Optional[List[CNE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_12",
            "bc_special_testing",
            "BPX.12",
        ),
        serialization_alias="BPX.12",
        title="BC Special Testing",
        description="Item #1725 | Table HL79999",
    )

    bpx_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_13",
            "bp_expiration_date_time",
            "BPX.13",
        ),
        serialization_alias="BPX.13",
        title="BP Expiration Date/Time",
        description="Item #1726",
    )

    bpx_14: str = Field(
        validation_alias=AliasChoices(
            "bpx_14",
            "bp_quantity",
            "BPX.14",
        ),
        serialization_alias="BPX.14",
        title="BP Quantity",
        description="Item #1727",
    )

    bpx_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_15",
            "bp_amount",
            "BPX.15",
        ),
        serialization_alias="BPX.15",
        title="BP Amount",
        description="Item #1728",
    )

    bpx_16: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_16",
            "bp_units",
            "BPX.16",
        ),
        serialization_alias="BPX.16",
        title="BP Units",
        description="Item #1729 | Table HL79999",
    )

    bpx_17: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_17",
            "bp_unique_id",
            "BPX.17",
        ),
        serialization_alias="BPX.17",
        title="BP Unique ID",
        description="Item #1730",
    )

    bpx_18: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_18",
            "bp_actual_dispensed_to_location",
            "BPX.18",
        ),
        serialization_alias="BPX.18",
        title="BP Actual Dispensed To Location",
        description="Item #1731",
    )

    bpx_19: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_19",
            "bp_actual_dispensed_to_address",
            "BPX.19",
        ),
        serialization_alias="BPX.19",
        title="BP Actual Dispensed To Address",
        description="Item #1732",
    )

    bpx_20: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_20",
            "bp_dispensed_to_receiver",
            "BPX.20",
        ),
        serialization_alias="BPX.20",
        title="BP Dispensed to Receiver",
        description="Item #1733",
    )

    bpx_21: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_21",
            "bp_dispensing_individual",
            "BPX.21",
        ),
        serialization_alias="BPX.21",
        title="BP Dispensing Individual",
        description="Item #1734",
    )

    @field_validator("bpx_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("bpx_4", "bpx_13", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    @field_validator("bpx_14", "bpx_15", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
