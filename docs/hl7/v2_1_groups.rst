v2.1 Groups
===========

.. _hl7-v2_1-ADR_A19_QUERY_RESPONSE:

ADR_A19_QUERY_RESPONSE: HL7 v2 ADR_A19.QUERY_RESPONSE group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ADR_A19_QUERY_RESPONSE.ADR_A19_QUERY_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``EVN``
     - :ref:`EVN <hl7-v2_1-EVN>`
     - O
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - R
     - PV1

.. _hl7-v2_1-ADT_A17_PATIENT:

ADT_A17_PATIENT: HL7 v2 ADT_A17.PATIENT group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ADT_A17_PATIENT.ADT_A17_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - R
     - PV1

.. _hl7-v2_1-BAR_P01_VISIT:

BAR_P01_VISIT: HL7 v2 BAR_P01.VISIT group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.BAR_P01_VISIT.BAR_P01_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - O
     - PV1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_1-DG1>`]
     - O
     - DG1
   * - ``PR1``
     - list[:ref:`PR1 <hl7-v2_1-PR1>`]
     - O
     - PR1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_1-GT1>`]
     - O
     - GT1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_1-NK1>`]
     - O
     - NK1
   * - ``IN1``
     - list[:ref:`IN1 <hl7-v2_1-IN1>`]
     - O
     - IN1
   * - ``ACC``
     - :ref:`ACC <hl7-v2_1-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_1-UB1>`
     - O
     - UB1

.. _hl7-v2_1-BAR_P02_PATIENT:

BAR_P02_PATIENT: HL7 v2 BAR_P02.PATIENT group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.BAR_P02_PATIENT.BAR_P02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - O
     - PV1

.. _hl7-v2_1-ORM_O01_CHOICE:

ORM_O01_CHOICE: HL7 v2 ORM_O01.CHOICE group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORM_O01_CHOICE.ORM_O01_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_1-OBR>`
     - O
     - OBR
   * - ``ORO``
     - :ref:`ORO <hl7-v2_1-ORO>`
     - O
     - ORO
   * - ``RX1``
     - :ref:`RX1 <hl7-v2_1-RX1>`
     - O
     - RX1

.. _hl7-v2_1-ORM_O01_ORDER:

ORM_O01_ORDER: HL7 v2 ORM_O01.ORDER group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORM_O01_ORDER.ORM_O01_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_1-ORC>`
     - R
     - ORC
   * - ``ORDER_DETAIL``
     - :ref:`ORM_O01_ORDER_DETAIL <hl7-v2_1-ORM_O01_ORDER_DETAIL>`
     - O
     - ORDER_DETAIL
   * - ``BLG``
     - :ref:`BLG <hl7-v2_1-BLG>`
     - O
     - BLG

.. _hl7-v2_1-ORM_O01_ORDER_DETAIL:

ORM_O01_ORDER_DETAIL: HL7 v2 ORM_O01.ORDER_DETAIL group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``CHOICE``
     - :ref:`ORM_O01_CHOICE <hl7-v2_1-ORM_O01_CHOICE>`
     - R
     - CHOICE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_1-NTE>`]
     - O
     - NTE
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_1-OBX>`]
     - O
     - OBX

.. _hl7-v2_1-ORM_O01_PATIENT:

ORM_O01_PATIENT: HL7 v2 ORM_O01.PATIENT group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORM_O01_PATIENT.ORM_O01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - R
     - PID
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_1-NTE>`]
     - O
     - NTE
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - O
     - PV1

.. _hl7-v2_1-ORR_O02_CHOICE:

