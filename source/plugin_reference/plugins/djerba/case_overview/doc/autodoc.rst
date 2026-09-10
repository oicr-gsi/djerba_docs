====================================
Package djerba: Plugin case_overview
====================================


        * :ref:`djerba.plugins.case_overview.plugin_summary`
        * :ref:`djerba.plugins.case_overview.plugin_description`
        * :ref:`djerba.plugins.case_overview.plugin_generic_params`
        * :ref:`djerba.plugins.case_overview.plugin_specific_params`
        
        .. _djerba.plugins.case_overview.plugin_summary:

***********************************
Summary
***********************************

Plugin to generate the Case Overview report section

Assay can be specified by:
- Short name, which looks up in a table of known assays
- Full name -- if this parameter is set manually, the short name is ignored
Typically the short name will be used, but the full name is supported as an INI parameter
in case assay names are introduced/changed at short notice

.. _djerba.plugins.case_overview.plugin_specific_params:

***********************************
Specific parameters
***********************************

==================== =======
Parameter            Default
==================== =======
assay                N/A    
assay_description    N/A    
donor                N/A    
normal_id            N/A    
patient_study_id     N/A    
primary_cancer       N/A    
report_id            N/A    
requisition_approved N/A    
site_of_biopsy       N/A    
study                N/A    
tumour_id            N/A    
==================== =======

.. _djerba.plugins.case_overview.plugin_generic_params:

***********************************
Generic parameters
***********************************

================== ========
Parameter          Default 
================== ========
attributes         clinical
configure_priority 200     
depends_configure  (empty) 
depends_extract    (empty) 
extract_priority   200     
render_priority    40      
================== ========

.. _djerba.plugins.case_overview.plugin_description:

***********************************
Description
***********************************

No description provided.
