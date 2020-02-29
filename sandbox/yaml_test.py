import yaml
import sys
files_list = [{'org_file1': 'target_file1'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},
              {'org_file2': 'target_file2'},              
              {'org_file2': 'target_file2'},              
              {'org_file3': 'target_file3'}]
print (yaml.dump(files_list))

with open('file1.yaml', 'w', encoding='utf8') as f:
    yaml.dump(files_list, f)

print('read data from yml\n')
with open('file1.yaml', 'r', encoding='utf8') as fn:
    #org_files_yml = yaml.load(fn, Loader=yaml.FullLoader)
    org_files_yml = yaml.load_all(fn, Loader=yaml.FullLoader)
    print('first org files list: %s \n' % org_files_yml)    
    print('first filelist size: %s \n' % sys.getsizeof(org_files_yml))
    #org_files_list = yaml.load(fn)
    #print ('data is \n %s' %org_files_list)
    for files in org_files_yml:
        print('files: %s' % files)
        print(type(files))
        for filelist in files:
            print('filelist: %s' % filelist)
            for org_file, target_file in filelist.items():
                #print (org_file, target_file)
                print('filelist size: %s' % sys.getsizeof(filelist))
    #    #for j,k in i.items():
    #    #    print(j,k)
#print ('data is \n %s' %org_files_list)
print('\nlast filelist size: %s' % sys.getsizeof(org_files_yml))
print('\nlast files size: %s' % sys.getsizeof(files))
