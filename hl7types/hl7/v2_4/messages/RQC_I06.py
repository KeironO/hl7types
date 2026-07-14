"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RQC_I06
Type: Message
"""
from __future__ import annotations

from .RQC_I05 import RQC_I05


class RQC_I06(RQC_I05):
    """RQC/RCL - Request/receipt of clinical data listing (S11.3.6).

    Attributes:
        MSH (MSH): Message Header, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
        PROVIDER (List[RQC_I05_PROVIDER]): required
        PID (PID): Patient identification, required
        NK1 (Optional[List[NK1]]): Next of kin / associated parties, optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    pass
