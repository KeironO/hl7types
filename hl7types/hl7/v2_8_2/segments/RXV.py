"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RXV
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class RXV(HL7Model):
    """Pharmacy/Treatment Infusion (S4.A.8).

    Attributes
    ----------
    rxv_1 : str | None
        RXV.1 - Set ID - RXV (SI) O S4.A.8.1

    rxv_2 : str
        RXV.2 - Bolus Type (ID) R S4.A.8.2 | 0917 - Bolus Type

    rxv_3 : str | None
        RXV.3 - Bolus Dose Amount (NM) O S4.A.8.3

    rxv_4 : CWE | None
        RXV.4 - Bolus Dose Amount Units (CWE) O S4.A.8.4 | 9999 - no table for CE

    rxv_5 : str | None
        RXV.5 - Bolus Dose Volume (NM) O S4.A.8.5

    rxv_6 : CWE | None
        RXV.6 - Bolus Dose Volume Units (CWE) O S4.A.8.6 | 9999 - no table for CE

    rxv_7 : str
        RXV.7 - PCA Type (ID) R S4.A.8.7 | 0918 - PCA Type

    rxv_8 : str | None
        RXV.8 - PCA Dose Amount (NM) O S4.A.8.8

    rxv_9 : CWE | None
        RXV.9 - PCA Dose Amount Units (CWE) O S4.A.8.9 | 9999 - no table for CE

    rxv_10 : str | None
        RXV.10 - PCA Dose Amount Volume (NM) O S4.A.8.10

    rxv_11 : CWE | None
        RXV.11 - PCA Dose Amount Volume Units (CWE) O S4.A.8.11 | 9999 - no table for CE

    rxv_12 : str | None
        RXV.12 - Max Dose Amount (NM) O S4.A.8.12

    rxv_13 : CWE | None
        RXV.13 - Max Dose Amount Units (CWE) O S4.A.8.13 | 9999 - no table for CE

    rxv_14 : str | None
        RXV.14 - Max Dose Amount Volume (NM) O S4.A.8.14

    rxv_15 : CWE | None
        RXV.15 - Max Dose Amount Volume Units (CWE) O S4.A.8.15 | 9999 - no table for CE

    rxv_16 : CQ
        RXV.16 - Max Dose per Time (CQ) R S4.A.8.16

    rxv_17 : CQ | None
        RXV.17 - Lockout Interval (CQ) O S4.A.8.17

    rxv_18 : CWE | None
        RXV.18 - Syringe Manufacturer (CWE) O S4.A.8.18

    rxv_19 : CWE | None
        RXV.19 - Syringe Model Number (CWE) O S4.A.8.19

    rxv_20 : str | None
        RXV.20 - Syringe Size (NM) C S4.A.8.20

    rxv_21 : CWE | None
        RXV.21 - Syringe Size Units (CWE) C S4.A.8.21

    rxv_22 : str | None
        RXV.22 - Action Code (ID) O S4.A.9.2 | 0206 - Segment Action Code
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
        description="O | Item #03318",
    )

    rxv_2: str = Field(
        validation_alias=AliasChoices(
            "rxv_2",
            "bolus_type",
            "RXV.2",
        ),
        serialization_alias="RXV.2",
        title="Bolus Type",
        description="R | Item #03319 | Table 0917 - Bolus Type | LEN:1",
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
        description="O | Item #03320",
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
        description="O | Item #03321 | Table 9999 - no table for CE",
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
        description="O | Item #03322",
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
        description="O | Item #03323 | Table 9999 - no table for CE",
    )

    rxv_7: str = Field(
        validation_alias=AliasChoices(
            "rxv_7",
            "pca_type",
            "RXV.7",
        ),
        serialization_alias="RXV.7",
        title="PCA Type",
        description="R | Item #03324 | Table 0918 - PCA Type | LEN:2",
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
        description="O | Item #03325",
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
        description="O | Item #03326 | Table 9999 - no table for CE",
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
        description="O | Item #03327",
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
        description="O | Item #03328 | Table 9999 - no table for CE",
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
        description="O | Item #03329",
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
        description="O | Item #03330 | Table 9999 - no table for CE",
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
        description="O | Item #03331",
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
        description="O | Item #03332 | Table 9999 - no table for CE",
    )

    rxv_16: CQ = Field(
        validation_alias=AliasChoices(
            "rxv_16",
            "max_dose_per_time",
            "RXV.16",
        ),
        serialization_alias="RXV.16",
        title="Max Dose per Time",
        description="R | Item #03333",
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
        description="O | Item #03334",
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
        description="O | Item #03339",
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
        description="O | Item #03385",
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
        description="C | Item #03386",
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
        description="C | Item #03431",
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
        description="O | Item #00816 | Table 0206 - Segment Action Code",
    )

    @field_validator("rxv_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("rxv_3", "rxv_5", "rxv_8", "rxv_10", "rxv_12", "rxv_14", "rxv_20", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
