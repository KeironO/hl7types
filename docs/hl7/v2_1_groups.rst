v2.1 Groups
===========

.. _hl7-v2_1-ADR_A19_QUERY_RESPONSE:

ADR_A19_QUERY_RESPONSE HL7 v2 ADR_A19.QUERY_RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ADR_A19_QUERY_RESPONSE.ADR_A19_QUERY_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``EVN``
     - Optional[:ref:`EVN <hl7-v2_1-EVN>`]
     - optional
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT

.. _hl7-v2_1-ADT_A17_PATIENT:

ADT_A17_PATIENT HL7 v2 ADT_A17.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ADT_A17_PATIENT.ADT_A17_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_1-PV1>`
     - required
     - PATIENT VISIT

.. _hl7-v2_1-BAR_P01_VISIT:

BAR_P01_VISIT HL7 v2 BAR_P01.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.BAR_P01_VISIT.BAR_P01_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     - PATIENT VISIT
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_1-DG1>`]]
     - optional
     - DIAGNOSIS
   * - ``PR1``
     - Optional[List[:ref:`PR1 <hl7-v2_1-PR1>`]]
     - optional
     - PROCEDURES
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_1-GT1>`]]
     - optional
     - GUARANTOR
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_1-NK1>`]]
     - optional
     - NEXT OF KIN
   * - ``IN1``
     - Optional[List[:ref:`IN1 <hl7-v2_1-IN1>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_1-ACC>`]
     - optional
     - ACCIDENT
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_1-UB1>`]
     - optional
     - UB82 DATA

.. _hl7-v2_1-BAR_P02_PATIENT:

BAR_P02_PATIENT HL7 v2 BAR_P02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.BAR_P02_PATIENT.BAR_P02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     - PATIENT VISIT

.. _hl7-v2_1-ORM_O01_CHOICE:

ORM_O01_CHOICE HL7 v2 ORM_O01.CHOICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORM_O01_CHOICE.ORM_O01_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_1-OBR>`]
     - optional
     - OBSERVATION REQUEST
   * - ``ORO``
     - Optional[:ref:`ORO <hl7-v2_1-ORO>`]
     - optional
     - ORDER OTHER
   * - ``RX1``
     - Optional[:ref:`RX1 <hl7-v2_1-RX1>`]
     - optional
     - PHARMACY ORDER

.. _hl7-v2_1-ORM_O01_ORDER:

ORM_O01_ORDER HL7 v2 ORM_O01.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORM_O01_ORDER.ORM_O01_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_1-ORC>`
     - required
     - COMMON ORDER
   * - ``ORDER_DETAIL``
     - Optional[:ref:`ORM_O01_ORDER_DETAIL <hl7-v2_1-ORM_O01_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``BLG``
     - Optional[:ref:`BLG <hl7-v2_1-BLG>`]
     - optional
     - BILLING

.. _hl7-v2_1-ORM_O01_ORDER_DETAIL:

ORM_O01_ORDER_DETAIL HL7 v2 ORM_O01.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CHOICE``
     - :ref:`ORM_O01_CHOICE <hl7-v2_1-ORM_O01_CHOICE>`
     - required
     - CHOICE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NOTES AND COMMENTS
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_1-OBX>`]]
     - optional
     - RESULT

.. _hl7-v2_1-ORM_O01_PATIENT:

ORM_O01_PATIENT HL7 v2 ORM_O01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORM_O01_PATIENT.ORM_O01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NOTES AND COMMENTS
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     - PATIENT VISIT

.. _hl7-v2_1-ORR_O02_CHOICE:

ORR_O02_CHOICE HL7 v2 ORR_O02.CHOICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORR_O02_CHOICE.ORR_O02_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_1-OBR>`]
     - optional
     - OBSERVATION REQUEST
   * - ``ORO``
     - Optional[:ref:`ORO <hl7-v2_1-ORO>`]
     - optional
     - ORDER OTHER
   * - ``RX1``
     - Optional[:ref:`RX1 <hl7-v2_1-RX1>`]
     - optional
     - PHARMACY ORDER

.. _hl7-v2_1-ORR_O02_ORDER:

ORR_O02_ORDER HL7 v2 ORR_O02.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORR_O02_ORDER.ORR_O02_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_1-ORC>`
     - required
     - COMMON ORDER
   * - ``ORDER_DETAIL``
     - Optional[:ref:`ORR_O02_ORDER_DETAIL <hl7-v2_1-ORR_O02_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NOTES AND COMMENTS

