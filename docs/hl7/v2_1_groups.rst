v2.1 Groups
===========

.. _hl7-v2_1-ADR_A19_QUERY_RESPONSE:

.. py:class:: hl7types.hl7.v2_1.groups.ADR_A19_QUERY_RESPONSE.ADR_A19_QUERY_RESPONSE
   :noindex:

   HL7 v2 ADR_A19.QUERY_RESPONSE group.

ADR_A19_QUERY_RESPONSE
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``EVN``
     -
     - Optional[:ref:`EVN <hl7-v2_1-EVN>`]
     - optional
     -
     - EVN: Optional
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - optional
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - optional
     -
     - PV1: Required

.. _hl7-v2_1-ADT_A17_PATIENT:

.. py:class:: hl7types.hl7.v2_1.groups.ADT_A17_PATIENT.ADT_A17_PATIENT
   :noindex:

   HL7 v2 ADT_A17.PATIENT group.

ADT_A17_PATIENT
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - optional
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - optional
     -
     - PV1: Required

.. _hl7-v2_1-BAR_P01_VISIT:

.. py:class:: hl7types.hl7.v2_1.groups.BAR_P01_VISIT.BAR_P01_VISIT
   :noindex:

   HL7 v2 BAR_P01.VISIT group.

BAR_P01_VISIT
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     -
     - PV1: Optional
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``PR1``
     -
     - Optional[List[:ref:`PR1 <hl7-v2_1-PR1>`]]
     - optional
     -
     - PR1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_1-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``IN1``
     -
     - Optional[List[:ref:`IN1 <hl7-v2_1-IN1>`]]
     - optional
     -
     - IN1: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_1-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_1-UB1>`]
     - optional
     -
     - UB1: Optional

.. _hl7-v2_1-BAR_P02_PATIENT:

.. py:class:: hl7types.hl7.v2_1.groups.BAR_P02_PATIENT.BAR_P02_PATIENT
   :noindex:

   HL7 v2 BAR_P02.PATIENT group.

BAR_P02_PATIENT
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - optional
     -
     - PID: Required
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     -
     - PV1: Optional

.. _hl7-v2_1-ORM_O01_CHOICE:

.. py:class:: hl7types.hl7.v2_1.groups.ORM_O01_CHOICE.ORM_O01_CHOICE
   :noindex:

   HL7 v2 ORM_O01.CHOICE group.

ORM_O01_CHOICE
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``OBR``
     -
     - Optional[:ref:`OBR <hl7-v2_1-OBR>`]
     - optional
     -
     - OBR: Optional
   * - ``ORO``
     -
     - Optional[:ref:`ORO <hl7-v2_1-ORO>`]
     - optional
     -
     - ORO: Optional
   * - ``RX1``
     -
     - Optional[:ref:`RX1 <hl7-v2_1-RX1>`]
     - optional
     -
     - RX1: Optional

.. _hl7-v2_1-ORM_O01_ORDER:

.. py:class:: hl7types.hl7.v2_1.groups.ORM_O01_ORDER.ORM_O01_ORDER
   :noindex:

   HL7 v2 ORM_O01.ORDER group.

ORM_O01_ORDER
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ORC``
     -
     - :ref:`ORC <hl7-v2_1-ORC>`
     - optional
     -
     - ORC: Required
   * - ``ORDER_DETAIL``
     -
     - Optional[:ref:`ORM_O01_ORDER_DETAIL <hl7-v2_1-ORM_O01_ORDER_DETAIL>`]
     - optional
     -
     - ORDER_DETAIL: Optional
   * - ``BLG``
     -
     - Optional[:ref:`BLG <hl7-v2_1-BLG>`]
     - optional
     -
     - BLG: Optional

.. _hl7-v2_1-ORM_O01_ORDER_DETAIL:

.. py:class:: hl7types.hl7.v2_1.groups.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_DETAIL
   :noindex:

   HL7 v2 ORM_O01.ORDER_DETAIL group.

ORM_O01_ORDER_DETAIL
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``CHOICE``
     -
     - :ref:`ORM_O01_CHOICE <hl7-v2_1-ORM_O01_CHOICE>`
     - optional
     -
     - CHOICE: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_1-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_1-ORM_O01_PATIENT:

.. py:class:: hl7types.hl7.v2_1.groups.ORM_O01_PATIENT.ORM_O01_PATIENT
   :noindex:

   HL7 v2 ORM_O01.PATIENT group.

ORM_O01_PATIENT
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - optional
     -
     - PID: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     -
     - PV1: Optional

.. _hl7-v2_1-ORR_O02_CHOICE:

.. py:class:: hl7types.hl7.v2_1.groups.ORR_O02_CHOICE.ORR_O02_CHOICE
   :noindex:

   HL7 v2 ORR_O02.CHOICE group.

ORR_O02_CHOICE
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``OBR``
     -
     - Optional[:ref:`OBR <hl7-v2_1-OBR>`]
     - optional
     -
     - OBR: Optional
   * - ``ORO``
     -
     - Optional[:ref:`ORO <hl7-v2_1-ORO>`]
     - optional
     -
     - ORO: Optional
   * - ``RX1``
     -
     - Optional[:ref:`RX1 <hl7-v2_1-RX1>`]
     - optional
     -
     - RX1: Optional

.. _hl7-v2_1-ORR_O02_ORDER:

.. py:class:: hl7types.hl7.v2_1.groups.ORR_O02_ORDER.ORR_O02_ORDER
   :noindex:

   HL7 v2 ORR_O02.ORDER group.

ORR_O02_ORDER
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ORC``
     -
     - :ref:`ORC <hl7-v2_1-ORC>`
     - optional
     -
     - ORC: Required
   * - ``ORDER_DETAIL``
     -
     - Optional[:ref:`ORR_O02_ORDER_DETAIL <hl7-v2_1-ORR_O02_ORDER_DETAIL>`]
     - optional
     -
     - ORDER_DETAIL: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_1-ORR_O02_ORDER_DETAIL:

.. py:class:: hl7types.hl7.v2_1.groups.ORR_O02_ORDER_DETAIL.ORR_O02_ORDER_DETAIL
   :noindex:

   HL7 v2 ORR_O02.ORDER_DETAIL group.

ORR_O02_ORDER_DETAIL
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``CHOICE``
     -
     - :ref:`ORR_O02_CHOICE <hl7-v2_1-ORR_O02_CHOICE>`
     - optional
     -
     - CHOICE: Required

.. _hl7-v2_1-ORR_O02_PATIENT:

.. py:class:: hl7types.hl7.v2_1.groups.ORR_O02_PATIENT.ORR_O02_PATIENT
   :noindex:

   HL7 v2 ORR_O02.PATIENT group.

ORR_O02_PATIENT
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``PID``
     -
     - Optional[:ref:`PID <hl7-v2_1-PID>`]
     - optional
     -
     - PID: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``ORDER``
     -
     - List[:ref:`ORR_O02_ORDER <hl7-v2_1-ORR_O02_ORDER>`]
     - optional
     -
     - ORDER: Required, repeating

.. _hl7-v2_1-ORU_R01_OBSERVATION:

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R01_OBSERVATION.ORU_R01_OBSERVATION
   :noindex:

   HL7 v2 ORU_R01.OBSERVATION group.

ORU_R01_OBSERVATION
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``OBX``
     -
     - Optional[:ref:`OBX <hl7-v2_1-OBX>`]
     - optional
     -
     - OBX: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_1-ORU_R01_ORDER_OBSERVATION:

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R01_ORDER_OBSERVATION.ORU_R01_ORDER_OBSERVATION
   :noindex:

   HL7 v2 ORU_R01.ORDER_OBSERVATION group.

ORU_R01_ORDER_OBSERVATION
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ORC``
     -
     - Optional[:ref:`ORC <hl7-v2_1-ORC>`]
     - optional
     -
     - ORC: Optional
   * - ``OBR``
     -
     - :ref:`OBR <hl7-v2_1-OBR>`
     - optional
     -
     - OBR: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``OBSERVATION``
     -
     - List[:ref:`ORU_R01_OBSERVATION <hl7-v2_1-ORU_R01_OBSERVATION>`]
     - optional
     -
     - OBSERVATION: Required, repeating

.. _hl7-v2_1-ORU_R01_PATIENT:

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R01_PATIENT.ORU_R01_PATIENT
   :noindex:

   HL7 v2 ORU_R01.PATIENT group.

ORU_R01_PATIENT
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - optional
     -
     - PID: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     -
     - PV1: Optional

.. _hl7-v2_1-ORU_R01_PATIENT_RESULT:

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT_RESULT
   :noindex:

   HL7 v2 ORU_R01.PATIENT_RESULT group.

ORU_R01_PATIENT_RESULT
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``PATIENT``
     -
     - Optional[:ref:`ORU_R01_PATIENT <hl7-v2_1-ORU_R01_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER_OBSERVATION``
     -
     - List[:ref:`ORU_R01_ORDER_OBSERVATION <hl7-v2_1-ORU_R01_ORDER_OBSERVATION>`]
     - optional
     -
     - ORDER_OBSERVATION: Required, repeating

