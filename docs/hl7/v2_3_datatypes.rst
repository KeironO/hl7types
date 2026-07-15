v2.3 Data Types
===============

.. _hl7-v2_3-AD:

AD: Address
~~~~~~~~~~~

Section 2.8.1

.. py:class:: hl7types.hl7.v2_3.datatypes.AD.AD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ad_1``
     - AD.1
     - str
     - O
     - street address
   * - ``ad_2``
     - AD.2
     - str
     - O
     - other designation
   * - ``ad_3``
     - AD.3
     - str
     - O
     - city
   * - ``ad_4``
     - AD.4
     - str
     - O
     - state or province
   * - ``ad_5``
     - AD.5
     - str
     - O
     - zip or postal code
   * - ``ad_6``
     - AD.6
     - str
     - O
     - country
   * - ``ad_7``
     - AD.7
     - str
     - O
     - address type
   * - ``ad_8``
     - AD.8
     - str
     - O
     - other geographic designation

.. _hl7-v2_3-CD:

CD: Channel definition
~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.2

.. py:class:: hl7types.hl7.v2_3.datatypes.CD.CD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cd_1``
     - CD.1
     - str
     - O
     - channel identifier
   * - ``cd_2``
     - CD.2
     - str
     - O
     - electrode names
   * - ``cd_3``
     - CD.3
     - str
     - O
     - channel sensitivity/units
   * - ``cd_4``
     - CD.4
     - str
     - O
     - calibration parameters
   * - ``cd_5``
     - CD.5
     - str
     - O
     - sampling frequency
   * - ``cd_6``
     - CD.6
     - str
     - O
     - minimum/maximum data values

.. _hl7-v2_3-CE:

CE: Coded element
~~~~~~~~~~~~~~~~~

Section 2.8.3

.. py:class:: hl7types.hl7.v2_3.datatypes.CE.CE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ce_1``
     - CE.1
     - str
     - O
     - identifier
   * - ``ce_2``
     - CE.2
     - str
     - O
     - text
   * - ``ce_3``
     - CE.3
     - str
     - O
     - name of coding system
   * - ``ce_4``
     - CE.4
     - str
     - O
     - alternate identifier
   * - ``ce_5``
     - CE.5
     - str
     - O
     - alternate text
   * - ``ce_6``
     - CE.6
     - str
     - O
     - name of alternate coding system

.. _hl7-v2_3-CF:

CF: Coded element with formatted values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.4

.. py:class:: hl7types.hl7.v2_3.datatypes.CF.CF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cf_1``
     - CF.1
     - str
     - O
     - identifier
   * - ``cf_2``
     - CF.2
     - str
     - O
     - formatted text
   * - ``cf_3``
     - CF.3
     - str
     - O
     - name of coding system
   * - ``cf_4``
     - CF.4
     - str
     - O
     - alternate identifier
   * - ``cf_5``
     - CF.5
     - str
     - O
     - alternate formatted text
   * - ``cf_6``
     - CF.6
     - str
     - O
     - name of alternate coding system

.. _hl7-v2_3-CK:

CK: Composite id with check digit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.5

.. py:class:: hl7types.hl7.v2_3.datatypes.CK.CK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ck_1``
     - CK.1
     - str
     - O
     - ID number (NM)
   * - ``ck_2``
     - CK.2
     - str
     - O
     - check digit
   * - ``ck_3``
     - CK.3
     - str
     - O
     - code identifying the check digit scheme employed
   * - ``ck_4``
     - CK.4
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - assigning authority

.. _hl7-v2_3-CM_ABS_RANGE:

CM_ABS_RANGE: Absolute range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_ABS_RANGE.CM_ABS_RANGE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_abs_range_1``
     - CM_ABS_RANGE.1
     - str
     - O
     - Range
   * - ``cm_abs_range_2``
     - CM_ABS_RANGE.2
     - str
     - O
     - Numeric Change
   * - ``cm_abs_range_3``
     - CM_ABS_RANGE.3
     - str
     - O
     - Percent per Change
   * - ``cm_abs_range_4``
     - CM_ABS_RANGE.4
     - str
     - O
     - Days

.. _hl7-v2_3-CM_AUI:

CM_AUI: Authorization information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_AUI.CM_AUI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_aui_1``
     - CM_AUI.1
     - str
     - O
     - authorization number
   * - ``cm_aui_2``
     - CM_AUI.2
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     - date
   * - ``cm_aui_3``
     - CM_AUI.3
     - str
     - O
     - source

.. _hl7-v2_3-CM_CCD:

CM_CCD: Charge time
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_CCD.CM_CCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_ccd_1``
     - CM_CCD.1
     - str
     - O
     - when to charge code
   * - ``cm_ccd_2``
     - CM_CCD.2
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     - date/time

.. _hl7-v2_3-CM_DDI:

