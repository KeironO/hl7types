"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RXO
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CN import CN


class RXO(HL7Model):
    """HL7 v2 RXO segment.

    Attributes
    ----------
    rxo_1 : CE
        RXO.1 (req) - Requested Give Code (CE)

    rxo_2 : str
        RXO.2 (req) - Requested Give Amount - Minimum (NM)

    rxo_3 : str | None
        RXO.3 (opt) - Requested Give Amount - Maximum (NM)

    rxo_4 : CE
        RXO.4 (req) - Requested Give Units (CE)

    rxo_5 : CE | None
        RXO.5 (opt) - Requested Dosage Form (CE)

    rxo_6 : list[CE] | None
        RXO.6 (opt, rep) - Provider's Pharmacy Instructions (CE)

    rxo_7 : list[CE] | None
        RXO.7 (opt, rep) - Provider's Administration Instructions (CE)

    rxo_8 : str | None
        RXO.8 (opt) - Deliver To Location (CM)

    rxo_9 : str | None
        RXO.9 (opt) - Allow Substitutions (ID)

    rxo_10 : CE | None
        RXO.10 (opt) - Requested Dispense Code (CE)

    rxo_11 : str | None
        RXO.11 (opt) - Requested Dispense Amount (NM)

    rxo_12 : CE | None
        RXO.12 (opt) - Requested Dispense Units (CE)

    rxo_13 : str | None
        RXO.13 (opt) - Number of Refills (NM)

    rxo_14 : CN | None
        RXO.14 (opt) - Ordering Provider's DEA Number (CN)

    rxo_15 : CN | None
        RXO.15 (opt) - Pharmacist/Treatment Supplier's Verifier ID (CN)

    rxo_16 : str | None
        RXO.16 (opt) - Needs Human Review (ID)

    rxo_17 : str | None
        RXO.17 (opt) - Requested Give Per (Time Unit) (ST)

    rxo_18 : str | None
        RXO.18 (opt) - Requested Give Strength (NM)

    rxo_19 : CE | None
        RXO.19 (opt) - Requested Give Strength Units (CE)

    rxo_20 : CE | None
        RXO.20 (opt) - Indication (CE)

    rxo_21 : str | None
        RXO.21 (opt) - Requested Give Rate Amount (ST)

    rxo_22 : CE | None
        RXO.22 (opt) - Requested Give Rate Units (CE)
    """

    rxo_1: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxo_1",
            "requested_give_code",
            "RXO.1",
        ),
        serialization_alias="RXO.1",
        title="Requested Give Code",
        description="Item #292",
    )

    rxo_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxo_2",
            "requested_give_amount_minimum",
            "RXO.2",
        ),
        serialization_alias="RXO.2",
        title="Requested Give Amount - Minimum",
        description="Item #293",
    )

    rxo_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_3",
            "requested_give_amount_maximum",
            "RXO.3",
        ),
        serialization_alias="RXO.3",
        title="Requested Give Amount - Maximum",
        description="Item #294",
    )

    rxo_4: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxo_4",
            "requested_give_units",
            "RXO.4",
        ),
        serialization_alias="RXO.4",
        title="Requested Give Units",
        description="Item #295",
    )

    rxo_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_5",
            "requested_dosage_form",
            "RXO.5",
        ),
        serialization_alias="RXO.5",
        title="Requested Dosage Form",
        description="Item #296",
    )

    rxo_6: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_6",
            "provider_s_pharmacy_instructions",
            "RXO.6",
        ),
        serialization_alias="RXO.6",
        title="Provider's Pharmacy Instructions",
        description="Item #297",
    )

    rxo_7: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_7",
            "provider_s_administration_instructions",
            "RXO.7",
        ),
        serialization_alias="RXO.7",
        title="Provider's Administration Instructions",
        description="Item #298",
    )

    rxo_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_8",
            "deliver_to_location",
            "RXO.8",
        ),
        serialization_alias="RXO.8",
        title="Deliver To Location",
        description="Item #299",
    )

    rxo_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_9",
            "allow_substitutions",
            "RXO.9",
        ),
        serialization_alias="RXO.9",
        title="Allow Substitutions",
        description="Item #300 | Table HL70161",
    )

    rxo_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_10",
            "requested_dispense_code",
            "RXO.10",
        ),
        serialization_alias="RXO.10",
        title="Requested Dispense Code",
        description="Item #301",
    )

    rxo_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_11",
            "requested_dispense_amount",
            "RXO.11",
        ),
        serialization_alias="RXO.11",
        title="Requested Dispense Amount",
        description="Item #302",
    )

    rxo_12: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_12",
            "requested_dispense_units",
            "RXO.12",
        ),
        serialization_alias="RXO.12",
        title="Requested Dispense Units",
        description="Item #303",
    )

    rxo_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_13",
            "number_of_refills",
            "RXO.13",
        ),
        serialization_alias="RXO.13",
        title="Number of Refills",
        description="Item #304",
    )

    rxo_14: Optional[CN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_14",
            "ordering_provider_s_dea_number",
            "RXO.14",
        ),
        serialization_alias="RXO.14",
        title="Ordering Provider's DEA Number",
        description="Item #305",
    )

    rxo_15: Optional[CN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_15",
            "pharmacist_treatment_supplier_s_verifier_id",
            "RXO.15",
        ),
        serialization_alias="RXO.15",
        title="Pharmacist/Treatment Supplier's Verifier ID",
        description="Item #306",
    )

    rxo_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_16",
            "needs_human_review",
            "RXO.16",
        ),
        serialization_alias="RXO.16",
        title="Needs Human Review",
        description="Item #307 | Table HL70136",
    )

    rxo_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_17",
            "requested_give_per_time_unit",
            "RXO.17",
        ),
        serialization_alias="RXO.17",
        title="Requested Give Per (Time Unit)",
        description="Item #308",
    )

    rxo_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_18",
            "requested_give_strength",
            "RXO.18",
        ),
        serialization_alias="RXO.18",
        title="Requested Give Strength",
        description="Item #1121",
    )

    rxo_19: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_19",
            "requested_give_strength_units",
            "RXO.19",
        ),
        serialization_alias="RXO.19",
        title="Requested Give Strength Units",
        description="Item #1122",
    )

    rxo_20: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_20",
            "indication",
            "RXO.20",
        ),
        serialization_alias="RXO.20",
        title="Indication",
        description="Item #1123",
    )

    rxo_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_21",
            "requested_give_rate_amount",
            "RXO.21",
        ),
        serialization_alias="RXO.21",
        title="Requested Give Rate Amount",
        description="Item #1218",
    )

    rxo_22: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_22",
            "requested_give_rate_units",
            "RXO.22",
        ),
        serialization_alias="RXO.22",
        title="Requested Give Rate Units",
        description="Item #1219",
    )

    model_config = {"populate_by_name": True}
