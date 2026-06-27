"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CER
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.ED import ED
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON


class CER(HL7Model):
    """HL7 v2 CER segment.

    Attributes
    ----------
    cer_1 : str
        CER.1 (req) - Set ID - CER (SI)

    cer_2 : str | None
        CER.2 (opt) - Serial Number (ST)

    cer_3 : str | None
        CER.3 (opt) - Version (ST)

    cer_4 : XON | None
        CER.4 (opt) - Granting Authority (XON)

    cer_5 : XCN | None
        CER.5 (opt) - Issuing Authority (XCN)

    cer_6 : ED | None
        CER.6 (opt) - Signature (ED)

    cer_7 : str | None
        CER.7 (opt) - Granting Country (ID)

    cer_8 : CWE | None
        CER.8 (opt) - Granting State/Province (CWE)

    cer_9 : CWE | None
        CER.9 (opt) - Granting County/Parish (CWE)

    cer_10 : CWE | None
        CER.10 (opt) - Certificate Type (CWE)

    cer_11 : CWE | None
        CER.11 (opt) - Certificate Domain (CWE)

    cer_12 : EI | None
        CER.12 (opt) - Subject ID (EI)

    cer_13 : str
        CER.13 (req) - Subject Name (ST)

    cer_14 : list[CWE] | None
        CER.14 (opt, rep) - Subject Directory Attribute Extension (CWE)

    cer_15 : CWE | None
        CER.15 (opt) - Subject Public Key Info (CWE)

    cer_16 : CWE | None
        CER.16 (opt) - Authority Key Identifier (CWE)

    cer_17 : str | None
        CER.17 (opt) - Basic Constraint (ID)

    cer_18 : list[CWE] | None
        CER.18 (opt, rep) - CRL Distribution Point (CWE)

    cer_19 : str | None
        CER.19 (opt) - Jurisdiction Country (ID)

    cer_20 : CWE | None
        CER.20 (opt) - Jurisdiction State/Province (CWE)

    cer_21 : CWE | None
        CER.21 (opt) - Jurisdiction County/Parish (CWE)

    cer_22 : list[CWE] | None
        CER.22 (opt, rep) - Jurisdiction Breadth (CWE)

    cer_23 : str | None
        CER.23 (opt) - Granting Date (DTM)

    cer_24 : str | None
        CER.24 (opt) - Issuing Date (DTM)

    cer_25 : str | None
        CER.25 (opt) - Activation Date (DTM)

    cer_26 : str | None
        CER.26 (opt) - Inactivation Date (DTM)

    cer_27 : str | None
        CER.27 (opt) - Expiration Date (DTM)

    cer_28 : str | None
        CER.28 (opt) - Renewal Date (DTM)

    cer_29 : str | None
        CER.29 (opt) - Revocation Date (DTM)

    cer_30 : CWE | None
        CER.30 (opt) - Revocation Reason Code (CWE)

    cer_31 : CWE | None
        CER.31 (opt) - Certificate Status Code (CWE)
    """

    cer_1: str = Field(
        validation_alias=AliasChoices(
            "cer_1",
            "set_id_cer",
            "CER.1",
        ),
        serialization_alias="CER.1",
        title="Set ID - CER",
        description="Item #1856",
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
        description="Item #1857",
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
        description="Item #1858",
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
        description="Item #1859",
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
        description="Item #1860",
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
        description="Item #1861",
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
        description="Item #1862 | Table HL70399",
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
        description="Item #1863 | Table HL70347",
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
        description="Item #1864 | Table HL70289",
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
        description="Item #1865",
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
        description="Item #1866",
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
        description="Item #1867",
    )

    cer_13: str = Field(
        validation_alias=AliasChoices(
            "cer_13",
            "subject_name",
            "CER.13",
        ),
        serialization_alias="CER.13",
        title="Subject Name",
        description="Item #1907",
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
        description="Item #1868",
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
        description="Item #1869",
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
        description="Item #1870",
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
        description="Item #1871 | Table HL70136",
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
        description="Item #1872",
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
        description="Item #1875 | Table HL70399",
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
        description="Item #1873 | Table HL70347",
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
        description="Item #1874 | Table HL70289",
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
        description="Item #1895 | Table HL70547",
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
        description="Item #1876",
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
        description="Item #1877",
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
        description="Item #1878",
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
        description="Item #1879",
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
        description="Item #1880",
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
        description="Item #1881",
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
        description="Item #1882",
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
        description="Item #1883",
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
        description="Item #1884 | Table HL70536",
    )

    @field_validator("cer_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("cer_23", "cer_24", "cer_25", "cer_26", "cer_27", "cer_28", "cer_29", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