.. _hl7-v2_1-ORU_R03_OBSERVATION:

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R03_OBSERVATION.ORU_R03_OBSERVATION
   :noindex:

   HL7 v2 ORU_R03.OBSERVATION group.

ORU_R03_OBSERVATION
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``OBX``
     -
     - Optional[:ref:`OBX <hl7-v2_1-OBX>`]
     - optional
     -
     - OBX: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_1-ORU_R03_ORDER_OBSERVATION:

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R03_ORDER_OBSERVATION.ORU_R03_ORDER_OBSERVATION
   :noindex:

   HL7 v2 ORU_R03.ORDER_OBSERVATION group.

ORU_R03_ORDER_OBSERVATION
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ORC``
     -
     - Optional[:ref:`ORC <hl7-v2_1-ORC>`]
     - optional
     -
     - ORC: Optional
   * - ``OBR``
     -
     - :ref:`OBR <hl7-v2_1-OBR>`
     - optional
     -
     - OBR: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``OBSERVATION``
     -
     - List[:ref:`ORU_R03_OBSERVATION <hl7-v2_1-ORU_R03_OBSERVATION>`]
     - optional
     -
     - OBSERVATION: Required, repeating

.. _hl7-v2_1-ORU_R03_PATIENT:

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R03_PATIENT.ORU_R03_PATIENT
   :noindex:

   HL7 v2 ORU_R03.PATIENT group.

ORU_R03_PATIENT
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_1-PID>`
     - optional
     -
     - PID: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     -
     - PV1: Optional

.. _hl7-v2_1-ORU_R03_PATIENT_RESULT:

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R03_PATIENT_RESULT.ORU_R03_PATIENT_RESULT
   :noindex:

   HL7 v2 ORU_R03.PATIENT_RESULT group.

ORU_R03_PATIENT_RESULT
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``PATIENT``
     -
     - Optional[:ref:`ORU_R03_PATIENT <hl7-v2_1-ORU_R03_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER_OBSERVATION``
     -
     - List[:ref:`ORU_R03_ORDER_OBSERVATION <hl7-v2_1-ORU_R03_ORDER_OBSERVATION>`]
     - optional
     -
     - ORDER_OBSERVATION: Required, repeating
