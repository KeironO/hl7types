"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ORF_R04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSA import MSA
from ..segments.MSH import MSH

from ..groups.ORF_R04_ORDER import ORF_R04_ORDER
from ..groups.ORF_R04_QUERY_RESPONSE import ORF_R04_QUERY_RESPONSE

_DSC = DSC
_MSA = MSA
_MSH = MSH
_ORF_R04_ORDER = ORF_R04_ORDER
_ORF_R04_QUERY_RESPONSE = ORF_R04_QUERY_RESPONSE


class ORF_R04(HL7Model):
    """HL7 v2 ORF_R04 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        MSA (MSA): MESSAGE ACKNOWLEDGMENT, required
        QUERY_RESPONSE (List[ORF_R04_QUERY_RESPONSE]): required
        ORDER (List[ORF_R04_ORDER]): required
        DSC (Optional[DSC]): CONTINUATION POINTER, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MESSAGE ACKNOWLEDGMENT",
    )

    QUERY_RESPONSE: List[_ORF_R04_QUERY_RESPONSE] = Field(
        min_length=1,
        title="QUERY_RESPONSE",
    )

    ORDER: List[_ORF_R04_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="CONTINUATION POINTER",
    )

    model_config = ConfigDict(populate_by_name=True)
