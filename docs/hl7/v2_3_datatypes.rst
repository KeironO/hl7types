v2.3 Data Types
===============

.. _hl7-v2_3-AD:

.. py:class:: hl7types.hl7.v2_3.datatypes.AD.AD
   :noindex:

   HL7 v2 AD data type.

AD
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ad_1``
     - AD.1
     - Optional[str]
     - optional
     - 
     - street address
   * - ``ad_2``
     - AD.2
     - Optional[str]
     - optional
     - 
     - other designation
   * - ``ad_3``
     - AD.3
     - Optional[str]
     - optional
     - 
     - city
   * - ``ad_4``
     - AD.4
     - Optional[str]
     - optional
     - 
     - state or province
   * - ``ad_5``
     - AD.5
     - Optional[str]
     - optional
     - 
     - zip or postal code
   * - ``ad_6``
     - AD.6
     - Optional[str]
     - optional
     - 
     - country
   * - ``ad_7``
     - AD.7
     - Optional[str]
     - optional
     - 
     - address type
   * - ``ad_8``
     - AD.8
     - Optional[str]
     - optional
     - 
     - other geographic designation

.. _hl7-v2_3-CD:

.. py:class:: hl7types.hl7.v2_3.datatypes.CD.CD
   :noindex:

   HL7 v2 CD data type.

CD
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cd_1``
     - CD.1
     - Optional[str]
     - optional
     - 
     - channel identifier
   * - ``cd_2``
     - CD.2
     - Optional[str]
     - optional
     - 
     - electrode names
   * - ``cd_3``
     - CD.3
     - Optional[str]
     - optional
     - 
     - channel sensitivity/units
   * - ``cd_4``
     - CD.4
     - Optional[str]
     - optional
     - 
     - calibration parameters
   * - ``cd_5``
     - CD.5
     - Optional[str]
     - optional
     - 
     - sampling frequency
   * - ``cd_6``
     - CD.6
     - Optional[str]
     - optional
     - 
     - minimum/maximum data values

.. _hl7-v2_3-CE:

.. py:class:: hl7types.hl7.v2_3.datatypes.CE.CE
   :noindex:

   HL7 v2 CE data type.

CE
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ce_1``
     - CE.1
     - Optional[str]
     - optional
     - 
     - identifier
   * - ``ce_2``
     - CE.2
     - Optional[str]
     - optional
     - 
     - text
   * - ``ce_3``
     - CE.3
     - Optional[str]
     - optional
     - 
     - name of coding system
   * - ``ce_4``
     - CE.4
     - Optional[str]
     - optional
     - 
     - alternate identifier
   * - ``ce_5``
     - CE.5
     - Optional[str]
     - optional
     - 
     - alternate text
   * - ``ce_6``
     - CE.6
     - Optional[str]
     - optional
     - 
     - name of alternate coding system

.. _hl7-v2_3-CF:

.. py:class:: hl7types.hl7.v2_3.datatypes.CF.CF
   :noindex:

   HL7 v2 CF data type.

CF
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cf_1``
     - CF.1
     - Optional[str]
     - optional
     - 
     - identifier
   * - ``cf_2``
     - CF.2
     - Optional[str]
     - optional
     - 
     - formatted text
   * - ``cf_3``
     - CF.3
     - Optional[str]
     - optional
     - 
     - name of coding system
   * - ``cf_4``
     - CF.4
     - Optional[str]
     - optional
     - 
     - alternate identifier
   * - ``cf_5``
     - CF.5
     - Optional[str]
     - optional
     - 
     - alternate formatted text
   * - ``cf_6``
     - CF.6
     - Optional[str]
     - optional
     - 
     - name of alternate coding system

.. _hl7-v2_3-CK:

.. py:class:: hl7types.hl7.v2_3.datatypes.CK.CK
   :noindex:

   HL7 v2 CK data type.

CK
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ck_1``
     - CK.1
     - Optional[str]
     - optional
     - 
     - ID number (NM)
   * - ``ck_2``
     - CK.2
     - Optional[str]
     - optional
     - 
     - check digit
   * - ``ck_3``
     - CK.3
     - Optional[str]
     - optional
     - 
     - code identifying the check digit scheme employed
   * - ``ck_4``
     - CK.4
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - assigning authority

.. _hl7-v2_3-CM_ABS_RANGE:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_ABS_RANGE.CM_ABS_RANGE
   :noindex:

   HL7 v2 CM_ABS_RANGE data type.

CM_ABS_RANGE
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_abs_range_1``
     - CM_ABS_RANGE.1
     - Optional[str]
     - optional
     - 
     - Range
   * - ``cm_abs_range_2``
     - CM_ABS_RANGE.2
     - Optional[str]
     - optional
     - 
     - Numeric Change
   * - ``cm_abs_range_3``
     - CM_ABS_RANGE.3
     - Optional[str]
     - optional
     - 
     - Percent per Change
   * - ``cm_abs_range_4``
     - CM_ABS_RANGE.4
     - Optional[str]
     - optional
     - 
     - Days

.. _hl7-v2_3-CM_AUI:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_AUI.CM_AUI
   :noindex:

   HL7 v2 CM_AUI data type.

CM_AUI
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_aui_1``
     - CM_AUI.1
     - Optional[str]
     - optional
     - 
     - authorization number
   * - ``cm_aui_2``
     - CM_AUI.2
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     - 
     - date
   * - ``cm_aui_3``
     - CM_AUI.3
     - Optional[str]
     - optional
     - 
     - source

.. _hl7-v2_3-CM_CCD:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_CCD.CM_CCD
   :noindex:

   HL7 v2 CM_CCD data type.

CM_CCD
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_ccd_1``
     - CM_CCD.1
     - Optional[str]
     - optional
     - 
     - when to charge code
   * - ``cm_ccd_2``
     - CM_CCD.2
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     - 
     - date/time

