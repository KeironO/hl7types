"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CWE
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator, ValidationInfo
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback


class CWE(HL7Model):
    """HL7 v2 CWE data type.

    Attributes
    ----------
    cwe_1 : str | None
        CWE.1 (opt) - Identifier (ST)

    cwe_2 : str | None
        CWE.2 (opt) - Text (ST)

    cwe_3 : str | None
        CWE.3 (opt) - Name of Coding System (ID)

    cwe_4 : str | None
        CWE.4 (opt) - Alternate Identifier (ST)

    cwe_5 : str | None
        CWE.5 (opt) - Alternate Text (ST)

    cwe_6 : str | None
        CWE.6 (opt) - Name of Alternate Coding System (ID)

    cwe_7 : str | None
        CWE.7 (opt) - Coding System Version ID (ST)

    cwe_8 : str | None
        CWE.8 (opt) - Alternate Coding System Version ID (ST)

    cwe_9 : str | None
        CWE.9 (opt) - Original Text (ST)

    cwe_10 : str | None
        CWE.10 (opt) - Second Alternate Identifier (ST)

    cwe_11 : str | None
        CWE.11 (opt) - Second Alternate Text (ST)

    cwe_12 : str | None
        CWE.12 (opt) - Name of Second Alternate Coding System (ID)

    cwe_13 : str | None
        CWE.13 (opt) - Second Alternate Coding System Version ID (ST)

    cwe_14 : str | None
        CWE.14 (opt) - Coding System OID (ST)

    cwe_15 : str | None
        CWE.15 (opt) - Value Set OID (ST)

    cwe_16 : str | None
        CWE.16 (opt) - Value Set Version ID (DTM)

    cwe_17 : str | None
        CWE.17 (opt) - Alternate Coding System OID (ST)

    cwe_18 : str | None
        CWE.18 (opt) - Alternate Value Set OID (ST)

    cwe_19 : str | None
        CWE.19 (opt) - Alternate Value Set Version ID (DTM)

    cwe_20 : str | None
        CWE.20 (opt) - Second Alternate Coding System OID (ST)

    cwe_21 : str | None
        CWE.21 (opt) - Second Alternate Value Set OID (ST)

    cwe_22 : str | None
        CWE.22 (opt) - Second Alternate Value Set Version ID (DTM)
    """

    cwe_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_1",
            "identifier",
            "CWE.1",
        ),
        serialization_alias="CWE.1",
        title="Identifier",
    )

    cwe_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_2",
            "text",
            "CWE.2",
        ),
        serialization_alias="CWE.2",
        title="Text",
    )

    cwe_3: Optional[str] = Field(
        default=None,
        max_length=12,
        validation_alias=AliasChoices(
            "cwe_3",
            "name_of_coding_system",
            "CWE.3",
        ),
        serialization_alias="CWE.3",
        title="Name of Coding System",
    )

    cwe_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_4",
            "alternate_identifier",
            "CWE.4",
        ),
        serialization_alias="CWE.4",
        title="Alternate Identifier",
    )

    cwe_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_5",
            "alternate_text",
            "CWE.5",
        ),
        serialization_alias="CWE.5",
        title="Alternate Text",
    )

    cwe_6: Optional[str] = Field(
        default=None,
        max_length=12,
        validation_alias=AliasChoices(
            "cwe_6",
            "name_of_alternate_coding_system",
            "CWE.6",
        ),
        serialization_alias="CWE.6",
        title="Name of Alternate Coding System",
    )

    cwe_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_7",
            "coding_system_version_id",
            "CWE.7",
        ),
        serialization_alias="CWE.7",
        title="Coding System Version ID",
    )

    cwe_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_8",
            "alternate_coding_system_version_id",
            "CWE.8",
        ),
        serialization_alias="CWE.8",
        title="Alternate Coding System Version ID",
    )

    cwe_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_9",
            "original_text",
            "CWE.9",
        ),
        serialization_alias="CWE.9",
        title="Original Text",
    )

    cwe_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_10",
            "second_alternate_identifier",
            "CWE.10",
        ),
        serialization_alias="CWE.10",
        title="Second Alternate Identifier",
    )

    cwe_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_11",
            "second_alternate_text",
            "CWE.11",
        ),
        serialization_alias="CWE.11",
        title="Second Alternate Text",
    )

    cwe_12: Optional[str] = Field(
        default=None,
        max_length=12,
        validation_alias=AliasChoices(
            "cwe_12",
            "name_of_second_alternate_coding_system",
            "CWE.12",
        ),
        serialization_alias="CWE.12",
        title="Name of Second Alternate Coding System",
    )

    cwe_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_13",
            "second_alternate_coding_system_version_id",
            "CWE.13",
        ),
        serialization_alias="CWE.13",
        title="Second Alternate Coding System Version ID",
    )

    cwe_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_14",
            "coding_system_oid",
            "CWE.14",
        ),
        serialization_alias="CWE.14",
        title="Coding System OID",
    )

    cwe_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_15",
            "value_set_oid",
            "CWE.15",
        ),
        serialization_alias="CWE.15",
        title="Value Set OID",
    )

    cwe_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_16",
            "value_set_version_id",
            "CWE.16",
        ),
        serialization_alias="CWE.16",
        title="Value Set Version ID",
    )

    cwe_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_17",
            "alternate_coding_system_oid",
            "CWE.17",
        ),
        serialization_alias="CWE.17",
        title="Alternate Coding System OID",
    )

    cwe_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_18",
            "alternate_value_set_oid",
            "CWE.18",
        ),
        serialization_alias="CWE.18",
        title="Alternate Value Set OID",
    )

    cwe_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_19",
            "alternate_value_set_version_id",
            "CWE.19",
        ),
        serialization_alias="CWE.19",
        title="Alternate Value Set Version ID",
    )

    cwe_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_20",
            "second_alternate_coding_system_oid",
            "CWE.20",
        ),
        serialization_alias="CWE.20",
        title="Second Alternate Coding System OID",
    )

    cwe_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_21",
            "second_alternate_value_set_oid",
            "CWE.21",
        ),
        serialization_alias="CWE.21",
        title="Second Alternate Value Set OID",
    )

    cwe_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_22",
            "second_alternate_value_set_version_id",
            "CWE.22",
        ),
        serialization_alias="CWE.22",
        title="Second Alternate Value Set Version ID",
    )

    @field_validator("cwe_16", "cwe_19", "cwe_22", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
