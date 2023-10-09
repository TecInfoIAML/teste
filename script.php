<?php
// Código PHP anterior
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Receber dados do formulário e montar em um array
    $dados = [
        "estado_civil" => $_POST["estado_civil"],
        "ordem_inscricao" => $_POST["ordem_inscricao"],
        "horario_aula" => $_POST["horario_aula"],
        "qualificacao_previa" => $_POST["qualificacao_previa"],
        "qualificacao_anterior"=> $_POST["qualificacao_anterior"],
        "nacionalidade" => $_POST["nacionalidade"],
        "escolaridade_materna"=>$_POST["escolaridade_materna"],
        "escolaridade_paterna"=>$_POST["escolaridade_paterna"],
        "profissao_materna"=>$_POST["profissao_materna"],
        "profissao_paterna"=>$_POST["profissao_paterna"],
        "nota_admissao" =>$_POST["nota_admissao"],
        "necessidades_educacionais"=>$_POST["necessidades_educacionais"],
        "devedor"=>$_POST["devedor"],
        "mensalidade_em_dia"=>$_POST["mensalidade_em_dia"],
        "sexo"=>$_POST["sexo"],
        "bolsista"=>$_POST["bolsista"],
        "idade_na_inscricao"=>$_POST["idade_na_inscricao"],
        "internaconal"=>$_POST["internaconal"],
        "disciplinas_inscrita1"=>$_POST["disciplinas_inscrita1"],
        "disciplinas_aprovadas"=>$_POST["disciplinas_aprovadas"],
        "disciplinas_inscrita2"=>$_POST["disciplinas_inscrita2"],
        "disciplinas_aprovadas2"=>$_POST["disciplinas_aprovadas2"]
        
    ];

    // Enviar dados para a API Python
    $url = 'http://21339de0-85d7-4708-a0f6-404d0b59524b.southcentralus.azurecontainer.io/score';  // Substitua pela URL da sua API
    $options = [
        'http' => [
            'header' => 'Content-Type: application/json',
            'method' => 'POST',
            'content' => json_encode($dados)
        ]
    ];
    $context = stream_context_create($options);
    $resultado_api = file_get_contents($url, false, $context);

    // Analisar a resposta JSON
    $resultado = json_decode($resultado_api, true);

    // Verificar a previsão
    if ($resultado["previsao"] == 1) {
        $status_evasao = "Evasão";
    } else {
        $status_evasao = "Não evadido";
    }

    // Agora, você pode exibir $status_evasao no seu HTML
}
// Resto do código PHP
?>