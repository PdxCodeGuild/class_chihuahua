from django.shortcuts import render
import subprocess, sys
import pandas as pd



# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    vm_list = []
    spath = "static\\scripts\\vminfo.ps1"
    p = subprocess.run(["powershell.exe",
                        spath
                        
    ])
    vminfo = pd.read_csv('static\\scripts\\report.csv')
    position = 0
    for vm in vminfo['VMName']:
        vm = vminfo['VMName'][position]
        vm_list.append(vm)
        position += 1
    print(vm_list)
    
    return render(request, 'pages/about.html')

def create(request):
    return render(request, 'pages/create.html')

def delete(request):
    vm_list = []
    spath = "static\\scripts\\vminfo.ps1"
    p = subprocess.run(["powershell.exe",
                        spath
                        
    ])
    vminfo = pd.read_csv('static\\scripts\\report.csv')
    position = 0
    for vm in vminfo['VMName']:
        vm = vminfo['VMName'][position]
        vm_list.append(vm)
        position += 1
    print(vm_list)
    return render(request, 'pages/delete.html', {'vm_list':vm_list})

def createVM(request):
    vm_name = request.POST['vmName']
    vm_ram = request.POST['ramCount']
    cpu_count = request.POST['coreCount']
    vm_loc = '"D:\Hyper-V\VM\Virtual Machines"'
    version = int(request.POST['version'])
    boot_device = 'VHD'
    vm_gen = 2
    vm_switch = 'testsw'
    vmhd_loc = f'"D:\\Hyper-V\\Virtual Hard Disks\\{vm_name}.vhdx"'
    if version == 10:
        winVersion = f"New-VHD -ParentPath 'D:\\Hyper-V\\Templates\\Windows10template.vhdx' -Path 'D:\\Hyper-V\\Virtual Hard Disks\\{vm_name}.vhdx' -Differencing\n"
    elif version == 11:
        winVersion = f"New-VHD -ParentPath 'D:\\Hyper-V\\Templates\\Windows11template.vhdx' -Path 'D:\\Hyper-V\\Virtual Hard Disks\\{vm_name}.vhdx' -Differencing\n"
    
    p = subprocess.run([
                "powershell.exe",
                winVersion,
                f"New-VM -Name '{vm_name}' -MemoryStartupBytes {vm_ram}GB -BootDevice {boot_device} -VHDPath {vmhd_loc} -Path {vm_loc} -Generation {vm_gen} -Switch {vm_switch}\n",
                f"Set-VMProcessor '{vm_name}' -Count {cpu_count}\n",
                f"Start-VM -Name '{vm_name}'"
            ],
            stdout=sys.stdout)
    collectVM(request)
    print(vm_name, cpu_count, vm_ram, version)
    return render(request, 'pages/about.html')

def deleteVM(request):
    vm_name = request.POST['vmName']
    
    p = subprocess.run([
            "powershell.exe",
            f"Stop-VM -Name '{vm_name}' -force\n",
            f"Remove-VM -Name '{vm_name}' -force\n",
            f'Remove-Item "D:\Hyper-V\Virtual Hard Disks\{vm_name}.*" -force\n',
            f'Remove-Item "D:\Hyper-V\VM\Virtual Machines\{vm_name}" -force -Confirm:$false\n',
        ],
        stdout=sys.stdout)
    collectVM(request)
    return render(request, 'pages/about.html')

def collectVM(request):
    spath = "static\\scripts\\vminfo.ps1"
    p = subprocess.run(["powershell.exe",
                        spath
                        
    ])
    vminfo = pd.read_csv('static\\scripts\\report.csv')
    for vm in vminfo['VMName']:
        position = 0
        vm = vminfo['VMName'][position]
        vm_dict = {vm:[vminfo['CPUCount'][position], vminfo['RAM'][position]]}
        position += 1
    print(vm_dict)
    
    return render(request, 'pages/about.html')

def powerOn(request):
    vmname = request.POST['vmName']
    p = subprocess.run([
        'powershell.exe',
        f'Start-VM {vmname}'
        
    ])
def powerOff(request):
    vmname = request.POST['vmName']
    p = subprocess.run([
        'powershell.exe',
        f'Stop-VM {vmname}'
    ])
def edit(request):
    vm_list = []
    spath = "static\\scripts\\vminfo.ps1"
    p = subprocess.run(["powershell.exe",
                        spath
                        
    ])
    vminfo = pd.read_csv('static\\scripts\\report.csv')
    position = 0
    for vm in vminfo['VMName']:
        vm = vminfo['VMName'][position]
        vm_list.append(vm)
        position += 1
    print(vm_list)
    return render(request, 'pages/edit.html', {'vm_list':vm_list})

def editVM(request):
    vmname = request.POST['vmName']
    vm_ram = request.POST['ramCount']
    cpu_count = request.POST['coreCount']
    p = subprocess.run([
        'powershell.exe',
        f'Stop-VM {vmname}\n',
        f'Set-VM -StaticMemory -Name {vmname} -ProcessorCount {cpu_count} -MemoryStartupBytes {vm_ram}GB\n',
        f'Start-VM {vmname}\n'
    ])
    return render(request, 'pages/about.html')