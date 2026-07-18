"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OM2
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.DLT import DLT
from ..datatypes.RFR import RFR

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class OM2(HL7Model):
    """Numeric Observation (S8.8.9).

    Attributes
    ----------
    om2_1 : str | None
        OM2.1 - Sequence Number - Test/Observation Master File (NM) O S8.8.10.1

    om2_2 : CWE | None
        OM2.2 - Units of Measure (CWE) O S8.8.9.2 | 9999 - no table for CE

    om2_3 : list[str] | None
        OM2.3 - Range of Decimal Precision (NM) O rep S8.8.9.3

    om2_4 : CWE | None
        OM2.4 - Corresponding SI Units of Measure (CWE) O S8.8.9.4 | 9999 - no table for CE

    om2_5 : str | None
        OM2.5 - SI Conversion Factor (TX) O S8.8.9.5

    om2_6 : list[RFR] | None
        OM2.6 - Reference (Normal) Range for Ordinal and Continuous Observations (RFR) O rep S8.8.9.6

    om2_7 : list[RFR] | None
        OM2.7 - Critical Range for Ordinal and Continuous Observations (RFR) O rep S8.8.9.7

    om2_8 : RFR | None
        OM2.8 - Absolute Range for Ordinal and Continuous Observations (RFR) O S8.8.9.8

    om2_9 : list[DLT] | None
        OM2.9 - Delta Check Criteria (DLT) O rep S8.8.9.9

    om2_10 : str | None
        OM2.10 - Minimum Meaningful Increments (NM) O S8.8.9.10
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
        description="O | Item #00586",
    )

    om2_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_2",
            "units_of_measure",
            "OM2.2",
        ),
        serialization_alias="OM2.2",
        title="Units of Measure",
        description="O | Item #00627 | Table 9999 - no table for CE",
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
        description="O | Item #00628",
    )

    om2_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_4",
            "corresponding_si_units_of_measure",
            "OM2.4",
        ),
        serialization_alias="OM2.4",
        title="Corresponding SI Units of Measure",
        description="O | Item #00629 | Table 9999 - no table for CE",
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
        description="O | Item #00630",
    )

    om2_6: Optional[List[RFR]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_6",
            "reference_normal_range_for_ordinal_and_continuous_observations",
            "OM2.6",
        ),
        serialization_alias="OM2.6",
        title=(
            "Reference (Normal) Range for Ordinal and Continuous Observations"
        ),
        description="O | Item #00631",
    )

    om2_7: Optional[List[RFR]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_7",
            "critical_range_for_ordinal_and_continuous_observations",
            "OM2.7",
        ),
        serialization_alias="OM2.7",
        title="Critical Range for Ordinal and Continuous Observations",
        description="O | Item #00632",
    )

    om2_8: Optional[RFR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_8",
            "absolute_range_for_ordinal_and_continuous_observations",
            "OM2.8",
        ),
        serialization_alias="OM2.8",
        title="Absolute Range for Ordinal and Continuous Observations",
        description="O | Item #00633",
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
        description="O | Item #00634",
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
        description="O | Item #00635",
    )

    @field_validator("om2_1", "om2_3", "om2_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
