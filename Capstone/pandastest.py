import pandas as  pd

# view = pd.read_csv("static\\scripts\\report.csv")

# vm_dict = {}
# position = 0

# for vm in view['VMName']:
        
#         vm_dict[position] = {'Name':view['VMName'][position], 'CPU':view['CPUCount'][position], 'RAM':view['RAM'][position]}
#         position += 1

# print(vm_dict)

    # vm_list = []
    # spath = "static\\scripts\\vminfo.ps1"
    # p = subprocess.run(["powershell.exe",
    #                     spath
                        
    # ])
    # vminfo = pd.read_csv('static\\scripts\\report.csv')
    # position = 0
    # for vm in vminfo['VMName']:
    #     vm = vminfo['VMName'][position]
    #     vm_list.append(vm)
    #     position += 1
    # print(vm_list)
    
view = pd.read_csv("static\\scripts\\report.csv")

vm_list =[]
vm_dict = {}
position = 0

for item in view['VMName']:
        vm_dict = {'VM': view['VMName'][position],
                   'CPU': view['CPUCount'][position],
                   'RAM': view['RAM'][position]}
        vm_list.append(vm_dict)
        position += 1
       

print(vm_list)