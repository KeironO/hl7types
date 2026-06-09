"""Strict vs lenient ER7 decoding of ACK messages.

Strict mode (default / strict=True):
  - Complete messages decode correctly.
  - Missing required segments raise ValidationError.

Lenient mode (strict=False):
  - Complete messages decode correctly.
  - Missing required segments are replaced with empty placeholders; a
    UserWarning names the missing segment and references strict=False.

Both decode_er7() and ACK.model_validate_er7() expose the same contract,
with strict=True as the default for both.
"""
from __future__ import annotations

import pytest
from pydantic import ValidationError

from hl7types import decode_er7
from hl7types.hl7.v2_5_1.messages.ACK import ACK

ACK_WIRE = (
    r"MSH|^~\&|SEND|FAC|RECV|FAC|20240101120000||ACK|MSG001|P|2.5.1" + "\r"
    "MSA|AA|MSG001\r"
)

ACK_MISSING_MSA_WIRE = (
    r"MSH|^~\&|SEND|FAC|RECV|FAC|20240101120000||ACK|MSG001|P|2.5.1" + "\r"
)



@pytest.mark.parametrize("decode", [
    pytest.param(lambda w: decode_er7(w, msg_cls=ACK, strict=False),  id="decode_er7/lenient"),
    pytest.param(lambda w: decode_er7(w, msg_cls=ACK, strict=True),   id="decode_er7/strict"),
    pytest.param(lambda w: decode_er7(w, msg_cls=ACK),                id="decode_er7/default"),
    pytest.param(lambda w: ACK.model_validate_er7(w, strict=False),   id="model_validate_er7/lenient"),
    pytest.param(lambda w: ACK.model_validate_er7(w, strict=True),    id="model_validate_er7/strict"),
    pytest.param(lambda w: ACK.model_validate_er7(w),                 id="model_validate_er7/default"),
])
def test_complete_ack_decodes_correctly(decode) -> None:
    msg = decode(ACK_WIRE)
    assert isinstance(msg, ACK)
    assert msg.MSH.msh_3.hd_1 == "SEND"
    assert msg.MSH.msh_10 == "MSG001"
    assert msg.MSH.msh_12.vid_1 == "2.5.1"
    assert msg.MSA.msa_1 == "AA"
    assert msg.MSA.msa_2 == "MSG001"



@pytest.mark.parametrize("decode", [
    pytest.param(lambda w: decode_er7(w, msg_cls=ACK, strict=False),       id="decode_er7"),
    pytest.param(lambda w: ACK.model_validate_er7(w, strict=False),        id="model_validate_er7"),
])
def test_lenient_missing_msa_warns_and_injects_placeholder(decode) -> None:
    with pytest.warns(UserWarning, match=r"MSA.*strict=False"):
        msg = decode(ACK_MISSING_MSA_WIRE)

    # Segments present on the wire still decode correctly.
    assert msg.MSH.msh_3.hd_1 == "SEND"
    assert msg.MSH.msh_10 == "MSG001"

    # Missing MSA is injected as an empty placeholder: no fields were decoded
    # from the wire (model_fields_set is empty) and optional fields carry their
    # schema defaults rather than wire values.
    assert msg.MSA.model_fields_set == set()
    assert msg.MSA.msa_3 is None


@pytest.mark.parametrize("decode", [
    pytest.param(lambda w: decode_er7(w, msg_cls=ACK, strict=True),  id="decode_er7/explicit"),
    pytest.param(lambda w: decode_er7(w, msg_cls=ACK),               id="decode_er7/default"),
    pytest.param(lambda w: ACK.model_validate_er7(w, strict=True),   id="model_validate_er7/explicit"),
    pytest.param(lambda w: ACK.model_validate_er7(w),                id="model_validate_er7/default"),
])
def test_strict_missing_msa_raises_validation_error(decode) -> None:
    with pytest.raises(ValidationError, match=r"MSA"):
        decode(ACK_MISSING_MSA_WIRE)
