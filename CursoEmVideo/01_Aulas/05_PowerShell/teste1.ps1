$size = Get-ChildItem E:\Multimedia\wallpaper | Measure-Object -Property Length -Sum | Select-Object Sum

Get-LocalUser | Where-Object {$_.Name -eq "Administrator"}

Get-LocalUser

Write-Host($size)

Write-Output($size)

if ($size -gt 1000) {
    Write-Host("é maior que 1000")
}
else {
    Write-Host("é menor que 1000")
}

Get-ChildItem -Path E:\Multimedia\wallpaper |
  Where-Object {$_.length -gt 10000} |
    Sort-Object -Property length |
      Format-Table -Property name, length