import pytest

from apps.responses import Response


class TestRespNotAllowedUser:
    def test_should_response_raises_an_error_when_resource_is_not_str(self, client):
        with pytest.raises(ValueError) as e:
            Response(None)

        assert e.value.__str__() == "O parâmetro resource precisa ser um string"

    def test_should_response_raises_an_error_when_msg_parameter_is_not_str(
        self, client
    ):
        with pytest.raises(ValueError) as e:
            Response("Auth").notallowed_user(None)

        assert e.value.__str__() == "O parâmetro msg precisa ser um string"

    def test_should_response_correctly_when_it_is_called(self, client):
        response = Response("Auth").notallowed_user()
        res = response.json
        assert response.status_code == 401
        assert res["message"] == "Este usuário não possui permissões necessárias."
        assert res["resource"] == "Auth"


class TestRespDataInvalid:
    def test_should_raises_an_error_when_error_parameter_is_not_dict(self, client):
        with pytest.raises(ValueError) as e:
            Response("Auth").data_invalid(None, "Some text")

        assert e.value.__str__() == "O parâmetro errors precisa ser um dict"

    def test_should_raises_an_error_when_msg_parameter_is_not_str(self, client):
        with pytest.raises(ValueError) as e:
            Response("Auth").data_invalid({}, None)

        assert e.value.__str__() == "O parâmetro msg precisa ser um string"

    def test_should_response_correctly_when_it_is_called(self, client):
        error = {"some-field": "some error"}
        response = Response("Auth").data_invalid(error)
        res = response.json
        assert response.status_code == 400
        assert res["message"] == "Ocorreu um erro nos campos informados."
        assert res["resource"] == "Auth"
        assert res["errors"] == error


class TestRespDoesNotExist:
    def test_should_raises_an_error_when_description_parameter_is_not_str(self, client):
        with pytest.raises(ValueError) as e:
            Response("Auth").does_not_exist(None)

        assert e.value.__str__() == "O parâmetro description precisa ser um string"

    def test_should_response_correctly_when_it_is_called(self, client):
        error = "Some description"
        response = Response("Auth").does_not_exist(error)
        res = response.json
        assert response.status_code == 404
        assert res["message"] == f"Este(a) {error} não existe."
        assert res["resource"] == "Auth"


class TestRespException:
    def test_should_raises_an_error_when_msg_parameter_is_not_str(self, client):
        with pytest.raises(ValueError) as e:
            Response("Auth").exception(None, "some description")

        assert e.value.__str__() == "O parâmetro msg precisa ser um string"

    def test_should_raises_an_error_when_description_parameter_is_not_str(self, client):
        with pytest.raises(ValueError) as e:
            Response("Auth").exception("Some message", None)

        assert e.value.__str__() == "O parâmetro description precisa ser um string"

    def test_should_response_correctly_when_it_is_called(self, client):
        error = "Some description"
        response = Response("Auth").exception(description=error)
        res = response.json
        assert response.status_code == 500
        assert res["message"] == "Ocorreu um erro no servidor. Contate o administrador."
        assert res["resource"] == "Auth"


class TestRespAlreadyExists:
    def test_should_raises_an_error_when_description_parameter_is_not_str(self, client):
        with pytest.raises(ValueError) as e:
            Response("Auth").already_exists(None)

        assert e.value.__str__() == "O parâmetro description precisa ser um string"

    def test_should_response_correctly_when_it_is_called(self, client):
        error = "Some description"
        response = Response("Auth").already_exists(description=error)
        res = response.json
        assert response.status_code == 409
        assert res["message"] == f"Já existe um(a) {error} com estes dados."
        assert res["resource"] == "Auth"


class TestRespOk:
    def test_should_raises_an_error_when_message_parameter_is_not_str(self, client):
        with pytest.raises(ValueError) as e:
            Response("Auth").ok(message=None)

        assert e.value.__str__() == "O parâmetro message precisa ser um string"

    def test_should_raises_an_error_when_status_parameter_is_not_int(self, client):
        with pytest.raises(ValueError) as e:
            Response("Auth").ok(message="Some message", status="Some status error")

        assert e.value.__str__() == "O parâmetro status precisa ser um int"

    def test_should_response_correctly_when_it_is_called(self, client):
        msg = "Success"
        response = Response("Auth").ok(message=msg)
        res = response.json
        assert response.status_code == 200
        assert res["message"] == msg
        assert res["resource"] == "Auth"

    def test_should_response_correctly_with_dict_data_argument(self):
        msg = "Success"
        data = {"foo": "bar"}
        response = Response("Auth").ok(message=msg, data=data)
        res = response.json
        assert response.status_code == 200
        assert res["message"] == msg
        assert res["resource"] == "Auth"
        assert res["data"] == data

    def test_should_response_correctly_with_list_data_argument(self):
        msg = "Success"
        data = [{"foo": "bar"}]
        response = Response("Auth").ok(message=msg, data=data)
        res = response.json
        assert response.status_code == 200
        assert res["message"] == msg
        assert res["resource"] == "Auth"
        assert res["data"] == data

    def test_should_response_correctly_with_extra_argument(self):
        msg = "Success"
        data = {"foo": "bar"}
        extra = {"ping": "pong"}
        response = Response("Auth").ok(message=msg, data=data, **extra)
        res = response.json
        assert response.status_code == 200
        assert res["message"] == msg
        assert res["resource"] == "Auth"
        assert res["data"] == data
        assert res["ping"] == "pong"
