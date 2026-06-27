"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CSU
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator, ValidationInfo
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback


class CSU(HL7Model):
    """HL7 v2 CSU data type.

    Attributes
    ----------
    csu_1 : str
        CSU.1 (req) - Channel Sensitivity (NM)

    csu_2 : str | None
        CSU.2 (opt) - Unit of Measure Identifier (ST)

    csu_3 : str | None
        CSU.3 (opt) - Unit of Measure Description (ST)

    csu_4 : str | None
        CSU.4 (opt) - Unit of Measure Coding System (ID)

    csu_5 : str | None
        CSU.5 (opt) - Alternate Unit of Measure Identifier (ST)

    csu_6 : str | None
        CSU.6 (opt) - Alternate Unit of Measure Description (ST)

    csu_7 : str | None
        CSU.7 (opt) - Alternate Unit of Measure Coding System (ID)

    csu_8 : str | None
        CSU.8 (opt) - Unit of Measure Coding System Version ID (ST)

    csu_9 : str | None
        CSU.9 (opt) - Alternate Unit of Measure Coding System Version ID (ST)

    csu_10 : str | None
        CSU.10 (opt) - Original Text (ST)

    csu_11 : str | None
        CSU.11 (opt) - Second Alternate Unit of Measure Identifier (ST)

    csu_12 : str | None
        CSU.12 (opt) - Second Alternate Unit of Measure Text (ST)

    csu_13 : str | None
        CSU.13 (opt) - Name of Second Alternate Unit of Measure Coding Sy (ID)

    csu_14 : str | None
        CSU.14 (opt) - Second Alternate Unit of Measure Coding System Ver (ST)

    csu_15 : str | None
        CSU.15 (opt) - Unit of Measure Coding System OID (ST)

    csu_16 : str | None
        CSU.16 (opt) - Unit of Measure Value Set OID (ST)

    csu_17 : str | None
        CSU.17 (opt) - Unit of Measure Value Set Version ID (DTM)

    csu_18 : str | None
        CSU.18 (opt) - Alternate Unit of Measure Coding System OID (ST)

    csu_19 : str | None
        CSU.19 (opt) - Alternate Unit of Measure Value Set OID (ST)

    csu_20 : str | None
        CSU.20 (opt) - Alternate Unit of Measure Value Set Version ID (DTM)

    csu_21 : str | None
        CSU.21 (opt) - Alternate Unit of Measure Coding System OID (ST)

    csu_22 : str | None
        CSU.22 (opt) - Alternate Unit of Measure Value Set OID (ST)

    csu_23 : str | None
        CSU.23 (opt) - Alternate Unit of Measure Value Set Version ID (ST)
    """

    csu_1: str = Field(
        validation_alias=AliasChoices(
            "csu_1",
            "channel_sensitivity",
            "CSU.1",
        ),
        serialization_alias="CSU.1",
        title="Channel Sensitivity",
    )

    csu_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_2",
            "unit_of_measure_identifier",
            "CSU.2",
        ),
        serialization_alias="CSU.2",
        title="Unit of Measure Identifier",
    )

    csu_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_3",
            "unit_of_measure_description",
            "CSU.3",
        ),
        serialization_alias="CSU.3",
        title="Unit of Measure Description",
    )

    csu_4: Optional[str] = Field(
        default=None,
        max_length=12,
        validation_alias=AliasChoices(
            "csu_4",
            "unit_of_measure_coding_system",
            "CSU.4",
        ),
        serialization_alias="CSU.4",
        title="Unit of Measure Coding System",
    )

    csu_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_5",
            "alternate_unit_of_measure_identifier",
            "CSU.5",
        ),
        serialization_alias="CSU.5",
        title="Alternate Unit of Measure Identifier",
    )

    csu_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_6",
            "alternate_unit_of_measure_description",
            "CSU.6",
        ),
        serialization_alias="CSU.6",
        title="Alternate Unit of Measure Description",
    )

    csu_7: Optional[str] = Field(
        default=None,
        max_length=12,
        validation_alias=AliasChoices(
            "csu_7",
            "alternate_unit_of_measure_coding_system",
            "CSU.7",
        ),
        serialization_alias="CSU.7",
        title="Alternate Unit of Measure Coding System",
    )

    csu_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_8",
            "unit_of_measure_coding_system_version_id",
            "CSU.8",
        ),
        serialization_alias="CSU.8",
        title="Unit of Measure Coding System Version ID",
    )

    csu_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_9",
            "alternate_unit_of_measure_coding_system_version_id",
            "CSU.9",
        ),
        serialization_alias="CSU.9",
        title="Alternate Unit of Measure Coding System Version ID",
    )

    csu_10: Optional[str] = Field(
        default=None,
        max_length=199,
        validation_alias=AliasChoices(
            "csu_10",
            "original_text",
            "CSU.10",
        ),
        serialization_alias="CSU.10",
        title="Original Text",
    )

    csu_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_11",
            "second_alternate_unit_of_measure_identifier",
            "CSU.11",
        ),
        serialization_alias="CSU.11",
        title="Second Alternate Unit of Measure Identifier",
    )

    csu_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_12",
            "second_alternate_unit_of_measure_text",
            "CSU.12",
        ),
        serialization_alias="CSU.12",
        title="Second Alternate Unit of Measure Text",
    )

    csu_13: Optional[str] = Field(
        default=None,
        max_length=12,
        validation_alias=AliasChoices(
            "csu_13",
            "name_of_second_alternate_unit_of_measure_coding_sy",
            "CSU.13",
        ),
        serialization_alias="CSU.13",
        title="Name of Second Alternate Unit of Measure Coding Sy",
    )

    csu_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_14",
            "second_alternate_unit_of_measure_coding_system_ver",
            "CSU.14",
        ),
        serialization_alias="CSU.14",
        title="Second Alternate Unit of Measure Coding System Ver",
    )

    csu_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_15",
            "unit_of_measure_coding_system_oid",
            "CSU.15",
        ),
        serialization_alias="CSU.15",
        title="Unit of Measure Coding System OID",
    )

    csu_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_16",
            "unit_of_measure_value_set_oid",
            "CSU.16",
        ),
        serialization_alias="CSU.16",
        title="Unit of Measure Value Set OID",
    )

    csu_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_17",
            "unit_of_measure_value_set_version_id",
            "CSU.17",
        ),
        serialization_alias="CSU.17",
        title="Unit of Measure Value Set Version ID",
    )

    csu_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_18",
            "alternate_unit_of_measure_coding_system_oid",
            "CSU.18",
        ),
        serialization_alias="CSU.18",
        title="Alternate Unit of Measure Coding System OID",
    )

    csu_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_19",
            "alternate_unit_of_measure_value_set_oid",
            "CSU.19",
        ),
        serialization_alias="CSU.19",
        title="Alternate Unit of Measure Value Set OID",
    )

    csu_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_20",
            "alternate_unit_of_measure_value_set_version_id",
            "CSU.20",
        ),
        serialization_alias="CSU.20",
        title="Alternate Unit of Measure Value Set Version ID",
    )

    csu_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_21",
            "alternate_unit_of_measure_coding_system_oid",
            "CSU.21",
        ),
        serialization_alias="CSU.21",
        title="Alternate Unit of Measure Coding System OID",
    )

    csu_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_22",
            "alternate_unit_of_measure_value_set_oid",
            "CSU.22",
        ),
        serialization_alias="CSU.22",
        title="Alternate Unit of Measure Value Set OID",
    )

    csu_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_23",
            "alternate_unit_of_measure_value_set_version_id",
            "CSU.23",
        ),
        serialization_alias="CSU.23",
        title="Alternate Unit of Measure Value Set Version ID",
    )

    @field_validator("csu_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("csu_17", "csu_20", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
