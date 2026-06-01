"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: OM2
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CE import CE
from ..datatypes.TX import TX


class OM2(HL7Model):
    """HL7 v2 OM2 segment.

    Attributes
    ----------
    om2_1 : str | None
        OM2.1 (opt) - Segment Type ID (ST)

    om2_2 : str | None
        OM2.2 (opt) - Sequence Number - Test/ Observation Master File (NM)

    om2_3 : CE | None
        OM2.3 (opt) - Units of Measure (CE)

    om2_4 : str | None
        OM2.4 (opt) - Range of Decimal Precision (NM)

    om2_5 : CE | None
        OM2.5 (opt) - Corresponding SI Units of Measure (CE)

    om2_6 : list[TX] | None
        OM2.6 (req, rep) - SI Conversion Factor (TX) [optional: TX has no required components]

    om2_7 : list[str] | None
        OM2.7 (opt, rep) - Reference (normal) range - ordinal & continuous observations (CM)

    om2_8 : str | None
        OM2.8 (opt) - Critical range for ordinal and continuous observations (CM)

    om2_9 : str | None
        OM2.9 (opt) - Absolute range for ordinal and continuous observations (CM)

    om2_10 : list[str] | None
        OM2.10 (opt, rep) - Delta Check Criteria (CM)

    om2_11 : str | None
        OM2.11 (opt) - Minimum Meaningful Increments (NM)
    """

    om2_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_1",
            "segment_type_id",
            "OM2.1",
        ),
        serialization_alias="OM2.1",
        title="Segment Type ID",
        description="Item #585",
    )

    om2_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_2",
            "sequence_number_test_observation_master_file",
            "OM2.2",
        ),
        serialization_alias="OM2.2",
        title="Sequence Number - Test/ Observation Master File",
        description="Item #586",
    )

    om2_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_3",
            "units_of_measure",
            "OM2.3",
        ),
        serialization_alias="OM2.3",
        title="Units of Measure",
        description="Item #627",
    )

    om2_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_4",
            "range_of_decimal_precision",
            "OM2.4",
        ),
        serialization_alias="OM2.4",
        title="Range of Decimal Precision",
        description="Item #628",
    )

    om2_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_5",
            "corresponding_si_units_of_measure",
            "OM2.5",
        ),
        serialization_alias="OM2.5",
        title="Corresponding SI Units of Measure",
        description="Item #629",
    )

    om2_6: Optional[List[TX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_6",
            "si_conversion_factor",
            "OM2.6",
        ),
        serialization_alias="OM2.6",
        title="SI Conversion Factor",
        description="Item #630",
    )

    om2_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_7",
            "reference_normal_range_ordinal_continuous_observations",
            "OM2.7",
        ),
        serialization_alias="OM2.7",
        title="Reference (normal) range - ordinal & continuous observations",
        description="Item #631",
    )

    om2_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_8",
            "critical_range_for_ordinal_and_continuous_observations",
            "OM2.8",
        ),
        serialization_alias="OM2.8",
        title="Critical range for ordinal and continuous observations",
        description="Item #632",
    )

    om2_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_9",
            "absolute_range_for_ordinal_and_continuous_observations",
            "OM2.9",
        ),
        serialization_alias="OM2.9",
        title="Absolute range for ordinal and continuous observations",
        description="Item #633",
    )

    om2_10: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_10",
            "delta_check_criteria",
            "OM2.10",
        ),
        serialization_alias="OM2.10",
        title="Delta Check Criteria",
        description="Item #634",
    )

    om2_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_11",
            "minimum_meaningful_increments",
            "OM2.11",
        ),
        serialization_alias="OM2.11",
        title="Minimum Meaningful Increments",
        description="Item #635",
    )

    @field_validator("om2_2", "om2_4", "om2_11", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
