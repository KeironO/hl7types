"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CON
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XPN import XPN


class CON(HL7Model):
    """HL7 v2 CON segment.

    Attributes
    ----------
    con_1 : str
        CON.1 (req) - Set ID - CON (SI)

    con_2 : CWE | None
        CON.2 (opt) - Consent Type (CWE)

    con_3 : str | None
        CON.3 (opt) - Consent Form ID and Version (ST)

    con_4 : EI | None
        CON.4 (opt) - Consent Form Number (EI)

    con_5 : list[str] | None
        CON.5 (opt, rep) - Consent Text (FT)

    con_6 : list[str] | None
        CON.6 (opt, rep) - Subject-specific Consent Text (FT)

    con_7 : list[str] | None
        CON.7 (opt, rep) - Consent Background Information (FT)

    con_8 : list[str] | None
        CON.8 (opt, rep) - Subject-specific Consent Background Text (FT)

    con_9 : list[str] | None
        CON.9 (opt, rep) - Consenter-imposed limitations (FT)

    con_10 : CNE | None
        CON.10 (opt) - Consent Mode (CNE)

    con_11 : CNE
        CON.11 (req) - Consent Status (CNE)

    con_12 : str | None
        CON.12 (opt) - Consent Discussion Date/Time (DTM)

    con_13 : str | None
        CON.13 (opt) - Consent Decision Date/Time (DTM)

    con_14 : str | None
        CON.14 (opt) - Consent Effective Date/Time (DTM)

    con_15 : str | None
        CON.15 (opt) - Consent End Date/Time (DTM)

    con_16 : str | None
        CON.16 (opt) - Subject Competence Indicator (ID)

    con_17 : str | None
        CON.17 (opt) - Translator Assistance Indicator (ID)

    con_18 : CWE | None
        CON.18 (opt) - Language Translated To (CWE)

    con_19 : str | None
        CON.19 (opt) - Informational Material Supplied Indicator (ID)

    con_20 : CWE | None
        CON.20 (opt) - Consent Bypass Reason (CWE)

    con_21 : str | None
        CON.21 (opt) - Consent Disclosure Level (ID)

    con_22 : CWE | None
        CON.22 (opt) - Consent Non-disclosure Reason (CWE)

    con_23 : CWE | None
        CON.23 (opt) - Non-subject Consenter Reason (CWE)

    con_24 : list[XPN]
        CON.24 (req, rep) - Consenter ID (XPN)

    con_25 : list[CWE]
        CON.25 (req, rep) - Relationship to Subject (CWE)
    """

    con_1: str = Field(
        validation_alias=AliasChoices(
            "con_1",
            "set_id_con",
            "CON.1",
        ),
        serialization_alias="CON.1",
        title="Set ID - CON",
        description="Item #1776",
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
        description="Item #1777 | Table HL70496",
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
        description="Item #1778",
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
        description="Item #1779",
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
        description="Item #1780",
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
        description="Item #1781",
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
        description="Item #1782",
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
        description="Item #1783",
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
        description="Item #1784",
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
        description="Item #1785 | Table HL70497",
    )

    con_11: CNE = Field(
        validation_alias=AliasChoices(
            "con_11",
            "consent_status",
            "CON.11",
        ),
        serialization_alias="CON.11",
        title="Consent Status",
        description="Item #1786 | Table HL70498",
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
        description="Item #1787",
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
        description="Item #1788",
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
        description="Item #1789",
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
        description="Item #1790",
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
        description="Item #1791 | Table HL70136",
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
        description="Item #1792 | Table HL70136",
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
        description="Item #1793 | Table HL70296",
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
        description="Item #1794 | Table HL70136",
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
        description="Item #1795 | Table HL70499",
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
        description="Item #1796 | Table HL70500",
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
        description="Item #1797 | Table HL70501",
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
        description="Item #1798 | Table HL70502",
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
        description="Item #1909",
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
        description="Item #1898 | Table HL70548",
    )

    @field_validator("con_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("con_12", "con_13", "con_14", "con_15", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
