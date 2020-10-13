# json_converter_egID
Set up to convert Egamma ID SFs rootfile to JSON

- Original Developers: Francesco Micheli and Vinzenz Stampf

- rootConversionUtils.py contains methods to read a TH2F from a root file and convert it to a json file
- ROOTtoJSON.py converts the root files from 2016LegacyReReco Id to jsons (one file for each id)



python ROOTtoJSON.py 2017 Ele

python ROOTtoJSON.py 2018 Ele

python ROOTtoJSON.py 2017 Pho

python ROOTtoJSON.py 2018 Pho

- combineJSONS.py merges all jsons files corresponding to the different IDs in one single file
python combineJSONS.py 2018 Ele

python combineJSONS.py 2017 Ele

python combineJSONS.py 2017 Pho

python combineJSONS.py 2018 Pho

- combineAllYearsJSON.py to combine all IDs of an object in one file
python combineAllYearsJSON.py Ele

python combineAllYearsJSON.py Pho