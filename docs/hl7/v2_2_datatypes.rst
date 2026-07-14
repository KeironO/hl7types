v2.2 Data Types
===============

.. _hl7-v2_2-AD:

AD Address (S2.4.5.10).
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.AD.AD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ad_1``
     - AD.1
     - Optional[str]
     - optional
     - street address
   * - ``ad_2``
     - AD.2
     - Optional[str]
     - optional
     - other designation
   * - ``ad_3``
     - AD.3
     - Optional[str]
     - optional
     - city
   * - ``ad_4``
     - AD.4
     - Optional[str]
     - optional
     - state or province
   * - ``ad_5``
     - AD.5
     - Optional[str]
     - optional
     - zip or postal code
   * - ``ad_6``
     - AD.6
     - Optional[str]
     - optional
     - country
   * - ``ad_7``
     - AD.7
     - Optional[str]
     - optional
     - type
   * - ``ad_8``
     - AD.8
     - Optional[str]
     - optional
     - other geographic designation

.. _hl7-v2_2-CE:

CE Coded element.
~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CE.CE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ce_1``
     - CE.1
     - Optional[str]
     - optional
     - identifier
   * - ``ce_2``
     - CE.2
     - Optional[str]
     - optional
     - text
   * - ``ce_3``
     - CE.3
     - Optional[str]
     - optional
     - name of coding system
   * - ``ce_4``
     - CE.4
     - Optional[str]
     - optional
     - alternate identifier
   * - ``ce_5``
     - CE.5
     - Optional[str]
     - optional
     - alternate text
   * - ``ce_6``
     - CE.6
     - Optional[str]
     - optional
     - name of alternate coding system

.. _hl7-v2_2-CK_ACCOUNT_NO:

CK_ACCOUNT_NO Abrechnungsnummer.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CK_ACCOUNT_NO.CK_ACCOUNT_NO
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ck_account_no_1``
     - CK_ACCOUNT_NO.1
     - Optional[str]
     - optional
     - account number
   * - ``ck_account_no_2``
     - CK_ACCOUNT_NO.2
     - Optional[str]
     - optional
     - Check digit
   * - ``ck_account_no_3``
     - CK_ACCOUNT_NO.3
     - Optional[str]
     - optional
     - Check digit scheme
   * - ``ck_account_no_4``
     - CK_ACCOUNT_NO.4
     - Optional[str]
     - optional
     - Facility ID

.. _hl7-v2_2-CK_PAT_ID:

CK_PAT_ID Ck für patienten-ids.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CK_PAT_ID.CK_PAT_ID
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ck_pat_id_1``
     - CK_PAT_ID.1
     - Optional[str]
     - optional
     - Patient ID
   * - ``ck_pat_id_2``
     - CK_PAT_ID.2
     - Optional[str]
     - optional
     - Check digit
   * - ``ck_pat_id_3``
     - CK_PAT_ID.3
     - Optional[str]
     - optional
     - Check digit scheme
   * - ``ck_pat_id_4``
     - CK_PAT_ID.4
     - Optional[str]
     - optional
     - Facility ID

.. _hl7-v2_2-CM_ABS_RANGE:

CM_ABS_RANGE Absolute range.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_ABS_RANGE.CM_ABS_RANGE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_abs_range_1``
     - CM_ABS_RANGE.1
     - Optional[str]
     - optional
     - Range
   * - ``cm_abs_range_2``
     - CM_ABS_RANGE.2
     - Optional[str]
     - optional
     - Numeric Change
   * - ``cm_abs_range_3``
     - CM_ABS_RANGE.3
     - Optional[str]
     - optional
     - Percent per Change
   * - ``cm_abs_range_4``
     - CM_ABS_RANGE.4
     - Optional[str]
     - optional
     - Days

.. _hl7-v2_2-CM_AUI:

CM_AUI Authorization information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_AUI.CM_AUI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_aui_1``
     - CM_AUI.1
     - Optional[str]
     - optional
     - authorization number
   * - ``cm_aui_2``
     - CM_AUI.2
     - Optional[str]
     - optional
     - date
   * - ``cm_aui_3``
     - CM_AUI.3
     - Optional[str]
     - optional
     - source

.. _hl7-v2_2-CM_BATCH_TOTAL:

CM_BATCH_TOTAL Cm for batch totals.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_BATCH_TOTAL.CM_BATCH_TOTAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_batch_total_1``
     - CM_BATCH_TOTAL.1
     - Optional[str]
     - optional
     - Batch total 1
   * - ``cm_batch_total_2``
     - CM_BATCH_TOTAL.2
     - Optional[str]
     - optional
     - Batch total 2

.. _hl7-v2_2-CM_CCD:

CM_CCD Charge time.
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_CCD.CM_CCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_ccd_1``
     - CM_CCD.1
     - Optional[str]
     - optional
     - When to Charge
   * - ``cm_ccd_2``
     - CM_CCD.2
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - date/time

.. _hl7-v2_2-CM_DDI:

CM_DDI Daily deductible.
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_DDI.CM_DDI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_ddi_1``
     - CM_DDI.1
     - Optional[str]
     - optional
     - delay days
   * - ``cm_ddi_2``
     - CM_DDI.2
     - Optional[str]
     - optional
     - amount
   * - ``cm_ddi_3``
     - CM_DDI.3
     - Optional[str]
     - optional
     - number of days

.. _hl7-v2_2-CM_DIN:

CM_DIN Activation date.
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_DIN.CM_DIN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_din_1``
     - CM_DIN.1
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - Date
   * - ``cm_din_2``
     - CM_DIN.2
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - institution name

.. _hl7-v2_2-CM_DLD:

CM_DLD Discharge location.
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_DLD.CM_DLD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_dld_1``
     - CM_DLD.1
     - Optional[str]
     - optional
     - discharge location
   * - ``cm_dld_2``
     - CM_DLD.2
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - effective date

.. _hl7-v2_2-CM_DLT:

CM_DLT Delta check.
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_DLT.CM_DLT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_dlt_1``
     - CM_DLT.1
     - Optional[str]
     - optional
     - Range
   * - ``cm_dlt_2``
     - CM_DLT.2
     - Optional[str]
     - optional
     - numeric threshold
   * - ``cm_dlt_3``
     - CM_DLT.3
     - Optional[str]
     - optional
     - change
   * - ``cm_dlt_4``
     - CM_DLT.4
     - Optional[str]
     - optional
     - length of time-days

.. _hl7-v2_2-CM_DTN:

CM_DTN Day type and number.
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_DTN.CM_DTN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_dtn_1``
     - CM_DTN.1
     - Optional[str]
     - optional
     - day type
   * - ``cm_dtn_2``
     - CM_DTN.2
     - Optional[str]
     - optional
     - number of days

.. _hl7-v2_2-CM_EIP:

CM_EIP Parent order.
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_EIP.CM_EIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_eip_1``
     - CM_EIP.1
     - Optional[str]
     - optional
     - parent´s placer order number
   * - ``cm_eip_2``
     - CM_EIP.2
     - Optional[str]
     - optional
     - parent´s filler order number

.. _hl7-v2_2-CM_ELD:

CM_ELD Error.
~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_ELD.CM_ELD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_eld_1``
     - CM_ELD.1
     - Optional[str]
     - optional
     - Segment-ID
   * - ``cm_eld_2``
     - CM_ELD.2
     - Optional[str]
     - optional
     - Sequence
   * - ``cm_eld_3``
     - CM_ELD.3
     - Optional[str]
     - optional
     - Field-Position
   * - ``cm_eld_4``
     - CM_ELD.4
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Code Identifying Error

.. _hl7-v2_2-CM_FILLER:

CM_FILLER Bearbeitungsnummer der leistungsstelle.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_FILLER.CM_FILLER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_filler_1``
     - CM_FILLER.1
     - Optional[str]
     - optional
     - unique filler id
   * - ``cm_filler_2``
     - CM_FILLER.2
     - Optional[str]
     - optional
     - filler application ID