CM_DDI: Daily deductible
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_DDI.CM_DDI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_ddi_1``
     - CM_DDI.1
     - str
     - O
     - delay days
   * - ``cm_ddi_2``
     - CM_DDI.2
     - str
     - O
     - amount
   * - ``cm_ddi_3``
     - CM_DDI.3
     - str
     - O
     - number of days

.. _hl7-v2_3-CM_DIN:

CM_DIN: Activation date
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_DIN.CM_DIN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_din_1``
     - CM_DIN.1
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     - date
   * - ``cm_din_2``
     - CM_DIN.2
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - institution name

.. _hl7-v2_3-CM_DLD:

CM_DLD: Discharge location
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_DLD.CM_DLD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_dld_1``
     - CM_DLD.1
     - str
     - O
     - discharge location
   * - ``cm_dld_2``
     - CM_DLD.2
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     - effective date

.. _hl7-v2_3-CM_DLT:

CM_DLT: Delta check
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_DLT.CM_DLT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_dlt_1``
     - CM_DLT.1
     - str
     - O
     - Range
   * - ``cm_dlt_2``
     - CM_DLT.2
     - str
     - O
     - numeric threshold
   * - ``cm_dlt_3``
     - CM_DLT.3
     - str
     - O
     - change
   * - ``cm_dlt_4``
     - CM_DLT.4
     - str
     - O
     - length of time-days

.. _hl7-v2_3-CM_DTN:

CM_DTN: Day type and number
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_DTN.CM_DTN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_dtn_1``
     - CM_DTN.1
     - str
     - O
     - day type
   * - ``cm_dtn_2``
     - CM_DTN.2
     - str
     - O
     - number of days

.. _hl7-v2_3-CM_EIP:

CM_EIP: Parent order
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_EIP.CM_EIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_eip_1``
     - CM_EIP.1
     - :ref:`EI <hl7-v2_3-EI>`
     - O
     - parent´s placer order number
   * - ``cm_eip_2``
     - CM_EIP.2
     - :ref:`EI <hl7-v2_3-EI>`
     - O
     - parent´s filler order number

.. _hl7-v2_3-CM_ELD:

CM_ELD: Error
~~~~~~~~~~~~~

Section 2

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_ELD.CM_ELD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_eld_1``
     - CM_ELD.1
     - str
     - O
     - segment ID
   * - ``cm_eld_2``
     - CM_ELD.2
     - str
     - O
     - sequence
   * - ``cm_eld_3``
     - CM_ELD.3
     - str
     - O
     - field position
   * - ``cm_eld_4``
     - CM_ELD.4
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - code identifying error

.. _hl7-v2_3-CM_LA1:

CM_LA1: Location with address information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_LA1.CM_LA1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_la1_1``
     - CM_LA1.1
     - str
     - O
     - point of care (ST)
   * - ``cm_la1_2``
     - CM_LA1.2
     - str
     - O
     - room
   * - ``cm_la1_3``
     - CM_LA1.3
     - str
     - O
     - bed
   * - ``cm_la1_4``
     - CM_LA1.4
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - facility (HD)
   * - ``cm_la1_5``
     - CM_LA1.5
     - str
     - O
     - location status
   * - ``cm_la1_6``
     - CM_LA1.6
     - str
     - O
     - person location type
   * - ``cm_la1_7``
     - CM_LA1.7
     - str
     - O
     - building
   * - ``cm_la1_8``
     - CM_LA1.8
     - str
     - O
     - floor
   * - ``cm_la1_9``
     - CM_LA1.9
     - str
     - O
     - street address
   * - ``cm_la1_10``
     - CM_LA1.10
     - str
     - O
     - other designation
   * - ``cm_la1_11``
     - CM_LA1.11
     - str
     - O
     - city
   * - ``cm_la1_12``
     - CM_LA1.12
     - str
     - O
     - state or province
   * - ``cm_la1_13``
     - CM_LA1.13
     - str
     - O
     - zip or postal code
   * - ``cm_la1_14``
     - CM_LA1.14
     - str
     - O
     - country
   * - ``cm_la1_15``
     - CM_LA1.15
     - str
     - O
     - address type
   * - ``cm_la1_16``
     - CM_LA1.16
     - str
     - O
     - other geographic designation

.. _hl7-v2_3-CM_MOC:

CM_MOC: Charge to practise
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_MOC.CM_MOC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_moc_1``
     - CM_MOC.1
     - :ref:`MO <hl7-v2_3-MO>`
     - O
     - dollar amount
   * - ``cm_moc_2``
     - CM_MOC.2
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - charge code

.. _hl7-v2_3-CM_MSG:

CM_MSG: Message type
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_MSG.CM_MSG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_msg_1``
     - CM_MSG.1
     - str
     - O
     - message type
   * - ``cm_msg_2``
     - CM_MSG.2
     - str
     - O
     - trigger event

