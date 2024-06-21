# ejscreen-dataset-creator-2024

## Description
`ejscreen-dataset-creator-2024` is a Python tool that automates the calculation of EJScreen indexes (`calIndexes`), percentiles (`percentileCal` and `percentileCalState`), bin and text fields (`calBinTxt`), and lookup tables to produce the EJScreen 2023 dataset. As an option, the dataset can be joined with the Census block groups or tracts to create a feature class (`exportSpatial`).

## Python Package Requirements
All required packages come preinstalled in the default ArcGIS Pro 3.1 environment, which includes Python 3. The following are the packages and versions used in the development of this tool. 

| Package       | Version       | 
| ------------- |--------------:|
| python        | 3.9.16        | 
| pandas        | 1.4.4         | 
| numpy         | 1.20.1        | 
| arcgis        | 2.1.0.2       |  
| arcpy         | 3.1           |

ArcGIS Pro is required to export the results to an Esri feature class. 
## Input Requirements

The only required input is a csv file that contains the required columns and data to produce an EJScreen dataset. These column names are designated in `col_names.py` by 3 different lists:
* Info Names (`info_names`) - columns containing identifying information about the block group or tract as well as demographic information for which percentiles are not calculated
* Data Names (`data_names`) - columns containing socioeconomic and environmental indicator values for which percentiles will be calculated
* Extra Columns (`extra_cols`) - columns containing non-demographic information that is typically included at the end of an EJScreen dataset

By default, the following columns are required:

| `col_names.info_names`       | `col_names.data_names`      | `col_names.extra_cols`      |
| ------------- | ------------- | ------------- |
| ID |  DEMOGIDX_2 | AREALAND | 
| STATE_NAME | DEMOGIDX_5 | AREAWATER | 
| ST_ABBREV | PEOPCOLORPCT | NPL_CNT | 
| CNTY_NAME | LOWINCPCT | TSDF_CNT | 
| REGION | UNEMPPCT | EXCEED_COUNT_80 | 
| ACSTOTPOP | LINGISOPCT | EXCEED_COUNT_80_SUP | 
| ACSIPOVBAS | LESSHSPCT | |
| ACSEDUCBAS | UNDER5PCT | |
| ACSTOTHH | OVER64PCT | |
| ACSTOTHU | LIFEEXPPCT | |
| ACSUNEMPBAS | PM25 | |
| PEOPCOLOR | OZONE | |
| LOWINCOME | DSLPM | |
| UNEMPLOYED | DWATER | |
| LINGISO | NO2 | |
| LESSHS | RSEI_AIR | |
| UNDER5 | PTRAF | |
| OVER64 | PRE1960PCT | |
| PRE1960 | PNPL |  |
|  | PRMP | |
|  | PTSDF | |
|  | UST | |
|  | PWDIS | |

## How to Use the Tool
### Generate Full EJScreen Dataset
Before running the tool, open `ejscreen_dataset.py` and edit the following parameters:
* `level` - set to 1 to calculate national percentiles or set to 2 to calculate state percentiles
* `input_csv_path` - file path to the input EJScreen dataset for which is used to generate the output
* `output_csv_path` - file path to output EJScreen csv file that will be generated by the tool
* `lookuptable_xlsx_path` - file path to output lookup table Excel file that will be generated by the tool
* `output_to_featureclass` - boolean. If True, then join output EJScreen table to matching geometry based on "ID" column and export to  feature class
* `geometry_featureclass_path` - file path to block group/tract feature class that the output table will be joined to
* `output_featureclass_path` - file path to the output feature class that will be generated by the tool
* `schema_csv_path` - file path to schema csv file. This is used as part of the Batch Update Fields geoprocessing tool which sets field order, length, data type, and alias. `ejscreen_schema.csv` is included in this repository and can be used in this case. More information about the Batch Update Fields tool can be found [here](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/batch-update-fields.htm).

Once the parameters have been updated, run the Python file to generate the output.

## How Tied  Values are Handled for Percentiles:
Due to the variety of environmental data, an indicator or index often falls between two raw values used to determine the percentile range. In that case, the lower percentile is used. There are no rounding operations, or it can be considered as "rounding down". When such interpolation falls on a series of tied values, the lowest percentile out of those percentiles for the tied values is chosen.


## EPA Disclaimer
The United States Environmental Protection Agency (EPA) GitHub project code is provided on an "as is" basis and the user assumes responsibility for its use.  EPA has relinquished control of the information and no longer has responsibility to protect the integrity, confidentiality, or availability of the information.  Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by EPA.  The EPA seal and logo shall not be used in any manner to imply endorsement of any commercial product or activity by EPA or the United States Government. 