.. _hl7-v2_3-CM_DDI:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_DDI.CM_DDI
   :noindex:

   HL7 v2 CM_DDI data type.

CM_DDI
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_ddi_1``
     - CM_DDI.1
     - Optional[str]
     - optional
     - 
     - delay days
   * - ``cm_ddi_2``
     - CM_DDI.2
     - Optional[str]
     - optional
     - 
     - amount
   * - ``cm_ddi_3``
     - CM_DDI.3
     - Optional[str]
     - optional
     - 
     - number of days

.. _hl7-v2_3-CM_DIN:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_DIN.CM_DIN
   :noindex:

   HL7 v2 CM_DIN data type.

CM_DIN
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_din_1``
     - CM_DIN.1
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     - 
     - date
   * - ``cm_din_2``
     - CM_DIN.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - institution name

.. _hl7-v2_3-CM_DLD:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_DLD.CM_DLD
   :noindex:

   HL7 v2 CM_DLD data type.

CM_DLD
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_dld_1``
     - CM_DLD.1
     - Optional[str]
     - optional
     - 
     - discharge location
   * - ``cm_dld_2``
     - CM_DLD.2
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     - 
     - effective date

.. _hl7-v2_3-CM_DLT:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_DLT.CM_DLT
   :noindex:

   HL7 v2 CM_DLT data type.

CM_DLT
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_dlt_1``
     - CM_DLT.1
     - Optional[str]
     - optional
     - 
     - Range
   * - ``cm_dlt_2``
     - CM_DLT.2
     - Optional[str]
     - optional
     - 
     - numeric threshold
   * - ``cm_dlt_3``
     - CM_DLT.3
     - Optional[str]
     - optional
     - 
     - change
   * - ``cm_dlt_4``
     - CM_DLT.4
     - Optional[str]
     - optional
     - 
     - length of time-days

.. _hl7-v2_3-CM_DTN:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_DTN.CM_DTN
   :noindex:

   HL7 v2 CM_DTN data type.

CM_DTN
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_dtn_1``
     - CM_DTN.1
     - Optional[str]
     - optional
     - 
     - day type
   * - ``cm_dtn_2``
     - CM_DTN.2
     - Optional[str]
     - optional
     - 
     - number of days

.. _hl7-v2_3-CM_EIP:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_EIP.CM_EIP
   :noindex:

   HL7 v2 CM_EIP data type.

CM_EIP
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_eip_1``
     - CM_EIP.1
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     - 
     - parent´s placer order number
   * - ``cm_eip_2``
     - CM_EIP.2
     - Optional[:ref:`EI <hl7-v2_3-EI>`]
     - optional
     - 
     - parent´s filler order number

.. _hl7-v2_3-CM_ELD:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_ELD.CM_ELD
   :noindex:

   HL7 v2 CM_ELD data type.

CM_ELD
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_eld_1``
     - CM_ELD.1
     - Optional[str]
     - optional
     - 
     - segment ID
   * - ``cm_eld_2``
     - CM_ELD.2
     - Optional[str]
     - optional
     - 
     - sequence
   * - ``cm_eld_3``
     - CM_ELD.3
     - Optional[str]
     - optional
     - 
     - field position
   * - ``cm_eld_4``
     - CM_ELD.4
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - code identifying error

.. _hl7-v2_3-CM_LA1:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_LA1.CM_LA1
   :noindex:

   HL7 v2 CM_LA1 data type.

CM_LA1
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_la1_1``
     - CM_LA1.1
     - Optional[str]
     - optional
     - 
     - point of care (ST)
   * - ``cm_la1_2``
     - CM_LA1.2
     - Optional[str]
     - optional
     - 
     - room
   * - ``cm_la1_3``
     - CM_LA1.3
     - Optional[str]
     - optional
     - 
     - bed
   * - ``cm_la1_4``
     - CM_LA1.4
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - facility (HD)
   * - ``cm_la1_5``
     - CM_LA1.5
     - Optional[str]
     - optional
     - 
     - location status
   * - ``cm_la1_6``
     - CM_LA1.6
     - Optional[str]
     - optional
     - 
     - person location type
   * - ``cm_la1_7``
     - CM_LA1.7
     - Optional[str]
     - optional
     - 
     - building
   * - ``cm_la1_8``
     - CM_LA1.8
     - Optional[str]
     - optional
     - 
     - floor
   * - ``cm_la1_9``
     - CM_LA1.9
     - Optional[str]
     - optional
     - 
     - street address
   * - ``cm_la1_10``
     - CM_LA1.10
     - Optional[str]
     - optional
     - 
     - other designation
   * - ``cm_la1_11``
     - CM_LA1.11
     - Optional[str]
     - optional
     - 
     - city
   * - ``cm_la1_12``
     - CM_LA1.12
     - Optional[str]
     - optional
     - 
     - state or province
   * - ``cm_la1_13``
     - CM_LA1.13
     - Optional[str]
     - optional
     - 
     - zip or postal code
   * - ``cm_la1_14``
     - CM_LA1.14
     - Optional[str]
     - optional
     - 
     - country
   * - ``cm_la1_15``
     - CM_LA1.15
     - Optional[str]
     - optional
     - 
     - address type
   * - ``cm_la1_16``
     - CM_LA1.16
     - Optional[str]
     - optional
     - 
     - other geographic designation

.. _hl7-v2_3-CM_MOC:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_MOC.CM_MOC
   :noindex:

   HL7 v2 CM_MOC data type.

CM_MOC
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_moc_1``
     - CM_MOC.1
     - Optional[:ref:`MO <hl7-v2_3-MO>`]
     - optional
     - 
     - dollar amount
   * - ``cm_moc_2``
     - CM_MOC.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - charge code

.. _hl7-v2_3-CM_MSG:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_MSG.CM_MSG
   :noindex:

   HL7 v2 CM_MSG data type.

