
**********************
Glossary
**********************

.. note:: Terms denoted as "script mode" are subcommands or *modes* of the main ``djerba.py`` script.

=================== ==========================================================================================================================================================
Term                Definition                                                                                                                                                
=================== ==========================================================================================================================================================
Assay               The process described by a report (eg. whole genome sequencing, targeted sequencing). An assay is associated with a group of Djerba components.           
Attribute           A component may have one or more attributes to determine the type of output document produced. Examples: clinical, research, simple.                      
Component           A plugin, helper, or merger. Modular components used to generate reports.                                                                                 
Configure           First step of Djerba report generation. Input a minimal INI file, output a fully specified INI file with all parameters shown. Script mode.               
Core                The central element of Djerba, which loads and runs components, and combines their HTML output into a PDF document.                                       
Extract             Second step of Djerba report generation. Input a fully specified INI file, output a JSON file with results. Script mode.                                  
Fully specified INI An INI file with all defined parameters explicitly specified for every component.                                                                         
Helper              Component type. Inputs an INI section, writes files to the workspace for use by other components.                                                         
Merger              Component type. Inputs an INI section. Takes lists of items (eg. genes) in a specific format, removes duplicates, and outputs an HTML table.              
Minimal INI         An INI file with sufficient information for the Djerba config step to run, filling in other values automatically.                                         
Plugin              Most commonly used component type. Takes an INI section as input, runs configure, extract and render steps, and outputs HTML.                             
Priority            Integer value to determine running order for components. Components run from lowest to highest priority value. Can be configured separately for each step.
Render              Third and final step of Djerba report generation. Input JSON from the extract step, output an HTML document and optional PDF. Script mode.                
Report              Run the configure, extract, and render steps in sequence to generate HTML/PDF from INI. Script mode. May also refer to the completed report document.     
Setup               Initialize an INI config file with sections and blank parameters for a given assay. Script mode.                                                          
Step                One of the three stages of report generation: configure, extract, and render.                                                                             
Top-level package   The main package from which a Djerba component is imported. A Djerba report may use multiple top-level packages.                                          
Update              Regenerate the HTML and PDF output with revised genomic summary text. Script mode.                                                                        
Workspace           Working directory in which Djerba components can read or write files. The workspace enables transfer of information from one component to another.        
=================== ==========================================================================================================================================================
