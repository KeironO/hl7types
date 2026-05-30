# hl7types

[![Documentation](https://readthedocs.org/projects/hl7types/badge/?version=latest)](https://hl7types.readthedocs.io)

HL7 v2 (Health Level Seven Version 2) is the most widely deployed healthcare messaging standard in the world, used to exchange clinical and administrative data between hospital systems, laboratories, pharmacies, and other healthcare applications. It defines a pipe-delimited wire format (ER7) for encoding messages such as patient admissions, lab results, and order requests, and is the backbone of interoperability in the majority of existing healthcare infrastructure globally.

`hl7types` provides typed, Pydantic-powered Python models for HL7 v2 messages, segments, and datatypes, with built-in ER7 and XML serialisation. Models are generated directly from the HL7 specification, giving you full type safety, IDE autocompletion, and validation out of the box.

With thanks to the [fhir.resources](https://github.com/nazrulworld/fhir.resources) project for demonstrating what modern, Pydantic-powered healthcare data tooling can look like.

All HL7 v2 model classes are generated using [hl7-parser](https://github.com/KeironO/hl7-parser).

HL7® is a registered trademark owned by [Health Level Seven International](https://www.hl7.org/legal/trademarks.cfm).


## Version info

Each HL7 version is available as a sub-package under `hl7types.hl7.<version>`, where the version string uses underscores in place of dots , so v2.5.1 is at `hl7types.hl7.v2_5_1` and v2.1 is at `hl7types.hl7.v2_1`.

**Available versions:**

- v2.1 (`hl7types.hl7.v2_1`)
- v2.2 (`hl7types.hl7.v2_2`)
- v2.3 (`hl7types.hl7.v2_3`)
- v2.3.1 (`hl7types.hl7.v2_3_1`)
- v2.4 (`hl7types.hl7.v2_4`)
- v2.5 (`hl7types.hl7.v2_5`)
- v2.5.1 (`hl7types.hl7.v2_5_1`)
- v2.6 (`hl7types.hl7.v2_6`)
- v2.7 (`hl7types.hl7.v2_7`)
- v2.7.1 (`hl7types.hl7.v2_7_1`)
- v2.8 (`hl7types.hl7.v2_8`)
- v2.8.1 (`hl7types.hl7.v2_8_1`)
- v2.8.2 (`hl7types.hl7.v2_8_2`)

## Installation

```bash
pip install hl7types
```

## Usage

**Example 1:** Construct an ADT^A01 message from typed models and access fields directly:

```python
>>> from hl7types.hl7.v2_5_1.datatypes import CE, CX, FN, HD, MSG, PT, SAD, TS, VID, XAD, XPN, XTN
>>> from hl7types.hl7.v2_5_1.messages import ADT_A01
>>> from hl7types.hl7.v2_5_1.segments import EVN, MSH, PID, PV1
>>> msh = MSH(
...     msh_3=HD(hd_1="HL7TYPES"),
...     msh_4=HD(hd_1="YSBYTY PONTYPANDY"),
...     msh_5=HD(hd_1="WPAS"),
...     msh_6=HD(hd_1="YSBYTY CWM YSWYTH"),
...     msh_7=TS(ts_1="20240101090000"),
...     msh_9=MSG(msg_1="ADT", msg_2="A01"),
...     msh_10="MSG000001",
...     msh_11=PT(pt_1="P"),
...     msh_12=VID(vid_1="2.5.1"),
...     msh_17="CYM",
... )
>>> evn = EVN(evn_2=TS(ts_1="20260101000000"), evn_3=TS(ts_1="20240101090000"))
>>> pid = PID(
...     pid_3=[CX(cx_1="M12345", cx_4=HD(hd_1="WPAS"), cx_5="PI")],
...     pid_5=[XPN(xpn_1=FN(fn_1="Jones"), xpn_2="Brynn", xpn_5="Mr")],
...     pid_7=TS(ts_1="19930707"),
...     pid_8="M",
...     pid_11=[XAD(xad_1=SAD(sad_1="18 Stryd Mill"), xad_3="Pontypandy", xad_5="CF41 7ZQ", xad_6="CYM", xad_7="H")],
...     pid_13=[XTN(xtn_1="0118 999 881 999 119 725 3", xtn_2="PRN", xtn_3="PH")],
...     pid_15=CE(ce_1="cy", ce_2="Cymraeg"),
... )
>>> msg = ADT_A01(MSH=msh, EVN=evn, PID=pid, PV1=PV1(pv1_2="I"))
>>> isinstance(msg.PID.pid_5[0], XPN)
True
>>> msg.PID.pid_5[0].xpn_1.fn_1
'Jones'
>>> msg.PID.pid_8
'M'
```

---

**Example 2:** Encode to ER7 (pipe-delimited):

```python
>>> er7 = msg.model_dump_er7()
>>> for segment in er7.split("\r"):
...     print(segment)
MSH|^~\&|HL7TYPES|YSBYTY PONTYPANDY|WPAS|YSBYTY CWM YSWYTH|20240101090000||ADT^A01|MSG000001|P|2.5.1|||||CYM
EVN||20260101000000|20240101090000
PID|||M12345^^^WPAS^PI||Jones^Brynn^^^Mr||19930707|M|||18 Stryd Mill^^Pontypandy^Rhondda Cynon Taf^CF41 7ZQ^CYM^H||0118 999 881 999 119 725 3^PRN^PH||cy^Cymraeg
PV1||I
```

---

**Example 3:** Decode an ER7 string back into typed models:

```python
>>> decoded = ADT_A01.model_validate_er7(er7)
>>> isinstance(decoded.PID.pid_5[0], XPN)
True
>>> decoded.PID.pid_5[0].xpn_1.fn_1
'Jones'
>>> decoded.PID.pid_8
'M'
```

---

**Example 4:** Standard Pydantic serialisation is available on all models:

```python
>>> import json
>>> data = json.loads(msg.PID.model_dump_json())
>>> data["PID.8"]
'M'
```

---

**Example 5:** Type validation is enforced , passing the wrong type raises a `ValidationError`:

```python
>>> from pydantic import ValidationError
>>> try:
...     PID(pid_3="not-a-list")
... except ValidationError as e:
...     print(e)
2 validation errors for PID
pid_3
  Input should be a valid list [type=list_type, input_value='not-a-list', input_type=str]
    For further information visit https://errors.pydantic.dev/2.13/v/list_type
pid_5
  Field required [type=missing, input_value={'pid_3': 'not-a-list'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/missing
```

---

**Example 6:** Fields accept human-readable aliases as well as the positional names , all three forms are equivalent:

```python
>>> from hl7types.hl7.v2_5_1.segments import MSH
>>> from hl7types.hl7.v2_5_1.datatypes import HD
>>> # these are all the same field
>>> MSH(msh_3=HD(hd_1="HL7TYPES")).msh_3.hd_1
'HL7TYPES'
>>> MSH(sending_application=HD(hd_1="HL7TYPES")).msh_3.hd_1
'HL7TYPES'
>>> MSH(**{"MSH.3": HD(hd_1="HL7TYPES")}).msh_3.hd_1
'HL7TYPES'
```

---

**Example 7:** By default, decoding is lenient. Required segments absent from the wire produce an empty placeholder rather than raising an error. Pass `strict=True` to enforce the spec instead:

```python
>>> from hl7types import decode_er7
>>> from hl7types.hl7.v2_5_1.messages import ACK
>>> from pydantic import ValidationError
>>>
>>> # ACK wire with MSA omitted
>>> wire = "MSH|^~\\&|SEND|FAC|RECV|FAC|20240101120000||ACK|MSG001|P|2.5.1\r"
>>>
>>> # Lenient (default): succeeds, msg.MSA is an empty placeholder
>>> msg = decode_er7(wire, msg_cls=ACK)
>>> msg.MSA.model_fields_set
set()
>>>
>>> # Strict: raises if a required segment is missing
>>> try:
...     decode_er7(wire, msg_cls=ACK, strict=True)
... except ValidationError as e:
...     print(e)
1 validation error for ACK
MSA
  Field required [type=missing, ...]
```

`strict=True` is also accepted by `model_validate_er7`:

```python
>>> ACK.model_validate_er7(wire, strict=True)  # raises ValidationError
```

---

**Example 8:** Encode to XML:

```python
>>> print(msg.model_dump_xml())
```

```xml
<?xml version="1.0" encoding="UTF-8"?><ADT_A01 xmlns="urn:hl7-org:v2xml">
    <MSH>
        <MSH.1>|</MSH.1>
        <MSH.2>^~\&amp;</MSH.2>
        <MSH.3>
            ...
```

## Custom segments and the registry

Real-world HL7 deployments frequently extend the standard with vendor-specific Z-segments (e.g. `ZWCC`, `ZPID`). The `HL7Registry` lets you register custom segment and message models so they are recognised during encoding and decoding without touching the generated code.

**Example 9:** Define a custom Z-segment and encode a message that includes it:

```python
>>> from typing import Optional
>>> from pydantic import Field
>>> from hl7types import HL7Registry
>>> from hl7types.hl7 import HL7Model
>>> from hl7types.hl7.v2_5_1.segments import MSA, MSH
>>> from hl7types.hl7.v2_5_1.datatypes import HD, MSG, PT, TS, VID
>>>
>>> class ZWCC(HL7Model):
...     zwcc_1: Optional[str] = Field(None, serialization_alias="ZWCC.1")
...     zwcc_2: Optional[str] = Field(None, serialization_alias="ZWCC.2")
...
>>> _ZWCC = ZWCC
>>>
>>> class WCCACKMessage(HL7Model):
...     MSH: MSH
...     MSA: MSA
...     ZWCC: Optional[_ZWCC] = None
...
>>> msh = MSH(
...     msh_3=HD(hd_1="WPAS"), msh_5=HD(hd_1="SEND"),
...     msh_7=TS(ts_1="20260101120000"), msh_9=MSG(msg_1="ACK"),
...     msh_10="MSG000002", msh_11=PT(pt_1="P"), msh_12=VID(vid_1="2.5.1"),
... )
>>> msg = WCCACKMessage(MSH=msh, MSA=MSA(msa_1="AA", msa_2="MSG000001"), ZWCC=ZWCC(zwcc_1="WPAS", zwcc_2="20260101120000"))
>>> for segment in msg.model_dump_er7().split("\r"):
...     print(segment)
MSH|^~\&|WPAS||SEND||20260101120000||ACK|MSG000002|P|2.5.1
MSA|AA|MSG000001
ZWCC|WPAS|20260101120000
```

---

**Example 10:** Decode a wire string containing a custom segment by registering the message class:

```python
>>> from hl7types import decode_er7
>>>
>>> wire = (
...     "MSH|^~\\&|WPAS||SEND||20260101120000||ACK|MSG000002|P|2.5.1\r"
...     "MSA|AA|MSG000001\r"
...     "ZWCC|WPAS|20260101120000\r"
... )
>>>
>>> registry = HL7Registry()
>>> registry.register_segment("ZWCC", ZWCC)
>>> registry.register_message("2.5.1", "ACK", WCCACKMessage)
>>>
>>> msg = decode_er7(wire, registry=registry)
>>> msg.ZWCC.zwcc_1
'WPAS'
```

`MSH`, `FHS`, and `BHS` cannot be overridden — the decoder relies on them internally to detect encoding characters and message type. Attempting to register them raises immediately:

```python
>>> registry.register_segment("MSH", ZWCC)
ValueError: 'MSH' is a delimiter-definition segment and cannot be overridden
```

Each `HL7Registry` instance is independent, so concurrent pipelines with different vendor extensions can each hold their own registry without shared state.

---

## License

Proudly licensed under the MIT License. See [LICENSE](LICENSE) for details.
