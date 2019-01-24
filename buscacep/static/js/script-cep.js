$(document).ready(function () {
    $("#id_cep").change(function () {
        var cep = $("#id_cep").val();

        if (cep.length == 9) {
            $.getJSON("http://viacep.com.br/ws/" + cep + "/json/ ", function (data) {
                var endereco = data;
                var localidade = endereco.localidade.toUpperCase()
                var logradouro = endereco.logradouro;
                var bairro = endereco.bairro;
                var uf = endereco.uf;
                function RemoveAccents(str) {
                  var accents    = 'ÀÁÂÃÄÅàáâãäåÒÓÔÕÕÖØòóôõöøÈÉÊËèéêëðÇçÐÌÍÎÏìíîïÙÚÛÜùúûüÑñŠšŸÿýŽž';
                  var accentsOut = "AAAAAAaaaaaaOOOOOOOooooooEEEEeeeeeCcDIIIIiiiiUUUUuuuuNnSsYyyZz";
                  str = str.split('');
                  var strLen = str.length;
                  var i, x;
                  for (i = 0; i < strLen; i++) {
                    if ((x = accents.indexOf(str[i])) != -1) {
                      str[i] = accentsOut[x];
                    }
                  }
                  return str.join('');
                }

                $('#id_localidade').val(RemoveAccents(localidade));
                $("#id_logradouro").val(logradouro);
                $("#id_bairro").val(bairro);
                $("#id_uf").val(uf);
            });
        }

    });
});
