"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RDF
Type: Segment
"""
from __future__ import annotations

import re

from typing import List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.RCD import RCD

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class RDF(HL7Model):
    """Table Row Definition (S5.5.7).

    Attributes
    ----------
    rdf_1 : str
        RDF.1 - Number of Columns per Row (NM) R S5.5.7.1

    rdf_2 : list[RCD]
        RDF.2 - Column Description (RCD) R rep S5.5.7.2 | 0440 - Data Types
    """

    rdf_1: str = Field(
        validation_alias=AliasChoices(
            "rdf_1",
            "number_of_columns_per_row",
            "RDF.1",
        ),
        serialization_alias="RDF.1",
        title="Number of Columns per Row",
        description="R | Item #00701",
    )

    rdf_2: List[RCD] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "rdf_2",
            "column_description",
            "RDF.2",
        ),
        serialization_alias="RDF.2",
        title="Column Description",
        description="R | Item #00702 | Table 0440 - Data Types",
    )

    @field_validator("rdf_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