ORR_O02_CHOICE: HL7 v2 ORR_O02.CHOICE group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORR_O02_CHOICE.ORR_O02_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_1-OBR>`
     - O
     - OBR
   * - ``ORO``
     - :ref:`ORO <hl7-v2_1-ORO>`
     - O
     - ORO
   * - ``RX1``
     - :ref:`RX1 <hl7-v2_1-RX1>`
     - O
     - RX1

.. _hl7-v2_1-ORR_O02_ORDER:

ORR_O02_ORDER: HL7 v2 ORR_O02.ORDER group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORR_O02_ORDER.ORR_O02_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_1-ORC>`
     - R
     - ORC
   * - ``ORDER_DETAIL``
     - :ref:`ORR_O02_ORDER_DETAIL <hl7-v2_1-ORR_O02_ORDER_DETAIL>`
     - O
     - ORDER_DETAIL
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_1-NTE>`]
     - O
     - NTE

.. _hl7-v2_1-ORR_O02_ORDER_DETAIL:

ORR_O02_ORDER_DETAIL: HL7 v2 ORR_O02.ORDER_DETAIL group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORR_O02_ORDER_DETAIL.ORR_O02_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``CHOICE``
     - :ref:`ORR_O02_CHOICE <hl7-v2_1-ORR_O02_CHOICE>`
     - R
     - CHOICE

.. _hl7-v2_1-ORR_O02_PATIENT:

ORR_O02_PATIENT: HL7 v2 ORR_O02.PATIENT group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORR_O02_PATIENT.ORR_O02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - O
     - PID
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_1-NTE>`]
     - O
     - NTE
   * - ``ORDER``
     - list[:ref:`ORR_O02_ORDER <hl7-v2_1-ORR_O02_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_1-ORU_R01_OBSERVATION:

ORU_R01_OBSERVATION: HL7 v2 ORU_R01.OBSERVATION group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R01_OBSERVATION.ORU_R01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_1-OBX>`
     - O
     - OBX
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_1-NTE>`]
     - O
     - NTE

.. _hl7-v2_1-ORU_R01_ORDER_OBSERVATION:

ORU_R01_ORDER_OBSERVATION: HL7 v2 ORU_R01.ORDER_OBSERVATION group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R01_ORDER_OBSERVATION.ORU_R01_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_1-ORC>`
     - O
     - ORC
   * - ``OBR``
     - :ref:`OBR <hl7-v2_1-OBR>`
     - R
     - OBR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_1-NTE>`]
     - O
     - NTE
   * - ``OBSERVATION``
     - list[:ref:`ORU_R01_OBSERVATION <hl7-v2_1-ORU_R01_OBSERVATION>`]
     - R
     - OBSERVATION

.. _hl7-v2_1-ORU_R01_PATIENT:

ORU_R01_PATIENT: HL7 v2 ORU_R01.PATIENT group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R01_PATIENT.ORU_R01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - R
     - PID
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_1-NTE>`]
     - O
     - NTE
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - O
     - PV1

.. _hl7-v2_1-ORU_R01_PATIENT_RESULT:

ORU_R01_PATIENT_RESULT: HL7 v2 ORU_R01.PATIENT_RESULT group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT_RESULT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``PATIENT``
     - :ref:`ORU_R01_PATIENT <hl7-v2_1-ORU_R01_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER_OBSERVATION``
     - list[:ref:`ORU_R01_ORDER_OBSERVATION <hl7-v2_1-ORU_R01_ORDER_OBSERVATION>`]
     - R
     - ORDER_OBSERVATION

.. _hl7-v2_1-ORU_R03_OBSERVATION:

ORU_R03_OBSERVATION: HL7 v2 ORU_R03.OBSERVATION group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R03_OBSERVATION.ORU_R03_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_1-OBX>`
     - O
     - OBX
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_1-NTE>`]
     - O
     - NTE

.. _hl7-v2_1-ORU_R03_ORDER_OBSERVATION:

ORU_R03_ORDER_OBSERVATION: HL7 v2 ORU_R03.ORDER_OBSERVATION group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R03_ORDER_OBSERVATION.ORU_R03_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_1-ORC>`
     - O
     - ORC
   * - ``OBR``
     - :ref:`OBR <hl7-v2_1-OBR>`
     - R
     - OBR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_1-NTE>`]
     - O
     - NTE
   * - ``OBSERVATION``
     - list[:ref:`ORU_R03_OBSERVATION <hl7-v2_1-ORU_R03_OBSERVATION>`]
     - R
     - OBSERVATION

.. _hl7-v2_1-ORU_R03_PATIENT:

ORU_R03_PATIENT: HL7 v2 ORU_R03.PATIENT group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R03_PATIENT.ORU_R03_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - R
     - PID
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_1-NTE>`]
     - O
     - NTE
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - O
     - PV1

.. _hl7-v2_1-ORU_R03_PATIENT_RESULT:

ORU_R03_PATIENT_RESULT: HL7 v2 ORU_R03.PATIENT_RESULT group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R03_PATIENT_RESULT.ORU_R03_PATIENT_RESULT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``PATIENT``
     - :ref:`ORU_R03_PATIENT <hl7-v2_1-ORU_R03_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER_OBSERVATION``
     - list[:ref:`ORU_R03_ORDER_OBSERVATION <hl7-v2_1-ORU_R03_ORDER_OBSERVATION>`]
     - R
     - ORDER_OBSERVATION
