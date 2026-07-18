"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CER
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.ED import ED
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON

_RE_SI = re.compile(r'\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class CER(HL7Model):
    """Certificate Detail (S15.4.2).

    Attributes
    ----------
    cer_1 : str
        CER.1 - Set ID - CER (SI) R S15.4.2.1

    cer_2 : str | None
        CER.2 - Serial Number (ST) O S15.4.2.2

    cer_3 : str | None
        CER.3 - Version (ST) O S15.4.2.3

    cer_4 : XON | None
        CER.4 - Granting Authority (XON) O S15.4.2.4

    cer_5 : XCN | None
        CER.5 - Issuing Authority (XCN) O S15.4.2.5

    cer_6 : ED | None
        CER.6 - Signature (ED) O S15.4.2.6

    cer_7 : str | None
        CER.7 - Granting Country (ID) O S15.4.2.7 | 0399 - Country Code

    cer_8 : CWE | None
        CER.8 - Granting State/Province (CWE) O S15.4.2.8 | 0347 - State/Province

    cer_9 : CWE | None
        CER.9 - Granting County/Parish (CWE) O S15.4.2.9 | 0289 - County/Parish

    cer_10 : CWE | None
        CER.10 - Certificate Type (CWE) O S15.4.2.10

    cer_11 : CWE | None
        CER.11 - Certificate Domain (CWE) O S15.4.2.11

    cer_12 : EI | None
        CER.12 - Subject ID (EI) C S15.4.2.12

    cer_13 : str
        CER.13 - Subject Name (ST) R S15.4.2.13

    cer_14 : list[CWE] | None
        CER.14 - Subject Directory Attribute Extension (CWE) O rep S15.4.2.14

    cer_15 : CWE | None
        CER.15 - Subject Public Key Info (CWE) O S15.4.2.15

    cer_16 : CWE | None
        CER.16 - Authority Key Identifier (CWE) O S15.4.2.16

    cer_17 : str | None
        CER.17 - Basic Constraint (ID) O S15.4.2.17 | 0136 - Yes/no Indicator

    cer_18 : list[CWE] | None
        CER.18 - CRL Distribution Point (CWE) O rep S15.4.2.18

    cer_19 : str | None
        CER.19 - Jurisdiction Country (ID) O S15.4.2.19 | 0399 - Country Code

    cer_20 : CWE | None
        CER.20 - Jurisdiction State/Province (CWE) O S15.4.2.20 | 0347 - State/Province

    cer_21 : CWE | None
        CER.21 - Jurisdiction County/Parish (CWE) O S15.4.2.21 | 0289 - County/Parish

    cer_22 : list[CWE] | None
        CER.22 - Jurisdiction Breadth (CWE) O rep S15.4.2.22 | 0547 - Jurisdictional Breadth

    cer_23 : str | None
        CER.23 - Granting Date (DTM) O S15.4.2.23

    cer_24 : str | None
        CER.24 - Issuing Date (DTM) O S15.4.2.24

    cer_25 : str | None
        CER.25 - Activation Date (DTM) O S15.4.2.25

    cer_26 : str | None
        CER.26 - Inactivation Date (DTM) O S15.4.2.26

    cer_27 : str | None
        CER.27 - Expiration Date (DTM) O S15.4.2.27

    cer_28 : str | None
        CER.28 - Renewal Date (DTM) O S15.4.2.28

    cer_29 : str | None
        CER.29 - Revocation Date (DTM) O S15.4.2.29

    cer_30 : CWE | None
        CER.30 - Revocation Reason Code (CWE) O S15.4.2.30

    cer_31 : CWE | None
        CER.31 - Certificate Status Code (CWE) O S15.4.2.31 | 0536 - Certificate Status
    """

    cer_1: str = Field(
        validation_alias=AliasChoices(
            "cer_1",
            "set_id_cer",
            "CER.1",
        ),
        serialization_alias="CER.1",
        title="Set ID - CER",
        description="R | Item #01856 | LEN:4",
    )

    cer_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_2",
            "serial_number",
            "CER.2",
        ),
        serialization_alias="CER.2",
        title="Serial Number",
        description="O | Item #01857",
    )

    cer_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_3",
            "version",
            "CER.3",
        ),
        serialization_alias="CER.3",
        title="Version",
        description="O | Item #01858",
    )

    cer_4: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_4",
            "granting_authority",
            "CER.4",
        ),
        serialization_alias="CER.4",
        title="Granting Authority",
        description="O | Item #01859",
    )

    cer_5: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_5",
            "issuing_authority",
            "CER.5",
        ),
        serialization_alias="CER.5",
        title="Issuing Authority",
        description="O | Item #01860",
    )

    cer_6: Optional[ED] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_6",
            "signature",
            "CER.6",
        ),
        serialization_alias="CER.6",
        title="Signature",
        description="O | Item #01861",
    )

    cer_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_7",
            "granting_country",
            "CER.7",
        ),
        serialization_alias="CER.7",
        title="Granting Country",
        description="O | Item #01862 | Table 0399 - Country Code | LEN:3",
    )

    cer_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_8",
            "granting_state_province",
            "CER.8",
        ),
        serialization_alias="CER.8",
        title="Granting State/Province",
        description="O | Item #01863 | Table 0347 - State/Province",
    )

    cer_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_9",
            "granting_county_parish",
            "CER.9",
        ),
        serialization_alias="CER.9",
        title="Granting County/Parish",
        description="O | Item #01864 | Table 0289 - County/Parish",
    )

    cer_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_10",
            "certificate_type",
            "CER.10",
        ),
        serialization_alias="CER.10",
        title="Certificate Type",
        description="O | Item #01865",
    )

    cer_11: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_11",
            "certificate_domain",
            "CER.11",
        ),
        serialization_alias="CER.11",
        title="Certificate Domain",
        description="O | Item #01866",
    )

    cer_12: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_12",
            "subject_id",
            "CER.12",
        ),
        serialization_alias="CER.12",
        title="Subject ID",
        description="C | Item #01867",
    )

    cer_13: str = Field(
        validation_alias=AliasChoices(
            "cer_13",
            "subject_name",
            "CER.13",
        ),
        serialization_alias="CER.13",
        title="Subject Name",
        description="R | Item #01907",
    )

    cer_14: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_14",
            "subject_directory_attribute_extension",
            "CER.14",
        ),
        serialization_alias="CER.14",
        title="Subject Directory Attribute Extension",
        description="O | Item #01868",
    )

    cer_15: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_15",
            "subject_public_key_info",
            "CER.15",
        ),
        serialization_alias="CER.15",
        title="Subject Public Key Info",
        description="O | Item #01869",
    )

    cer_16: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_16",
            "authority_key_identifier",
            "CER.16",
        ),
        serialization_alias="CER.16",
        title="Authority Key Identifier",
        description="O | Item #01870",
    )

    cer_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_17",
            "basic_constraint",
            "CER.17",
        ),
        serialization_alias="CER.17",
        title="Basic Constraint",
        description="O | Item #01871 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    cer_18: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_18",
            "crl_distribution_point",
            "CER.18",
        ),
        serialization_alias="CER.18",
        title="CRL Distribution Point",
        description="O | Item #01872",
    )

    cer_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_19",
            "jurisdiction_country",
            "CER.19",
        ),
        serialization_alias="CER.19",
        title="Jurisdiction Country",
        description="O | Item #01875 | Table 0399 - Country Code | LEN:3",
    )

    cer_20: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_20",
            "jurisdiction_state_province",
            "CER.20",
        ),
        serialization_alias="CER.20",
        title="Jurisdiction State/Province",
        description="O | Item #01873 | Table 0347 - State/Province",
    )

    cer_21: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_21",
            "jurisdiction_county_parish",
            "CER.21",
        ),
        serialization_alias="CER.21",
        title="Jurisdiction County/Parish",
        description="O | Item #01874 | Table 0289 - County/Parish",
    )

    cer_22: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_22",
            "jurisdiction_breadth",
            "CER.22",
        ),
        serialization_alias="CER.22",
        title="Jurisdiction Breadth",
        description="O | Item #01895 | Table 0547 - Jurisdictional Breadth",
    )

    cer_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_23",
            "granting_date",
            "CER.23",
        ),
        serialization_alias="CER.23",
        title="Granting Date",
        description="O | Item #01876",
    )

    cer_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_24",
            "issuing_date",
            "CER.24",
        ),
        serialization_alias="CER.24",
        title="Issuing Date",
        description="O | Item #01877",
    )

    cer_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_25",
            "activation_date",
            "CER.25",
        ),
        serialization_alias="CER.25",
        title="Activation Date",
        description="O | Item #01878",
    )

    cer_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_26",
            "inactivation_date",
            "CER.26",
        ),
        serialization_alias="CER.26",
        title="Inactivation Date",
        description="O | Item #01879",
    )

    cer_27: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_27",
            "expiration_date",
            "CER.27",
        ),
        serialization_alias="CER.27",
        title="Expiration Date",
        description="O | Item #01880",
    )

    cer_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_28",
            "renewal_date",
            "CER.28",
        ),
        serialization_alias="CER.28",
        title="Renewal Date",
        description="O | Item #01881",
    )

    cer_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_29",
            "revocation_date",
            "CER.29",
        ),
        serialization_alias="CER.29",
        title="Revocation Date",
        description="O | Item #01882",
    )

    cer_30: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_30",
            "revocation_reason_code",
            "CER.30",
        ),
        serialization_alias="CER.30",
        title="Revocation Reason Code",
        description="O | Item #01883",
    )

    cer_31: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cer_31",
            "certificate_status_code",
            "CER.31",
        ),
        serialization_alias="CER.31",
        title="Certificate Status Code",
        description="O | Item #01884 | Table 0536 - Certificate Status",
    )

    @field_validator("cer_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("cer_23", "cer_24", "cer_25", "cer_26", "cer_27", "cer_28", "cer_29", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
