"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CON
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XPN import XPN

_RE_SI = re.compile(r'\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class CON(HL7Model):
    """Consent Segment (S9.7.1).

    Attributes
    ----------
    con_1 : str
        CON.1 - Set ID - CON (SI) R S9.7.1.1

    con_2 : CWE | None
        CON.2 - Consent Type (CWE) O S9.7.1.2 | 0496 - Consent Type

    con_3 : str | None
        CON.3 - Consent Form ID and Version (ST) O S9.7.1.3

    con_4 : EI | None
        CON.4 - Consent Form Number (EI) O S9.7.1.4

    con_5 : list[str] | None
        CON.5 - Consent Text (FT) O rep S9.7.1.5

    con_6 : list[str] | None
        CON.6 - Subject-specific Consent Text (FT) O rep S9.7.1.6

    con_7 : list[str] | None
        CON.7 - Consent Background Information (FT) O rep S9.7.1.7

    con_8 : list[str] | None
        CON.8 - Subject-specific Consent Background Text (FT) O rep S9.7.1.8

    con_9 : list[str] | None
        CON.9 - Consenter-imposed limitations (FT) O rep S9.7.1.9

    con_10 : CNE | None
        CON.10 - Consent Mode (CNE) O S9.7.1.10 | 0497 - Consent Mode

    con_11 : CNE
        CON.11 - Consent Status (CNE) R S9.7.1.11 | 0498 - Consent Status

    con_12 : str | None
        CON.12 - Consent Discussion Date/Time (DTM) O S9.7.1.12

    con_13 : str | None
        CON.13 - Consent Decision Date/Time (DTM) O S9.7.1.13

    con_14 : str | None
        CON.14 - Consent Effective Date/Time (DTM) O S9.7.1.14

    con_15 : str | None
        CON.15 - Consent End Date/Time (DTM) O S9.7.1.15

    con_16 : str | None
        CON.16 - Subject Competence Indicator (ID) O S9.7.1.16 | 0136 - Yes/no Indicator

    con_17 : str | None
        CON.17 - Translator Assistance Indicator (ID) O S9.7.1.17 | 0136 - Yes/no Indicator

    con_18 : CWE | None
        CON.18 - Language Translated To (CWE) O S9.7.1.18 | 0296 - Primary Language

    con_19 : str | None
        CON.19 - Informational Material Supplied Indicator (ID) O S9.7.1.19 | 0136 - Yes/no Indicator

    con_20 : CWE | None
        CON.20 - Consent Bypass Reason (CWE) O S9.7.1.20 | 0499 - Consent Bypass Reason

    con_21 : str | None
        CON.21 - Consent Disclosure Level (ID) O S9.7.1.21 | 0500 - Consent Disclosure Level

    con_22 : CWE | None
        CON.22 - Consent Non-disclosure Reason (CWE) O S9.7.1.22 | 0501 - Consent Non-Disclosure Reason

    con_23 : CWE | None
        CON.23 - Non-subject Consenter Reason (CWE) O S9.7.1.23 | 0502 - Non-Subject Consenter Reason

    con_24 : list[XPN]
        CON.24 - Consenter ID (XPN) R rep S9.7.1.24

    con_25 : list[CWE]
        CON.25 - Relationship to Subject (CWE) R rep S9.7.1.25 | 0548 - Signatory's Relationship to Subject
    """

    con_1: str = Field(
        validation_alias=AliasChoices(
            "con_1",
            "set_id_con",
            "CON.1",
        ),
        serialization_alias="CON.1",
        title="Set ID - CON",
        description="R | Item #01776 | LEN:4",
    )

    con_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_2",
            "consent_type",
            "CON.2",
        ),
        serialization_alias="CON.2",
        title="Consent Type",
        description="O | Item #01777 | Table 0496 - Consent Type",
    )

    con_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_3",
            "consent_form_id_and_version",
            "CON.3",
        ),
        serialization_alias="CON.3",
        title="Consent Form ID and Version",
        description="O | Item #01778",
    )

    con_4: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_4",
            "consent_form_number",
            "CON.4",
        ),
        serialization_alias="CON.4",
        title="Consent Form Number",
        description="O | Item #01779",
    )

    con_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_5",
            "consent_text",
            "CON.5",
        ),
        serialization_alias="CON.5",
        title="Consent Text",
        description="O | Item #01780",
    )

    con_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_6",
            "subject_specific_consent_text",
            "CON.6",
        ),
        serialization_alias="CON.6",
        title="Subject-specific Consent Text",
        description="O | Item #01781",
    )

    con_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_7",
            "consent_background_information",
            "CON.7",
        ),
        serialization_alias="CON.7",
        title="Consent Background Information",
        description="O | Item #01782",
    )

    con_8: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_8",
            "subject_specific_consent_background_text",
            "CON.8",
        ),
        serialization_alias="CON.8",
        title="Subject-specific Consent Background Text",
        description="O | Item #01783",
    )

    con_9: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_9",
            "consenter_imposed_limitations",
            "CON.9",
        ),
        serialization_alias="CON.9",
        title="Consenter-imposed limitations",
        description="O | Item #01784",
    )

    con_10: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_10",
            "consent_mode",
            "CON.10",
        ),
        serialization_alias="CON.10",
        title="Consent Mode",
        description="O | Item #01785 | Table 0497 - Consent Mode",
    )

    con_11: CNE = Field(
        validation_alias=AliasChoices(
            "con_11",
            "consent_status",
            "CON.11",
        ),
        serialization_alias="CON.11",
        title="Consent Status",
        description="R | Item #01786 | Table 0498 - Consent Status",
    )

    con_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_12",
            "consent_discussion_date_time",
            "CON.12",
        ),
        serialization_alias="CON.12",
        title="Consent Discussion Date/Time",
        description="O | Item #01787",
    )

    con_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_13",
            "consent_decision_date_time",
            "CON.13",
        ),
        serialization_alias="CON.13",
        title="Consent Decision Date/Time",
        description="O | Item #01788",
    )

    con_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_14",
            "consent_effective_date_time",
            "CON.14",
        ),
        serialization_alias="CON.14",
        title="Consent Effective Date/Time",
        description="O | Item #01789",
    )

    con_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_15",
            "consent_end_date_time",
            "CON.15",
        ),
        serialization_alias="CON.15",
        title="Consent End Date/Time",
        description="O | Item #01790",
    )

    con_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_16",
            "subject_competence_indicator",
            "CON.16",
        ),
        serialization_alias="CON.16",
        title="Subject Competence Indicator",
        description="O | Item #01791 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    con_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_17",
            "translator_assistance_indicator",
            "CON.17",
        ),
        serialization_alias="CON.17",
        title="Translator Assistance Indicator",
        description="O | Item #01792 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    con_18: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_18",
            "language_translated_to",
            "CON.18",
        ),
        serialization_alias="CON.18",
        title="Language Translated To",
        description="O | Item #01793 | Table 0296 - Primary Language",
    )

    con_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_19",
            "informational_material_supplied_indicator",
            "CON.19",
        ),
        serialization_alias="CON.19",
        title="Informational Material Supplied Indicator",
        description="O | Item #01794 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    con_20: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_20",
            "consent_bypass_reason",
            "CON.20",
        ),
        serialization_alias="CON.20",
        title="Consent Bypass Reason",
        description="O | Item #01795 | Table 0499 - Consent Bypass Reason",
    )

    con_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_21",
            "consent_disclosure_level",
            "CON.21",
        ),
        serialization_alias="CON.21",
        title="Consent Disclosure Level",
        description=(
            "O | Item #01796 | Table 0500 - Consent Disclosure Level | LEN:1"
        ),
    )

    con_22: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_22",
            "consent_non_disclosure_reason",
            "CON.22",
        ),
        serialization_alias="CON.22",
        title="Consent Non-disclosure Reason",
        description=(
            "O | Item #01797 | Table 0501 - Consent Non-Disclosure Reason"
        ),
    )

    con_23: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "con_23",
            "non_subject_consenter_reason",
            "CON.23",
        ),
        serialization_alias="CON.23",
        title="Non-subject Consenter Reason",
        description=(
            "O | Item #01798 | Table 0502 - Non-Subject Consenter Reason"
        ),
    )

    con_24: List[XPN] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "con_24",
            "consenter_id",
            "CON.24",
        ),
        serialization_alias="CON.24",
        title="Consenter ID",
        description="R | Item #01909",
    )

    con_25: List[CWE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "con_25",
            "relationship_to_subject",
            "CON.25",
        ),
        serialization_alias="CON.25",
        title="Relationship to Subject",
        description=(
            "R | Item #01898 | Table 0548 - Signatory's Relationship to Subject"
        ),
    )

    @field_validator("con_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("con_12", "con_13", "con_14", "con_15", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
