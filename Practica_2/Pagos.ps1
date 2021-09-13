$Ahorro = 10000
$Total = $Ahorro
While($true){
    $Retiro = Read-Host -Prompt "Cuanto Desea Retirar? [1] 1000 [2] 500 [3] 200 [4] 100 [5] Salir"

    Switch($Retiro){
        1{
        $Total = $Total-1000
        Write-Host $Total
        }
        2{
        $Total = $Total-500
        Write-Host $Total
        }
        3{
        $Total = $Total-200
        Write-Host $Total
        }
        4{
        $Total = $Total-100
        Write-Host $Total
        }
        5{
        exit
        }
        default{
        Write-Host "Ingresa un valor correcto"
        }
    }
}
