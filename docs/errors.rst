Error Handling
==============

``hl7types`` provides ``errs_from_exception``, a helper that converts a Pydantic
``ValidationError`` into a list of fully spec-compliant ``ERR`` segments ready to be embedded in
a negative acknowledgement. It handles the structural differences between HL7 versions
automatically, so the correct ``ERR`` form is produced regardless of whether you are working with
v2.1 or v2.8.2. We fawn over good error handling here.

Any time a Pydantic ``ValidationError`` is raised, whether from ``decode_er7``, direct model
construction, or ``model_validate``, ``errs_from_exception`` converts it into a list of ``ERR``
segment instances, one per violated field, using the correct ``ERR`` structure for the HL7
version in use. Those segments can then be placed directly into a negative acknowledgement and
returned to the sender. Don't get caught deer in the headlights when validation fails we've
got you covered, no ifs, ands, or bucks.

.. code-block:: python

   from hl7types import decode_er7, HL7Registry
   from hl7types.utils.error import errs_from_exception
   from hl7types.hl7.v2_8_2.messages import ACK
   from hl7types.hl7.v2_8_2.segments import MSA, MSH
   from hl7types.hl7.v2_8_2.datatypes import HD, MSG, PT, TS, VID

   try:
       decode_er7(wire, registry=registry, strict=True)
   except Exception as e:
       errs = errs_from_exception(e, "2.8.2")

       msh = MSH(
           msh_3=HD(hd_1="RECEIVING_APP"),
           msh_5=HD(hd_1="SENDING_APP"),
           msh_7=TS(ts_1="20260101120000"),
           msh_9=MSG(msg_1="ACK"),
           msh_10="MSG000002",
           msh_11=PT(pt_1="P"),
           msh_12=VID(vid_1="2.8.2"),
       )
       msa = MSA(msa_1="AE", msa_2="MSG000001")

       nak = ACK(MSH=msh, MSA=msa, ERR=errs)
       print(nak.model_dump_er7())

Output::

   MSH|^~\&|RECEIVING_APP||SENDING_APP||20260101120000||ACK|MSG000002|P|2.8.2
   MSA|AE|MSG000001
   ERR||PID^1^3|101^Required field missing^HL70357|E
   ERR||PID^1^8|103^Table value not found^HL70357|E

Each ``ERR`` segment identifies the offending segment and field position (``ERR.2``), carries a
structured HL7 error code from table HL70357 (``ERR.3``), and sets severity to ``E`` for error
(``ERR.4``). ``MSA.1`` is set to ``AE`` (application error) to signal to the sender that the
message was rejected. Quite the reindeer of errors, all neatly lined up.

If the exception is not a ``ValidationError``, ``errs_from_exception`` returns an empty list. It
is the caller's responsibility to handle other exception types independently. No need to go
stag-gering around looking for errors that aren't thereif the list is empty, you're in the
clear. Deerly noted.

Error codes
-----------

Error codes are drawn from HL7 table 0357. The following codes are generated automatically from
Pydantic validation errors. The bucks stop here:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Code
     - Description
     - Triggered by
   * - ``101``
     - Required field missing
     - A required field was absent from the message
   * - ``102``
     - Data type error
     - A field value did not match the expected HL7 datatype
   * - ``103``
     - Table value not found
     - A coded field contained a value not present in the referenced table
   * - ``104``
     - Value too long
     - A field value exceeded the maximum defined length
   * - ``199``
     - Other HL7 Error
     - Any validation error not covered by the above categories

Version differences
-------------------

The structure of the ``ERR`` segment changed significantly across HL7 versions.
``errs_from_exception`` produces the correct form automatically based on the version string
passed to it. It's a doe or die situation, and we handle every version without missing a
single hart-beat.

**v2.1 and v2.2:** ``ERR.1`` is a repeating CM field carrying the error code and location as a
single composite string. Fawn-damentally simple:

.. code-block:: python

   errs = errs_from_exception(e, "2.1")
   # ERR|101~PID.3

**v2.3 and v2.3.1:** ``ERR.1`` is a repeating ``ELD`` (error location and description)
datatype. The error code is carried in ``ELD.4`` as a ``CE`` coded element referencing
table HL70060. Things are getting a little more stag-gered:

.. code-block:: python

   errs = errs_from_exception(e, "2.3")
   # ERR|PID^1^3^101&Required field missing&HL70060

**v2.4 and later:** ``ERR`` carries a fully structured response. The error code appears in
``ERR.3`` as a ``CWE`` referencing table HL70357, the field location in ``ERR.2`` as an ``ERL``,
and the severity in ``ERR.4``. Elk-egant:

.. code-block:: python

   errs = errs_from_exception(e, "2.8.2")
   # ERR||PID^1^3|101^Required field missing^HL70357|E
