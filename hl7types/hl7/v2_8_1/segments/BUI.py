"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: BUI
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.NR import NR
from ..datatypes.XON import XON


class BUI(HL7Model):
    """Blood Unit Information (S4.17.2).

    Attributes
    ----------
    bui_1 : str | None
        BUI.1 - Set ID - BUI (SI) O S4.17.2.1

    bui_2 : EI
        BUI.2 - Blood Unit Identifier (EI) R S4.17.2.2

    bui_3 : CWE
        BUI.3 - Blood Unit Type (CWE) R S4.17.2.3 | 0566 - Blood Unit Type

    bui_4 : str
        BUI.4 - Blood Unit Weight (NM) R S4.17.2.4

    bui_5 : CNE
        BUI.5 - Weight Units (CNE) R S4.17.2.5 | 0929 - Weight Units

    bui_6 : str
        BUI.6 - Blood Unit Volume (NM) R S4.17.2.6

    bui_7 : CNE
        BUI.7 - Volume Units (CNE) R S4.17.2.7 | 0930 - Volume Units

    bui_8 : str
        BUI.8 - Container Catalog Number (ST) R S4.17.2.8

    bui_9 : str
        BUI.9 - Container Lot Number (ST) R S4.17.2.9

    bui_10 : XON
        BUI.10 - Container Manufacturer (XON) R S4.17.2.10

    bui_11 : NR
        BUI.11 - Transport Temperature (NR) R S4.17.2.11

    bui_12 : CNE
        BUI.12 - Transport Temperature Units (CNE) R S4.17.2.12 | 0931 - Temperature Units
    """

    bui_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bui_1",
            "set_id_bui",
            "BUI.1",
        ),
        serialization_alias="BUI.1",
        title="Set ID - BUI",
        description="O | Item #03373 | LEN:4",
    )

    bui_2: EI = Field(
        validation_alias=AliasChoices(
            "bui_2",
            "blood_unit_identifier",
            "BUI.2",
        ),
        serialization_alias="BUI.2",
        title="Blood Unit Identifier",
        description="R | Item #03374",
    )

    bui_3: CWE = Field(
        validation_alias=AliasChoices(
            "bui_3",
            "blood_unit_type",
            "BUI.3",
        ),
        serialization_alias="BUI.3",
        title="Blood Unit Type",
        description="R | Item #03375 | Table 0566 - Blood Unit Type",
    )

    bui_4: str = Field(
        validation_alias=AliasChoices(
            "bui_4",
            "blood_unit_weight",
            "BUI.4",
        ),
        serialization_alias="BUI.4",
        title="Blood Unit Weight",
        description="R | Item #03376",
    )

    bui_5: CNE = Field(
        validation_alias=AliasChoices(
            "bui_5",
            "weight_units",
            "BUI.5",
        ),
        serialization_alias="BUI.5",
        title="Weight Units",
        description="R | Item #03377 | Table 0929 - Weight Units",
    )

    bui_6: str = Field(
        validation_alias=AliasChoices(
            "bui_6",
            "blood_unit_volume",
            "BUI.6",
        ),
        serialization_alias="BUI.6",
        title="Blood Unit Volume",
        description="R | Item #03378",
    )

    bui_7: CNE = Field(
        validation_alias=AliasChoices(
            "bui_7",
            "volume_units",
            "BUI.7",
        ),
        serialization_alias="BUI.7",
        title="Volume Units",
        description="R | Item #03379 | Table 0930 - Volume Units",
    )

    bui_8: str = Field(
        validation_alias=AliasChoices(
            "bui_8",
            "container_catalog_number",
            "BUI.8",
        ),
        serialization_alias="BUI.8",
        title="Container Catalog Number",
        description="R | Item #03380",
    )

    bui_9: str = Field(
        validation_alias=AliasChoices(
            "bui_9",
            "container_lot_number",
            "BUI.9",
        ),
        serialization_alias="BUI.9",
        title="Container Lot Number",
        description="R | Item #03381",
    )

    bui_10: XON = Field(
        validation_alias=AliasChoices(
            "bui_10",
            "container_manufacturer",
            "BUI.10",
        ),
        serialization_alias="BUI.10",
        title="Container Manufacturer",
        description="R | Item #03382",
    )

    bui_11: NR = Field(
        validation_alias=AliasChoices(
            "bui_11",
            "transport_temperature",
            "BUI.11",
        ),
        serialization_alias="BUI.11",
        title="Transport Temperature",
        description="R | Item #03383",
    )

    bui_12: CNE = Field(
        validation_alias=AliasChoices(
            "bui_12",
            "transport_temperature_units",
            "BUI.12",
        ),
        serialization_alias="BUI.12",
        title="Transport Temperature Units",
        description="R | Item #03384 | Table 0931 - Temperature Units",
    )

    @field_validator("bui_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("bui_4", "bui_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