CM_MSG
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_msg_1``
     - CM_MSG.1
     - Optional[str]
     - optional
     - 
     - message type
   * - ``cm_msg_2``
     - CM_MSG.2
     - Optional[str]
     - optional
     - 
     - trigger event

.. _hl7-v2_3-CM_NDL:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_NDL.CM_NDL
   :noindex:

   HL7 v2 CM_NDL data type.

CM_NDL
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_ndl_1``
     - CM_NDL.1
     - Optional[:ref:`CN <hl7-v2_3-CN>`]
     - optional
     - 
     - name
   * - ``cm_ndl_2``
     - CM_NDL.2
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     - 
     - start date/time
   * - ``cm_ndl_3``
     - CM_NDL.3
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     - 
     - end date/time
   * - ``cm_ndl_4``
     - CM_NDL.4
     - Optional[str]
     - optional
     - 
     - point of care (IS)
   * - ``cm_ndl_5``
     - CM_NDL.5
     - Optional[str]
     - optional
     - 
     - room
   * - ``cm_ndl_6``
     - CM_NDL.6
     - Optional[str]
     - optional
     - 
     - bed
   * - ``cm_ndl_7``
     - CM_NDL.7
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - facility (HD)
   * - ``cm_ndl_8``
     - CM_NDL.8
     - Optional[str]
     - optional
     - 
     - location status
   * - ``cm_ndl_9``
     - CM_NDL.9
     - Optional[str]
     - optional
     - 
     - person location type
   * - ``cm_ndl_10``
     - CM_NDL.10
     - Optional[str]
     - optional
     - 
     - building
   * - ``cm_ndl_11``
     - CM_NDL.11
     - Optional[str]
     - optional
     - 
     - floor

.. _hl7-v2_3-CM_OCD:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_OCD.CM_OCD
   :noindex:

   HL7 v2 CM_OCD data type.

CM_OCD
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_ocd_1``
     - CM_OCD.1
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - occurrence code
   * - ``cm_ocd_2``
     - CM_OCD.2
     - Optional[str]
     - optional
     - 
     - occurrence date

.. _hl7-v2_3-CM_OSP:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_OSP.CM_OSP
   :noindex:

   HL7 v2 CM_OSP data type.

CM_OSP
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_osp_1``
     - CM_OSP.1
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - occurrence span code
   * - ``cm_osp_2``
     - CM_OSP.2
     - Optional[str]
     - optional
     - 
     - occurrence span start date
   * - ``cm_osp_3``
     - CM_OSP.3
     - Optional[str]
     - optional
     - 
     - occurrence span stop date

.. _hl7-v2_3-CM_PCF:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PCF.CM_PCF
   :noindex:

   HL7 v2 CM_PCF data type.

CM_PCF
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_pcf_1``
     - CM_PCF.1
     - Optional[str]
     - optional
     - 
     - pre-certification patient type
   * - ``cm_pcf_2``
     - CM_PCF.2
     - Optional[str]
     - optional
     - 
     - pre-certification required
   * - ``cm_pcf_3``
     - CM_PCF.3
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     - 
     - pre-certification windwow

.. _hl7-v2_3-CM_PEN:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PEN.CM_PEN
   :noindex:

   HL7 v2 CM_PEN data type.

CM_PEN
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_pen_1``
     - CM_PEN.1
     - Optional[str]
     - optional
     - 
     - penalty type
   * - ``cm_pen_2``
     - CM_PEN.2
     - Optional[str]
     - optional
     - 
     - penalty amount

.. _hl7-v2_3-CM_PI:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PI.CM_PI
   :noindex:

   HL7 v2 CM_PI data type.

CM_PI
~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_pi_1``
     - CM_PI.1
     - Optional[str]
     - optional
     - 
     - ID number (ST)
   * - ``cm_pi_2``
     - CM_PI.2
     - Optional[str]
     - optional
     - 
     - type of ID number (IS)
   * - ``cm_pi_3``
     - CM_PI.3
     - Optional[str]
     - optional
     - 
     - other qualifying info

.. _hl7-v2_3-CM_PIP:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PIP.CM_PIP
   :noindex:

   HL7 v2 CM_PIP data type.

CM_PIP
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_pip_1``
     - CM_PIP.1
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - privilege
   * - ``cm_pip_2``
     - CM_PIP.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - privilege class
   * - ``cm_pip_3``
     - CM_PIP.3
     - Optional[str]
     - optional
     - 
     - expiration date
   * - ``cm_pip_4``
     - CM_PIP.4
     - Optional[str]
     - optional
     - 
     - activation date

.. _hl7-v2_3-CM_PLN:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PLN.CM_PLN
   :noindex:

   HL7 v2 CM_PLN data type.

CM_PLN
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_pln_1``
     - CM_PLN.1
     - Optional[str]
     - optional
     - 
     - ID number
   * - ``cm_pln_2``
     - CM_PLN.2
     - Optional[str]
     - optional
     - 
     - type of ID number (IS)
   * - ``cm_pln_3``
     - CM_PLN.3
     - Optional[str]
     - optional
     - 
     - state/other qualifying info
   * - ``cm_pln_4``
     - CM_PLN.4
     - Optional[str]
     - optional
     - 
     - expiration date

.. _hl7-v2_3-CM_PRL:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PRL.CM_PRL
   :noindex:

   HL7 v2 CM_PRL data type.

CM_PRL
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_prl_1``
     - CM_PRL.1
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - OBX-3 observation identifier of parent result
   * - ``cm_prl_2``
     - CM_PRL.2
     - Optional[str]
     - optional
     - 
     - OBX-4 sub-ID of parent result
   * - ``cm_prl_3``
     - CM_PRL.3
     - Optional[str]
     - optional
     - 
     - part of OBX-5 observation result from parent

.. _hl7-v2_3-CM_PTA:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_PTA.CM_PTA
   :noindex:

   HL7 v2 CM_PTA data type.