.. _hl7-v2_2-CM_FINANCE:

CM_FINANCE Cm für finanzen.
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_FINANCE.CM_FINANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_finance_1``
     - CM_FINANCE.1
     - Optional[str]
     - optional
     - financial class ID
   * - ``cm_finance_2``
     - CM_FINANCE.2
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - effective date

.. _hl7-v2_2-CM_GROUP_ID:

CM_GROUP_ID Auftragsgruppennummer.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_GROUP_ID.CM_GROUP_ID
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_group_id_1``
     - CM_GROUP_ID.1
     - Optional[str]
     - optional
     - unique group id
   * - ``cm_group_id_2``
     - CM_GROUP_ID.2
     - Optional[str]
     - optional
     - placer application id

.. _hl7-v2_2-CM_INTERNAL_LOCATION:

CM_INTERNAL_LOCATION Cm für ortsangaben im krankenhaus.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_INTERNAL_LOCATION.CM_INTERNAL_LOCATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_internal_location_1``
     - CM_INTERNAL_LOCATION.1
     - Optional[str]
     - optional
     - nurse unit (Station)
   * - ``cm_internal_location_2``
     - CM_INTERNAL_LOCATION.2
     - Optional[str]
     - optional
     - Room
   * - ``cm_internal_location_3``
     - CM_INTERNAL_LOCATION.3
     - Optional[str]
     - optional
     - Bed
   * - ``cm_internal_location_4``
     - CM_INTERNAL_LOCATION.4
     - Optional[str]
     - optional
     - Facility ID
   * - ``cm_internal_location_5``
     - CM_INTERNAL_LOCATION.5
     - Optional[str]
     - optional
     - Bed Status
   * - ``cm_internal_location_6``
     - CM_INTERNAL_LOCATION.6
     - Optional[str]
     - optional
     - Etage
   * - ``cm_internal_location_7``
     - CM_INTERNAL_LOCATION.7
     - Optional[str]
     - optional
     - Klinik
   * - ``cm_internal_location_8``
     - CM_INTERNAL_LOCATION.8
     - Optional[str]
     - optional
     - Zentrum

.. _hl7-v2_2-CM_JOB_CODE:

CM_JOB_CODE Berufsbezeichnung.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_JOB_CODE.CM_JOB_CODE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_job_code_1``
     - CM_JOB_CODE.1
     - Optional[str]
     - optional
     - job code
   * - ``cm_job_code_2``
     - CM_JOB_CODE.2
     - Optional[str]
     - optional
     - employee classification

.. _hl7-v2_2-CM_LA1:

CM_LA1 Location with address information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_LA1.CM_LA1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_la1_1``
     - CM_LA1.1
     - Optional[str]
     - optional
     - Dispense / Deliver to Location
   * - ``cm_la1_2``
     - CM_LA1.2
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     - location

.. _hl7-v2_2-CM_LICENSE_NO:

CM_LICENSE_NO Cm für führerscheinlizenzen.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_LICENSE_NO.CM_LICENSE_NO
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_license_no_1``
     - CM_LICENSE_NO.1
     - Optional[str]
     - optional
     - License Number
   * - ``cm_license_no_2``
     - CM_LICENSE_NO.2
     - Optional[str]
     - optional
     - issuing state,province,country

.. _hl7-v2_2-CM_MOC:

CM_MOC Charge to practise.
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_MOC.CM_MOC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_moc_1``
     - CM_MOC.1
     - Optional[str]
     - optional
     - dollar amount
   * - ``cm_moc_2``
     - CM_MOC.2
     - Optional[str]
     - optional
     - charge code

.. _hl7-v2_2-CM_MSG:

CM_MSG Message type.
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_MSG.CM_MSG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_msg_1``
     - CM_MSG.1
     - Optional[str]
     - optional
     - message type
   * - ``cm_msg_2``
     - CM_MSG.2
     - Optional[str]
     - optional
     - Trigger Event