.. _hl7-v2_1-ORR_O02_ORDER_DETAIL:

ORR_O02_ORDER_DETAIL HL7 v2 ORR_O02.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORR_O02_ORDER_DETAIL.ORR_O02_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CHOICE``
     - :ref:`ORR_O02_CHOICE <hl7-v2_1-ORR_O02_CHOICE>`
     - required
     - CHOICE

.. _hl7-v2_1-ORR_O02_PATIENT:

ORR_O02_PATIENT HL7 v2 ORR_O02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORR_O02_PATIENT.ORR_O02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - Optional[:ref:`PID <hl7-v2_1-PID>`]
     - optional
     - PATIENT IDENTIFICATION
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NOTES AND COMMENTS
   * - ``ORDER``
     - List[:ref:`ORR_O02_ORDER <hl7-v2_1-ORR_O02_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_1-ORU_R01_OBSERVATION:

ORU_R01_OBSERVATION HL7 v2 ORU_R01.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R01_OBSERVATION.ORU_R01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_1-OBX>`]
     - optional
     - RESULT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NOTES AND COMMENTS

.. _hl7-v2_1-ORU_R01_ORDER_OBSERVATION:

ORU_R01_ORDER_OBSERVATION HL7 v2 ORU_R01.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R01_ORDER_OBSERVATION.ORU_R01_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_1-ORC>`]
     - optional
     - COMMON ORDER
   * - ``OBR``
     - :ref:`OBR <hl7-v2_1-OBR>`
     - required
     - OBSERVATION REQUEST
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NOTES AND COMMENTS
   * - ``OBSERVATION``
     - List[:ref:`ORU_R01_OBSERVATION <hl7-v2_1-ORU_R01_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_1-ORU_R01_PATIENT:

ORU_R01_PATIENT HL7 v2 ORU_R01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R01_PATIENT.ORU_R01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NOTES AND COMMENTS
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     - PATIENT VISIT

.. _hl7-v2_1-ORU_R01_PATIENT_RESULT:

ORU_R01_PATIENT_RESULT HL7 v2 ORU_R01.PATIENT_RESULT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT_RESULT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORU_R01_PATIENT <hl7-v2_1-ORU_R01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER_OBSERVATION``
     - List[:ref:`ORU_R01_ORDER_OBSERVATION <hl7-v2_1-ORU_R01_ORDER_OBSERVATION>`]
     - required
     - ORDER_OBSERVATION

.. _hl7-v2_1-ORU_R03_OBSERVATION:

ORU_R03_OBSERVATION HL7 v2 ORU_R03.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R03_OBSERVATION.ORU_R03_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_1-OBX>`]
     - optional
     - RESULT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NOTES AND COMMENTS

.. _hl7-v2_1-ORU_R03_ORDER_OBSERVATION:

ORU_R03_ORDER_OBSERVATION HL7 v2 ORU_R03.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R03_ORDER_OBSERVATION.ORU_R03_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_1-ORC>`]
     - optional
     - COMMON ORDER
   * - ``OBR``
     - :ref:`OBR <hl7-v2_1-OBR>`
     - required
     - OBSERVATION REQUEST
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NOTES AND COMMENTS
   * - ``OBSERVATION``
     - List[:ref:`ORU_R03_OBSERVATION <hl7-v2_1-ORU_R03_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_1-ORU_R03_PATIENT:

ORU_R03_PATIENT HL7 v2 ORU_R03.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R03_PATIENT.ORU_R03_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_1-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_1-NTE>`]]
     - optional
     - NOTES AND COMMENTS
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_1-PV1>`]
     - optional
     - PATIENT VISIT

.. _hl7-v2_1-ORU_R03_PATIENT_RESULT:

ORU_R03_PATIENT_RESULT HL7 v2 ORU_R03.PATIENT_RESULT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_1.groups.ORU_R03_PATIENT_RESULT.ORU_R03_PATIENT_RESULT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORU_R03_PATIENT <hl7-v2_1-ORU_R03_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER_OBSERVATION``
     - List[:ref:`ORU_R03_ORDER_OBSERVATION <hl7-v2_1-ORU_R03_ORDER_OBSERVATION>`]
     - required
     - ORDER_OBSERVATION