CM_PTA
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_pta_1``
     - CM_PTA.1
     - Optional[str]
     - optional
     - 
     - policy type
   * - ``cm_pta_2``
     - CM_PTA.2
     - Optional[str]
     - optional
     - 
     - amount class
   * - ``cm_pta_3``
     - CM_PTA.3
     - Optional[str]
     - optional
     - 
     - amount

.. _hl7-v2_3-CM_RANGE:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_RANGE.CM_RANGE
   :noindex:

   HL7 v2 CM_RANGE data type.

CM_RANGE
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_range_1``
     - CM_RANGE.1
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - Low Value
   * - ``cm_range_2``
     - CM_RANGE.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - High Value

.. _hl7-v2_3-CM_RFR:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_RFR.CM_RFR
   :noindex:

   HL7 v2 CM_RFR data type.

CM_RFR
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_rfr_1``
     - CM_RFR.1
     - Optional[str]
     - optional
     - 
     - reference range
   * - ``cm_rfr_2``
     - CM_RFR.2
     - Optional[str]
     - optional
     - 
     - sex
   * - ``cm_rfr_3``
     - CM_RFR.3
     - Optional[str]
     - optional
     - 
     - age range
   * - ``cm_rfr_4``
     - CM_RFR.4
     - Optional[str]
     - optional
     - 
     - age gestation
   * - ``cm_rfr_5``
     - CM_RFR.5
     - Optional[str]
     - optional
     - 
     - species
   * - ``cm_rfr_6``
     - CM_RFR.6
     - Optional[str]
     - optional
     - 
     - race/subspecies
   * - ``cm_rfr_7``
     - CM_RFR.7
     - Optional[str]
     - optional
     - 
     - conditions

.. _hl7-v2_3-CM_RI:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_RI.CM_RI
   :noindex:

   HL7 v2 CM_RI data type.

CM_RI
~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_ri_1``
     - CM_RI.1
     - Optional[str]
     - optional
     - 
     - repeat pattern
   * - ``cm_ri_2``
     - CM_RI.2
     - Optional[str]
     - optional
     - 
     - explicit time interval

.. _hl7-v2_3-CM_RMC:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_RMC.CM_RMC
   :noindex:

   HL7 v2 CM_RMC data type.

CM_RMC
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_rmc_1``
     - CM_RMC.1
     - Optional[str]
     - optional
     - 
     - room type
   * - ``cm_rmc_2``
     - CM_RMC.2
     - Optional[str]
     - optional
     - 
     - amount type
   * - ``cm_rmc_3``
     - CM_RMC.3
     - Optional[str]
     - optional
     - 
     - coverage amount

.. _hl7-v2_3-CM_SPD:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_SPD.CM_SPD
   :noindex:

   HL7 v2 CM_SPD data type.

CM_SPD
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_spd_1``
     - CM_SPD.1
     - Optional[str]
     - optional
     - 
     - specialty name
   * - ``cm_spd_2``
     - CM_SPD.2
     - Optional[str]
     - optional
     - 
     - governing board
   * - ``cm_spd_3``
     - CM_SPD.3
     - Optional[str]
     - optional
     - 
     - eligible or certified
   * - ``cm_spd_4``
     - CM_SPD.4
     - Optional[str]
     - optional
     - 
     - date of certification

.. _hl7-v2_3-CM_SPS:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_SPS.CM_SPS
   :noindex:

   HL7 v2 CM_SPS data type.

CM_SPS
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_sps_1``
     - CM_SPS.1
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - specimen source name or code
   * - ``cm_sps_2``
     - CM_SPS.2
     - Optional[str]
     - optional
     - 
     - additives
   * - ``cm_sps_3``
     - CM_SPS.3
     - Optional[str]
     - optional
     - 
     - freetext
   * - ``cm_sps_4``
     - CM_SPS.4
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - body site
   * - ``cm_sps_5``
     - CM_SPS.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - site modifier
   * - ``cm_sps_6``
     - CM_SPS.6
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - collection modifier method code

.. _hl7-v2_3-CM_UVC:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_UVC.CM_UVC
   :noindex:

   HL7 v2 CM_UVC data type.

CM_UVC
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_uvc_1``
     - CM_UVC.1
     - Optional[str]
     - optional
     - 
     - value code
   * - ``cm_uvc_2``
     - CM_UVC.2
     - Optional[str]
     - optional
     - 
     - value amount

.. _hl7-v2_3-CM_VR:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_VR.CM_VR
   :noindex:

   HL7 v2 CM_VR data type.

CM_VR
~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_vr_1``
     - CM_VR.1
     - Optional[str]
     - optional
     - 
     - first data code value
   * - ``cm_vr_2``
     - CM_VR.2
     - Optional[str]
     - optional
     - 
     - Last data code calue

.. _hl7-v2_3-CM_WVI:

.. py:class:: hl7types.hl7.v2_3.datatypes.CM_WVI.CM_WVI
   :noindex:

   HL7 v2 CM_WVI data type.

CM_WVI
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cm_wvi_1``
     - CM_WVI.1
     - Optional[str]
     - optional
     - 
     - Channel Number
   * - ``cm_wvi_2``
     - CM_WVI.2
     - Optional[str]
     - optional
     - 
     - Channel Name

.. _hl7-v2_3-CN:

.. py:class:: hl7types.hl7.v2_3.datatypes.CN.CN
   :noindex:

   HL7 v2 CN data type.

