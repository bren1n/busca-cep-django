$(document).ready(function () {
    $("#id_cep").change(function () {
        var cep = $("#id_cep").val();

        if (cep.length == 8) {
            $.getJSON("http://viacep.com.br/ws/" + cep + "/json/ ", function (data) {
                var endereco = data;
                var localidade = endereco.localidade;
                var logradouro = endereco.logradouro;
                var bairro = endereco.bairro;
                var uf = endereco.uf;

                $("#id_localidade").val(localidade);
                $("#id_logradouro").val(logradouro);
                $("#id_bairro").val(bairro);
                $("#id_uf").val(uf);
            });
        }

    });
});