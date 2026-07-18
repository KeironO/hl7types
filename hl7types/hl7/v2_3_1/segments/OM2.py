"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OM2
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.DLT import DLT
from ..datatypes.NR import NR
from ..datatypes.RFR import RFR

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class OM2(HL7Model):
    """OM2 - numeric observation segment (S8.7.4).

    Attributes
    ----------
    om2_1 : str | None
        OM2.1 - Sequence Number - Test/Observation Master File (NM) NA S8.7.8.1

    om2_2 : CE | None
        OM2.2 - Units of Measure (CE) NA S8.7.4.2

    om2_3 : list[str] | None
        OM2.3 - Range of Decimal Precision (NM) NA rep S8.7.4.3

    om2_4 : CE | None
        OM2.4 - Corresponding SI Units of Measure (CE) NA S8.7.4.4

    om2_5 : str | None
        OM2.5 - SI Conversion Factor (TX) NA S8.7.4.5

    om2_6 : RFR | None
        OM2.6 - Reference (Normal) Range - Ordinal & Continuous Obs (RFR) NA S8.7.4.6

    om2_7 : NR | None
        OM2.7 - Critical Range for Ordinal & Continuous Obs (NR) NA S8.7.4.7

    om2_8 : RFR | None
        OM2.8 - Absolute Range for Ordinal & Continuous Obs (RFR) NA S8.7.4.8

    om2_9 : list[DLT] | None
        OM2.9 - Delta Check Criteria (DLT) NA rep S8.7.4.9

    om2_10 : str | None
        OM2.10 - Minimum Meaningful Increments (NM) NA S8.7.4.10
    """

    om2_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_1",
            "sequence_number_test_observation_master_file",
            "OM2.1",
        ),
        serialization_alias="OM2.1",
        title="Sequence Number - Test/Observation Master File",
        description="NA | Item #00586 | LEN:4",
    )

    om2_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_2",
            "units_of_measure",
            "OM2.2",
        ),
        serialization_alias="OM2.2",
        title="Units of Measure",
        description="NA | Item #00627",
    )

    om2_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_3",
            "range_of_decimal_precision",
            "OM2.3",
        ),
        serialization_alias="OM2.3",
        title="Range of Decimal Precision",
        description="NA | Item #00628 | LEN:10",
    )

    om2_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_4",
            "corresponding_si_units_of_measure",
            "OM2.4",
        ),
        serialization_alias="OM2.4",
        title="Corresponding SI Units of Measure",
        description="NA | Item #00629",
    )

    om2_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_5",
            "si_conversion_factor",
            "OM2.5",
        ),
        serialization_alias="OM2.5",
        title="SI Conversion Factor",
        description="NA | Item #00630",
    )

    om2_6: Optional[RFR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_6",
            "reference_normal_range_ordinal_continuous_obs",
            "OM2.6",
        ),
        serialization_alias="OM2.6",
        title="Reference (Normal) Range - Ordinal & Continuous Obs",
        description="NA | Item #00631",
    )

    om2_7: Optional[NR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_7",
            "critical_range_for_ordinal_continuous_obs",
            "OM2.7",
        ),
        serialization_alias="OM2.7",
        title="Critical Range for Ordinal & Continuous Obs",
        description="NA | Item #00632",
    )

    om2_8: Optional[RFR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_8",
            "absolute_range_for_ordinal_continuous_obs",
            "OM2.8",
        ),
        serialization_alias="OM2.8",
        title="Absolute Range for Ordinal & Continuous Obs",
        description="NA | Item #00633",
    )

    om2_9: Optional[List[DLT]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_9",
            "delta_check_criteria",
            "OM2.9",
        ),
        serialization_alias="OM2.9",
        title="Delta Check Criteria",
        description="NA | Item #00634",
    )

    om2_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_10",
            "minimum_meaningful_increments",
            "OM2.10",
        ),
        serialization_alias="OM2.10",
        title="Minimum Meaningful Increments",
        description="NA | Item #00635 | LEN:20",
    )

    @field_validator("om2_1", "om2_3", "om2_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