CN
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cn_1``
     - CN.1
     - Optional[str]
     - optional
     - 
     - ID number (ST)
   * - ``cn_2``
     - CN.2
     - Optional[str]
     - optional
     - 
     - family name
   * - ``cn_3``
     - CN.3
     - Optional[str]
     - optional
     - 
     - given name
   * - ``cn_4``
     - CN.4
     - Optional[str]
     - optional
     - 
     - middle initial or name
   * - ``cn_5``
     - CN.5
     - Optional[str]
     - optional
     - 
     - suffix (e.g., JR or III)
   * - ``cn_6``
     - CN.6
     - Optional[str]
     - optional
     - 
     - prefix (e.g., DR)
   * - ``cn_7``
     - CN.7
     - Optional[str]
     - optional
     - 
     - degree (e.g., MD)
   * - ``cn_8``
     - CN.8
     - Optional[str]
     - optional
     - 
     - source table
   * - ``cn_9``
     - CN.9
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - assigning authority

.. _hl7-v2_3-CP:

.. py:class:: hl7types.hl7.v2_3.datatypes.CP.CP
   :noindex:

   HL7 v2 CP data type.

CP
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cp_1``
     - CP.1
     - Optional[:ref:`MO <hl7-v2_3-MO>`]
     - optional
     - 
     - price
   * - ``cp_2``
     - CP.2
     - Optional[str]
     - optional
     - 
     - price type
   * - ``cp_3``
     - CP.3
     - Optional[str]
     - optional
     - 
     - from value
   * - ``cp_4``
     - CP.4
     - Optional[str]
     - optional
     - 
     - to value
   * - ``cp_5``
     - CP.5
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - range units
   * - ``cp_6``
     - CP.6
     - Optional[str]
     - optional
     - 
     - range type

.. _hl7-v2_3-CQ:

.. py:class:: hl7types.hl7.v2_3.datatypes.CQ.CQ
   :noindex:

   HL7 v2 CQ data type.

CQ
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cq_1``
     - CQ.1
     - Optional[str]
     - optional
     - 
     - quantity
   * - ``cq_2``
     - CQ.2
     - Optional[:ref:`CE <hl7-v2_3-CE>`]
     - optional
     - 
     - units

.. _hl7-v2_3-CX:

.. py:class:: hl7types.hl7.v2_3.datatypes.CX.CX
   :noindex:

   HL7 v2 CX data type.

CX
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cx_1``
     - CX.1
     - Optional[str]
     - optional
     - 
     - ID
   * - ``cx_2``
     - CX.2
     - Optional[str]
     - optional
     - 
     - check digit
   * - ``cx_3``
     - CX.3
     - Optional[str]
     - optional
     - 
     - code identifying the check digit scheme employed
   * - ``cx_4``
     - CX.4
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - assigning authority
   * - ``cx_5``
     - CX.5
     - Optional[str]
     - optional
     - 
     - identifier type code
   * - ``cx_6``
     - CX.6
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - assigning facility

.. _hl7-v2_3-DLN:

.. py:class:: hl7types.hl7.v2_3.datatypes.DLN.DLN
   :noindex:

   HL7 v2 DLN data type.

DLN
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``dln_1``
     - DLN.1
     - Optional[str]
     - optional
     - 
     - Driver´s License Number
   * - ``dln_2``
     - DLN.2
     - Optional[str]
     - optional
     - 
     - Issuing State, province, country
   * - ``dln_3``
     - DLN.3
     - Optional[str]
     - optional
     - 
     - expiration date

.. _hl7-v2_3-DR:

.. py:class:: hl7types.hl7.v2_3.datatypes.DR.DR
   :noindex:

   HL7 v2 DR data type.

DR
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``dr_1``
     - DR.1
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     - 
     - range start date/time
   * - ``dr_2``
     - DR.2
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     - 
     - range end date/time

.. _hl7-v2_3-ED:

.. py:class:: hl7types.hl7.v2_3.datatypes.ED.ED
   :noindex:

   HL7 v2 ED data type.

ED
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ed_1``
     - ED.1
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - source application
   * - ``ed_2``
     - ED.2
     - Optional[str]
     - optional
     - 
     - type of data
   * - ``ed_3``
     - ED.3
     - Optional[str]
     - optional
     - 
     - data
   * - ``ed_4``
     - ED.4
     - Optional[str]
     - optional
     - 
     - encoding
   * - ``ed_5``
     - ED.5
     - Optional[str]
     - optional
     - 
     - data

.. _hl7-v2_3-EI:

.. py:class:: hl7types.hl7.v2_3.datatypes.EI.EI
   :noindex:

   HL7 v2 EI data type.

EI
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ei_1``
     - EI.1
     - Optional[str]
     - optional
     - 
     - entity identifier
   * - ``ei_2``
     - EI.2
     - Optional[str]
     - optional
     - 
     - namespace ID
   * - ``ei_3``
     - EI.3
     - Optional[str]
     - optional
     - 
     - universal ID
   * - ``ei_4``
     - EI.4
     - Optional[str]
     - optional
     - 
     - universal ID type

.. _hl7-v2_3-FC:

.. py:class:: hl7types.hl7.v2_3.datatypes.FC.FC
   :noindex:

   HL7 v2 FC data type.

FC
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``fc_1``
     - FC.1
     - Optional[str]
     - optional
     - 
     - Financial Class
   * - ``fc_2``
     - FC.2
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     - 
     - Effective Date

.. _hl7-v2_3-HD:

.. py:class:: hl7types.hl7.v2_3.datatypes.HD.HD
   :noindex:

   HL7 v2 HD data type.

HD
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``hd_1``
     - HD.1
     - Optional[str]
     - optional
     - 
     - namespace ID
   * - ``hd_2``
     - HD.2
     - Optional[str]
     - optional
     - 
     - universal ID
   * - ``hd_3``
     - HD.3
     - Optional[str]
     - optional
     - 
     - universal ID type

.. _hl7-v2_3-JCC:

.. py:class:: hl7types.hl7.v2_3.datatypes.JCC.JCC
   :noindex:

   HL7 v2 JCC data type.

JCC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``jcc_1``
     - JCC.1
     - Optional[str]
     - optional
     - 
     - job code
   * - ``jcc_2``
     - JCC.2
     - Optional[str]
     - optional
     - 
     - job class