.. _hl7-v2_3-CM_NDL:

CM_NDL: Observing practitioner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_NDL.CM_NDL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_ndl_1``
     - CM_NDL.1
     - :ref:`CN <hl7-v2_3-CN>`
     - O
     - name
   * - ``cm_ndl_2``
     - CM_NDL.2
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     - start date/time
   * - ``cm_ndl_3``
     - CM_NDL.3
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     - end date/time
   * - ``cm_ndl_4``
     - CM_NDL.4
     - str
     - O
     - point of care (IS)
   * - ``cm_ndl_5``
     - CM_NDL.5
     - str
     - O
     - room
   * - ``cm_ndl_6``
     - CM_NDL.6
     - str
     - O
     - bed
   * - ``cm_ndl_7``
     - CM_NDL.7
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - facility (HD)
   * - ``cm_ndl_8``
     - CM_NDL.8
     - str
     - O
     - location status
   * - ``cm_ndl_9``
     - CM_NDL.9
     - str
     - O
     - person location type
   * - ``cm_ndl_10``
     - CM_NDL.10
     - str
     - O
     - building
   * - ``cm_ndl_11``
     - CM_NDL.11
     - str
     - O
     - floor

.. _hl7-v2_3-CM_OCD:

CM_OCD: Occurence
~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_OCD.CM_OCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_ocd_1``
     - CM_OCD.1
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - occurrence code
   * - ``cm_ocd_2``
     - CM_OCD.2
     - str
     - O
     - occurrence date

.. _hl7-v2_3-CM_OSP:

CM_OSP: Occurence span
~~~~~~~~~~~~~~~~~~~~~~

Section 6.5.11.8

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_OSP.CM_OSP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_osp_1``
     - CM_OSP.1
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - occurrence span code
   * - ``cm_osp_2``
     - CM_OSP.2
     - str
     - O
     - occurrence span start date
   * - ``cm_osp_3``
     - CM_OSP.3
     - str
     - O
     - occurrence span stop date

.. _hl7-v2_3-CM_PCF:

CM_PCF: Pre-certification required
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.8.20

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PCF.CM_PCF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_pcf_1``
     - CM_PCF.1
     - str
     - O
     - pre-certification patient type
   * - ``cm_pcf_2``
     - CM_PCF.2
     - str
     - O
     - pre-certification required
   * - ``cm_pcf_3``
     - CM_PCF.3
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     - pre-certification windwow

.. _hl7-v2_3-CM_PEN:

CM_PEN: Penalty
~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PEN.CM_PEN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_pen_1``
     - CM_PEN.1
     - str
     - O
     - penalty type
   * - ``cm_pen_2``
     - CM_PEN.2
     - str
     - O
     - penalty amount

.. _hl7-v2_3-CM_PI:

CM_PI: Person identifier
~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PI.CM_PI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_pi_1``
     - CM_PI.1
     - str
     - O
     - ID number (ST)
   * - ``cm_pi_2``
     - CM_PI.2
     - str
     - O
     - type of ID number (IS)
   * - ``cm_pi_3``
     - CM_PI.3
     - str
     - O
     - other qualifying info

.. _hl7-v2_3-CM_PIP:

CM_PIP: Privileges
~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PIP.CM_PIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_pip_1``
     - CM_PIP.1
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - privilege
   * - ``cm_pip_2``
     - CM_PIP.2
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - privilege class
   * - ``cm_pip_3``
     - CM_PIP.3
     - str
     - O
     - expiration date
   * - ``cm_pip_4``
     - CM_PIP.4
     - str
     - O
     - activation date

.. _hl7-v2_3-CM_PLN:

CM_PLN: Practitioner id numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PLN.CM_PLN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_pln_1``
     - CM_PLN.1
     - str
     - O
     - ID number
   * - ``cm_pln_2``
     - CM_PLN.2
     - str
     - O
     - type of ID number (IS)
   * - ``cm_pln_3``
     - CM_PLN.3
     - str
     - O
     - state/other qualifying info
   * - ``cm_pln_4``
     - CM_PLN.4
     - str
     - O
     - expiration date

.. _hl7-v2_3-CM_PRL:

CM_PRL: Parent result link
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PRL.CM_PRL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_prl_1``
     - CM_PRL.1
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - OBX-3 observation identifier of parent result
   * - ``cm_prl_2``
     - CM_PRL.2
     - str
     - O
     - OBX-4 sub-ID of parent result
   * - ``cm_prl_3``
     - CM_PRL.3
     - str
     - O
     - part of OBX-5 observation result from parent

.. _hl7-v2_3-CM_PTA:

CM_PTA: Policy type
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PTA.CM_PTA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_pta_1``
     - CM_PTA.1
     - str
     - O
     - policy type
   * - ``cm_pta_2``
     - CM_PTA.2
     - str
     - O
     - amount class
   * - ``cm_pta_3``
     - CM_PTA.3
     - str
     - O
     - amount

