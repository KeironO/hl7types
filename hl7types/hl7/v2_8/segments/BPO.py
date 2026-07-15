"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: BPO
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD


class BPO(HL7Model):
    """Blood product order (S4.14.1).

    Attributes
    ----------
    bpo_1 : str
        BPO.1 - Set ID - BPO (SI) R S4.14.1.1

    bpo_2 : CWE
        BPO.2 - BP Universal Service Identifier (CWE) R S4.14.1.2 | 9999 - no table for CE

    bpo_3 : list[CWE] | None
        BPO.3 - BP  Processing Requirements (CWE) O rep S4.14.1.3 | 0508 - Blood Product Processing Requirements

    bpo_4 : str
        BPO.4 - BP Quantity (NM) R S4.14.1.4

    bpo_5 : str | None
        BPO.5 - BP Amount (NM) O S4.14.1.5

    bpo_6 : CWE | None
        BPO.6 - BP Units (CWE) O S4.14.1.6 | 9999 - no table for CE

    bpo_7 : str | None
        BPO.7 - BP Intended Use Date/Time (DTM) O S4.14.1.7

    bpo_8 : PL | None
        BPO.8 - BP Intended Dispense From Location (PL) O S4.14.1.8

    bpo_9 : XAD | None
        BPO.9 - BP Intended Dispense From Address (XAD) O S4.14.1.9

    bpo_10 : str | None
        BPO.10 - BP Requested Dispense Date/Time (DTM) O S4.14.1.10

    bpo_11 : PL | None
        BPO.11 - BP Requested Dispense To Location (PL) O S4.14.1.11

    bpo_12 : XAD | None
        BPO.12 - BP Requested Dispense To Address (XAD) O S4.14.1.12

    bpo_13 : list[CWE] | None
        BPO.13 - BP Indication for Use (CWE) O rep S4.14.1.13 | 0509 - Indication for Use

    bpo_14 : str | None
        BPO.14 - BP Informed Consent Indicator (ID) O S4.14.1.14 | 0136 - Yes/no Indicator
    """

    bpo_1: str = Field(
        validation_alias=AliasChoices(
            "bpo_1",
            "set_id_bpo",
            "BPO.1",
        ),
        serialization_alias="BPO.1",
        title="Set ID - BPO",
        description="R | Item #01700 | LEN:4",
    )

    bpo_2: CWE = Field(
        validation_alias=AliasChoices(
            "bpo_2",
            "bp_universal_service_identifier",
            "BPO.2",
        ),
        serialization_alias="BPO.2",
        title="BP Universal Service Identifier",
        description="R | Item #01701 | Table 9999 - no table for CE",
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
        description=(
            "O | Item #01702 | Table 0508 - Blood Product Processing Requirements"
        ),
    )

    bpo_4: str = Field(
        validation_alias=AliasChoices(
            "bpo_4",
            "bp_quantity",
            "BPO.4",
        ),
        serialization_alias="BPO.4",
        title="BP Quantity",
        description="R | Item #01703",
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
        description="O | Item #01704",
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
        description="O | Item #01705 | Table 9999 - no table for CE",
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
        description="O | Item #01706",
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
        description="O | Item #01707",
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
        description="O | Item #01708",
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
        description="O | Item #01709",
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
        description="O | Item #01710",
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
        description="O | Item #01711",
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
        description="O | Item #01712 | Table 0509 - Indication for Use",
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
        description="O | Item #01713 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    @field_validator("bpo_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("bpo_4", "bpo_5", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("bpo_7", "bpo_10", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
