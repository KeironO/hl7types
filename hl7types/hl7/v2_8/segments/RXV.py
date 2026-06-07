"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RXV
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE


class RXV(HL7Model):
    """HL7 v2 RXV segment.

    Attributes
    ----------
    rxv_1 : str | None
        RXV.1 (opt) - Set ID - RXV (SI)

    rxv_2 : str
        RXV.2 (req) - Bolus Type (ID)

    rxv_3 : str | None
        RXV.3 (opt) - Bolus Dose Amount (NM)

    rxv_4 : CWE | None
        RXV.4 (opt) - Bolus Dose Amount Units (CWE)

    rxv_5 : str | None
        RXV.5 (opt) - Bolus Dose Volume (NM)

    rxv_6 : CWE | None
        RXV.6 (opt) - Bolus Dose Volume Units (CWE)

    rxv_7 : str
        RXV.7 (req) - PCA Type (ID)

    rxv_8 : str | None
        RXV.8 (opt) - PCA Dose Amount (NM)

    rxv_9 : CWE | None
        RXV.9 (opt) - PCA Dose Amount Units (CWE)

    rxv_10 : str | None
        RXV.10 (opt) - PCA Dose Amount Volume (NM)

    rxv_11 : CWE | None
        RXV.11 (opt) - PCA Dose Amount Volume Units (CWE)

    rxv_12 : str | None
        RXV.12 (opt) - Max Dose Amount (NM)

    rxv_13 : CWE | None
        RXV.13 (opt) - Max Dose Amount Units (CWE)

    rxv_14 : str | None
        RXV.14 (opt) - Max Dose Amount Volume (NM)

    rxv_15 : CWE | None
        RXV.15 (opt) - Max Dose Amount Volume Units (CWE)

    rxv_16 : CQ
        RXV.16 (req) - Max Dose per Time (CQ)

    rxv_17 : CQ | None
        RXV.17 (opt) - Lockout Interval (CQ)

    rxv_18 : CWE | None
        RXV.18 (opt) - Syringe Manufacturer (CWE)

    rxv_19 : CWE | None
        RXV.19 (opt) - Syringe Model Number (CWE)

    rxv_20 : str | None
        RXV.20 (opt) - Syringe Size (NM)

    rxv_21 : CWE | None
        RXV.21 (opt) - Syringe Size Units (CWE)

    rxv_22 : str | None
        RXV.22 (opt) - Action Code (ID)
    """

    rxv_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_1",
            "set_id_rxv",
            "RXV.1",
        ),
        serialization_alias="RXV.1",
        title="Set ID - RXV",
        description="Item #3318",
    )

    rxv_2: str = Field(
        validation_alias=AliasChoices(
            "rxv_2",
            "bolus_type",
            "RXV.2",
        ),
        serialization_alias="RXV.2",
        title="Bolus Type",
        description="Item #3319 | Table HL70917",
    )

    rxv_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_3",
            "bolus_dose_amount",
            "RXV.3",
        ),
        serialization_alias="RXV.3",
        title="Bolus Dose Amount",
        description="Item #3320",
    )

    rxv_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_4",
            "bolus_dose_amount_units",
            "RXV.4",
        ),
        serialization_alias="RXV.4",
        title="Bolus Dose Amount Units",
        description="Item #3321 | Table HL79999",
    )

    rxv_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_5",
            "bolus_dose_volume",
            "RXV.5",
        ),
        serialization_alias="RXV.5",
        title="Bolus Dose Volume",
        description="Item #3322",
    )

    rxv_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_6",
            "bolus_dose_volume_units",
            "RXV.6",
        ),
        serialization_alias="RXV.6",
        title="Bolus Dose Volume Units",
        description="Item #3323 | Table HL79999",
    )

    rxv_7: str = Field(
        validation_alias=AliasChoices(
            "rxv_7",
            "pca_type",
            "RXV.7",
        ),
        serialization_alias="RXV.7",
        title="PCA Type",
        description="Item #3324 | Table HL70918",
    )

    rxv_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_8",
            "pca_dose_amount",
            "RXV.8",
        ),
        serialization_alias="RXV.8",
        title="PCA Dose Amount",
        description="Item #3325",
    )

    rxv_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_9",
            "pca_dose_amount_units",
            "RXV.9",
        ),
        serialization_alias="RXV.9",
        title="PCA Dose Amount Units",
        description="Item #3326 | Table HL79999",
    )

    rxv_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_10",
            "pca_dose_amount_volume",
            "RXV.10",
        ),
        serialization_alias="RXV.10",
        title="PCA Dose Amount Volume",
        description="Item #3327",
    )

    rxv_11: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_11",
            "pca_dose_amount_volume_units",
            "RXV.11",
        ),
        serialization_alias="RXV.11",
        title="PCA Dose Amount Volume Units",
        description="Item #3328 | Table HL79999",
    )

    rxv_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_12",
            "max_dose_amount",
            "RXV.12",
        ),
        serialization_alias="RXV.12",
        title="Max Dose Amount",
        description="Item #3329",
    )

    rxv_13: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_13",
            "max_dose_amount_units",
            "RXV.13",
        ),
        serialization_alias="RXV.13",
        title="Max Dose Amount Units",
        description="Item #3330 | Table HL79999",
    )

    rxv_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_14",
            "max_dose_amount_volume",
            "RXV.14",
        ),
        serialization_alias="RXV.14",
        title="Max Dose Amount Volume",
        description="Item #3331",
    )

    rxv_15: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_15",
            "max_dose_amount_volume_units",
            "RXV.15",
        ),
        serialization_alias="RXV.15",
        title="Max Dose Amount Volume Units",
        description="Item #3332 | Table HL79999",
    )

    rxv_16: CQ = Field(
        validation_alias=AliasChoices(
            "rxv_16",
            "max_dose_per_time",
            "RXV.16",
        ),
        serialization_alias="RXV.16",
        title="Max Dose per Time",
        description="Item #3333",
    )

    rxv_17: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_17",
            "lockout_interval",
            "RXV.17",
        ),
        serialization_alias="RXV.17",
        title="Lockout Interval",
        description="Item #3334",
    )

    rxv_18: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_18",
            "syringe_manufacturer",
            "RXV.18",
        ),
        serialization_alias="RXV.18",
        title="Syringe Manufacturer",
        description="Item #3339",
    )

    rxv_19: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_19",
            "syringe_model_number",
            "RXV.19",
        ),
        serialization_alias="RXV.19",
        title="Syringe Model Number",
        description="Item #3385",
    )

    rxv_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_20",
            "syringe_size",
            "RXV.20",
        ),
        serialization_alias="RXV.20",
        title="Syringe Size",
        description="Item #3386",
    )

    rxv_21: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_21",
            "syringe_size_units",
            "RXV.21",
        ),
        serialization_alias="RXV.21",
        title="Syringe Size Units",
        description="Item #3431",
    )

    rxv_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxv_22",
            "action_code",
            "RXV.22",
        ),
        serialization_alias="RXV.22",
        title="Action Code",
        description="Item #816 | Table HL70206",
    )

    @field_validator("rxv_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("rxv_3", "rxv_5", "rxv_8", "rxv_10", "rxv_12", "rxv_14", "rxv_20", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
