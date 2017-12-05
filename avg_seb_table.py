import pandas as pd
import numpy as N
import csv

# julian day index for ROS days
jd1004 = ['49', '53', '348', '360']
jd1011 = ['18', '8', '19', '50']
jd1031 = ['34', '38', '28', '34']
jd1032 = ['50', '33', '54', '345', '52']

'''# julian day index for day after ROS day
jd1004 = ['50', '54', '349', '361']
jd1011 = ['19', '9', '20', '51']
jd1031 = ['35', '39', '29', '35']
jd1032 = ['51', '34', '55', '346', '53']'''

# julian day index for day before ROS day
'''jd1004 = ['48', '52', '347', '359']
jd1011 = ['17', '7', '18', '49']
jd1031 = ['33', '37', '27', '33']
jd1032 = ['49', '32', '53', '344', '51']'''

e = ['e1','e2','e3','e4','e5']
# type 1004
knet04r = N.zeros(len(jd1004))
lnet04r = N.zeros(len(jd1004))
se04r = N.zeros(len(jd1004))
le04r = N.zeros(len(jd1004))
ge04r = N.zeros(len(jd1004))

# type 1011
knet11r = N.zeros(len(jd1011))
lnet11r = N.zeros(len(jd1011))
se11r = N.zeros(len(jd1011))
le11r = N.zeros(len(jd1011))
ge11r = N.zeros(len(jd1011))

# type 1031
knet31r = N.zeros(len(jd1031))
lnet31r = N.zeros(len(jd1031))
se31r = N.zeros(len(jd1031))
le31r = N.zeros(len(jd1031))
ge31r = N.zeros(len(jd1031))

# type 1032
knet32r = N.zeros(len(jd1032))
lnet32r = N.zeros(len(jd1032))
se32r = N.zeros(len(jd1032))
le32r = N.zeros(len(jd1032))
ge32r = N.zeros(len(jd1032))


# gets fluxes for types 1004
for i in range(len(jd1004)):
    # ROS files
    with open('G:\\sntherm_AG\\fl04_'+e[i]+'.txt','rt') as text:
        knet = []
        lnet = []
        se = []
        le = []
        ge = []        
        for line in text:
            line_chars = line.strip().split()
            knet.append(line_chars[5])
            lnet.append(line_chars[9])
            se.append(line_chars[13])
            le.append(line_chars[14])
            ge.append(line_chars[15])
        knet_a = N.array(knet,dtype=N.float)
        lnet_a = N.array(lnet,dtype=N.float)
        se_a = N.array(se,dtype=N.float)
        le_a = N.array(le, dtype=N.float)
        ge_a = N.array(ge,dtype =N.float)
        
        knet04r[i] = N.mean(knet_a)
        lnet04r[i] = N.mean(lnet_a)
        se04r[i] = N.mean(se_a)
        le04r[i] = N.mean(le_a)
        ge04r[i] = N.mean(ge_a)
        del knet, lnet, se, le, ge
        del knet_a, lnet_a, se_a, le_a, ge_a
    
        
# gets fluxes for types 1011            
for i in range(len(jd1011)):
    with open('G:\\sntherm_AG\\fl11_'+e[i]+'.txt','rt') as text:
        knet = []
        lnet = []
        se = []
        le = []
        ge = []        
        for line in text:
            line_chars = line.strip().split()
            knet.append(line_chars[5])
            lnet.append(line_chars[9])
            se.append(line_chars[13])
            le.append(line_chars[14])
            ge.append(line_chars[15])
        knet_a = N.array(knet,dtype=N.float)
        lnet_a = N.array(lnet,dtype=N.float)
        se_a = N.array(se,dtype=N.float)
        le_a = N.array(le, dtype=N.float)
        ge_a = N.array(ge,dtype =N.float)
        
        knet11r[i] = N.mean(knet_a)
        lnet11r[i] = N.mean(lnet_a)
        se11r[i] = N.mean(se_a)
        le11r[i] = N.mean(le_a)
        ge11r[i] = N.mean(ge_a)
        del knet, lnet, se, le, ge
        del knet_a, lnet_a, se_a, le_a, ge_a
    
    

# gets fluxes for type 1031        
for i in range(len(jd1031)):
    with open('G:\\sntherm_AG\\fl31_'+e[i]+'.txt','rt') as text:
        knet = []
        lnet = []
        se = []
        le = []
        ge = []        
        for line in text:
            line_chars = line.strip().split()
            knet.append(line_chars[5])
            lnet.append(line_chars[9])
            se.append(line_chars[13])
            le.append(line_chars[14])
            ge.append(line_chars[15])
        knet_a = N.array(knet,dtype=N.float)
        lnet_a = N.array(lnet,dtype=N.float)
        se_a = N.array(se,dtype=N.float)
        le_a = N.array(le, dtype=N.float)
        ge_a = N.array(ge,dtype =N.float)
        
        knet31r[i] = N.mean(knet_a)
        lnet31r[i] = N.mean(lnet_a)
        se31r[i] = N.mean(se_a)
        le31r[i] = N.mean(le_a)
        ge31r[i] = N.mean(ge_a)
        del knet, lnet, se, le, ge
        del knet_a, lnet_a, se_a, le_a, ge_a
    
    

# gets fluxes for type 1032        
for i in range(len(jd1032)):
    with open('G:\\sntherm_AG\\fl32_'+e[i]+'.txt','rt') as text:
        knet = []
        lnet = []
        se = []
        le = []
        ge = []        
        for line in text:
            line_chars = line.strip().split()
            knet.append(line_chars[5])
            lnet.append(line_chars[9])
            se.append(line_chars[13])
            le.append(line_chars[14])
            ge.append(line_chars[15])
        knet_a = N.array(knet,dtype=N.float)
        lnet_a = N.array(lnet,dtype=N.float)
        se_a = N.array(se,dtype=N.float)
        le_a = N.array(le, dtype=N.float)
        ge_a = N.array(ge,dtype =N.float)
        
        knet32r[i] = N.mean(knet_a)
        lnet32r[i] = N.mean(lnet_a)
        se32r[i] = N.mean(se_a)
        le32r[i] = N.mean(le_a)
        ge32r[i] = N.mean(ge_a)
        del knet, lnet, se, le, ge
        del knet_a, lnet_a, se_a, le_a, ge_a

#df = []
names = ['knet04r','lnet04r','se04r','le04r','ge04r','knet11r','lnet11r','se11r','le11r','ge11r','knet31r','lnet31r','se31r','le31r','ge31r','knet32r','lnet32r','se32r','le32r','ge32r']    

arrays = [names,knet04r,lnet04r,se04r,le04r,ge04r,knet11r,lnet11r,se11r,le11r,ge11r,knet31r,lnet31r,se31r,le31r,ge31r,knet32r,lnet32r,se32r,le32r,ge32r]    
with open("G:\\Figures for Thesis\\avg_seb_df.csv",'wb') as f:
    writer = csv.writer(f)
    writer.writerows(arrays)
#for array in arrays:
##df = pd.concat(arrays)
#new_df = pd.DataFrame(df)
#df.to_csv("G:\\Figures for Thesis\\avg_seb_df.csv")

 