v2.1 Messages
=============

.. _hl7-v2_1-ACK:

.. py:class:: hl7types.hl7.v2_1.messages.ACK.ACK
   :noindex:

   HL7 v2 ACK message.

ACK
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_1-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_1-ERR>`]
     - optional
     - ERR: Optional

.. _hl7-v2_1-ADR_A19:

.. py:class:: hl7types.hl7.v2_1.messages.ADR_A19.ADR_A19
   :noindex:

   HL7 v2 ADR_A19 message.

ADR_A19
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_1-MSA>`
     - required
     - MSA: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_1-QRD>`
     - required
     - QRD: Required
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`ADR_A19_QUERY_RESPONSE <hl7-v2_1-ADR_A19_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_1-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_1-ADT_A01:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A01.ADT_A01
   :noindex:

   HL7 v2 ADT_A01 message.

ADT_A01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``NK1``
     -
     - :ref:`NK1 <hl7-v2_1-NK1>`
     - required
     - NK1: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DG1: Optional

.. _hl7-v2_1-ADT_A02:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A02.ADT_A02
   :noindex:

   HL7 v2 ADT_A02 message.

ADT_A02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required

.. _hl7-v2_1-ADT_A03:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A03.ADT_A03
   :noindex:

   HL7 v2 ADT_A03 message.

ADT_A03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required

.. _hl7-v2_1-ADT_A04:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A04.ADT_A04
   :noindex:

   HL7 v2 ADT_A04 message.

ADT_A04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``NK1``
     -
     - :ref:`NK1 <hl7-v2_1-NK1>`
     - required
     - NK1: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DG1: Optional

.. _hl7-v2_1-ADT_A05:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A05.ADT_A05
   :noindex:

   HL7 v2 ADT_A05 message.

ADT_A05
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``NK1``
     -
     - :ref:`NK1 <hl7-v2_1-NK1>`
     - required
     - NK1: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DG1: Optional

.. _hl7-v2_1-ADT_A06:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A06.ADT_A06
   :noindex:

   HL7 v2 ADT_A06 message.

ADT_A06
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required

.. _hl7-v2_1-ADT_A07:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A07.ADT_A07
   :noindex:

   HL7 v2 ADT_A07 message.

ADT_A07
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required

.. _hl7-v2_1-ADT_A08:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A08.ADT_A08
   :noindex:

   HL7 v2 ADT_A08 message.

ADT_A08
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``NK1``
     -
     - :ref:`NK1 <hl7-v2_1-NK1>`
     - required
     - NK1: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DG1: Optional

.. _hl7-v2_1-ADT_A09:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A09.ADT_A09
   :noindex:

   HL7 v2 ADT_A09 message.

ADT_A09
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DG1: Optional

.. _hl7-v2_1-ADT_A10:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A10.ADT_A10
   :noindex:

   HL7 v2 ADT_A10 message.

ADT_A10
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DG1: Optional

.. _hl7-v2_1-ADT_A11:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A11.ADT_A11
   :noindex:

   HL7 v2 ADT_A11 message.

ADT_A11
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DG1: Optional

.. _hl7-v2_1-ADT_A12:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A12.ADT_A12
   :noindex:

   HL7 v2 ADT_A12 message.

ADT_A12
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DG1: Optional

.. _hl7-v2_1-ADT_A13:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A13.ADT_A13
   :noindex:

   HL7 v2 ADT_A13 message.

ADT_A13
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DG1: Optional

.. _hl7-v2_1-ADT_A14:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A14.ADT_A14
   :noindex:

   HL7 v2 ADT_A14 message.

ADT_A14
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``NK1``
     -
     - :ref:`NK1 <hl7-v2_1-NK1>`
     - required
     - NK1: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DG1: Optional

.. _hl7-v2_1-ADT_A15:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A15.ADT_A15
   :noindex:

   HL7 v2 ADT_A15 message.

ADT_A15
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DG1: Optional