.. _hl7-v2_3-CM_RANGE:

CM_RANGE: Wertebereich
~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_RANGE.CM_RANGE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_range_1``
     - CM_RANGE.1
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - Low Value
   * - ``cm_range_2``
     - CM_RANGE.2
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - High Value

.. _hl7-v2_3-CM_RFR:

CM_RFR: Reference range
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_RFR.CM_RFR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_rfr_1``
     - CM_RFR.1
     - str
     - O
     - reference range
   * - ``cm_rfr_2``
     - CM_RFR.2
     - str
     - O
     - sex
   * - ``cm_rfr_3``
     - CM_RFR.3
     - str
     - O
     - age range
   * - ``cm_rfr_4``
     - CM_RFR.4
     - str
     - O
     - age gestation
   * - ``cm_rfr_5``
     - CM_RFR.5
     - str
     - O
     - species
   * - ``cm_rfr_6``
     - CM_RFR.6
     - str
     - O
     - race/subspecies
   * - ``cm_rfr_7``
     - CM_RFR.7
     - str
     - O
     - conditions

.. _hl7-v2_3-CM_RI:

CM_RI: Interval
~~~~~~~~~~~~~~~

Section 4.4

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_RI.CM_RI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_ri_1``
     - CM_RI.1
     - str
     - O
     - repeat pattern
   * - ``cm_ri_2``
     - CM_RI.2
     - str
     - O
     - explicit time interval

.. _hl7-v2_3-CM_RMC:

CM_RMC: Room coverage
~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_RMC.CM_RMC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_rmc_1``
     - CM_RMC.1
     - str
     - O
     - room type
   * - ``cm_rmc_2``
     - CM_RMC.2
     - str
     - O
     - amount type
   * - ``cm_rmc_3``
     - CM_RMC.3
     - str
     - O
     - coverage amount

.. _hl7-v2_3-CM_SPD:

CM_SPD: Specialty
~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_SPD.CM_SPD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_spd_1``
     - CM_SPD.1
     - str
     - O
     - specialty name
   * - ``cm_spd_2``
     - CM_SPD.2
     - str
     - O
     - governing board
   * - ``cm_spd_3``
     - CM_SPD.3
     - str
     - O
     - eligible or certified
   * - ``cm_spd_4``
     - CM_SPD.4
     - str
     - O
     - date of certification

.. _hl7-v2_3-CM_SPS:

CM_SPS: Specimen source
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_SPS.CM_SPS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_sps_1``
     - CM_SPS.1
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - specimen source name or code
   * - ``cm_sps_2``
     - CM_SPS.2
     - str
     - O
     - additives
   * - ``cm_sps_3``
     - CM_SPS.3
     - str
     - O
     - freetext
   * - ``cm_sps_4``
     - CM_SPS.4
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - body site
   * - ``cm_sps_5``
     - CM_SPS.5
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - site modifier
   * - ``cm_sps_6``
     - CM_SPS.6
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - collection modifier method code

.. _hl7-v2_3-CM_UVC:

CM_UVC: Value code and amount
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_UVC.CM_UVC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_uvc_1``
     - CM_UVC.1
     - str
     - O
     - value code
   * - ``cm_uvc_2``
     - CM_UVC.2
     - str
     - O
     - value amount

.. _hl7-v2_3-CM_VR:

CM_VR: Value qualifier
~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_VR.CM_VR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_vr_1``
     - CM_VR.1
     - str
     - O
     - first data code value
   * - ``cm_vr_2``
     - CM_VR.2
     - str
     - O
     - Last data code calue

.. _hl7-v2_3-CM_WVI:

CM_WVI: Channel identifier
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_WVI.CM_WVI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cm_wvi_1``
     - CM_WVI.1
     - str
     - O
     - Channel Number
   * - ``cm_wvi_2``
     - CM_WVI.2
     - str
     - O
     - Channel Name

.. _hl7-v2_3-CN:

CN: Composite id number and name (2.8.7)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.7

.. py:class:: hl7types.hl7.v2_3.datatypes.CN.CN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cn_1``
     - CN.1
     - str
     - O
     - ID number (ST)
   * - ``cn_2``
     - CN.2
     - str
     - O
     - family name
   * - ``cn_3``
     - CN.3
     - str
     - O
     - given name
   * - ``cn_4``
     - CN.4
     - str
     - O
     - middle initial or name
   * - ``cn_5``
     - CN.5
     - str
     - O
     - suffix (e.g., JR or III)
   * - ``cn_6``
     - CN.6
     - str
     - O
     - prefix (e.g., DR)
   * - ``cn_7``
     - CN.7
     - str
     - O
     - degree (e.g., MD)
   * - ``cn_8``
     - CN.8
     - str
     - O
     - source table
   * - ``cn_9``
     - CN.9
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - assigning authority

