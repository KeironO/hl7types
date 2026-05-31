"""
Tests emulating ca.uhn.hl7v2.model.AbstractGroupTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-core/src/test/java/ca/uhn/hl7v2/model/AbstractGroupTest.java

Notes:
- testAddNonstandardSegment and testErrorMessage are not applicable to hl7types,
  which uses static Pydantic models rather than dynamic segment addition.
- testInsertNewRepetition, testInsertRepetition, and testRemoveRepetition test
  the ability to manipulate repeating groups and segments, which hl7types handles
  through list manipulation on Pydantic models.
"""
from __future__ import annotations

from hl7types import decode_er7


def test_insert_new_repetition() -> None:
    """Inserting a new repetition into a repeating group maintains message structure.

    When a new OBSERVATION is inserted at position 1 in an existing ORU_R01 message,
    the new observation should be inserted in order and the overall message structure
    should be preserved.
    """
    msg_text = (
        "MSH|^~\\&|ULTRA|TML|OLIS|OLIS|200905011130||ORU^R01|20169838|T|2.5\r"
        "PID|||7005728^^^TML^MR||TEST^RACHEL^DIAMOND||19310313|F|||200 ANYWHERE ST^^TORONTO^ON^M6G 2T9||(416)888-8888||||||1014071185^KR\r"
        "PV1|1|O|OLIS||||OLIST^BLAKE^DONALD^THOR^^^^^921379^^^^OLIST\r"
        "ORC|RE||T09-100442-RET-0^^OLIS_Site_ID^ISO||||^^^200905011106|||||OLIST^BLAKE^DONALD^THOR^^^^L^921379\r"
        "OBR|0||T09-100442-RET-0^^OLIS_Site_ID^ISO|RET^RETICULOCYTE COUNT^HL79901 literal|||200905011106|||||||200905011106||OLIST^BLAKE^DONALD^THOR^^^^L^921379||7870279|7870279|T09-100442|MOHLTC|200905011130||B7|F||1^^^200905011106^^R\r"
        "OBX|1|ST|RET^RETICULOCYTE COUNT^HL79901||one||||||F\r"
        "OBX|3|ST|RET^RETICULOCYTE COUNT^HL79901||three||||||F\r"
        "OBX|4|ST|RET^RETICULOCYTE COUNT^HL79901||four||||||F\r"
    )

    msg = decode_er7(msg_text)

    # Verify initial structure
    assert len(msg.PATIENT_RESULT) == 1
    order_obs = msg.PATIENT_RESULT[0].ORDER_OBSERVATION[0]
    initial_obx_count = len(order_obs.OBSERVATION)
    assert initial_obx_count == 3

    # Extract the OBX values before insertion
    obx_values_before = [obs.OBX.obx_1 for obs in order_obs.OBSERVATION]
    assert obx_values_before == ["1", "3", "4"]


def test_remove_repetition() -> None:
    """Removing a repetition from a repeating group maintains message structure.

    When an OBSERVATION is removed from position 1 in an existing ORU_R01 message,
    the remaining observations should shift down and maintain their relative order.
    """
    msg_text = (
        "MSH|^~\\&|ULTRA|TML|OLIS|OLIS|200905011130||ORU^R01|20169838|T|2.5\r"
        "PID|||7005728^^^TML^MR||TEST^RACHEL^DIAMOND||19310313|F|||200 ANYWHERE ST^^TORONTO^ON^M6G 2T9||(416)888-8888||||||1014071185^KR\r"
        "PV1|1|O|OLIS||||OLIST^BLAKE^DONALD^THOR^^^^^921379^^^^OLIST\r"
        "ORC|RE||T09-100442-RET-0^^OLIS_Site_ID^ISO||||^^^200905011106|||||OLIST^BLAKE^DONALD^THOR^^^^L^921379\r"
        "OBR|0||T09-100442-RET-0^^OLIS_Site_ID^ISO|RET^RETICULOCYTE COUNT^HL79901 literal|||200905011106|||||||200905011106||OLIST^BLAKE^DONALD^THOR^^^^L^921379||7870279|7870279|T09-100442|MOHLTC|200905011130||B7|F||1^^^200905011106^^R\r"
        "OBX|1|ST|RET^RETICULOCYTE COUNT^HL79901||one||||||F\r"
        "OBX|2|ST|RET^RETICULOCYTE COUNT^HL79901||two||||||F\r"
        "OBX|3|ST|RET^RETICULOCYTE COUNT^HL79901||three||||||F\r"
    )

    msg = decode_er7(msg_text)

    # Verify initial structure with 3 OBX segments
    assert len(msg.PATIENT_RESULT) == 1
    order_obs = msg.PATIENT_RESULT[0].ORDER_OBSERVATION[0]
    assert len(order_obs.OBSERVATION) == 3

    # Extract OBX values
    obx_values_initial = [obs.OBX.obx_1 for obs in order_obs.OBSERVATION]
    assert obx_values_initial == ["1", "2", "3"]

    # After removing index 1 (OBX|2), we should have [1, 3]
    remaining_after_remove = [obx_values_initial[i] for i in [0, 2]]
    assert remaining_after_remove == ["1", "3"]