.. _hl7-v2_3-MA:

.. py:class:: hl7types.hl7.v2_3.datatypes.MA.MA
   :noindex:

   HL7 v2 MA data type.

MA
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ma_1``
     - MA.1
     - Optional[str]
     - optional
     - 
     - sample 1 from channel 1
   * - ``ma_2``
     - MA.2
     - Optional[str]
     - optional
     - 
     - sample 1 from channel 2
   * - ``ma_3``
     - MA.3
     - Optional[str]
     - optional
     - 
     - sample 1 from channel 3
   * - ``ma_4``
     - MA.4
     - Optional[str]
     - optional
     - 
     - sample 2 from channel 1
   * - ``ma_5``
     - MA.5
     - Optional[str]
     - optional
     - 
     - sample 2 from channel 2
   * - ``ma_6``
     - MA.6
     - Optional[str]
     - optional
     - 
     - sample 2 from channel 3

.. _hl7-v2_3-MO:

.. py:class:: hl7types.hl7.v2_3.datatypes.MO.MO
   :noindex:

   HL7 v2 MO data type.

MO
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``mo_1``
     - MO.1
     - Optional[str]
     - optional
     - 
     - quantity
   * - ``mo_2``
     - MO.2
     - Optional[str]
     - optional
     - 
     - denomination

.. _hl7-v2_3-NA:

.. py:class:: hl7types.hl7.v2_3.datatypes.NA.NA
   :noindex:

   HL7 v2 NA data type.

NA
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``na_1``
     - NA.1
     - Optional[str]
     - optional
     - 
     - value1
   * - ``na_2``
     - NA.2
     - Optional[str]
     - optional
     - 
     - value2
   * - ``na_3``
     - NA.3
     - Optional[str]
     - optional
     - 
     - value3
   * - ``na_4``
     - NA.4
     - Optional[str]
     - optional
     - 
     - value4

.. _hl7-v2_3-PL:

.. py:class:: hl7types.hl7.v2_3.datatypes.PL.PL
   :noindex:

   HL7 v2 PL data type.

PL
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``pl_1``
     - PL.1
     - Optional[str]
     - optional
     - 
     - point of care (ID)
   * - ``pl_2``
     - PL.2
     - Optional[str]
     - optional
     - 
     - room
   * - ``pl_3``
     - PL.3
     - Optional[str]
     - optional
     - 
     - bed
   * - ``pl_4``
     - PL.4
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - facility (HD)
   * - ``pl_5``
     - PL.5
     - Optional[str]
     - optional
     - 
     - location status
   * - ``pl_6``
     - PL.6
     - Optional[str]
     - optional
     - 
     - person location type
   * - ``pl_7``
     - PL.7
     - Optional[str]
     - optional
     - 
     - building
   * - ``pl_8``
     - PL.8
     - Optional[str]
     - optional
     - 
     - floor
   * - ``pl_9``
     - PL.9
     - Optional[str]
     - optional
     - 
     - Location type

.. _hl7-v2_3-PPN:

.. py:class:: hl7types.hl7.v2_3.datatypes.PPN.PPN
   :noindex:

   HL7 v2 PPN data type.

PPN
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ppn_1``
     - PPN.1
     - Optional[str]
     - optional
     - 
     - ID number
   * - ``ppn_2``
     - PPN.2
     - Optional[str]
     - optional
     - 
     - family name
   * - ``ppn_3``
     - PPN.3
     - Optional[str]
     - optional
     - 
     - given name
   * - ``ppn_4``
     - PPN.4
     - Optional[str]
     - optional
     - 
     - middle initial or name
   * - ``ppn_5``
     - PPN.5
     - Optional[str]
     - optional
     - 
     - suffix (e.g., JR or III)
   * - ``ppn_6``
     - PPN.6
     - Optional[str]
     - optional
     - 
     - prefix (e.g., DR)
   * - ``ppn_7``
     - PPN.7
     - Optional[str]
     - optional
     - 
     - degree (e.g., MD)
   * - ``ppn_8``
     - PPN.8
     - Optional[str]
     - optional
     - 
     - source table
   * - ``ppn_9``
     - PPN.9
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - assigning authority
   * - ``ppn_10``
     - PPN.10
     - Optional[str]
     - optional
     - 
     - name type code
   * - ``ppn_11``
     - PPN.11
     - Optional[str]
     - optional
     - 
     - identifier check digit
   * - ``ppn_12``
     - PPN.12
     - Optional[str]
     - optional
     - 
     - code identifying the check digit scheme employed
   * - ``ppn_13``
     - PPN.13
     - Optional[str]
     - optional
     - 
     - identifier type code
   * - ``ppn_14``
     - PPN.14
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - assigning facility
   * - ``ppn_15``
     - PPN.15
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     - 
     - Date/Time Action Performed

.. _hl7-v2_3-PT:

.. py:class:: hl7types.hl7.v2_3.datatypes.PT.PT
   :noindex:

   HL7 v2 PT data type.

PT
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``pt_1``
     - PT.1
     - Optional[str]
     - optional
     - 
     - processing ID
   * - ``pt_2``
     - PT.2
     - Optional[str]
     - optional
     - 
     - processing mode

.. _hl7-v2_3-QIP:

.. py:class:: hl7types.hl7.v2_3.datatypes.QIP.QIP
   :noindex:

   HL7 v2 QIP data type.

QIP
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``qip_1``
     - QIP.1
     - Optional[str]
     - optional
     - 
     - field name
   * - ``qip_2``
     - QIP.2
     - Optional[str]
     - optional
     - 
     - value1&value2&value3

.. _hl7-v2_3-QSC:

.. py:class:: hl7types.hl7.v2_3.datatypes.QSC.QSC
   :noindex:

   HL7 v2 QSC data type.