.. _hl7-v2_3-CP:

CP: Composite price
~~~~~~~~~~~~~~~~~~~

Section 2.8.8

.. py:class:: hl7types.hl7.v2_3.datatypes.CP.CP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cp_1``
     - CP.1
     - :ref:`MO <hl7-v2_3-MO>`
     - O
     - price
   * - ``cp_2``
     - CP.2
     - str
     - O
     - price type
   * - ``cp_3``
     - CP.3
     - str
     - O
     - from value
   * - ``cp_4``
     - CP.4
     - str
     - O
     - to value
   * - ``cp_5``
     - CP.5
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - range units
   * - ``cp_6``
     - CP.6
     - str
     - O
     - range type

.. _hl7-v2_3-CQ:

CQ: Composite quantity with units
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.9

.. py:class:: hl7types.hl7.v2_3.datatypes.CQ.CQ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cq_1``
     - CQ.1
     - str
     - O
     - quantity
   * - ``cq_2``
     - CQ.2
     - :ref:`CE <hl7-v2_3-CE>`
     - O
     - units

.. _hl7-v2_3-CX:

CX: Extended composite id with check digit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.10

.. py:class:: hl7types.hl7.v2_3.datatypes.CX.CX
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cx_1``
     - CX.1
     - str
     - O
     - ID
   * - ``cx_2``
     - CX.2
     - str
     - O
     - check digit
   * - ``cx_3``
     - CX.3
     - str
     - O
     - code identifying the check digit scheme employed
   * - ``cx_4``
     - CX.4
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - assigning authority
   * - ``cx_5``
     - CX.5
     - str
     - O
     - identifier type code
   * - ``cx_6``
     - CX.6
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - assigning facility

.. _hl7-v2_3-DLN:

DLN: Driver's license number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.11

.. py:class:: hl7types.hl7.v2_3.datatypes.DLN.DLN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``dln_1``
     - DLN.1
     - str
     - O
     - Driver´s License Number
   * - ``dln_2``
     - DLN.2
     - str
     - O
     - Issuing State, province, country
   * - ``dln_3``
     - DLN.3
     - str
     - O
     - expiration date

.. _hl7-v2_3-DR:

DR: Date time range
~~~~~~~~~~~~~~~~~~~

Section 2.8.12

.. py:class:: hl7types.hl7.v2_3.datatypes.DR.DR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``dr_1``
     - DR.1
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     - range start date/time
   * - ``dr_2``
     - DR.2
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     - range end date/time

.. _hl7-v2_3-ED:

ED: Encapsulated data
~~~~~~~~~~~~~~~~~~~~~

Section 2.8.14

.. py:class:: hl7types.hl7.v2_3.datatypes.ED.ED
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ed_1``
     - ED.1
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - source application
   * - ``ed_2``
     - ED.2
     - str
     - O
     - type of data
   * - ``ed_3``
     - ED.3
     - str
     - O
     - data
   * - ``ed_4``
     - ED.4
     - str
     - O
     - encoding
   * - ``ed_5``
     - ED.5
     - str
     - O
     - data

.. _hl7-v2_3-EI:

EI: Entity identifier
~~~~~~~~~~~~~~~~~~~~~

Section 2.8.15

.. py:class:: hl7types.hl7.v2_3.datatypes.EI.EI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ei_1``
     - EI.1
     - str
     - O
     - entity identifier
   * - ``ei_2``
     - EI.2
     - str
     - O
     - namespace ID
   * - ``ei_3``
     - EI.3
     - str
     - O
     - universal ID
   * - ``ei_4``
     - EI.4
     - str
     - O
     - universal ID type

.. _hl7-v2_3-FC:

FC: Financial class
~~~~~~~~~~~~~~~~~~~

Section 2.8.16

.. py:class:: hl7types.hl7.v2_3.datatypes.FC.FC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``fc_1``
     - FC.1
     - str
     - O
     - Financial Class
   * - ``fc_2``
     - FC.2
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     - Effective Date

.. _hl7-v2_3-HD:

HD: Hierarchic designator
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.18

.. py:class:: hl7types.hl7.v2_3.datatypes.HD.HD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``hd_1``
     - HD.1
     - str
     - O
     - namespace ID
   * - ``hd_2``
     - HD.2
     - str
     - O
     - universal ID
   * - ``hd_3``
     - HD.3
     - str
     - O
     - universal ID type

.. _hl7-v2_3-JCC:

JCC: Job code class
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.JCC.JCC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``jcc_1``
     - JCC.1
     - str
     - O
     - job code
   * - ``jcc_2``
     - JCC.2
     - str
     - O
     - job class

.. _hl7-v2_3-MA:

MA: Multiplexed array
~~~~~~~~~~~~~~~~~~~~~

Section 2.8.2