.. _hl7-v2_2-CM_NDL:

CM_NDL Observing practitioner.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_NDL.CM_NDL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_ndl_1``
     - CM_NDL.1
     - Optional[str]
     - optional
     - interpreter / technician
   * - ``cm_ndl_2``
     - CM_NDL.2
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - start date/time
   * - ``cm_ndl_3``
     - CM_NDL.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - end date/time
   * - ``cm_ndl_4``
     - CM_NDL.4
     - Optional[str]
     - optional
     - location

.. _hl7-v2_2-CM_OCD:

CM_OCD Occurence.
~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_OCD.CM_OCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_ocd_1``
     - CM_OCD.1
     - Optional[str]
     - optional
     - occurrence code
   * - ``cm_ocd_2``
     - CM_OCD.2
     - Optional[str]
     - optional
     - occurrence date

.. _hl7-v2_2-CM_OSP:

CM_OSP Occurence span.
~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_OSP.CM_OSP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_osp_1``
     - CM_OSP.1
     - Optional[str]
     - optional
     - occurrence span code
   * - ``cm_osp_2``
     - CM_OSP.2
     - Optional[str]
     - optional
     - occurrence span start date
   * - ``cm_osp_3``
     - CM_OSP.3
     - Optional[str]
     - optional
     - occurrence span stop date

.. _hl7-v2_2-CM_PAT_ID:

CM_PAT_ID Patient id.
~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_PAT_ID.CM_PAT_ID
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_pat_id_1``
     - CM_PAT_ID.1
     - Optional[str]
     - optional
     - Patient ID
   * - ``cm_pat_id_2``
     - CM_PAT_ID.2
     - Optional[str]
     - optional
     - Check digit
   * - ``cm_pat_id_3``
     - CM_PAT_ID.3
     - Optional[str]
     - optional
     - Check digit scheme
   * - ``cm_pat_id_4``
     - CM_PAT_ID.4
     - Optional[str]
     - optional
     - Facility ID
   * - ``cm_pat_id_5``
     - CM_PAT_ID.5
     - Optional[str]
     - optional
     - type

.. _hl7-v2_2-CM_PAT_ID_0192:

CM_PAT_ID_0192 Patient id with table 0192.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_PAT_ID_0192.CM_PAT_ID_0192
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_pat_id_0192_1``
     - CM_PAT_ID_0192.1
     - Optional[str]
     - optional
     - Patient ID
   * - ``cm_pat_id_0192_2``
     - CM_PAT_ID_0192.2
     - Optional[str]
     - optional
     - Check digit
   * - ``cm_pat_id_0192_3``
     - CM_PAT_ID_0192.3
     - Optional[str]
     - optional
     - Check digit scheme
   * - ``cm_pat_id_0192_4``
     - CM_PAT_ID_0192.4
     - Optional[str]
     - optional
     - Facility ID
   * - ``cm_pat_id_0192_5``
     - CM_PAT_ID_0192.5
     - Optional[str]
     - optional
     - type

.. _hl7-v2_2-CM_PCF:

CM_PCF Pre-certification required.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_PCF.CM_PCF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_pcf_1``
     - CM_PCF.1
     - Optional[str]
     - optional
     - pre-certification patient type
   * - ``cm_pcf_2``
     - CM_PCF.2
     - Optional[str]
     - optional
     - pre-certication required
   * - ``cm_pcf_3``
     - CM_PCF.3
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - pre-certification window

.. _hl7-v2_2-CM_PEN:

CM_PEN Penalty.
~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_PEN.CM_PEN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_pen_1``
     - CM_PEN.1
     - Optional[str]
     - optional
     - Penalty ID
   * - ``cm_pen_2``
     - CM_PEN.2
     - Optional[str]
     - optional
     - penalty amount

.. _hl7-v2_2-CM_PIP:

