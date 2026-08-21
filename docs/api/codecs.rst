Codecs
======

.. automodule:: hl7types.codecs.er7.encoder
   :members:
   :undoc-members:
   :exclude-members: EncodingChars, is_segment

.. automodule:: hl7types.codecs.er7.decoder
   :members:
   :undoc-members:
   :exclude-members: is_segment_cls

Hybrid ER7 decoding
-------------------

The hybrid decoder provides two views of the same message. The generic view
retains the original wire string, unknown segments, and empty values without
requiring generated HL7 models. The optional typed view uses lenient decoding
for known content and reports warnings or validation errors as diagnostics.

.. autofunction:: hl7types.codecs.er7.hybrid.decode_er7_hybrid

.. autoclass:: hl7types.codecs.er7.hybrid.HybridMessage
   :members:

.. autoclass:: hl7types.codecs.er7.hybrid.HybridDecodeDiagnostic
   :members:

Generic ER7 types
~~~~~~~~~~~~~~~~~

.. autoclass:: hl7types.codecs.er7.generic.GenericMessage
   :members:

.. autoclass:: hl7types.codecs.er7.generic.GenericSegment
   :members:

.. autoclass:: hl7types.codecs.er7.generic.GenericField
   :members:

.. autoclass:: hl7types.codecs.er7.generic.GenericRepetition
   :members:

.. autoclass:: hl7types.codecs.er7.generic.GenericComponent
   :members:

XML decoding
------------

.. automodule:: hl7types.codecs.xml.decoder
   :members:
   :undoc-members:
   :exclude-members:

Fallback parsing types
----------------------

.. autoclass:: hl7types.hl7._validators.NonStandardDateWarning
   :show-inheritance:

.. data:: hl7types.DateParser

   Type alias for a fallback date/datetime parser callable::

      DateParser = Callable[[str], str]

   The callable receives a raw non-HL7 string and must return a valid HL7 DT
   or DTM string, or raise any exception to signal failure. Pass instances as
   ``dt_parser=`` or ``dtm_parser=`` to any decode function.

   See :ref:`fallback-parsing` for usage examples.