.. py:class:: hl7types.hl7.v2_3.datatypes.MA.MA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ma_1``
     - MA.1
     - str
     - O
     - sample 1 from channel 1
   * - ``ma_2``
     - MA.2
     - str
     - O
     - sample 1 from channel 2
   * - ``ma_3``
     - MA.3
     - str
     - O
     - sample 1 from channel 3
   * - ``ma_4``
     - MA.4
     - str
     - O
     - sample 2 from channel 1
   * - ``ma_5``
     - MA.5
     - str
     - O
     - sample 2 from channel 2
   * - ``ma_6``
     - MA.6
     - str
     - O
     - sample 2 from channel 3

.. _hl7-v2_3-MO:

MO: Money
~~~~~~~~~

Section 2.8.23

.. py:class:: hl7types.hl7.v2_3.datatypes.MO.MO
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``mo_1``
     - MO.1
     - str
     - O
     - quantity
   * - ``mo_2``
     - MO.2
     - str
     - O
     - denomination

.. _hl7-v2_3-NA:

NA: Numeric array
~~~~~~~~~~~~~~~~~

Section 2.8.24

.. py:class:: hl7types.hl7.v2_3.datatypes.NA.NA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``na_1``
     - NA.1
     - str
     - O
     - value1
   * - ``na_2``
     - NA.2
     - str
     - O
     - value2
   * - ``na_3``
     - NA.3
     - str
     - O
     - value3
   * - ``na_4``
     - NA.4
     - str
     - O
     - value4

.. _hl7-v2_3-PL:

PL: Person location
~~~~~~~~~~~~~~~~~~~

Section 2.8.26

.. py:class:: hl7types.hl7.v2_3.datatypes.PL.PL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pl_1``
     - PL.1
     - str
     - O
     - point of care (ID)
   * - ``pl_2``
     - PL.2
     - str
     - O
     - room
   * - ``pl_3``
     - PL.3
     - str
     - O
     - bed
   * - ``pl_4``
     - PL.4
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - facility (HD)
   * - ``pl_5``
     - PL.5
     - str
     - O
     - location status
   * - ``pl_6``
     - PL.6
     - str
     - O
     - person location type
   * - ``pl_7``
     - PL.7
     - str
     - O
     - building
   * - ``pl_8``
     - PL.8
     - str
     - O
     - floor
   * - ``pl_9``
     - PL.9
     - str
     - O
     - Location type

.. _hl7-v2_3-PPN:

PPN: Performing person time stamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.27

.. py:class:: hl7types.hl7.v2_3.datatypes.PPN.PPN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ppn_1``
     - PPN.1
     - str
     - O
     - ID number
   * - ``ppn_2``
     - PPN.2
     - str
     - O
     - family name
   * - ``ppn_3``
     - PPN.3
     - str
     - O
     - given name
   * - ``ppn_4``
     - PPN.4
     - str
     - O
     - middle initial or name
   * - ``ppn_5``
     - PPN.5
     - str
     - O
     - suffix (e.g., JR or III)
   * - ``ppn_6``
     - PPN.6
     - str
     - O
     - prefix (e.g., DR)
   * - ``ppn_7``
     - PPN.7
     - str
     - O
     - degree (e.g., MD)
   * - ``ppn_8``
     - PPN.8
     - str
     - O
     - source table
   * - ``ppn_9``
     - PPN.9
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - assigning authority
   * - ``ppn_10``
     - PPN.10
     - str
     - O
     - name type code
   * - ``ppn_11``
     - PPN.11
     - str
     - O
     - identifier check digit
   * - ``ppn_12``
     - PPN.12
     - str
     - O
     - code identifying the check digit scheme employed
   * - ``ppn_13``
     - PPN.13
     - str
     - O
     - identifier type code
   * - ``ppn_14``
     - PPN.14
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - assigning facility
   * - ``ppn_15``
     - PPN.15
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     - Date/Time Action Performed

.. _hl7-v2_3-PT:

PT: Processing type
~~~~~~~~~~~~~~~~~~~

Section 2.8.29

.. py:class:: hl7types.hl7.v2_3.datatypes.PT.PT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pt_1``
     - PT.1
     - str
     - O
     - processing ID
   * - ``pt_2``
     - PT.2
     - str
     - O
     - processing mode

.. _hl7-v2_3-QIP:

QIP: Query input parameter list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.30

.. py:class:: hl7types.hl7.v2_3.datatypes.QIP.QIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``qip_1``
     - QIP.1
     - str
     - O
     - field name
   * - ``qip_2``
     - QIP.2
     - str
     - O
     - value1&value2&value3

.. _hl7-v2_3-QSC:

QSC: Query selection criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.31

