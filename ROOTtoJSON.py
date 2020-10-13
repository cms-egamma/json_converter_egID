import sys
import glob

import rootConversionUtils as convutils


year=str(sys.argv[1])
object=str(sys.argv[2])

if object == 'Ele':
    yearPrefix2016 = '2016LegacyReReco'
    idList2016 = ['Veto','Loose', 'Medium', 'Tight','MVA80noIso', 'MVA90noIso','MVA80iso', 'MVA90iso']
    fullName2016 = ['cutBasedElectronID-Fall17-94X-V2-veto','cutBasedElectronID-Fall17-94X-V2-loose', 'cutBasedElectronID-Fall17-94X-V2-medium', 'cutBasedElectronID-Fall17-94X-V2-tight','mvaEleID-Fall17-noIso-V2-wp80','mvaEleID-Fall17-noIso-V2-wp90','mvaEleID-Fall17-iso-V2-wp80','mvaEleID-Fall17-iso-V2-wp90'] 
    
    yearPrefix2018 = "2018"
    idList2018 = ['Veto','Loose', 'Medium', 'Tight','MVA80noIso', 'MVA90noIso','MVA80iso', 'MVA90iso']
    fullName2018 = fullName2016 = ['cutBasedElectronID-Fall17-94X-V2-veto','cutBasedElectronID-Fall17-94X-V2-loose', 'cutBasedElectronID-Fall17-94X-V2-medium', 'cutBasedElectronID-Fall17-94X-V2-tight','mvaEleID-Fall17-noIso-V2-wp80','mvaEleID-Fall17-noIso-V2-wp90','mvaEleID-Fall17-iso-V2-wp80','mvaEleID-Fall17-iso-V2-wp90'] 
    
    yearPrefix2017 = "2017"
    idList2017 = ['Veto','Loose', 'Medium', 'Tight','MVA80noIso', 'MVA90noIso','MVA80iso', 'MVA90iso']
    fullName2017 = fullName2016 = ['cutBasedElectronID-Fall17-94X-V2-veto','cutBasedElectronID-Fall17-94X-V2-loose', 'cutBasedElectronID-Fall17-94X-V2-medium', 'cutBasedElectronID-Fall17-94X-V2-tight','mvaEleID-Fall17-noIso-V2-wp80','mvaEleID-Fall17-noIso-V2-wp90','mvaEleID-Fall17-iso-V2-wp80','mvaEleID-Fall17-iso-V2-wp90'] 


if object == 'Pho':
    yearPrefix2016 = '2016LegacyReReco'
    idList2016 = ['Loose', 'Medium', 'Tight', 'MVA80', 'MVA90']
    fullName2016 = ['cutBasedPhotonID-Fall17-94X-V2-loose', 'cutBasedPhotonID-Fall17-94X-V2-medium', 'cutBasedPhotonID-Fall17-94X-V2-tight','mvaPhoID-RunIIFall17-v2-wp80', 'mvaPhoID-RunIIFall17-v2-wp90'] 

    yearPrefix2018 = "2018"
    idList2018 = ['Loose', 'Medium', 'Tight', 'MVA80', 'MVA90']
    fullName2018 = fullName2016 = ['cutBasedPhotonID-Fall17-94X-V2-loose', 'cutBasedPhotonID-Fall17-94X-V2-medium', 'cutBasedPhotonID-Fall17-94X-V2-tight','mvaPhoID-RunIIFall17-v2-wp80', 'mvaPhoID-RunIIFall17-v2-wp90'] 

    yearPrefix2017 = "2017"
    idList2017 = ['Loose', 'Medium', 'Tight', 'MVA80', 'MVA90']
    fullName2017 = fullName2016 = ['cutBasedPhotonID-Fall17-94X-V2-loose', 'cutBasedPhotonID-Fall17-94X-V2-medium', 'cutBasedPhotonID-Fall17-94X-V2-tight','mvaPhoID-RunIIFall17-v2-wp80', 'mvaPhoID-RunIIFall17-v2-wp90'] 


print(year)
if year == '2016' :
    idList = idList2016
    yearPrefix = yearPrefix2016
    fullName = fullName2016
elif year == '2017':
    idList = idList2017
    yearPrefix = yearPrefix2017
    fullName = fullName2017
elif year == '2018':
    idList = idList2018
    yearPrefix = yearPrefix2018
    fullName = fullName2018
elif year == 'Reco2018':
    idList = ['ElectronReco']
    yearPrefix = yearPrefix2018
    fullName = ['reco-eff']
elif year == 'Reco2017':
    idList = ['ElectronReco_pt10','ElectronReco_pt20']
    yearPrefix = yearPrefix2017
    fullName = ['reco-eff-pt10','reco-eff-pt20']
elif year == 'Reco2016':
    idList = ['ElectronReco_pt10','ElectronReco_pt20']
    yearPrefix = '2016'
    fullName = ['reco-eff-pt10','reco-eff-pt20']

else:
    print("year not properly set")
    sys.exit()


for i,n in enumerate(idList): 
#   convutils.readFile(str(yearPrefix)+str("_")+n+str("_Fall17V2.root"),"EGamma_SF2D",fullName[i],yearPrefix)
    #convutils.readFile(str(yearPrefix)+str("_")+n+str(".root"),"EGamma_SF2D",fullName[i],yearPrefix)

    if object == 'Ele':
        convutils.readFile("egammaEffi.txt_EGM2D_"+n+"_UL"+str(yearPrefix)+(".root"),"EGamma_SF2D",fullName[i],yearPrefix)

    if object == 'Pho':
        convutils.readFile("egammaEffi.txt_EGM2D_Photon_"+n+"_UL"+str(yearPrefix)+(".root"),"EGamma_SF2D",fullName[i],yearPrefix)

###egammaEffi.txt_EGM2D_MVA80noIso_UL17.root