CM_PIP Privileges.
~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_PIP.CM_PIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_pip_1``
     - CM_PIP.1
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Privilege
   * - ``cm_pip_2``
     - CM_PIP.2
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - privilege class
   * - ``cm_pip_3``
     - CM_PIP.3
     - Optional[str]
     - optional
     - expiration date
   * - ``cm_pip_4``
     - CM_PIP.4
     - Optional[str]
     - optional
     - activation date

.. _hl7-v2_2-CM_PLACER:

CM_PLACER Auftragsnummer des auftraggebers / der auftraggebenden stelle.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_PLACER.CM_PLACER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_placer_1``
     - CM_PLACER.1
     - Optional[str]
     - optional
     - unique placer id
   * - ``cm_placer_2``
     - CM_PLACER.2
     - Optional[str]
     - optional
     - placer application

.. _hl7-v2_2-CM_PLN:

CM_PLN Practitioner id numbers.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_PLN.CM_PLN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_pln_1``
     - CM_PLN.1
     - Optional[str]
     - optional
     - ID number
   * - ``cm_pln_2``
     - CM_PLN.2
     - Optional[str]
     - optional
     - type of ID number (ID)
   * - ``cm_pln_3``
     - CM_PLN.3
     - Optional[str]
     - optional
     - state/other qualifiying info

.. _hl7-v2_2-CM_POSITION:

CM_POSITION Sitzplatz bzw. saal / tisch / stuhl.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_POSITION.CM_POSITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_position_1``
     - CM_POSITION.1
     - Optional[str]
     - optional
     - Saal
   * - ``cm_position_2``
     - CM_POSITION.2
     - Optional[str]
     - optional
     - Tisch
   * - ``cm_position_3``
     - CM_POSITION.3
     - Optional[str]
     - optional
     - Stuhl

.. _hl7-v2_2-CM_PRACTITIONER:

CM_PRACTITIONER Maßnahme durchgeführt von.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_PRACTITIONER.CM_PRACTITIONER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_practitioner_1``
     - CM_PRACTITIONER.1
     - Optional[str]
     - optional
     - Procedure Practitioner  ID
   * - ``cm_practitioner_2``
     - CM_PRACTITIONER.2
     - Optional[str]
     - optional
     - procedure practitioner type

.. _hl7-v2_2-CM_PTA:

CM_PTA Policy type.
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_PTA.CM_PTA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_pta_1``
     - CM_PTA.1
     - Optional[str]
     - optional
     - policy type
   * - ``cm_pta_2``
     - CM_PTA.2
     - Optional[str]
     - optional
     - amount class
   * - ``cm_pta_3``
     - CM_PTA.3
     - Optional[str]
     - optional
     - amount

.. _hl7-v2_2-CM_RANGE:

CM_RANGE Wertebereich.
~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_RANGE.CM_RANGE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_range_1``
     - CM_RANGE.1
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Low Value
   * - ``cm_range_2``
     - CM_RANGE.2
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - High Value

.. _hl7-v2_2-CM_RFR:

CM_RFR Reference range.
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_RFR.CM_RFR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_rfr_1``
     - CM_RFR.1
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Reference Range
   * - ``cm_rfr_2``
     - CM_RFR.2
     - Optional[str]
     - optional
     - Sex
   * - ``cm_rfr_3``
     - CM_RFR.3
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Age Range
   * - ``cm_rfr_4``
     - CM_RFR.4
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Gestational Age Range
   * - ``cm_rfr_5``
     - CM_RFR.5
     - Optional[str]
     - optional
     - Species
   * - ``cm_rfr_6``
     - CM_RFR.6
     - Optional[str]
     - optional
     - Race / Subspecies
   * - ``cm_rfr_7``
     - CM_RFR.7
     - Optional[str]
     - optional
     - Text Condition

.. _hl7-v2_2-CM_RI:

CM_RI Interval.
~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_RI.CM_RI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_ri_1``
     - CM_RI.1
     - Optional[str]
     - optional
     - repeat pattern
   * - ``cm_ri_2``
     - CM_RI.2
     - Optional[str]
     - optional
     - explicit time intevall

