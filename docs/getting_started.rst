Getting Started
===============

Installation
------------

Install ``hl7types`` using ``pip``:

.. code-block:: bash

   pip install hl7types

Or with ``uv``:

.. code-block:: bash

   uv add hl7types

To install directly from the repository:

.. code-block:: bash

   pip install git+https://github.com/KeironO/hl7types.git

Or with ``uv``:

.. code-block:: bash

   uv add git+https://github.com/KeironO/hl7types.git

Building a message
------------------

Every HL7 v2 message is a structured container of segments. Each segment has a defined role in the
message and carries a specific set of fields. The message type determines which segments are
required and which are optional.

We will use :ref:`ACK <hl7-v2_5_1-ACK>` (general acknowledgement) as our example,  it is one of
the most common messages in any HL7 deployment and has a minimal structure that makes it easy to
reason about. It requires exactly two segments: :ref:`MSH <hl7-v2_5_1-MSH>` (message header),
which is mandatory in every HL7 v2 message and carries routing and encoding metadata, and
:ref:`MSA <hl7-v2_5_1-MSA>` (message acknowledgement), which carries the acknowledgement code and
the control ID of the message being acknowledged.

Segments themselves are composed of datatypes. :ref:`MSH <hl7-v2_5_1-MSH>` uses
:ref:`HD <hl7-v2_5_1-HD>` (hierarchic designator) to identify sending and receiving applications,
:ref:`TS <hl7-v2_5_1-TS>` (time stamp) for the message date and time,
:ref:`MSG <hl7-v2_5_1-MSG>` to encode the message type and trigger event,
:ref:`PT <hl7-v2_5_1-PT>` for the processing ID, and
:ref:`VID <hl7-v2_5_1-VID>` for the HL7 version. Each of these is itself a typed model, so
invalid values are caught at construction time rather than at the wire boundary.

.. code-block:: python

   from hl7types.hl7.v2_5_1.messages import ACK
   from hl7types.hl7.v2_5_1.segments import MSA, MSH
   from hl7types.hl7.v2_5_1.datatypes import HD, MSG, PT, TS, VID

   msh = MSH(
       msh_3=HD(hd_1="SENDING_APP"),
       msh_5=HD(hd_1="RECEIVING_APP"),
       msh_7=TS(ts_1="20260101120000"),
       msh_9=MSG(msg_1="ACK"),
       msh_10="MSG000001",
       msh_11=PT(pt_1="P"),
       msh_12=VID(vid_1="2.5.1"),
   )

   msa = MSA(
       msa_1="AA",        # AA = Application Accept
       msa_2="MSG000001", # control ID of the message being acknowledged
   )

   ack = ACK(MSH=msh, MSA=msa)

Encoding to ER7
---------------

ER7 is the traditional pipe-delimited wire format defined by the HL7 v2 specification. Each
segment occupies its own line, identified by its three-letter name (``MSH``, ``MSA``, and so on).
Within a segment, fields are separated by ``|``, components within a field by ``^``, repeated
values by ``~``, and subcomponents by ``&``. These four characters, along with the escape character
``\``, are declared in ``MSH.2`` and are present in every ER7 message.

An important detail of the ER7 wire format is that segments are terminated by a carriage return (``\r``),
not a newline (``\n``). This is mandated by the HL7 specification and is the norm
across all HL7 v2 implementations, so splitting on ``\r`` is the correct way to recover individual
segments from a raw wire string.

Call ``model_dump_er7()`` to encode the message:

.. code-block:: python

   er7 = ack.model_dump_er7()

   for segment in er7.split("\r"):
       print(segment)

Output::

   MSH|^~\&|SENDING_APP||RECEIVING_APP||20260101120000||ACK|MSG000001|P|2.5.1
   MSA|AA|MSG000001

Decoding back from ER7
-----------------------

Rather than specifying the message class explicitly, use the top-level ``decode_er7`` helper.
It reads the message type and version directly from :ref:`MSH <hl7-v2_5_1-MSH>` in the wire
string and resolves the correct model class automatically, which is how real pipelines work,
the receiving system does not always know the message type in advance.

.. code-block:: python

   from hl7types import decode_er7

   decoded = decode_er7(er7)

   print(decoded.MSH.msh_3.hd_1)   # "SENDING_APP"
   print(decoded.MSA.msa_1)        # "AA"
   print(decoded.MSA.msa_2)        # "MSG000001"

The result is a fully typed :ref:`ACK <hl7-v2_5_1-ACK>` instance,  field access, validation, and
serialisation all work exactly as they did on the original object.
