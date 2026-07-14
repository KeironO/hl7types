v2.1 Messages
=============

.. _hl7-v2_1-ACK:

ACK General acknowledgment message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ACK.ACK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_1-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_1-ERR>`]
     - optional
     - ERROR

.. _hl7-v2_1-ADR_A19:

ADR_A19 HL7 v2 ADR_A19 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADR_A19.ADR_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_1-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``QRD``
     - :ref:`QRD <hl7-v2_1-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QUERY_RESPONSE``
     - List[:ref:`ADR_A19_QUERY_RESPONSE <hl7-v2_1-ADR_A19_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_1-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_1-ADT_A01:

ADT_A01 HL7 v2 ADT_A01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A01.ADT_A01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NK1``
     - :ref:`NK1 <hl7-v2_1-NK1>`
     - required
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DIAGNOSIS

.. _hl7-v2_1-ADT_A02:

ADT_A02 HL7 v2 ADT_A02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A02.ADT_A02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT

.. _hl7-v2_1-ADT_A03:

ADT_A03 HL7 v2 ADT_A03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A03.ADT_A03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT

.. _hl7-v2_1-ADT_A04:

ADT_A04 HL7 v2 ADT_A04 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A04.ADT_A04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NK1``
     - :ref:`NK1 <hl7-v2_1-NK1>`
     - required
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DIAGNOSIS

.. _hl7-v2_1-ADT_A05:

ADT_A05 HL7 v2 ADT_A05 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A05.ADT_A05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NK1``
     - :ref:`NK1 <hl7-v2_1-NK1>`
     - required
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DIAGNOSIS

.. _hl7-v2_1-ADT_A06:

ADT_A06 HL7 v2 ADT_A06 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A06.ADT_A06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT

.. _hl7-v2_1-ADT_A07:

ADT_A07 HL7 v2 ADT_A07 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A07.ADT_A07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT

.. _hl7-v2_1-ADT_A08:

ADT_A08 HL7 v2 ADT_A08 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A08.ADT_A08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NK1``
     - :ref:`NK1 <hl7-v2_1-NK1>`
     - required
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DIAGNOSIS

.. _hl7-v2_1-ADT_A09:

ADT_A09 HL7 v2 ADT_A09 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A09.ADT_A09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DIAGNOSIS

.. _hl7-v2_1-ADT_A10:

ADT_A10 HL7 v2 ADT_A10 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A10.ADT_A10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DIAGNOSIS

.. _hl7-v2_1-ADT_A11:

ADT_A11 HL7 v2 ADT_A11 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A11.ADT_A11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DIAGNOSIS

.. _hl7-v2_1-ADT_A12:

ADT_A12 HL7 v2 ADT_A12 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A12.ADT_A12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DIAGNOSIS

.. _hl7-v2_1-ADT_A13:

ADT_A13 HL7 v2 ADT_A13 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A13.ADT_A13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DIAGNOSIS

.. _hl7-v2_1-ADT_A14:

ADT_A14 HL7 v2 ADT_A14 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A14.ADT_A14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NK1``
     - :ref:`NK1 <hl7-v2_1-NK1>`
     - required
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DIAGNOSIS

.. _hl7-v2_1-ADT_A15:

ADT_A15 HL7 v2 ADT_A15 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A15.ADT_A15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DIAGNOSIS

.. _hl7-v2_1-ADT_A16:

ADT_A16 HL7 v2 ADT_A16 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A16.ADT_A16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DIAGNOSIS

.. _hl7-v2_1-ADT_A17:

ADT_A17 HL7 v2 ADT_A17 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A17.ADT_A17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PATIENT``
     - List[:ref:`ADT_A17_PATIENT <hl7-v2_1-ADT_A17_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_1-ADT_A18:

ADT_A18 HL7 v2 ADT_A18 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A18.ADT_A18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``MRG``
     - :ref:`MRG <hl7-v2_1-MRG>`
     - required
     - MERGE PATIENT INFORMATION
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     - PATIENT VISIT

.. _hl7-v2_1-ADT_A20:

ADT_A20 HL7 v2 ADT_A20 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A20.ADT_A20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``NPU``
     - :ref:`NPU <hl7-v2_1-NPU>`
     - required
     - NON-PATIENT UPDATE

.. _hl7-v2_1-ADT_A21:

ADT_A21 HL7 v2 ADT_A21 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A21.ADT_A21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT

.. _hl7-v2_1-ADT_A22:

ADT_A22 HL7 v2 ADT_A22 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A22.ADT_A22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT

.. _hl7-v2_1-ADT_A23:

ADT_A23 HL7 v2 ADT_A23 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A23.ADT_A23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT

.. _hl7-v2_1-ADT_A24:

ADT_A24 HL7 v2 ADT_A24 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A24.ADT_A24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT

.. _hl7-v2_1-BAR_P01:

BAR_P01 HL7 v2 BAR_P01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.BAR_P01.BAR_P01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``VISIT``
     - List[:ref:`BAR_P01_VISIT <hl7-v2_1-BAR_P01_VISIT>`]
     - required
     - VISIT

.. _hl7-v2_1-BAR_P02:

BAR_P02 HL7 v2 BAR_P02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.BAR_P02.BAR_P02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PATIENT``
     - List[:ref:`BAR_P02_PATIENT <hl7-v2_1-BAR_P02_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_1-DFT_P03:

DFT_P03 HL7 v2 DFT_P03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.DFT_P03.DFT_P03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     - PATIENT VISIT
   * - ``FT1``
     - Optional[List[:ref:`FT1 <hl7-v2_1-FT1>`]]
     - optional
     - FINANCIAL TRANSACTION

.. _hl7-v2_1-DSR_Q01:

DSR_Q01 HL7 v2 DSR_Q01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.DSR_Q01.DSR_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_1-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``QRD``
     - :ref:`QRD <hl7-v2_1-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_1-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_1-DSP>`]
     - required
     - DISPLAY DATA
   * - ``DSC``
     - :ref:`DSC <hl7-v2_1-DSC>`
     - required
     - CONTINUATION POINTER

.. _hl7-v2_1-DSR_Q03:

DSR_Q03 HL7 v2 DSR_Q03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.DSR_Q03.DSR_Q03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``QRD``
     - :ref:`QRD <hl7-v2_1-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_1-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_1-DSP>`]
     - required
     - DISPLAY DATA
   * - ``DSC``
     - :ref:`DSC <hl7-v2_1-DSC>`
     - required
     - CONTINUATION POINTER

.. _hl7-v2_1-MCF_Q02:

MCF_Q02 HL7 v2 MCF_Q02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.MCF_Q02.MCF_Q02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_1-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT

.. _hl7-v2_1-ORM_O01:

ORM_O01 HL7 v2 ORM_O01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ORM_O01.ORM_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NOTES AND COMMENTS
   * - ``PATIENT``
     - Optional[:ref:`ORM_O01_PATIENT <hl7-v2_1-ORM_O01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ORM_O01_ORDER <hl7-v2_1-ORM_O01_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_1-ORR_O02:

ORR_O02 HL7 v2 ORR_O02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ORR_O02.ORR_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_1-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NOTES AND COMMENTS
   * - ``PATIENT``
     - Optional[:ref:`ORR_O02_PATIENT <hl7-v2_1-ORR_O02_PATIENT>`]
     - optional
     - PATIENT

.. _hl7-v2_1-ORU_R01:

ORU_R01 HL7 v2 ORU_R01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ORU_R01.ORU_R01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``PATIENT_RESULT``
     - List[:ref:`ORU_R01_PATIENT_RESULT <hl7-v2_1-ORU_R01_PATIENT_RESULT>`]
     - required
     - PATIENT_RESULT
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_1-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_1-ORU_R03:

ORU_R03 HL7 v2 ORU_R03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.ORU_R03.ORU_R03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``PATIENT_RESULT``
     - List[:ref:`ORU_R03_PATIENT_RESULT <hl7-v2_1-ORU_R03_PATIENT_RESULT>`]
     - required
     - PATIENT_RESULT
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_1-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_1-QRY_A19:

QRY_A19 HL7 v2 QRY_A19 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.QRY_A19.QRY_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``QRD``
     - :ref:`QRD <hl7-v2_1-QRD>`
     - required
     - QUERY DEFINITION

.. _hl7-v2_1-QRY_Q01:

QRY_Q01 HL7 v2 QRY_Q01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.QRY_Q01.QRY_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``QRD``
     - :ref:`QRD <hl7-v2_1-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_1-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSC``
     - :ref:`DSC <hl7-v2_1-DSC>`
     - required
     - CONTINUATION POINTER

.. _hl7-v2_1-QRY_Q02:

QRY_Q02 HL7 v2 QRY_Q02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.QRY_Q02.QRY_Q02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``QRD``
     - :ref:`QRD <hl7-v2_1-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_1-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSC``
     - :ref:`DSC <hl7-v2_1-DSC>`
     - required
     - CONTINUATION POINTER

.. _hl7-v2_1-UDM_Q05:

UDM_Q05 HL7 v2 UDM_Q05 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.messages.UDM_Q05.UDM_Q05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MESSAGE HEADER
   * - ``URD``
     - :ref:`URD <hl7-v2_1-URD>`
     - required
     - RESULTS/UPDATE DEFINITION
   * - ``URS``
     - Optional[:ref:`URS <hl7-v2_1-URS>`]
     - optional
     - UNSOLICITED SELECTION
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_1-DSP>`]
     - required
     - DISPLAY DATA
   * - ``DSC``
     - :ref:`DSC <hl7-v2_1-DSC>`
     - required
     - CONTINUATION POINTER