.. _hl7-v2_2-CM_RMC:

CM_RMC Room coverage.
~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_RMC.CM_RMC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_rmc_1``
     - CM_RMC.1
     - Optional[str]
     - optional
     - room type
   * - ``cm_rmc_2``
     - CM_RMC.2
     - Optional[str]
     - optional
     - amount type
   * - ``cm_rmc_3``
     - CM_RMC.3
     - Optional[str]
     - optional
     - coverage amount

.. _hl7-v2_2-CM_SPD:

CM_SPD Specialty.
~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_SPD.CM_SPD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_spd_1``
     - CM_SPD.1
     - Optional[str]
     - optional
     - specialty name
   * - ``cm_spd_2``
     - CM_SPD.2
     - Optional[str]
     - optional
     - governing board
   * - ``cm_spd_3``
     - CM_SPD.3
     - Optional[str]
     - optional
     - eligible or certified
   * - ``cm_spd_4``
     - CM_SPD.4
     - Optional[str]
     - optional
     - date of certification

.. _hl7-v2_2-CM_SPS:

CM_SPS Specimen source.
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_SPS.CM_SPS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_sps_1``
     - CM_SPS.1
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - Specimen source name or code
   * - ``cm_sps_2``
     - CM_SPS.2
     - Optional[str]
     - optional
     - additives
   * - ``cm_sps_3``
     - CM_SPS.3
     - Optional[str]
     - optional
     - freetext
   * - ``cm_sps_4``
     - CM_SPS.4
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - body site
   * - ``cm_sps_5``
     - CM_SPS.5
     - Optional[:ref:`CE <hl7-v2_2-CE>`]
     - optional
     - site modifier

.. _hl7-v2_2-CM_UVC:

CM_UVC Value code and amount.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_UVC.CM_UVC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_uvc_1``
     - CM_UVC.1
     - Optional[str]
     - optional
     - Value code
   * - ``cm_uvc_2``
     - CM_UVC.2
     - Optional[str]
     - optional
     - value amount

.. _hl7-v2_2-CM_VR:

CM_VR Value qualifier.
~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CM_VR.CM_VR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cm_vr_1``
     - CM_VR.1
     - Optional[str]
     - optional
     - First data code value
   * - ``cm_vr_2``
     - CM_VR.2
     - Optional[str]
     - optional
     - Last data code calue

.. _hl7-v2_2-CN_PERSON:

CN_PERSON Cn für personen.
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CN_PERSON.CN_PERSON
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cn_person_1``
     - CN_PERSON.1
     - Optional[str]
     - optional
     - ID number
   * - ``cn_person_2``
     - CN_PERSON.2
     - Optional[str]
     - optional
     - familiy name
   * - ``cn_person_3``
     - CN_PERSON.3
     - Optional[str]
     - optional
     - given name
   * - ``cn_person_4``
     - CN_PERSON.4
     - Optional[str]
     - optional
     - middle initial or name
   * - ``cn_person_5``
     - CN_PERSON.5
     - Optional[str]
     - optional
     - suffix (e.g. JR or III)
   * - ``cn_person_6``
     - CN_PERSON.6
     - Optional[str]
     - optional
     - prefix (e.g. DR)
   * - ``cn_person_7``
     - CN_PERSON.7
     - Optional[str]
     - optional
     - degree (e.g. MD)
   * - ``cn_person_8``
     - CN_PERSON.8
     - Optional[str]
     - optional
     - source table id

.. _hl7-v2_2-CN_PHYSICIAN:

