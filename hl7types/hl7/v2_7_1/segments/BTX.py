"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: BTX
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class BTX(HL7Model):
    """Blood Product Transfusion/Disposition (S4.13.3).

    Attributes
    ----------
    btx_1 : str
        BTX.1 - Set ID - BTX (SI) R S4.13.3.1

    btx_2 : EI | None
        BTX.2 - BC Donation ID (EI) C S4.13.3.2

    btx_3 : CNE | None
        BTX.3 - BC Component (CNE) C S4.13.3.3 | 9999 - no table for CE

    btx_4 : CNE | None
        BTX.4 - BC Blood Group (CNE) C S4.13.3.4 | 9999 - no table for CE

    btx_5 : CWE | None
        BTX.5 - CP Commercial Product (CWE) C S4.13.3.5 | 0512 - Commercial Product

    btx_6 : XON | None
        BTX.6 - CP Manufacturer (XON) C S4.13.3.6

    btx_7 : EI | None
        BTX.7 - CP Lot Number (EI) C S4.13.3.7

    btx_8 : str
        BTX.8 - BP Quantity (NM) R S4.13.3.8

    btx_9 : str | None
        BTX.9 - BP Amount (NM) O S4.13.3.9

    btx_10 : CWE | None
        BTX.10 - BP Units (CWE) O S4.13.3.10 | 9999 - no table for CE

    btx_11 : CWE
        BTX.11 - BP Transfusion/Disposition Status (CWE) R S4.13.3.11 | 0513 - Blood Product Transfusion/Disposition Status

    btx_12 : str
        BTX.12 - BP Message Status (ID) R S4.13.3.12 | 0511 - BP Observation Status Codes Interpretation

    btx_13 : str
        BTX.13 - BP Date/Time of Status (DTM) R S4.13.3.13

    btx_14 : XCN | None
        BTX.14 - BP Transfusion Administrator (XCN) O S4.13.3.14

    btx_15 : XCN | None
        BTX.15 - BP Transfusion Verifier (XCN) O S4.13.3.15

    btx_16 : str | None
        BTX.16 - BP Transfusion Start Date/Time of Status (DTM) O S4.13.3.16

    btx_17 : str | None
        BTX.17 - BP Transfusion End Date/Time of Status (DTM) O S4.13.3.17

    btx_18 : list[CWE] | None
        BTX.18 - BP Adverse Reaction Type (CWE) O rep S4.13.3.18 | 0514 - Transfusion Adverse Reaction

    btx_19 : CWE | None
        BTX.19 - BP Transfusion Interrupted Reason (CWE) O S4.13.3.19 | 0515 - Transfusion Interrupted Reason
    """

    btx_1: str = Field(
        validation_alias=AliasChoices(
            "btx_1",
            "set_id_btx",
            "BTX.1",
        ),
        serialization_alias="BTX.1",
        title="Set ID - BTX",
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
        description="C | Item #01737 | Table 9999 - no table for CE",
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
        description="C | Item #01738 | Table 9999 - no table for CE",
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
        description="R | Item #01742",
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
        description="O | Item #01743",
    )

    btx_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_10",
            "bp_units",
            "BTX.10",
        ),
        serialization_alias="BTX.10",
        title="BP Units",
        description="O | Item #01744 | Table 9999 - no table for CE",
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

    btx_13: str = Field(
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
            "bp_transfusion_administrator",
            "BTX.14",
        ),
        serialization_alias="BTX.14",
        title="BP Transfusion Administrator",
        description="O | Item #01748",
    )

    btx_15: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_15",
            "bp_transfusion_verifier",
            "BTX.15",
        ),
        serialization_alias="BTX.15",
        title="BP Transfusion Verifier",
        description="O | Item #01749",
    )

    btx_16: Optional[str] = Field(
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

    btx_17: Optional[str] = Field(
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

    @field_validator("btx_13", "btx_16", "btx_17", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
