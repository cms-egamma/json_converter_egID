#usage python combineJSONS.py year
import os, sys, json 
from collections import OrderedDict

json_list = []
current_dir = os.getcwd()
years = ['2017', '2018']
object = sys.argv[1]
year_list = []

#combined_filename = 'combined_eleIDSFs_'+year+'.json' 
combined_filename = 'run2_'+object+'IDs'+'.json' 
for (path, dir, files) in os.walk(current_dir):
    for year in years:
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.json' and year in filename and object in filename and 'combined' in filename:
                print "year : %s file name : %s "%(year,filename)
                json_path = "%s/%s" % (path, filename)
                json_list.append(json_path)
                year_list.append(year)

json_combine = OrderedDict()
iy=0;
for k in json_list:
    print(k)
    with open(k) as json_data:
        data = json.load(json_data,object_pairs_hook=OrderedDict)
        #temp = data['%s'%year_list[iy]]
        #json_combine.update(json.load(json_data,object_pairs_hook=OrderedDict))
        new_data = {"%s"%(year_list[iy]):data}
        json_combine.update(new_data)
        iy=iy+1

f =  open(current_dir+'/./'+combined_filename,'w')
json.dump(json_combine, f, sort_keys = False, indent = 4)
