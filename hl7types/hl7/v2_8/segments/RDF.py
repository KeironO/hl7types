"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RDF
Type: Segment
"""
from __future__ import annotations

from typing import List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.RCD import RCD


class RDF(HL7Model):
    """HL7 v2 RDF segment.

    Attributes
    ----------
    rdf_1 : str
        RDF.1 (req) - Number of Columns per Row (NM)

    rdf_2 : list[RCD]
        RDF.2 (req, rep) - Column Description (RCD)
    """

    rdf_1: str = Field(
        validation_alias=AliasChoices(
            "rdf_1",
            "number_of_columns_per_row",
            "RDF.1",
        ),
        serialization_alias="RDF.1",
        title="Number of Columns per Row",
        description="Item #701",
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
        description="Item #702 | Table HL70440",
    )

    @field_validator("rdf_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
