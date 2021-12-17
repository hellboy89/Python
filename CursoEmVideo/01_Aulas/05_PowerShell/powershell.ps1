<#
get-host
#>
clear
get-host | Select-Object version
$PSVersionTable

# comando abaixo para verificar o peso de uma pasta só.
Get-ChildItem E:\Multimedia\wallpaper | Measure-Object -Property Length -Sum | Select-Object Sum