.. _hl7-v2_1-ADT_A16:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A16.ADT_A16
   :noindex:

   HL7 v2 ADT_A16 message.

ADT_A16
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_1-DG1>`]
     - optional
     - DG1: Optional

.. _hl7-v2_1-ADT_A17:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A17.ADT_A17
   :noindex:

   HL7 v2 ADT_A17 message.

ADT_A17
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`ADT_A17_PATIENT <hl7-v2_1-ADT_A17_PATIENT>`]
     - required
     - PATIENT: Required, repeating

.. _hl7-v2_1-ADT_A18:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A18.ADT_A18
   :noindex:

   HL7 v2 ADT_A18 message.

ADT_A18
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``MRG``
     -
     - :ref:`MRG <hl7-v2_1-MRG>`
     - required
     - MRG: Required
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     - PV1: Optional

.. _hl7-v2_1-ADT_A20:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A20.ADT_A20
   :noindex:

   HL7 v2 ADT_A20 message.

ADT_A20
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``NPU``
     -
     - :ref:`NPU <hl7-v2_1-NPU>`
     - required
     - NPU: Required

.. _hl7-v2_1-ADT_A21:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A21.ADT_A21
   :noindex:

   HL7 v2 ADT_A21 message.

ADT_A21
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required

.. _hl7-v2_1-ADT_A22:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A22.ADT_A22
   :noindex:

   HL7 v2 ADT_A22 message.

ADT_A22
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required

.. _hl7-v2_1-ADT_A23:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A23.ADT_A23
   :noindex:

   HL7 v2 ADT_A23 message.

ADT_A23
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required

.. _hl7-v2_1-ADT_A24:

.. py:class:: hl7types.hl7.v2_1.messages.ADT_A24.ADT_A24
   :noindex:

   HL7 v2 ADT_A24 message.

ADT_A24
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PV1: Required

.. _hl7-v2_1-BAR_P01:

.. py:class:: hl7types.hl7.v2_1.messages.BAR_P01.BAR_P01
   :noindex:

   HL7 v2 BAR_P01 message.

BAR_P01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``VISIT``
     -
     - List[:ref:`BAR_P01_VISIT <hl7-v2_1-BAR_P01_VISIT>`]
     - required
     - VISIT: Required, repeating

.. _hl7-v2_1-BAR_P02:

.. py:class:: hl7types.hl7.v2_1.messages.BAR_P02.BAR_P02
   :noindex:

   HL7 v2 BAR_P02 message.

BAR_P02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`BAR_P02_PATIENT <hl7-v2_1-BAR_P02_PATIENT>`]
     - required
     - PATIENT: Required, repeating

.. _hl7-v2_1-DFT_P03:

.. py:class:: hl7types.hl7.v2_1.messages.DFT_P03.DFT_P03
   :noindex:

   HL7 v2 DFT_P03 message.

DFT_P03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_1-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     - PV1: Optional
   * - ``FT1``
     -
     - Optional[List[:ref:`FT1 <hl7-v2_1-FT1>`]]
     - optional
     - FT1: Optional, repeating

.. _hl7-v2_1-DSR_Q01:

.. py:class:: hl7types.hl7.v2_1.messages.DSR_Q01.DSR_Q01
   :noindex:

   HL7 v2 DSR_Q01 message.

DSR_Q01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_1-MSA>`
     - required
     - MSA: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_1-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_1-QRF>`]
     - optional
     - QRF: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_1-DSP>`]
     - required
     - DSP: Required, repeating
   * - ``DSC``
     -
     - :ref:`DSC <hl7-v2_1-DSC>`
     - required
     - DSC: Required

.. _hl7-v2_1-DSR_Q03:

.. py:class:: hl7types.hl7.v2_1.messages.DSR_Q03.DSR_Q03
   :noindex:

   HL7 v2 DSR_Q03 message.

DSR_Q03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_1-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_1-QRF>`]
     - optional
     - QRF: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_1-DSP>`]
     - required
     - DSP: Required, repeating
   * - ``DSC``
     -
     - :ref:`DSC <hl7-v2_1-DSC>`
     - required
     - DSC: Required

