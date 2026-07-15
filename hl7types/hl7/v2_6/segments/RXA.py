"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RXA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.LA2 import LA2
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN


class RXA(HL7Model):
    """Pharmacy/Treatment Administration (S4.14.7).

    Attributes
    ----------
    rxa_1 : str
        RXA.1 - Give Sub-ID Counter (NM) R S4.14.6.1

    rxa_2 : str
        RXA.2 - Administration Sub-ID Counter (NM) R S4.14.7.2

    rxa_3 : str
        RXA.3 - Date/Time Start of Administration (DTM) R S4.14.7.3

    rxa_4 : str
        RXA.4 - Date/Time End of Administration (DTM) R S4.14.7.4

    rxa_5 : CWE
        RXA.5 - Administered Code (CWE) R S4.14.7.5 | 0292 - Vaccines administered

    rxa_6 : str
        RXA.6 - Administered Amount (NM) R S4.14.7.6

    rxa_7 : CWE | None
        RXA.7 - Administered Units (CWE) C S4.14.7.7 | 9999 - no table for CE

    rxa_8 : CWE | None
        RXA.8 - Administered Dosage Form (CWE) O S4.14.7.8 | 9999 - no table for CE

    rxa_9 : list[CWE] | None
        RXA.9 - Administration Notes (CWE) O rep S4.14.6.9 | 9999 - no table for CE

    rxa_10 : list[XCN] | None
        RXA.10 - Administering Provider (XCN) O rep S4.14.7.10

    rxa_11 : LA2 | None
        RXA.11 - Administered-at Location (LA2) O S4.14.7.11

    rxa_12 : str | None
        RXA.12 - Administered Per (Time Unit) (ST) C S4.14.7.12

    rxa_13 : str | None
        RXA.13 - Administered Strength (NM) O S4.14.7.13

    rxa_14 : CWE | None
        RXA.14 - Administered Strength Units (CWE) O S4.14.7.14 | 9999 - no table for CE

    rxa_15 : list[str] | None
        RXA.15 - Substance Lot Number (ST) O rep S13.4.11.2

    rxa_16 : list[str] | None
        RXA.16 - Substance Expiration Date (DTM) O rep S4.14.5.19

    rxa_17 : list[CWE] | None
        RXA.17 - Substance Manufacturer Name (CWE) O rep S4.14.5.20 | 0227 - Manufacturers of Vaccines (code=MVX)

    rxa_18 : list[CWE] | None
        RXA.18 - Substance/Treatment Refusal Reason (CWE) O rep S4.14.7.18 | 9999 - no table for CE

    rxa_19 : list[CWE] | None
        RXA.19 - Indication (CWE) O rep S4.14.1.20 | 9999 - no table for CE

    rxa_20 : str | None
        RXA.20 - Completion Status (ID) O S4.14.7.20 | 0322 - Completion Status

    rxa_21 : str | None
        RXA.21 - Action Code - RXA (ID) O S4.14.7.21 | 0206 - Segment action code

    rxa_22 : str | None
        RXA.22 - System Entry Date/Time (DTM) O S4.14.7.22

    rxa_23 : str | None
        RXA.23 - Administered Drug Strength Volume (NM) O S4.14.7.23

    rxa_24 : CWE | None
        RXA.24 - Administered Drug Strength Volume Units (CWE) O S4.14.7.24 | 9999 - no table for CE

    rxa_25 : CWE | None
        RXA.25 - Administered Barcode Identifier (CWE) O S4.14.7.25 | 9999 - no table for CE

    rxa_26 : str | None
        RXA.26 - Pharmacy Order Type (ID) O S4.14.7.26 | 0480 - Pharmacy Order Types

    rxa_27 : PL | None
        RXA.27 - Administer-at (PL) O S4.14.7.27

    rxa_28 : XAD | None
        RXA.28 - Administered-at Address (XAD) O S4.14.7.28
    """

    rxa_1: str = Field(
        validation_alias=AliasChoices(
            "rxa_1",
            "give_sub_id_counter",
            "RXA.1",
        ),
        serialization_alias="RXA.1",
        title="Give Sub-ID Counter",
        description="R | Item #00342 | LEN:4",
    )

    rxa_2: str = Field(
        validation_alias=AliasChoices(
            "rxa_2",
            "administration_sub_id_counter",
            "RXA.2",
        ),
        serialization_alias="RXA.2",
        title="Administration Sub-ID Counter",
        description="R | Item #00344 | LEN:4",
    )

    rxa_3: str = Field(
        validation_alias=AliasChoices(
            "rxa_3",
            "date_time_start_of_administration",
            "RXA.3",
        ),
        serialization_alias="RXA.3",
        title="Date/Time Start of Administration",
        description="R | Item #00345 | LEN:24",
    )

    rxa_4: str = Field(
        validation_alias=AliasChoices(
            "rxa_4",
            "date_time_end_of_administration",
            "RXA.4",
        ),
        serialization_alias="RXA.4",
        title="Date/Time End of Administration",
        description="R | Item #00346 | LEN:24",
    )

    rxa_5: CWE = Field(
        validation_alias=AliasChoices(
            "rxa_5",
            "administered_code",
            "RXA.5",
        ),
        serialization_alias="RXA.5",
        title="Administered Code",
        description="R | Item #00347 | Table 0292 - Vaccines administered",
    )

    rxa_6: str = Field(
        validation_alias=AliasChoices(
            "rxa_6",
            "administered_amount",
            "RXA.6",
        ),
        serialization_alias="RXA.6",
        title="Administered Amount",
        description="R | Item #00348 | LEN:20",
    )

    rxa_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_7",
            "administered_units",
            "RXA.7",
        ),
        serialization_alias="RXA.7",
        title="Administered Units",
        description="C | Item #00349 | Table 9999 - no table for CE",
    )

    rxa_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_8",
            "administered_dosage_form",
            "RXA.8",
        ),
        serialization_alias="RXA.8",
        title="Administered Dosage Form",
        description="O | Item #00350 | Table 9999 - no table for CE",
    )

    rxa_9: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_9",
            "administration_notes",
            "RXA.9",
        ),
        serialization_alias="RXA.9",
        title="Administration Notes",
        description="O | Item #00351 | Table 9999 - no table for CE",
    )

    rxa_10: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_10",
            "administering_provider",
            "RXA.10",
        ),
        serialization_alias="RXA.10",
        title="Administering Provider",
        description="O | Item #00352",
    )

    rxa_11: Optional[LA2] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_11",
            "administered_at_location",
            "RXA.11",
        ),
        serialization_alias="RXA.11",
        title="Administered-at Location",
        description="O | Item #00353",
    )

    rxa_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_12",
            "administered_per_time_unit",
            "RXA.12",
        ),
        serialization_alias="RXA.12",
        title="Administered Per (Time Unit)",
        description="C | Item #00354 | LEN:20",
    )

    rxa_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_13",
            "administered_strength",
            "RXA.13",
        ),
        serialization_alias="RXA.13",
        title="Administered Strength",
        description="O | Item #01134 | LEN:20",
    )

    rxa_14: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_14",
            "administered_strength_units",
            "RXA.14",
        ),
        serialization_alias="RXA.14",
        title="Administered Strength Units",
        description="O | Item #01135 | Table 9999 - no table for CE",
    )

    rxa_15: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_15",
            "substance_lot_number",
            "RXA.15",
        ),
        serialization_alias="RXA.15",
        title="Substance Lot Number",
        description="O | Item #01129 | LEN:20",
    )

    rxa_16: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_16",
            "substance_expiration_date",
            "RXA.16",
        ),
        serialization_alias="RXA.16",
        title="Substance Expiration Date",
        description="O | Item #01130 | LEN:24",
    )

    rxa_17: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_17",
            "substance_manufacturer_name",
            "RXA.17",
        ),
        serialization_alias="RXA.17",
        title="Substance Manufacturer Name",
        description=(
            "O | Item #01131 | Table 0227 - Manufacturers of Vaccines (code=MVX)"
        ),
    )

    rxa_18: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_18",
            "substance_treatment_refusal_reason",
            "RXA.18",
        ),
        serialization_alias="RXA.18",
        title="Substance/Treatment Refusal Reason",
        description="O | Item #01136 | Table 9999 - no table for CE",
    )

    rxa_19: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_19",
            "indication",
            "RXA.19",
        ),
        serialization_alias="RXA.19",
        title="Indication",
        description="O | Item #01123 | Table 9999 - no table for CE",
    )

    rxa_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_20",
            "completion_status",
            "RXA.20",
        ),
        serialization_alias="RXA.20",
        title="Completion Status",
        description="O | Item #01223 | Table 0322 - Completion Status | LEN:2",
    )

    rxa_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_21",
            "action_code_rxa",
            "RXA.21",
        ),
        serialization_alias="RXA.21",
        title="Action Code - RXA",
        description=(
            "O | Item #01224 | Table 0206 - Segment action code | LEN:2"
        ),
    )

    rxa_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_22",
            "system_entry_date_time",
            "RXA.22",
        ),
        serialization_alias="RXA.22",
        title="System Entry Date/Time",
        description="O | Item #01225 | LEN:24",
    )

    rxa_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_23",
            "administered_drug_strength_volume",
            "RXA.23",
        ),
        serialization_alias="RXA.23",
        title="Administered Drug Strength Volume",
        description="O | Item #01696 | LEN:5",
    )

    rxa_24: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_24",
            "administered_drug_strength_volume_units",
            "RXA.24",
        ),
        serialization_alias="RXA.24",
        title="Administered Drug Strength Volume Units",
        description="O | Item #01697 | Table 9999 - no table for CE",
    )

    rxa_25: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_25",
            "administered_barcode_identifier",
            "RXA.25",
        ),
        serialization_alias="RXA.25",
        title="Administered Barcode Identifier",
        description="O | Item #01698 | Table 9999 - no table for CE",
    )

    rxa_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_26",
            "pharmacy_order_type",
            "RXA.26",
        ),
        serialization_alias="RXA.26",
        title="Pharmacy Order Type",
        description=(
            "O | Item #01699 | Table 0480 - Pharmacy Order Types | LEN:1"
        ),
    )

    rxa_27: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_27",
            "administer_at",
            "RXA.27",
        ),
        serialization_alias="RXA.27",
        title="Administer-at",
        description="O | Item #02264",
    )

    rxa_28: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_28",
            "administered_at_address",
            "RXA.28",
        ),
        serialization_alias="RXA.28",
        title="Administered-at Address",
        description="O | Item #02265",
    )

    @field_validator("rxa_1", "rxa_2", "rxa_6", "rxa_13", "rxa_23", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("rxa_3", "rxa_4", "rxa_16", "rxa_22", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
