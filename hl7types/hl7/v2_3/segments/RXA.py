"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RXA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class RXA(HL7Model):
    """Pharmacy administration segment (S4.8.14).

    Attributes
    ----------
    rxa_1 : str
        RXA.1 - Give Sub-ID Counter (ID) R S4.8.12

    rxa_2 : str
        RXA.2 - Administration Sub-ID Counter (NM) R S4.8.14.2

    rxa_3 : TS
        RXA.3 - Date/Time Start of Administration (TS) R S4.8.14.3

    rxa_4 : TS
        RXA.4 - Date/Time End of Administration (TS) R S4.8.14.4

    rxa_5 : CE
        RXA.5 - Administered Code (CE) R S4.8.14.5 | 0292 - Vaccines Administered

    rxa_6 : str
        RXA.6 - Administered Amount (NM) R S4.8.14.6

    rxa_7 : CE | None
        RXA.7 - Administered Units (CE) C S4.8.14.7

    rxa_8 : CE | None
        RXA.8 - Administered Dosage Form (CE) O S4.8.14.8

    rxa_9 : list[CE] | None
        RXA.9 - Administration Notes (CE) C rep S4.8.12

    rxa_10 : XCN | None
        RXA.10 - Administering Provider (XCN) O S4.8.14.10

    rxa_11 : str | None
        RXA.11 - Administered-at Location (CM) C S4.8.14.11

    rxa_12 : str | None
        RXA.12 - Administered Per (Time Unit) (ST) C S4.8.14.12

    rxa_13 : str | None
        RXA.13 - Administered Strength (NM) O S4.8.14.13

    rxa_14 : CE | None
        RXA.14 - Administered Strength Units (CE) O S4.8.14.14

    rxa_15 : list[str] | None
        RXA.15 - Substance Lot Number (ST) O rep S4.8.10

    rxa_16 : list[TS] | None
        RXA.16 - Substance Expiration Date (TS) O rep S4.8.10

    rxa_17 : list[CE] | None
        RXA.17 - Substance Manufacturer Name (CE) O rep S4.8.10 | 0227 - Manufacturers of Vaccines

    rxa_18 : list[CE] | None
        RXA.18 - Substance Refusal Reason (CE) O rep S4.8.14.18

    rxa_19 : list[CE] | None
        RXA.19 - Indication (CE) O rep S4.8.2

    rxa_20 : str | None
        RXA.20 - Completion Status (ID) O S4.8.14.20 | 0322 - Completion Status

    rxa_21 : str | None
        RXA.21 - Action Code-RXA (ID) O S4.8.14.21 | 0323 - Action Code

    rxa_22 : TS | None
        RXA.22 - System Entry Date/Time (TS) O S4.8.14.22
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

    rxa_3: TS = Field(
        validation_alias=AliasChoices(
            "rxa_3",
            "date_time_start_of_administration",
            "RXA.3",
        ),
        serialization_alias="RXA.3",
        title="Date/Time Start of Administration",
        description="R | Item #00345",
    )

    rxa_4: TS = Field(
        validation_alias=AliasChoices(
            "rxa_4",
            "date_time_end_of_administration",
            "RXA.4",
        ),
        serialization_alias="RXA.4",
        title="Date/Time End of Administration",
        description="R | Item #00346",
    )

    rxa_5: CE = Field(
        validation_alias=AliasChoices(
            "rxa_5",
            "administered_code",
            "RXA.5",
        ),
        serialization_alias="RXA.5",
        title="Administered Code",
        description="R | Item #00347 | Table 0292 - Vaccines Administered",
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

    rxa_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_7",
            "administered_units",
            "RXA.7",
        ),
        serialization_alias="RXA.7",
        title="Administered Units",
        description="C | Item #00349",
    )

    rxa_8: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_8",
            "administered_dosage_form",
            "RXA.8",
        ),
        serialization_alias="RXA.8",
        title="Administered Dosage Form",
        description="O | Item #00350",
    )

    rxa_9: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_9",
            "administration_notes",
            "RXA.9",
        ),
        serialization_alias="RXA.9",
        title="Administration Notes",
        description="C | Item #00351",
    )

    rxa_10: Optional[XCN] = Field(
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

    rxa_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_11",
            "administered_at_location",
            "RXA.11",
        ),
        serialization_alias="RXA.11",
        title="Administered-at Location",
        description="C | Item #00353",
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

    rxa_14: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_14",
            "administered_strength_units",
            "RXA.14",
        ),
        serialization_alias="RXA.14",
        title="Administered Strength Units",
        description="O | Item #01135",
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

    rxa_16: Optional[List[TS]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_16",
            "substance_expiration_date",
            "RXA.16",
        ),
        serialization_alias="RXA.16",
        title="Substance Expiration Date",
        description="O | Item #01130",
    )

    rxa_17: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_17",
            "substance_manufacturer_name",
            "RXA.17",
        ),
        serialization_alias="RXA.17",
        title="Substance Manufacturer Name",
        description="O | Item #01131 | Table 0227 - Manufacturers of Vaccines",
    )

    rxa_18: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_18",
            "substance_refusal_reason",
            "RXA.18",
        ),
        serialization_alias="RXA.18",
        title="Substance Refusal Reason",
        description="O | Item #01136",
    )

    rxa_19: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_19",
            "indication",
            "RXA.19",
        ),
        serialization_alias="RXA.19",
        title="Indication",
        description="O | Item #01123",
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
        title="Action Code-RXA",
        description="O | Item #01224 | Table 0323 - Action Code | LEN:2",
    )

    rxa_22: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_22",
            "system_entry_date_time",
            "RXA.22",
        ),
        serialization_alias="RXA.22",
        title="System Entry Date/Time",
        description="O | Item #01225",
    )

    @field_validator("rxa_2", "rxa_6", "rxa_13", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
