import pandas as  pd

view = pd.read_csv("static\\scripts\\report.csv")

# vm_dict = {}
# position = 0

# for vm in view['VMName']:
        
#         vm_dict[position] = {'Name':view['VMName'][position], 'CPU':view['CPUCount'][position], 'RAM':view['RAM'][position]}
#         position += 1

# print(vm_dict)

vm_list = []

for vm in view['VMName']:
        