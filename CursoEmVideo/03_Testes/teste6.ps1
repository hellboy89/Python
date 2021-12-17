While ($true) {
    $teste = Read-Host "
==========================================
Qual função deseja:
                    1 = Ipconfig
                    2 = Tracert
                    3 = Test-Netconnection
                    4 = Nslookup
                    5 = GPUpdate /Force
                    (S) = SAIR

                    DIGA => "
    ""
    if ($teste -like '1') {
        write-host "====================> IPCONFIG"
        ipconfig
    }
    elseif ($teste -like '2') {
        write-host "====================> TRACERT"
        $tracert = Read-Host "Informe o IP "
        tracert $tracert
    }
    elseif ($teste -like '3') {
        Write-Host "====================> TEST-NETCONNECTION"
        $ip_test = Read-Host "Informe o IP "
        $port_teste = Read-Host "Informe a PORTA "
        $comando_test = Test-NetConnection $ip_test -port $port_teste -InformationLevel Quiet
        ""
        if ($comando_test -like 'True') {
            Write-Host "Porta está ABERTA!"            
        }
        elseif ($comando_test -like 'False') {
            Write-Host "Porta está FECHADA!"
        }
    }
    elseif ($teste -like '4') {
        Write-Host "====================> NSLOOKUP"
        $ip_nslookup = Read-Host "Digite o IP "
        nslookup.exe $ip_nslookup
    }
    elseif ($teste -like '5') {
        gpupdate /force
    }
    elseif ($teste -like 'S') {
        break
    }
}