.. py:class:: hl7types.hl7.v2_3.datatypes.QSC.QSC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``qsc_1``
     - QSC.1
     - str
     - O
     - name of field
   * - ``qsc_2``
     - QSC.2
     - str
     - O
     - relational operator
   * - ``qsc_3``
     - QSC.3
     - str
     - O
     - Value
   * - ``qsc_4``
     - QSC.4
     - str
     - O
     - relational conjunction

.. _hl7-v2_3-RCD:

RCD: Row column definition
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.32

.. py:class:: hl7types.hl7.v2_3.datatypes.RCD.RCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``rcd_1``
     - RCD.1
     - str
     - O
     - HL7 item number
   * - ``rcd_2``
     - RCD.2
     - str
     - O
     - HL7 date type
   * - ``rcd_3``
     - RCD.3
     - str
     - O
     - maximum column width

.. _hl7-v2_3-RI:

RI: Repeat interval
~~~~~~~~~~~~~~~~~~~

Section 2.8.32

.. py:class:: hl7types.hl7.v2_3.datatypes.RI.RI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ri_1``
     - RI.1
     - str
     - O
     - repeat pattern
   * - ``ri_2``
     - RI.2
     - str
     - O
     - explicit time interval

.. _hl7-v2_3-RP:

RP: Reference pointer
~~~~~~~~~~~~~~~~~~~~~

Section 2.8.34

.. py:class:: hl7types.hl7.v2_3.datatypes.RP.RP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``rp_1``
     - RP.1
     - str
     - O
     - pointer
   * - ``rp_2``
     - RP.2
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - application ID
   * - ``rp_3``
     - RP.3
     - str
     - O
     - type of data
   * - ``rp_4``
     - RP.4
     - str
     - O
     - subtype

.. _hl7-v2_3-SCV:

SCV: Scheduling class value pair
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.35

.. py:class:: hl7types.hl7.v2_3.datatypes.SCV.SCV
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``scv_1``
     - SCV.1
     - str
     - O
     - parameter class
   * - ``scv_2``
     - SCV.2
     - str
     - O
     - parameter value

.. _hl7-v2_3-SN:

SN: Structured numeric
~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.37

.. py:class:: hl7types.hl7.v2_3.datatypes.SN.SN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``sn_1``
     - SN.1
     - str
     - O
     - comparator
   * - ``sn_2``
     - SN.2
     - str
     - O
     - num1
   * - ``sn_3``
     - SN.3
     - str
     - O
     - separator or suffix
   * - ``sn_4``
     - SN.4
     - str
     - O
     - num2

.. _hl7-v2_3-TQ:

TQ: Timing quantity
~~~~~~~~~~~~~~~~~~~

Section 2.8.41

.. py:class:: hl7types.hl7.v2_3.datatypes.TQ.TQ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``tq_1``
     - TQ.1
     - :ref:`CQ <hl7-v2_3-CQ>`
     - O
     - quantity
   * - ``tq_2``
     - TQ.2
     - str
     - O
     - interval
   * - ``tq_3``
     - TQ.3
     - str
     - O
     - duration
   * - ``tq_4``
     - TQ.4
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     - start date/time
   * - ``tq_5``
     - TQ.5
     - :ref:`TS <hl7-v2_3-TS>`
     - O
     - end date/time
   * - ``tq_6``
     - TQ.6
     - str
     - O
     - priority
   * - ``tq_7``
     - TQ.7
     - str
     - O
     - condition
   * - ``tq_8``
     - TQ.8
     - str
     - O
     - text (TX)
   * - ``tq_9``
     - TQ.9
     - str
     - O
     - conjunction
   * - ``tq_10``
     - TQ.10
     - str
     - O
     - order sequencing

.. _hl7-v2_3-TS:

TS: Time stamp
~~~~~~~~~~~~~~

Section 2.8.42

.. py:class:: hl7types.hl7.v2_3.datatypes.TS.TS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ts_1``
     - TS.1
     - str
     - O
     - time of an event
   * - ``ts_2``
     - TS.2
     - str
     - O
     - degree of precision

.. _hl7-v2_3-VH:

VH: Visiting hours
~~~~~~~~~~~~~~~~~~

Section 2.8.44

.. py:class:: hl7types.hl7.v2_3.datatypes.VH.VH
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``vh_1``
     - VH.1
     - str
     - O
     - start day range
   * - ``vh_2``
     - VH.2
     - str
     - O
     - end day range
   * - ``vh_3``
     - VH.3
     - str
     - O
     - start hour range
   * - ``vh_4``
     - VH.4
     - str
     - O
     - end hour range

.. _hl7-v2_3-XAD:

XAD: Extended address
~~~~~~~~~~~~~~~~~~~~~

Section 2.8.45

