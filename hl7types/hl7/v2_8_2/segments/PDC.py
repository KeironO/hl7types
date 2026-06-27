"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PDC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.XON import XON


class PDC(HL7Model):
    """HL7 v2 PDC segment.

    Attributes
    ----------
    pdc_1 : list[XON]
        PDC.1 (req, rep) - Manufacturer/Distributor (XON)

    pdc_2 : CWE
        PDC.2 (req) - Country (CWE)

    pdc_3 : str
        PDC.3 (req) - Brand Name (ST)

    pdc_4 : str | None
        PDC.4 (opt) - Device Family Name (ST)

    pdc_5 : CWE | None
        PDC.5 (opt) - Generic Name (CWE)

    pdc_6 : list[str] | None
        PDC.6 (opt, rep) - Model Identifier (ST)

    pdc_7 : str | None
        PDC.7 (opt) - Catalogue Identifier (ST)

    pdc_8 : list[str] | None
        PDC.8 (opt, rep) - Other Identifier (ST)

    pdc_9 : CWE | None
        PDC.9 (opt) - Product Code (CWE)

    pdc_10 : str | None
        PDC.10 (opt) - Marketing Basis (ID)

    pdc_11 : str | None
        PDC.11 (opt) - Marketing Approval ID (ST)

    pdc_12 : CQ | None
        PDC.12 (opt) - Labeled Shelf Life (CQ)

    pdc_13 : CQ | None
        PDC.13 (opt) - Expected Shelf Life (CQ)

    pdc_14 : str | None
        PDC.14 (opt) - Date First Marketed (DTM)

    pdc_15 : str | None
        PDC.15 (opt) - Date Last Marketed (DTM)
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
        description="Item #1247",
    )

    pdc_2: CWE = Field(
        validation_alias=AliasChoices(
            "pdc_2",
            "country",
            "PDC.2",
        ),
        serialization_alias="PDC.2",
        title="Country",
        description="Item #1248 | Table HL79999",
    )

    pdc_3: str = Field(
        validation_alias=AliasChoices(
            "pdc_3",
            "brand_name",
            "PDC.3",
        ),
        serialization_alias="PDC.3",
        title="Brand Name",
        description="Item #1249",
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
        description="Item #1250",
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
        description="Item #1251 | Table HL79999",
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
        description="Item #1252",
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
        description="Item #1253",
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
        description="Item #1254",
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
        description="Item #1255 | Table HL79999",
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
        description="Item #1256 | Table HL70330",
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
        description="Item #1257",
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
        description="Item #1258",
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
        description="Item #1259",
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
        description="Item #1260",
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
        description="Item #1261",
    )

    @field_validator("pdc_14", "pdc_15", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