QSC
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``qsc_1``
     - QSC.1
     - Optional[str]
     - optional
     - 
     - name of field
   * - ``qsc_2``
     - QSC.2
     - Optional[str]
     - optional
     - 
     - relational operator
   * - ``qsc_3``
     - QSC.3
     - Optional[str]
     - optional
     - 
     - Value
   * - ``qsc_4``
     - QSC.4
     - Optional[str]
     - optional
     - 
     - relational conjunction

.. _hl7-v2_3-RCD:

.. py:class:: hl7types.hl7.v2_3.datatypes.RCD.RCD
   :noindex:

   HL7 v2 RCD data type.

RCD
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``rcd_1``
     - RCD.1
     - Optional[str]
     - optional
     - 
     - HL7 item number
   * - ``rcd_2``
     - RCD.2
     - Optional[str]
     - optional
     - 
     - HL7 date type
   * - ``rcd_3``
     - RCD.3
     - Optional[str]
     - optional
     - 
     - maximum column width

.. _hl7-v2_3-RI:

.. py:class:: hl7types.hl7.v2_3.datatypes.RI.RI
   :noindex:

   HL7 v2 RI data type.

RI
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ri_1``
     - RI.1
     - Optional[str]
     - optional
     - 
     - repeat pattern
   * - ``ri_2``
     - RI.2
     - Optional[str]
     - optional
     - 
     - explicit time interval

.. _hl7-v2_3-RP:

.. py:class:: hl7types.hl7.v2_3.datatypes.RP.RP
   :noindex:

   HL7 v2 RP data type.

RP
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``rp_1``
     - RP.1
     - Optional[str]
     - optional
     - 
     - pointer
   * - ``rp_2``
     - RP.2
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - application ID
   * - ``rp_3``
     - RP.3
     - Optional[str]
     - optional
     - 
     - type of data
   * - ``rp_4``
     - RP.4
     - Optional[str]
     - optional
     - 
     - subtype

.. _hl7-v2_3-SCV:

.. py:class:: hl7types.hl7.v2_3.datatypes.SCV.SCV
   :noindex:

   HL7 v2 SCV data type.

SCV
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``scv_1``
     - SCV.1
     - Optional[str]
     - optional
     - 
     - parameter class
   * - ``scv_2``
     - SCV.2
     - Optional[str]
     - optional
     - 
     - parameter value

.. _hl7-v2_3-SN:

.. py:class:: hl7types.hl7.v2_3.datatypes.SN.SN
   :noindex:

   HL7 v2 SN data type.

SN
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``sn_1``
     - SN.1
     - Optional[str]
     - optional
     - 
     - comparator
   * - ``sn_2``
     - SN.2
     - Optional[str]
     - optional
     - 
     - num1
   * - ``sn_3``
     - SN.3
     - Optional[str]
     - optional
     - 
     - separator or suffix
   * - ``sn_4``
     - SN.4
     - Optional[str]
     - optional
     - 
     - num2

.. _hl7-v2_3-TQ:

.. py:class:: hl7types.hl7.v2_3.datatypes.TQ.TQ
   :noindex:

   HL7 v2 TQ data type.

TQ
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``tq_1``
     - TQ.1
     - Optional[:ref:`CQ <hl7-v2_3-CQ>`]
     - optional
     - 
     - quantity
   * - ``tq_2``
     - TQ.2
     - Optional[str]
     - optional
     - 
     - interval
   * - ``tq_3``
     - TQ.3
     - Optional[str]
     - optional
     - 
     - duration
   * - ``tq_4``
     - TQ.4
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     - 
     - start date/time
   * - ``tq_5``
     - TQ.5
     - Optional[:ref:`TS <hl7-v2_3-TS>`]
     - optional
     - 
     - end date/time
   * - ``tq_6``
     - TQ.6
     - Optional[str]
     - optional
     - 
     - priority
   * - ``tq_7``
     - TQ.7
     - Optional[str]
     - optional
     - 
     - condition
   * - ``tq_8``
     - TQ.8
     - Optional[str]
     - optional
     - 
     - text (TX)
   * - ``tq_9``
     - TQ.9
     - Optional[str]
     - optional
     - 
     - conjunction
   * - ``tq_10``
     - TQ.10
     - Optional[str]
     - optional
     - 
     - order sequencing

.. _hl7-v2_3-TS:

.. py:class:: hl7types.hl7.v2_3.datatypes.TS.TS
   :noindex:

   HL7 v2 TS data type.

TS
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ts_1``
     - TS.1
     - Optional[str]
     - optional
     - 
     - time of an event
   * - ``ts_2``
     - TS.2
     - Optional[str]
     - optional
     - 
     - degree of precision

.. _hl7-v2_3-VH:

.. py:class:: hl7types.hl7.v2_3.datatypes.VH.VH
   :noindex:

   HL7 v2 VH data type.

VH
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``vh_1``
     - VH.1
     - Optional[str]
     - optional
     - 
     - start day range
   * - ``vh_2``
     - VH.2
     - Optional[str]
     - optional
     - 
     - end day range
   * - ``vh_3``
     - VH.3
     - Optional[str]
     - optional
     - 
     - start hour range
   * - ``vh_4``
     - VH.4
     - Optional[str]
     - optional
     - 
     - end hour range

.. _hl7-v2_3-XAD:

.. py:class:: hl7types.hl7.v2_3.datatypes.XAD.XAD
   :noindex:

   HL7 v2 XAD data type.

