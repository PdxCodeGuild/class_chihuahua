$vms = Get-VM -ComputerName MERLIN-LAPTOP


$vmInfo = foreach ($vm in $vms) {
  [PSCustomObject]@{
    VMName = $vm.Name
    CPUCount = $vm.ProcessorCount
    RAM = "{0:N2}" -f ($vm.MemoryStartup / 1GB)
    
  }
}

$vmInfo | Export-Csv -Path .\static\scripts\report.csv -NoTypeInformation