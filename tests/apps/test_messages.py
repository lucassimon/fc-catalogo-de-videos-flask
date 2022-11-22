from apps.messages import Messages


def test_field_required():
    assert Messages.FIELD_REQUIRED.name == "FIELD_REQUIRED"
    assert Messages.FIELD_REQUIRED.value == "Campo obrigatório."


def test_does_not_exists():
    assert Messages.DOES_NOT_EXIST.name == "DOES_NOT_EXIST"
    assert Messages.DOES_NOT_EXIST.value == "Este(a) {} não existe."


def test_exception():
    assert Messages.EXCEPTION.name == "EXCEPTION"
    assert (
        Messages.EXCEPTION.value
        == "Ocorreu um erro no servidor. Contate o administrador."
    )


def test_already_exists():
    assert Messages.ALREADY_EXISTS.name == "ALREADY_EXISTS"
    assert Messages.ALREADY_EXISTS.value == "Já existe um(a) {} com estes dados."


def test_no_data():
    assert Messages.NO_DATA.name == "NO_DATA"
    assert Messages.NO_DATA.value == "Nenhum dado foi postado."


def test_password_didnot_match():
    assert Messages.PASSWORD_DIDNT_MATCH.name == "PASSWORD_DIDNT_MATCH"
    assert Messages.PASSWORD_DIDNT_MATCH.value == "As senhas não conferem."


def test_password_changed_ok():
    assert Messages.PASSWORD_CHANGED_OK.name == "PASSWORD_CHANGED_OK"
    assert Messages.PASSWORD_CHANGED_OK.value == "A senha foi alterada com sucesso."


def test_resource_created():
    assert Messages.RESOURCE_CREATED.name == "RESOURCE_CREATED"
    assert Messages.RESOURCE_CREATED.value == "{} criado(a)."


def test_resource_fetched_paginated():
    assert Messages.RESOURCE_FETCHED_PAGINATED.name == "RESOURCE_FETCHED_PAGINATED"
    assert Messages.RESOURCE_FETCHED_PAGINATED.value == "Lista os/as {} paginados(as)."


def test_resource_fetched():
    assert Messages.RESOURCE_FETCHED.name == "RESOURCE_FETCHED"
    assert Messages.RESOURCE_FETCHED.value == "{} retornado(a)."


def test_resource_updated():
    assert Messages.RESOURCE_UPDATED.name == "RESOURCE_UPDATED"
    assert Messages.RESOURCE_UPDATED.value == "{} atualizado(a)."


def test_resource_deleted():
    assert Messages.RESOURCE_DELETED.name == "RESOURCE_DELETED"
    assert Messages.RESOURCE_DELETED.value == "{} deletado(a)."


def test_token_created():
    assert Messages.TOKEN_CREATED.name == "TOKEN_CREATED"
    assert Messages.TOKEN_CREATED.value == "Token criado."


def test_invalid_credentials():
    assert Messages.INVALID_CREDENTIALS.name == "INVALID_CREDENTIALS"
    assert (
        Messages.INVALID_CREDENTIALS.value
        == "As credenciais estão inválidas para log in."
    )


def test_token_expired():
    assert Messages.TOKEN_EXPIRED.name == "TOKEN_EXPIRED"
    assert Messages.TOKEN_EXPIRED.value == "Token expirou."


def test_permission_denied():
    assert Messages.PERMISSION_DENIED.name == "PERMISSION_DENIED"
    assert Messages.PERMISSION_DENIED.value == "Permissão negada."


def test_resource_not_allowed():
    assert Messages.RESOURCE_NOT_ALLOWED.name == "RESOURCE_NOT_ALLOWED"
    assert (
        Messages.RESOURCE_NOT_ALLOWED.value
        == "O método solicitado não é permitido para este endpoint."
    )


def test_resource_not_found():
    assert Messages.RESOURCE_NOT_FOUND.name == "RESOURCE_NOT_FOUND"
    assert Messages.RESOURCE_NOT_FOUND.value == "Recurso não encontrado."


def test_resource_bad_request():
    assert Messages.RESOURCE_BAD_REQUEST.name == "RESOURCE_BAD_REQUEST"
    assert Messages.RESOURCE_BAD_REQUEST.value == "Houve um erro na requisição."


def test_resource_does_not_exist():
    assert Messages.RESOURCE_DOES_NOT_EXIST.name == "RESOURCE_DOES_NOT_EXIST"
    assert (
        Messages.RESOURCE_DOES_NOT_EXIST.value
        == "Um recurso com este ID não existe mais."
    )


def test_param_is_string():
    assert Messages.PARAM_IS_STRING.name == "PARAM_IS_STRING"
    assert Messages.PARAM_IS_STRING.value == "O parâmetro {} precisa ser um string"
