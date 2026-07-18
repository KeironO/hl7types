"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PDC
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.XON import XON

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class PDC(HL7Model):
    """Product Detail Country (S7.12.5).

    Attributes
    ----------
    pdc_1 : list[XON]
        PDC.1 - Manufacturer/Distributor (XON) R rep S7.12.5.1

    pdc_2 : CWE
        PDC.2 - Country (CWE) R S7.12.5.2 | 9999 - no table for CE

    pdc_3 : str
        PDC.3 - Brand Name (ST) R S7.12.5.3

    pdc_4 : str | None
        PDC.4 - Device Family Name (ST) O S7.12.5.4

    pdc_5 : CWE | None
        PDC.5 - Generic Name (CWE) O S7.12.5.5 | 9999 - no table for CE

    pdc_6 : list[str] | None
        PDC.6 - Model Identifier (ST) O rep S7.12.5.6

    pdc_7 : str | None
        PDC.7 - Catalogue Identifier (ST) O S7.12.5.7

    pdc_8 : list[str] | None
        PDC.8 - Other Identifier (ST) O rep S7.12.5.8

    pdc_9 : CWE | None
        PDC.9 - Product Code (CWE) O S7.12.5.9 | 9999 - no table for CE

    pdc_10 : str | None
        PDC.10 - Marketing Basis (ID) O S7.12.5.10 | 0330 - Marketing Basis

    pdc_11 : str | None
        PDC.11 - Marketing Approval ID (ST) O S7.12.5.11

    pdc_12 : CQ | None
        PDC.12 - Labeled Shelf Life (CQ) O S7.12.5.12

    pdc_13 : CQ | None
        PDC.13 - Expected Shelf Life (CQ) O S7.12.5.13

    pdc_14 : str | None
        PDC.14 - Date First Marketed (DTM) O S7.12.5.14

    pdc_15 : str | None
        PDC.15 - Date Last Marketed (DTM) O S7.12.5.15
    """

    pdc_1: List[XON] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "pdc_1",
            "manufacturer_distributor",
            "PDC.1",
        ),
        serialization_alias="PDC.1",
        title="Manufacturer/Distributor",
        description="R | Item #01247",
    )

    pdc_2: CWE = Field(
        validation_alias=AliasChoices(
            "pdc_2",
            "country",
            "PDC.2",
        ),
        serialization_alias="PDC.2",
        title="Country",
        description="R | Item #01248 | Table 9999 - no table for CE",
    )

    pdc_3: str = Field(
        validation_alias=AliasChoices(
            "pdc_3",
            "brand_name",
            "PDC.3",
        ),
        serialization_alias="PDC.3",
        title="Brand Name",
        description="R | Item #01249",
    )

    pdc_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pdc_4",
            "device_family_name",
            "PDC.4",
        ),
        serialization_alias="PDC.4",
        title="Device Family Name",
        description="O | Item #01250",
    )

    pdc_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pdc_5",
            "generic_name",
            "PDC.5",
        ),
        serialization_alias="PDC.5",
        title="Generic Name",
        description="O | Item #01251 | Table 9999 - no table for CE",
    )

    pdc_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pdc_6",
            "model_identifier",
            "PDC.6",
        ),
        serialization_alias="PDC.6",
        title="Model Identifier",
        description="O | Item #01252",
    )

    pdc_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pdc_7",
            "catalogue_identifier",
            "PDC.7",
        ),
        serialization_alias="PDC.7",
        title="Catalogue Identifier",
        description="O | Item #01253",
    )

    pdc_8: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pdc_8",
            "other_identifier",
            "PDC.8",
        ),
        serialization_alias="PDC.8",
        title="Other Identifier",
        description="O | Item #01254",
    )

    pdc_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pdc_9",
            "product_code",
            "PDC.9",
        ),
        serialization_alias="PDC.9",
        title="Product Code",
        description="O | Item #01255 | Table 9999 - no table for CE",
    )

    pdc_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pdc_10",
            "marketing_basis",
            "PDC.10",
        ),
        serialization_alias="PDC.10",
        title="Marketing Basis",
        description="O | Item #01256 | Table 0330 - Marketing Basis | LEN:4",
    )

    pdc_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pdc_11",
            "marketing_approval_id",
            "PDC.11",
        ),
        serialization_alias="PDC.11",
        title="Marketing Approval ID",
        description="O | Item #01257",
    )

    pdc_12: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pdc_12",
            "labeled_shelf_life",
            "PDC.12",
        ),
        serialization_alias="PDC.12",
        title="Labeled Shelf Life",
        description="O | Item #01258",
    )

    pdc_13: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pdc_13",
            "expected_shelf_life",
            "PDC.13",
        ),
        serialization_alias="PDC.13",
        title="Expected Shelf Life",
        description="O | Item #01259",
    )

    pdc_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pdc_14",
            "date_first_marketed",
            "PDC.14",
        ),
        serialization_alias="PDC.14",
        title="Date First Marketed",
        description="O | Item #01260",
    )

    pdc_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pdc_15",
            "date_last_marketed",
            "PDC.15",
        ),
        serialization_alias="PDC.15",
        title="Date Last Marketed",
        description="O | Item #01261",
    )

    @field_validator("pdc_14", "pdc_15", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