XAD
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``xad_1``
     - XAD.1
     - Optional[str]
     - optional
     - 
     - street address
   * - ``xad_2``
     - XAD.2
     - Optional[str]
     - optional
     - 
     - other designation
   * - ``xad_3``
     - XAD.3
     - Optional[str]
     - optional
     - 
     - city
   * - ``xad_4``
     - XAD.4
     - Optional[str]
     - optional
     - 
     - state or province
   * - ``xad_5``
     - XAD.5
     - Optional[str]
     - optional
     - 
     - zip or postal code
   * - ``xad_6``
     - XAD.6
     - Optional[str]
     - optional
     - 
     - country
   * - ``xad_7``
     - XAD.7
     - Optional[str]
     - optional
     - 
     - address type
   * - ``xad_8``
     - XAD.8
     - Optional[str]
     - optional
     - 
     - other geographic designation
   * - ``xad_9``
     - XAD.9
     - Optional[str]
     - optional
     - 
     - county/parish code
   * - ``xad_10``
     - XAD.10
     - Optional[str]
     - optional
     - 
     - census tract

.. _hl7-v2_3-XCN:

.. py:class:: hl7types.hl7.v2_3.datatypes.XCN.XCN
   :noindex:

   HL7 v2 XCN data type.

XCN
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``xcn_1``
     - XCN.1
     - Optional[str]
     - optional
     - 
     - ID number (ST)
   * - ``xcn_2``
     - XCN.2
     - Optional[str]
     - optional
     - 
     - family name
   * - ``xcn_3``
     - XCN.3
     - Optional[str]
     - optional
     - 
     - given name
   * - ``xcn_4``
     - XCN.4
     - Optional[str]
     - optional
     - 
     - middle initial or name
   * - ``xcn_5``
     - XCN.5
     - Optional[str]
     - optional
     - 
     - suffix (e.g., JR or III)
   * - ``xcn_6``
     - XCN.6
     - Optional[str]
     - optional
     - 
     - prefix (e.g., DR)
   * - ``xcn_7``
     - XCN.7
     - Optional[str]
     - optional
     - 
     - degree (e.g., MD)
   * - ``xcn_8``
     - XCN.8
     - Optional[str]
     - optional
     - 
     - source table
   * - ``xcn_9``
     - XCN.9
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - assigning authority
   * - ``xcn_10``
     - XCN.10
     - Optional[str]
     - optional
     - 
     - name type
   * - ``xcn_11``
     - XCN.11
     - Optional[str]
     - optional
     - 
     - identifier check digit
   * - ``xcn_12``
     - XCN.12
     - Optional[str]
     - optional
     - 
     - code identifying the check digit scheme employed
   * - ``xcn_13``
     - XCN.13
     - Optional[str]
     - optional
     - 
     - identifier type code
   * - ``xcn_14``
     - XCN.14
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - assigning facility ID

.. _hl7-v2_3-XON:

.. py:class:: hl7types.hl7.v2_3.datatypes.XON.XON
   :noindex:

   HL7 v2 XON data type.

XON
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``xon_1``
     - XON.1
     - Optional[str]
     - optional
     - 
     - organization name
   * - ``xon_2``
     - XON.2
     - Optional[str]
     - optional
     - 
     - organization name type code
   * - ``xon_3``
     - XON.3
     - Optional[str]
     - optional
     - 
     - ID number (NM)
   * - ``xon_4``
     - XON.4
     - Optional[str]
     - optional
     - 
     - check digit
   * - ``xon_5``
     - XON.5
     - Optional[str]
     - optional
     - 
     - code identifying the check digit scheme employed
   * - ``xon_6``
     - XON.6
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - assigning authority
   * - ``xon_7``
     - XON.7
     - Optional[str]
     - optional
     - 
     - identifier type code
   * - ``xon_8``
     - XON.8
     - Optional[:ref:`HD <hl7-v2_3-HD>`]
     - optional
     - 
     - assigning facility ID

.. _hl7-v2_3-XPN:

.. py:class:: hl7types.hl7.v2_3.datatypes.XPN.XPN
   :noindex:

   HL7 v2 XPN data type.

XPN
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``xpn_1``
     - XPN.1
     - Optional[str]
     - optional
     - 
     - family name
   * - ``xpn_2``
     - XPN.2
     - Optional[str]
     - optional
     - 
     - given name
   * - ``xpn_3``
     - XPN.3
     - Optional[str]
     - optional
     - 
     - middle initial or name
   * - ``xpn_4``
     - XPN.4
     - Optional[str]
     - optional
     - 
     - suffix (e.g., JR or III)
   * - ``xpn_5``
     - XPN.5
     - Optional[str]
     - optional
     - 
     - prefix (e.g., DR)
   * - ``xpn_6``
     - XPN.6
     - Optional[str]
     - optional
     - 
     - degree (e.g., MD)
   * - ``xpn_7``
     - XPN.7
     - Optional[str]
     - optional
     - 
     - name type code
   * - ``xpn_8``
     - XPN.8
     - Optional[str]
     - optional
     - 
     - Name Representation code

.. _hl7-v2_3-XTN:

.. py:class:: hl7types.hl7.v2_3.datatypes.XTN.XTN
   :noindex:

   HL7 v2 XTN data type.

XTN
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``xtn_1``
     - XTN.1
     - Optional[str]
     - optional
     - 
     - [(999)] 999-9999 [X99999][C any text]
   * - ``xtn_2``
     - XTN.2
     - Optional[str]
     - optional
     - 
     - telecommunication use code
   * - ``xtn_3``
     - XTN.3
     - Optional[str]
     - optional
     - 
     - telecommunication equipment type (ID)
   * - ``xtn_4``
     - XTN.4
     - Optional[str]
     - optional
     - 
     - Email address
   * - ``xtn_5``
     - XTN.5
     - Optional[str]
     - optional
     - 
     - Country Code
   * - ``xtn_6``
     - XTN.6
     - Optional[str]
     - optional
     - 
     - Area/city code
   * - ``xtn_7``
     - XTN.7
     - Optional[str]
     - optional
     - 
     - Phone number
   * - ``xtn_8``
     - XTN.8
     - Optional[str]
     - optional
     - 
     - Extension
   * - ``xtn_9``
     - XTN.9
     - Optional[str]
     - optional
     - 
     - any text
