#This file is used to define the column names for the import and export datasets.
#The values do not need to be altered by the user.

#Columns containing identifying information as well as data fields for which percentiles will NOT be calculated
#These columns will appear at the beginning of the output dataset. Add columns you want to appear at the end of the dataset to `extra_cols`
info_names = ["ID",
              "STATE_NAME",
              "ST_ABBREV",
              "CNTY_NAME",
              "REGION",
              "ACSTOTPOP",
              "ACSIPOVBAS",
              "ACSEDUCBAS",
              "ACSTOTHH","ACSTOTHU",
              "ACSUNEMPBAS", "ACSDISABBAS", "PEOPCOLOR",
              "LOWINCOME", "UNEMPLOYED", "DISABILITY", "LINGISO",
              "LESSHS",
              "UNDER5",
              "OVER64",
              "PRE1960",
              ]
#Columns containing data for which percentiles will be calculated
data_names = ["DEMOGIDX_2","DEMOGIDX_5",
         "PEOPCOLORPCT","LOWINCPCT","UNEMPPCT","DISABILITYPCT","LINGISOPCT","LESSHSPCT","UNDER5PCT","OVER64PCT","LIFEEXPPCT",
         "PM25","OZONE","DSLPM","RSEI_AIR","PTRAF","PRE1960PCT","PNPL","PRMP","PTSDF","UST","PWDIS", "DWATER", "NO2"]

#Columns containing the calculated index values
index_names = ["D2_PM25","D2_OZONE","D2_DSLPM","D2_RSEI_AIR","D2_PTRAF","D2_LDPNT","D2_PNPL","D2_PRMP","D2_PTSDF","D2_UST","D2_PWDIS", "D2_DWATER", "D2_NO2",
               "D5_PM25","D5_OZONE","D5_DSLPM","D5_RSEI_AIR","D5_PTRAF","D5_LDPNT","D5_PNPL","D5_PRMP","D5_PTSDF","D5_UST","D5_PWDIS","D5_DWATER", "D5_NO2"]

#Columns containing the percentile(P_), bin(B_), and text(T_) values.
percentile_bin_text_names = ["P_DEMOGIDX_2","P_DEMOGIDX_5","P_PEOPCOLORPCT","P_LOWINCPCT","P_UNEMPPCT","P_DISABILITYPCT","P_LINGISOPCT","P_LESSHSPCT","P_UNDER5PCT","P_OVER64PCT","P_LIFEEXPPCT","P_PM25","P_OZONE","P_DSLPM","P_RSEI_AIR","P_PTRAF","P_LDPNT","P_PNPL","P_PRMP","P_PTSDF","P_UST","P_PWDIS","P_DWATER","P_NO2",
                             "P_D2_PM25","P_D5_PM25","P_D2_OZONE","P_D5_OZONE","P_D2_DSLPM","P_D5_DSLPM","P_D2_RSEI_AIR","P_D5_RSEI_AIR","P_D2_PTRAF","P_D5_PTRAF","P_D2_LDPNT","P_D5_LDPNT","P_D2_PNPL","P_D5_PNPL","P_D2_PRMP","P_D5_PRMP","P_D2_PTSDF","P_D5_PTSDF","P_D2_UST","P_D5_UST","P_D2_PWDIS","P_D5_PWDIS","P_D2_DWATER","P_D5_DWATER","P_D2_NO2","P_D5_NO2",
                             "B_DEMOGIDX_2","B_DEMOGIDX_5","B_PEOPCOLORPCT","B_LOWINCPCT","B_UNEMPPCT","B_DISABILITYPCT","B_LINGISOPCT","B_LESSHSPCT","B_UNDER5PCT","B_OVER64PCT","B_LIFEEXPPCT","B_PM25","B_OZONE","B_DSLPM","B_RSEI_AIR","B_PTRAF","B_LDPNT","B_PNPL","B_PRMP","B_PTSDF","B_UST","B_PWDIS","B_DWATER","B_NO2",
                             "B_D2_PM25","B_D5_PM25","B_D2_OZONE","B_D5_OZONE","B_D2_DSLPM","B_D5_DSLPM","B_D2_RSEI_AIR","B_D5_RSEI_AIR","B_D2_PTRAF","B_D5_PTRAF","B_D2_LDPNT","B_D5_LDPNT","B_D2_PNPL","B_D5_PNPL","B_D2_PRMP","B_D5_PRMP","B_D2_PTSDF","B_D5_PTSDF","B_D2_UST","B_D5_UST","B_D2_PWDIS","B_D5_PWDIS","B_D2_DWATER","B_D5_DWATER","B_D2_NO2","B_D5_NO2",
                             "T_DEMOGIDX_2","T_DEMOGIDX_5","T_PEOPCOLORPCT","T_LOWINCPCT","T_UNEMPPCT","T_DISABILITYPCT","T_LINGISOPCT","T_LESSHSPCT","T_UNDER5PCT","T_OVER64PCT","T_LIFEEXPPCT","T_PM25","T_OZONE","T_DSLPM","T_RSEI_AIR","T_PTRAF","T_LDPNT","T_PNPL","T_PRMP","T_PTSDF","T_UST","T_PWDIS","T_DWATER","T_NO2",
                             "T_D2_PM25","T_D5_PM25","T_D2_OZONE","T_D5_OZONE","T_D2_DSLPM","T_D5_DSLPM","T_D2_RSEI_AIR","T_D5_RSEI_AIR","T_D2_PTRAF","T_D5_PTRAF","T_D2_LDPNT","T_D5_LDPNT","T_D2_PNPL","T_D5_PNPL","T_D2_PRMP","T_D5_PRMP","T_D2_PTSDF","T_D5_PTSDF","T_D2_UST","T_D5_UST","T_D2_PWDIS","T_D5_PWDIS","T_D2_DWATER","T_D5_DWATER","T_D2_NO2","T_D5_NO2"]

#Columns that you with to appear at the end of the EJScreen dataset.
#This allows `cols_all` to be easily created to allow for the output to have all columns in the correct order.
#Set value to [] if you do not with to utilize this list
extra_cols = ["AREALAND", "AREAWATER", "NPL_CNT", "TSDF_CNT", "EXCEED_COUNT_80" ,"EXCEED_COUNT_80_SUP"]



#A list of all columns in order. 
cols_all = info_names + data_names + index_names + percentile_bin_text_names + extra_cols