CN_PHYSICIAN Cn für ärzte.
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CN_PHYSICIAN.CN_PHYSICIAN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cn_physician_1``
     - CN_PHYSICIAN.1
     - Optional[str]
     - optional
     - physician ID
   * - ``cn_physician_2``
     - CN_PHYSICIAN.2
     - Optional[str]
     - optional
     - familiy name
   * - ``cn_physician_3``
     - CN_PHYSICIAN.3
     - Optional[str]
     - optional
     - given name
   * - ``cn_physician_4``
     - CN_PHYSICIAN.4
     - Optional[str]
     - optional
     - middle initial or name
   * - ``cn_physician_5``
     - CN_PHYSICIAN.5
     - Optional[str]
     - optional
     - suffix (e.g. JR or III)
   * - ``cn_physician_6``
     - CN_PHYSICIAN.6
     - Optional[str]
     - optional
     - prefix (e.g. DR)
   * - ``cn_physician_7``
     - CN_PHYSICIAN.7
     - Optional[str]
     - optional
     - degree (e.g. MD)
   * - ``cn_physician_8``
     - CN_PHYSICIAN.8
     - Optional[str]
     - optional
     - source table id
   * - ``cn_physician_9``
     - CN_PHYSICIAN.9
     - Optional[:ref:`AD <hl7-v2_2-AD>`]
     - optional
     - Adresse
   * - ``cn_physician_10``
     - CN_PHYSICIAN.10
     - Optional[str]
     - optional
     - Telefon
   * - ``cn_physician_11``
     - CN_PHYSICIAN.11
     - Optional[str]
     - optional
     - Faxnummer
   * - ``cn_physician_12``
     - CN_PHYSICIAN.12
     - Optional[str]
     - optional
     - Online-Nummer
   * - ``cn_physician_13``
     - CN_PHYSICIAN.13
     - Optional[str]
     - optional
     - E-Mail

.. _hl7-v2_2-CQ_QUANTITY:

CQ_QUANTITY Cq für mengenangaben.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.CQ_QUANTITY.CQ_QUANTITY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cq_quantity_1``
     - CQ_QUANTITY.1
     - Optional[str]
     - optional
     - quantity
   * - ``cq_quantity_2``
     - CQ_QUANTITY.2
     - Optional[str]
     - optional
     - units

.. _hl7-v2_2-PN:

PN Person name (S2.4.5.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.PN.PN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pn_1``
     - PN.1
     - Optional[str]
     - optional
     - familiy name
   * - ``pn_2``
     - PN.2
     - Optional[str]
     - optional
     - given name
   * - ``pn_3``
     - PN.3
     - Optional[str]
     - optional
     - middle initial or name
   * - ``pn_4``
     - PN.4
     - Optional[str]
     - optional
     - suffix (e.g. JR or III)
   * - ``pn_5``
     - PN.5
     - Optional[str]
     - optional
     - prefix (e.g. DR)
   * - ``pn_6``
     - PN.6
     - Optional[str]
     - optional
     - degree (e.g. MD)

.. _hl7-v2_2-TQ:

TQ Timing quantity (S2.4.5.20).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.TQ.TQ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``tq_1``
     - TQ.1
     - Optional[str]
     - optional
     - Quantity
   * - ``tq_2``
     - TQ.2
     - Optional[str]
     - optional
     - interval
   * - ``tq_3``
     - TQ.3
     - Optional[str]
     - optional
     - duration
   * - ``tq_4``
     - TQ.4
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - start date/time
   * - ``tq_5``
     - TQ.5
     - Optional[:ref:`TS <hl7-v2_2-TS>`]
     - optional
     - end date/time
   * - ``tq_6``
     - TQ.6
     - Optional[str]
     - optional
     - priority
   * - ``tq_7``
     - TQ.7
     - Optional[str]
     - optional
     - condition
   * - ``tq_8``
     - TQ.8
     - Optional[str]
     - optional
     - text (TX)
   * - ``tq_9``
     - TQ.9
     - Optional[str]
     - optional
     - conjunction
   * - ``tq_10``
     - TQ.10
     - Optional[str]
     - optional
     - order sequencing

.. _hl7-v2_2-TS:

TS Time stamp (S2.4.5.7).
~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.datatypes.TS.TS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ts_1``
     - TS.1
     - Optional[str]
     - optional
     - time of an event
   * - ``ts_2``
     - TS.2
     - Optional[str]
     - optional
     - degree of precision