.. _hl7-v2_1-MCF_Q02:

.. py:class:: hl7types.hl7.v2_1.messages.MCF_Q02.MCF_Q02
   :noindex:

   HL7 v2 MCF_Q02 message.

MCF_Q02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_1-MSA>`
     - required
     - MSA: Required

.. _hl7-v2_1-ORM_O01:

.. py:class:: hl7types.hl7.v2_1.messages.ORM_O01.ORM_O01
   :noindex:

   HL7 v2 ORM_O01 message.

ORM_O01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`ORM_O01_PATIENT <hl7-v2_1-ORM_O01_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`ORM_O01_ORDER <hl7-v2_1-ORM_O01_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_1-ORR_O02:

.. py:class:: hl7types.hl7.v2_1.messages.ORR_O02.ORR_O02
   :noindex:

   HL7 v2 ORR_O02 message.

ORR_O02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_1-MSA>`
     - required
     - MSA: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`ORR_O02_PATIENT <hl7-v2_1-ORR_O02_PATIENT>`]
     - optional
     - PATIENT: Optional

.. _hl7-v2_1-ORU_R01:

.. py:class:: hl7types.hl7.v2_1.messages.ORU_R01.ORU_R01
   :noindex:

   HL7 v2 ORU_R01 message.

ORU_R01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``PATIENT_RESULT``
     -
     - List[:ref:`ORU_R01_PATIENT_RESULT <hl7-v2_1-ORU_R01_PATIENT_RESULT>`]
     - required
     - PATIENT_RESULT: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_1-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_1-ORU_R03:

.. py:class:: hl7types.hl7.v2_1.messages.ORU_R03.ORU_R03
   :noindex:

   HL7 v2 ORU_R03 message.

ORU_R03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``PATIENT_RESULT``
     -
     - List[:ref:`ORU_R03_PATIENT_RESULT <hl7-v2_1-ORU_R03_PATIENT_RESULT>`]
     - required
     - PATIENT_RESULT: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_1-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_1-QRY_A19:

.. py:class:: hl7types.hl7.v2_1.messages.QRY_A19.QRY_A19
   :noindex:

   HL7 v2 QRY_A19 message.

QRY_A19
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_1-QRD>`
     - required
     - QRD: Required

.. _hl7-v2_1-QRY_Q01:

.. py:class:: hl7types.hl7.v2_1.messages.QRY_Q01.QRY_Q01
   :noindex:

   HL7 v2 QRY_Q01 message.

QRY_Q01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_1-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_1-QRF>`]
     - optional
     - QRF: Optional
   * - ``DSC``
     -
     - :ref:`DSC <hl7-v2_1-DSC>`
     - required
     - DSC: Required

.. _hl7-v2_1-QRY_Q02:

.. py:class:: hl7types.hl7.v2_1.messages.QRY_Q02.QRY_Q02
   :noindex:

   HL7 v2 QRY_Q02 message.

QRY_Q02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_1-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_1-QRF>`]
     - optional
     - QRF: Optional
   * - ``DSC``
     -
     - :ref:`DSC <hl7-v2_1-DSC>`
     - required
     - DSC: Required

.. _hl7-v2_1-UDM_Q05:

.. py:class:: hl7types.hl7.v2_1.messages.UDM_Q05.UDM_Q05
   :noindex:

   HL7 v2 UDM_Q05 message.

UDM_Q05
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_1-MSH>`
     - required
     - MSH: Required
   * - ``URD``
     -
     - :ref:`URD <hl7-v2_1-URD>`
     - required
     - URD: Required
   * - ``URS``
     -
     - Optional[:ref:`URS <hl7-v2_1-URS>`]
     - optional
     - URS: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_1-DSP>`]
     - required
     - DSP: Required, repeating
   * - ``DSC``
     -
     - :ref:`DSC <hl7-v2_1-DSC>`
     - required
     - DSC: Required