.. py:class:: hl7types.hl7.v2_3.datatypes.XAD.XAD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xad_1``
     - XAD.1
     - str
     - O
     - street address
   * - ``xad_2``
     - XAD.2
     - str
     - O
     - other designation
   * - ``xad_3``
     - XAD.3
     - str
     - O
     - city
   * - ``xad_4``
     - XAD.4
     - str
     - O
     - state or province
   * - ``xad_5``
     - XAD.5
     - str
     - O
     - zip or postal code
   * - ``xad_6``
     - XAD.6
     - str
     - O
     - country
   * - ``xad_7``
     - XAD.7
     - str
     - O
     - address type
   * - ``xad_8``
     - XAD.8
     - str
     - O
     - other geographic designation
   * - ``xad_9``
     - XAD.9
     - str
     - O
     - county/parish code
   * - ``xad_10``
     - XAD.10
     - str
     - O
     - census tract

.. _hl7-v2_3-XCN:

XCN: Extended composite id number and name (2.8.46)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.XCN.XCN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xcn_1``
     - XCN.1
     - str
     - O
     - ID number (ST)
   * - ``xcn_2``
     - XCN.2
     - str
     - O
     - family name
   * - ``xcn_3``
     - XCN.3
     - str
     - O
     - given name
   * - ``xcn_4``
     - XCN.4
     - str
     - O
     - middle initial or name
   * - ``xcn_5``
     - XCN.5
     - str
     - O
     - suffix (e.g., JR or III)
   * - ``xcn_6``
     - XCN.6
     - str
     - O
     - prefix (e.g., DR)
   * - ``xcn_7``
     - XCN.7
     - str
     - O
     - degree (e.g., MD)
   * - ``xcn_8``
     - XCN.8
     - str
     - O
     - source table
   * - ``xcn_9``
     - XCN.9
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - assigning authority
   * - ``xcn_10``
     - XCN.10
     - str
     - O
     - name type
   * - ``xcn_11``
     - XCN.11
     - str
     - O
     - identifier check digit
   * - ``xcn_12``
     - XCN.12
     - str
     - O
     - code identifying the check digit scheme employed
   * - ``xcn_13``
     - XCN.13
     - str
     - O
     - identifier type code
   * - ``xcn_14``
     - XCN.14
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - assigning facility ID

.. _hl7-v2_3-XON:

XON: Extended composite name and id for organizations (2.8.47)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.datatypes.XON.XON
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xon_1``
     - XON.1
     - str
     - O
     - organization name
   * - ``xon_2``
     - XON.2
     - str
     - O
     - organization name type code
   * - ``xon_3``
     - XON.3
     - str
     - O
     - ID number (NM)
   * - ``xon_4``
     - XON.4
     - str
     - O
     - check digit
   * - ``xon_5``
     - XON.5
     - str
     - O
     - code identifying the check digit scheme employed
   * - ``xon_6``
     - XON.6
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - assigning authority
   * - ``xon_7``
     - XON.7
     - str
     - O
     - identifier type code
   * - ``xon_8``
     - XON.8
     - :ref:`HD <hl7-v2_3-HD>`
     - O
     - assigning facility ID

.. _hl7-v2_3-XPN:

XPN: Extended person name
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.48

.. py:class:: hl7types.hl7.v2_3.datatypes.XPN.XPN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xpn_1``
     - XPN.1
     - str
     - O
     - family name
   * - ``xpn_2``
     - XPN.2
     - str
     - O
     - given name
   * - ``xpn_3``
     - XPN.3
     - str
     - O
     - middle initial or name
   * - ``xpn_4``
     - XPN.4
     - str
     - O
     - suffix (e.g., JR or III)
   * - ``xpn_5``
     - XPN.5
     - str
     - O
     - prefix (e.g., DR)
   * - ``xpn_6``
     - XPN.6
     - str
     - O
     - degree (e.g., MD)
   * - ``xpn_7``
     - XPN.7
     - str
     - O
     - name type code
   * - ``xpn_8``
     - XPN.8
     - str
     - O
     - Name Representation code

.. _hl7-v2_3-XTN:

XTN: Extended telecommunication number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.8.49

.. py:class:: hl7types.hl7.v2_3.datatypes.XTN.XTN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xtn_1``
     - XTN.1
     - str
     - O
     - [(999)] 999-9999 [X99999][C any text]
   * - ``xtn_2``
     - XTN.2
     - str
     - O
     - telecommunication use code
   * - ``xtn_3``
     - XTN.3
     - str
     - O
     - telecommunication equipment type (ID)
   * - ``xtn_4``
     - XTN.4
     - str
     - O
     - Email address
   * - ``xtn_5``
     - XTN.5
     - str
     - O
     - Country Code
   * - ``xtn_6``
     - XTN.6
     - str
     - O
     - Area/city code
   * - ``xtn_7``
     - XTN.7
     - str
     - O
     - Phone number
   * - ``xtn_8``
     - XTN.8
     - str
     - O
     - Extension
   * - ``xtn_9``
     - XTN.9
     - str
     - O
     - any text
