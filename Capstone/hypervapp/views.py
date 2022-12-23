from django.shortcuts import render
import subprocess, sys


# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def create(request):
    return render(request, 'pages/create.html')

def delete(request):
    return render(request, 'pages/delete.html')

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
    print(vm_name, cpu_count, vm_ram, version)
    return render(request, 'pages/about.html')

def deleteVM(request):
    vm_name = request.POST['vmName']
    
    p = subprocess.run([
            "powershell.exe",
            f"Stop-VM -Name '{vm_name}' -force\n",
            f"Remove-VM -Name '{vm_name}' -force\n",
            f'Remove-Item "D:\Hyper-V\Virtual Hard Disks\{vm_name}.*" -force\n',
            f'Remove-Item "D:\Hyper-V\VM\Virtual Machines\{vm_name}" -force'
        ],
            stdout=sys.stdout)
    return render(request, 'pages/about.html')

def collectVM(request):
    p = subprocess.run([
        "powershell.exe"
        "Get-VM | Out-file vms.csv"
    ])
    return render(request, 'pages/about.html')