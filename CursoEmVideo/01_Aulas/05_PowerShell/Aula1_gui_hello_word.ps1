#Referência: https://www.youtube.com/watch?v=Qh_sqzlXeDQ&list=PLRIhLt0RAxWZXhs7ZEaqYMCmHkbEIiver

# Parâmetro abaixo necessário para importar as bibliotecas.
[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")

# Desenhando a forma da janela e controles

$Form_HelloWord = New-Object System.Windows.Forms.Form
    # Define o nome da janela no título
    $Form_HelloWord.Text = "Hello Word"
    # Define o tamanho da janela
    $Form_HelloWord.Size = New-Object System.Drawing.Size(800, 600)
    $Form_HelloWord.FormBorderStyle = "FixedDialog"
    # Para a janela sempre ficar no topo
    $Form_HelloWord.TopMost = $false
    # Irá tirar o botão de maximizar
    $Form_HelloWord.MaximizeBox = $false
    # Desativar botão de minimizar
    $Form_HelloWord.MinimizeBox = $false
    # Irá desativar o botão de fechar
    $Form_HelloWord.ControlBox = $true
    # Posicionar a janela no centro do monitor
    $Form_HelloWord.StartPosition = "CenterScreen"
    $Form_HelloWord.Font = "Segoe UI"

# Adicionando as camadas do FORM.

$label_HelloWord = New-Object System.Windows.Forms.Label
    $label_HelloWord.Location = New-Object System.Drawing.Size(8,8)
    # Aqui mostra a posição que o texto irá ficar.
    $label_HelloWord.Size = New-Object System.Drawing.Size(240,32)
    $label_HelloWord.TextAlign = "MiddleCenter"
    $label_HelloWord.Text = "hello world"
    $Form_HelloWord.Controls.Add($label_HelloWord)

# Adicionando um botão

$button_ClickMe = New-Object System.Windows.Forms.Button
    # Define o tamanho do botão.
    $button_ClickMe.Location = New-Object System.Drawing.Size(8,80)
    # Define o tamanho dos limites da imagem.
    $button_ClickMe.Size = New-Object System.Drawing.Size(240,32)
    # Alinhamento do texto no botão.
    $button_ClickMe.TextAlign = "MiddleCenter"
    # Adiciona um botão com o nome "click em mim!"
    $button_ClickMe.Text = "Click em mim!"
    $button_ClickMe.Add_Click({
        # Após clicado no botão, o nome muda para este abaixo.
        $button_ClickMe.Text = "Você deveria clicar aqui!"
        # Abre o notepad após clicado no botão.
        Start-Process notepad.exe
    })
    $Form_HelloWord.Controls.Add($button_ClickMe)

# Mostrar o FORM.

$Form_HelloWord.Add_Shown({$Form_HelloWord.Activate()})
[void] $Form_HelloWord.ShowDialog()
