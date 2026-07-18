"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: BPX
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class BPX(HL7Model):
    """Blood product dispense status (S4.21.2).

    Attributes
    ----------
    bpx_1 : str
        BPX.1 - Set ID - BPX (SI) R S4.21.2.1

    bpx_2 : CWE
        BPX.2 - BP Dispense Status (CWE) R S4.21.2.2 | 0510 - Blood Product Dispense Status

    bpx_3 : str
        BPX.3 - BP Status (ID) R S4.21.2.3 | 0511 - BP Observation Status Codes Interpretation

    bpx_4 : TS
        BPX.4 - BP Date/Time of Status (TS) R S4.21.2.4

    bpx_5 : EI | None
        BPX.5 - BC Donation ID (EI) C S4.21.2.5

    bpx_6 : CNE | None
        BPX.6 - BC Component (CNE) C S4.21.2.6

    bpx_7 : CNE | None
        BPX.7 - BC Donation Type / Intended Use (CNE) O S4.21.2.7

    bpx_8 : CWE | None
        BPX.8 - CP Commercial Product (CWE) C S4.21.2.8 | 0512 - Commercial Product

    bpx_9 : XON | None
        BPX.9 - CP Manufacturer (XON) C S4.21.2.9

    bpx_10 : EI | None
        BPX.10 - CP Lot Number (EI) C S4.21.2.10

    bpx_11 : CNE | None
        BPX.11 - BP Blood Group (CNE) O S4.21.2.11

    bpx_12 : list[CNE] | None
        BPX.12 - BC Special Testing (CNE) O rep S4.21.2.12

    bpx_13 : TS | None
        BPX.13 - BP Expiration Date/Time (TS) O S4.21.2.13

    bpx_14 : str
        BPX.14 - BP Quantity (NM) R S4.21.2.14

    bpx_15 : str | None
        BPX.15 - BP Amount (NM) O S4.21.2.15

    bpx_16 : CE | None
        BPX.16 - BP Units (CE) O S4.21.2.16

    bpx_17 : EI | None
        BPX.17 - BP Unique ID (EI) O S4.21.2.17

    bpx_18 : PL | None
        BPX.18 - BP Actual Dispensed To Location (PL) O S4.21.2.18

    bpx_19 : XAD | None
        BPX.19 - BP Actual Dispensed To Address (XAD) O S4.21.2.19

    bpx_20 : XCN | None
        BPX.20 - BP Dispensed to Receiver (XCN) O S4.21.2.20

    bpx_21 : XCN | None
        BPX.21 - BP Dispensing Individual (XCN) O S4.21.2.21
    """

    bpx_1: str = Field(
        validation_alias=AliasChoices(
            "bpx_1",
            "set_id_bpx",
            "BPX.1",
        ),
        serialization_alias="BPX.1",
        title="Set ID - BPX",
        description="R | Item #01714 | LEN:4",
    )

    bpx_2: CWE = Field(
        validation_alias=AliasChoices(
            "bpx_2",
            "bp_dispense_status",
            "BPX.2",
        ),
        serialization_alias="BPX.2",
        title="BP Dispense Status",
        description=(
            "R | Item #01715 | Table 0510 - Blood Product Dispense Status"
        ),
    )

    bpx_3: str = Field(
        validation_alias=AliasChoices(
            "bpx_3",
            "bp_status",
            "BPX.3",
        ),
        serialization_alias="BPX.3",
        title="BP Status",
        description=(
            "R | Item #01716 | Table 0511 - BP Observation Status Codes "
            "Interpretation | LEN:1"
        ),
    )

    bpx_4: TS = Field(
        validation_alias=AliasChoices(
            "bpx_4",
            "bp_date_time_of_status",
            "BPX.4",
        ),
        serialization_alias="BPX.4",
        title="BP Date/Time of Status",
        description="R | Item #01717",
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
        description="C | Item #01718",
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
        description="C | Item #01719",
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
        description="O | Item #01720",
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
        description="C | Item #01721 | Table 0512 - Commercial Product",
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
        description="C | Item #01722",
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
        description="C | Item #01723",
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
        description="O | Item #01724",
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
        description="O | Item #01725",
    )

    bpx_13: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_13",
            "bp_expiration_date_time",
            "BPX.13",
        ),
        serialization_alias="BPX.13",
        title="BP Expiration Date/Time",
        description="O | Item #01726",
    )

    bpx_14: str = Field(
        validation_alias=AliasChoices(
            "bpx_14",
            "bp_quantity",
            "BPX.14",
        ),
        serialization_alias="BPX.14",
        title="BP Quantity",
        description="R | Item #01727 | LEN:5",
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
        description="O | Item #01728 | LEN:5",
    )

    bpx_16: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bpx_16",
            "bp_units",
            "BPX.16",
        ),
        serialization_alias="BPX.16",
        title="BP Units",
        description="O | Item #01729",
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
        description="O | Item #01730",
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
        description="O | Item #01731",
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
        description="O | Item #01732",
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
        description="O | Item #01733",
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
        description="O | Item #01734",
    )

    @field_validator("bpx_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("bpx_14", "bpx_15", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
