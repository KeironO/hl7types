"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: BTX
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
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class BTX(HL7Model):
    """Blood Product Transfusion/Disposition (S4.21.3).

    Attributes
    ----------
    btx_1 : str
        BTX.1 - Set ID _ BTX (SI) R S4.21.3.1

    btx_2 : EI | None
        BTX.2 - BC Donation ID (EI) C S4.21.3.2

    btx_3 : CNE | None
        BTX.3 - BC Component (CNE) C S4.21.3.3

    btx_4 : CNE | None
        BTX.4 - BC Blood Group (CNE) C S4.21.3.4

    btx_5 : CWE | None
        BTX.5 - CP Commercial Product (CWE) C S4.21.3.5 | 0512 - Commercial Product

    btx_6 : XON | None
        BTX.6 - CP Manufacturer (XON) C S4.21.3.6

    btx_7 : EI | None
        BTX.7 - CP Lot Number (EI) C S4.21.3.7

    btx_8 : str
        BTX.8 - BP Quantity (NM) R S4.21.3.8

    btx_9 : str | None
        BTX.9 - BP Amount (NM) O S4.21.3.9

    btx_10 : CE | None
        BTX.10 - BP Units (CE) O S4.21.3.10

    btx_11 : CWE
        BTX.11 - BP Transfusion/Disposition Status (CWE) R S4.21.3.11 | 0513 - Blood Product Transfusion/Disposition Status

    btx_12 : str
        BTX.12 - BP Message Status (ID) R S4.21.3.12 | 0511 - BP Observation Status Codes Interpretation

    btx_13 : TS
        BTX.13 - BP Date/Time of Status (TS) R S4.21.3.13

    btx_14 : XCN | None
        BTX.14 - BP Administrator (XCN) O S4.21.3.14

    btx_15 : XCN | None
        BTX.15 - BP Verifier (XCN) O S4.21.3.15

    btx_16 : TS | None
        BTX.16 - BP Transfusion Start Date/Time of Status (TS) O S4.21.3.16

    btx_17 : TS | None
        BTX.17 - BP Transfusion End Date/Time of Status (TS) O S4.21.3.17

    btx_18 : list[CWE] | None
        BTX.18 - BP Adverse Reaction Type (CWE) O rep S4.21.3.18 | 0514 - Transfusion Adverse Reaction

    btx_19 : CWE | None
        BTX.19 - BP Transfusion Interrupted Reason (CWE) O S4.21.3.19 | 0515 - Transfusion Interrupted Reason
    """

    btx_1: str = Field(
        validation_alias=AliasChoices(
            "btx_1",
            "set_id_btx",
            "BTX.1",
        ),
        serialization_alias="BTX.1",
        title="Set ID _ BTX",
        description="R | Item #01735 | LEN:4",
    )

    btx_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_2",
            "bc_donation_id",
            "BTX.2",
        ),
        serialization_alias="BTX.2",
        title="BC Donation ID",
        description="C | Item #01736",
    )

    btx_3: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_3",
            "bc_component",
            "BTX.3",
        ),
        serialization_alias="BTX.3",
        title="BC Component",
        description="C | Item #01737",
    )

    btx_4: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_4",
            "bc_blood_group",
            "BTX.4",
        ),
        serialization_alias="BTX.4",
        title="BC Blood Group",
        description="C | Item #01738",
    )

    btx_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_5",
            "cp_commercial_product",
            "BTX.5",
        ),
        serialization_alias="BTX.5",
        title="CP Commercial Product",
        description="C | Item #01739 | Table 0512 - Commercial Product",
    )

    btx_6: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_6",
            "cp_manufacturer",
            "BTX.6",
        ),
        serialization_alias="BTX.6",
        title="CP Manufacturer",
        description="C | Item #01740",
    )

    btx_7: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_7",
            "cp_lot_number",
            "BTX.7",
        ),
        serialization_alias="BTX.7",
        title="CP Lot Number",
        description="C | Item #01741",
    )

    btx_8: str = Field(
        validation_alias=AliasChoices(
            "btx_8",
            "bp_quantity",
            "BTX.8",
        ),
        serialization_alias="BTX.8",
        title="BP Quantity",
        description="R | Item #01742 | LEN:5",
    )

    btx_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_9",
            "bp_amount",
            "BTX.9",
        ),
        serialization_alias="BTX.9",
        title="BP Amount",
        description="O | Item #01743 | LEN:5",
    )

    btx_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_10",
            "bp_units",
            "BTX.10",
        ),
        serialization_alias="BTX.10",
        title="BP Units",
        description="O | Item #01744",
    )

    btx_11: CWE = Field(
        validation_alias=AliasChoices(
            "btx_11",
            "bp_transfusion_disposition_status",
            "BTX.11",
        ),
        serialization_alias="BTX.11",
        title="BP Transfusion/Disposition Status",
        description=(
            "R | Item #01745 | Table 0513 - Blood Product Transfusion/Disposition "
            "Status"
        ),
    )

    btx_12: str = Field(
        validation_alias=AliasChoices(
            "btx_12",
            "bp_message_status",
            "BTX.12",
        ),
        serialization_alias="BTX.12",
        title="BP Message Status",
        description=(
            "R | Item #01746 | Table 0511 - BP Observation Status Codes "
            "Interpretation | LEN:1"
        ),
    )

    btx_13: TS = Field(
        validation_alias=AliasChoices(
            "btx_13",
            "bp_date_time_of_status",
            "BTX.13",
        ),
        serialization_alias="BTX.13",
        title="BP Date/Time of Status",
        description="R | Item #01747",
    )

    btx_14: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_14",
            "bp_administrator",
            "BTX.14",
        ),
        serialization_alias="BTX.14",
        title="BP Administrator",
        description="O | Item #01748",
    )

    btx_15: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_15",
            "bp_verifier",
            "BTX.15",
        ),
        serialization_alias="BTX.15",
        title="BP Verifier",
        description="O | Item #01749",
    )

    btx_16: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_16",
            "bp_transfusion_start_date_time_of_status",
            "BTX.16",
        ),
        serialization_alias="BTX.16",
        title="BP Transfusion Start Date/Time of Status",
        description="O | Item #01750",
    )

    btx_17: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_17",
            "bp_transfusion_end_date_time_of_status",
            "BTX.17",
        ),
        serialization_alias="BTX.17",
        title="BP Transfusion End Date/Time of Status",
        description="O | Item #01751",
    )

    btx_18: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_18",
            "bp_adverse_reaction_type",
            "BTX.18",
        ),
        serialization_alias="BTX.18",
        title="BP Adverse Reaction Type",
        description=(
            "O | Item #01752 | Table 0514 - Transfusion Adverse Reaction"
        ),
    )

    btx_19: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_19",
            "bp_transfusion_interrupted_reason",
            "BTX.19",
        ),
        serialization_alias="BTX.19",
        title="BP Transfusion Interrupted Reason",
        description=(
            "O | Item #01753 | Table 0515 - Transfusion Interrupted Reason"
        ),
    )

    @field_validator("btx_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("btx_8", "btx_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
