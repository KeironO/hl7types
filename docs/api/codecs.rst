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
