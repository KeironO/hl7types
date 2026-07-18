"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: RX1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class RX1(HL7Model):
    """PHARMACY ORDER.

    Attributes
    ----------
    rx1_1 : str | None
        RX1.1 - UNUSED (ST) O S4-14

    rx1_2 : str | None
        RX1.2 - UNUSED (ST) O

    rx1_3 : str | None
        RX1.3 - ROUTE (ST) O | 0033 - ROUTE

    rx1_4 : str | None
        RX1.4 - SITE ADMINISTERED (ST) O | 0034 - SITE ADMINISTERED

    rx1_5 : str | None
        RX1.5 - IV SOLUTION RATE (CQ) O

    rx1_6 : str | None
        RX1.6 - DRUG STRENGTH (CQ) O

    rx1_7 : str | None
        RX1.7 - FINAL CONCENTRATION (NM) O

    rx1_8 : str | None
        RX1.8 - FINAL VOLUME IN ML. (NM) O

    rx1_9 : str | None
        RX1.9 - DRUG DOSE (CM) O

    rx1_10 : str | None
        RX1.10 - DRUG ROLE (ID) O

    rx1_11 : str | None
        RX1.11 - PRESCRIPTION SEQUENCE # (NM) O

    rx1_12 : str | None
        RX1.12 - QUANTITY DISPENSED (CQ) O

    rx1_13 : str | None
        RX1.13 - UNUSED (ST) O

    rx1_14 : CE | None
        RX1.14 - DRUG ID (CE) O | 0057 - DRUG CODE

    rx1_15 : list[str] | None
        RX1.15 - COMPONENT DRUG IDS (ID) O rep

    rx1_16 : str | None
        RX1.16 - PRESCRIPTION TYPE (ID) O

    rx1_17 : str | None
        RX1.17 - SUBSTITUTION STATUS (ID) O

    rx1_18 : str | None
        RX1.18 - RX ORDER STATUS (ID) O | 0038 - ORDER STATUS

    rx1_19 : str | None
        RX1.19 - NUMBER OF REFILLS (NM) O

    rx1_20 : str | None
        RX1.20 - UNUSED (ST) O

    rx1_21 : str | None
        RX1.21 - REFILLS REMAINING (NM) O

    rx1_22 : str | None
        RX1.22 - DEA CLASS (ID) O

    rx1_23 : str | None
        RX1.23 - ORDERING MD'S DEA NUMBER (NM) O

    rx1_24 : str | None
        RX1.24 - UNUSED (ST) O

    rx1_25 : str | None
        RX1.25 - LAST REFILL DATE/TIME (TS) O

    rx1_26 : str | None
        RX1.26 - RX NUMBER (ST) O

    rx1_27 : str | None
        RX1.27 - PRN STATUS (ID) O

    rx1_28 : list[str] | None
        RX1.28 - PHARMACY INSTRUCTIONS (TX) O rep

    rx1_29 : list[str] | None
        RX1.29 - PATIENT INSTRUCTIONS (TX) O rep

    rx1_30 : list[str] | None
        RX1.30 - INSTRUCTIONS (SIG) (TX) O rep
    """

    rx1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_1",
            "unused",
            "RX1.1",
        ),
        serialization_alias="RX1.1",
        title="UNUSED",
        description="O | Item #00770",
    )

    rx1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_2",
            "unused",
            "RX1.2",
        ),
        serialization_alias="RX1.2",
        title="UNUSED",
        description="O | Item #00771",
    )

    rx1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_3",
            "route",
            "RX1.3",
        ),
        serialization_alias="RX1.3",
        title="ROUTE",
        description="O | Item #00129 | Table 0033 - ROUTE | LEN:8",
    )

    rx1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_4",
            "site_administered",
            "RX1.4",
        ),
        serialization_alias="RX1.4",
        title="SITE ADMINISTERED",
        description="O | Item #00130 | Table 0034 - SITE ADMINISTERED | LEN:20",
    )

    rx1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_5",
            "iv_solution_rate",
            "RX1.5",
        ),
        serialization_alias="RX1.5",
        title="IV SOLUTION RATE",
        description="O | Item #00131 | LEN:10",
    )

    rx1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_6",
            "drug_strength",
            "RX1.6",
        ),
        serialization_alias="RX1.6",
        title="DRUG STRENGTH",
        description="O | Item #00133 | LEN:14",
    )

    rx1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_7",
            "final_concentration",
            "RX1.7",
        ),
        serialization_alias="RX1.7",
        title="FINAL CONCENTRATION",
        description="O | Item #00137 | LEN:10",
    )

    rx1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_8",
            "final_volume_in_ml",
            "RX1.8",
        ),
        serialization_alias="RX1.8",
        title="FINAL VOLUME IN ML.",
        description="O | Item #00138 | LEN:10",
    )

    rx1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_9",
            "drug_dose",
            "RX1.9",
        ),
        serialization_alias="RX1.9",
        title="DRUG DOSE",
        description="O | Item #00135 | LEN:10",
    )

    rx1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_10",
            "drug_role",
            "RX1.10",
        ),
        serialization_alias="RX1.10",
        title="DRUG ROLE",
        description="O | Item #00139 | LEN:1",
    )

    rx1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_11",
            "prescription_sequence",
            "RX1.11",
        ),
        serialization_alias="RX1.11",
        title="PRESCRIPTION SEQUENCE #",
        description="O | Item #00469 | LEN:3",
    )

    rx1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_12",
            "quantity_dispensed",
            "RX1.12",
        ),
        serialization_alias="RX1.12",
        title="QUANTITY DISPENSED",
        description="O | Item #00470 | LEN:4",
    )

    rx1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_13",
            "unused",
            "RX1.13",
        ),
        serialization_alias="RX1.13",
        title="UNUSED",
        description="O | Item #00772",
    )

    rx1_14: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_14",
            "drug_id",
            "RX1.14",
        ),
        serialization_alias="RX1.14",
        title="DRUG ID",
        description="O | Item #00473 | Table 0057 - DRUG CODE",
    )

    rx1_15: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_15",
            "component_drug_ids",
            "RX1.15",
        ),
        serialization_alias="RX1.15",
        title="COMPONENT DRUG IDS",
        description="O | Item #00474 | LEN:5",
    )

    rx1_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_16",
            "prescription_type",
            "RX1.16",
        ),
        serialization_alias="RX1.16",
        title="PRESCRIPTION TYPE",
        description="O | Item #00479 | LEN:2",
    )

    rx1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_17",
            "substitution_status",
            "RX1.17",
        ),
        serialization_alias="RX1.17",
        title="SUBSTITUTION STATUS",
        description="O | Item #00480 | LEN:1",
    )

    rx1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_18",
            "rx_order_status",
            "RX1.18",
        ),
        serialization_alias="RX1.18",
        title="RX ORDER STATUS",
        description="O | Item #00588 | Table 0038 - ORDER STATUS | LEN:2",
    )

    rx1_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_19",
            "number_of_refills",
            "RX1.19",
        ),
        serialization_alias="RX1.19",
        title="NUMBER OF REFILLS",
        description="O | Item #00481 | LEN:3",
    )

    rx1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_20",
            "unused",
            "RX1.20",
        ),
        serialization_alias="RX1.20",
        title="UNUSED",
        description="O | Item #00773",
    )

    rx1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_21",
            "refills_remaining",
            "RX1.21",
        ),
        serialization_alias="RX1.21",
        title="REFILLS REMAINING",
        description="O | Item #00482 | LEN:3",
    )

    rx1_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_22",
            "dea_class",
            "RX1.22",
        ),
        serialization_alias="RX1.22",
        title="DEA CLASS",
        description="O | Item #00619 | LEN:5",
    )

    rx1_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_23",
            "ordering_md_s_dea_number",
            "RX1.23",
        ),
        serialization_alias="RX1.23",
        title="ORDERING MD'S DEA NUMBER",
        description="O | Item #00620 | LEN:10",
    )

    rx1_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_24",
            "unused",
            "RX1.24",
        ),
        serialization_alias="RX1.24",
        title="UNUSED",
        description="O | Item #00774",
    )

    rx1_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_25",
            "last_refill_date_time",
            "RX1.25",
        ),
        serialization_alias="RX1.25",
        title="LAST REFILL DATE/TIME",
        description="O | Item #00483 | LEN:19",
    )

    rx1_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_26",
            "rx_number",
            "RX1.26",
        ),
        serialization_alias="RX1.26",
        title="RX NUMBER",
        description="O | Item #00596 | LEN:20",
    )

    rx1_27: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_27",
            "prn_status",
            "RX1.27",
        ),
        serialization_alias="RX1.27",
        title="PRN STATUS",
        description="O | Item #00621 | LEN:5",
    )

    rx1_28: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_28",
            "pharmacy_instructions",
            "RX1.28",
        ),
        serialization_alias="RX1.28",
        title="PHARMACY INSTRUCTIONS",
        description="O | Item #00484",
    )

    rx1_29: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_29",
            "patient_instructions",
            "RX1.29",
        ),
        serialization_alias="RX1.29",
        title="PATIENT INSTRUCTIONS",
        description="O | Item #00489",
    )

    rx1_30: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_30",
            "instructions_sig",
            "RX1.30",
        ),
        serialization_alias="RX1.30",
        title="INSTRUCTIONS (SIG)",
        description="O | Item #00618",
    )

    @field_validator("rx1_7", "rx1_8", "rx1_11", "rx1_19", "rx1_21", "rx1_23", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
