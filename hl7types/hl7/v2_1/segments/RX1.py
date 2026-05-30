"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: RX1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TX import TX


class RX1(HL7Model):
    """HL7 v2 RX1 segment.

    Attributes
    ----------
    rx1_1 : str | None
        RX1.1 (opt) - UNUSED (ST)

    rx1_2 : str | None
        RX1.2 (opt) - UNUSED (ST)

    rx1_3 : str | None
        RX1.3 (opt) - ROUTE (ST)

    rx1_4 : str | None
        RX1.4 (opt) - SITE ADMINISTERED (ST)

    rx1_5 : str | None
        RX1.5 (opt) - IV SOLUTION RATE (CQ)

    rx1_6 : str | None
        RX1.6 (opt) - DRUG STRENGTH (CQ)

    rx1_7 : str | None
        RX1.7 (opt) - FINAL CONCENTRATION (NM)

    rx1_8 : str | None
        RX1.8 (opt) - FINAL VOLUME IN ML. (NM)

    rx1_9 : str | None
        RX1.9 (opt) - DRUG DOSE (CM)

    rx1_10 : str | None
        RX1.10 (opt) - DRUG ROLE (ID)

    rx1_11 : str | None
        RX1.11 (opt) - PRESCRIPTION SEQUENCE # (NM)

    rx1_12 : str | None
        RX1.12 (opt) - QUANTITY DISPENSED (CQ)

    rx1_13 : str | None
        RX1.13 (opt) - UNUSED (ST)

    rx1_14 : CE | None
        RX1.14 (opt) - DRUG ID (CE)

    rx1_15 : list[str] | None
        RX1.15 (opt, rep) - COMPONENT DRUG IDS (ID)

    rx1_16 : str | None
        RX1.16 (opt) - PRESCRIPTION TYPE (ID)

    rx1_17 : str | None
        RX1.17 (opt) - SUBSTITUTION STATUS (ID)

    rx1_18 : str | None
        RX1.18 (opt) - RX ORDER STATUS (ID)

    rx1_19 : str | None
        RX1.19 (opt) - NUMBER OF REFILLS (NM)

    rx1_20 : str | None
        RX1.20 (opt) - UNUSED (ST)

    rx1_21 : str | None
        RX1.21 (opt) - REFILLS REMAINING (NM)

    rx1_22 : str | None
        RX1.22 (opt) - DEA CLASS (ID)

    rx1_23 : str | None
        RX1.23 (opt) - ORDERING MD'S DEA NUMBER (NM)

    rx1_24 : str | None
        RX1.24 (opt) - UNUSED (ST)

    rx1_25 : str | None
        RX1.25 (opt) - LAST REFILL DATE/TIME (TS)

    rx1_26 : str | None
        RX1.26 (opt) - RX NUMBER (ST)

    rx1_27 : str | None
        RX1.27 (opt) - PRN STATUS (ID)

    rx1_28 : list[TX] | None
        RX1.28 (opt, rep) - PHARMACY INSTRUCTIONS (TX)

    rx1_29 : list[TX] | None
        RX1.29 (opt, rep) - PATIENT INSTRUCTIONS (TX)

    rx1_30 : list[TX] | None
        RX1.30 (opt, rep) - INSTRUCTIONS (SIG) (TX)
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
        description="Item #770",
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
        description="Item #771",
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
        description="Item #129 | Table HL70033",
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
        description="Item #130 | Table HL70034",
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
        description="Item #131",
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
        description="Item #133",
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
        description="Item #137",
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
        description="Item #138",
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
        description="Item #135",
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
        description="Item #139",
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
        description="Item #469",
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
        description="Item #470",
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
        description="Item #772",
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
        description="Item #473 | Table HL70057",
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
        description="Item #474",
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
        description="Item #479",
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
        description="Item #480",
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
        description="Item #588 | Table HL70038",
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
        description="Item #481",
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
        description="Item #773",
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
        description="Item #482",
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
        description="Item #619",
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
        description="Item #620",
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
        description="Item #774",
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
        description="Item #483",
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
        description="Item #596",
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
        description="Item #621",
    )

    rx1_28: Optional[List[TX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_28",
            "pharmacy_instructions",
            "RX1.28",
        ),
        serialization_alias="RX1.28",
        title="PHARMACY INSTRUCTIONS",
        description="Item #484",
    )

    rx1_29: Optional[List[TX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_29",
            "patient_instructions",
            "RX1.29",
        ),
        serialization_alias="RX1.29",
        title="PATIENT INSTRUCTIONS",
        description="Item #489",
    )

    rx1_30: Optional[List[TX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rx1_30",
            "instructions_sig",
            "RX1.30",
        ),
        serialization_alias="RX1.30",
        title="INSTRUCTIONS (SIG)",
        description="Item #618",
    )

    model_config = {"populate_by_name": True}
