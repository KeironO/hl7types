"""Parse and validate an ORU^R01 lab result message."""

from pydantic import ValidationError

from hl7types import decode_er7, errs_from_exception
from hl7types.hl7.v2_5_1.messages import ORU_R01

# This is a valid ORU^R01 result message.
#
# ORU^R01 is commonly used for unsolicited observation results, such as
# laboratory results sent from a laboratory information system to another
# clinical system.
valid_wire = (
    "MSH|^~\\&|LABORDAI|YSBYTY CWMTAFF|HIS|YSBYTY CWMTAFF|20260301120000||ORU^R01^ORU_R01|MSG000002|P|2.5.1\r"
    "PID|1||CYM67890^^^YSBYTY CWMTAFF^MR||MORGAN^MYFANWY^^^MS||19881212|F\r"
    "OBR|1|ORD001|FIL001|FBC^Full Blood Count (Drat, Still Monday)^LOCAL|||20260301110000\r"
    "OBX|1|NM|WBC^White Blood Cells^LOCAL||7.5|10*9/L|4.0-11.0|N|||F\r"
    "OBX|2|NM|HGB^Haemoglobin^LOCAL||145|g/L|130-180|N|||F\r"
)


# This message is invalid.
#
# OBX.3 is the observation identifier. It says what the result represents,
# for example WBC or HGB. Here it is deliberately omitted.
invalid_wire = (
    "MSH|^~\\&|LABORDAI|YSBYTY CWMTAFF|HIS|YSBYTY CWMTAFF|20260301120000||ORU^R01^ORU_R01|MSG000003|P|2.5.1\r"
    "PID|1||CYM67890^^^YSBYTY CWMTAFF^MR||MORGAN^MYFANWY\r"
    "OBR|1|ORD002|FIL002|FBC^Full Blood Count (Drat, Still Monday)^LOCAL\r"
    "OBX|1|NM|||7.5|10*9/L\r"
)


print("Valid ORU^R01")

# Decode the valid ER7 message into a typed ORU_R01 model.
msg = decode_er7(valid_wire, msg_cls=ORU_R01)


# ORU_R01 messages are organised into nested groups.
#
# This example has one PATIENT_RESULT group containing:
# - one PATIENT group with the PID segment
# - one ORDER_OBSERVATION group with the OBR segment
# - two OBSERVATION groups, each containing one OBX segment
patient_result = msg.PATIENT_RESULT[0]
patient = patient_result.PATIENT
pid = patient.PID

print("Patient MRN:", pid.pid_3[0].cx_1)
print("Patient name:", pid.pid_5[0].xpn_1.fn_1 + ",", pid.pid_5[0].xpn_2)


# The ORDER_OBSERVATION group contains the OBR panel header.
order_observation = patient_result.ORDER_OBSERVATION[0]
obr = order_observation.OBR

print("Panel:", obr.obr_4.ce_2, "(" + obr.obr_4.ce_1 + ")")


# Each OBSERVATION group contains an OBX result.
for observation in order_observation.OBSERVATION:
    obx = observation.OBX

    test_name = obx.obx_3.ce_2
    result_value = obx.obx_5[0] if obx.obx_5 else None
    units = obx.obx_6.ce_1 if obx.obx_6 else None
    reference_range = obx.obx_7
    abnormal_flag = obx.obx_8[0] if obx.obx_8 else "N"

    print("Test:", test_name)
    print("Result:", result_value)
    print("Units:", units)
    print("Reference range:", reference_range)
    print("Abnormal flag:", abnormal_flag)


print("\nInvalid ORU^R01")

# Strict decoding is the default.
#
# Because OBX.3 is required, the invalid message raises a ValidationError.
try:
    decode_er7(invalid_wire, msg_cls=ORU_R01)
except ValidationError as exc:
    print("Validation failed as expected")
    print("Number of errors:", exc.error_count())

    for error in exc.errors():
        location = " > ".join(str(part) for part in error["loc"])
        print(location + ":", error["msg"])

    # Convert the ValidationError into HL7 ERR segments.
    #
    # These ERR segments can be included in a negative ACK so the sending
    # system can see why the message was rejected.
    err_segments = errs_from_exception(exc, "2.5.1")

    print("\nERR segments for negative ACK:")
    for err_segment in err_segments:
        print(err_segment.model_dump_er7())
