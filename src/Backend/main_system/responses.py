import traceback
from django.http import JsonResponse


# Standardowe responsy, errory HTTP itp


def get_json_response_from(obj, http_code, iterate=False):
    if type(obj) == list or iterate:
        data_dict = {}
        for single_obj, i in zip(obj, range(len(obj))):
            data_dict[i] = single_obj.to_dict()
    else:
        data_dict = obj.to_dict()
    response = JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})
    response.status_code = http_code
    return response


def get_ok_response(message):
    frontend_message = FrontendMessage(200)
    frontend_message.add_message("OK")
    frontend_message.add_message(message)

    return get_json_response_from(frontend_message, 200)


def get_bad_request_error(message):
    frontend_message = FrontendMessage(400)
    frontend_message.add_message(message)

    return get_json_response_from(frontend_message, 400)


def get_internal_server_error(error):
    # wyświetlanie błędu
    print()
    print("500 WYSTĄPIŁ WEWNĘTRZNY BŁĄD SERWERA")
    print(error)
    print(type(error).__name__)
    print(error.args)
    traceback.print_exc()
    print()

    frontend_message = FrontendMessage(500)
    frontend_message.add_message("Wystąpił wewnętrzy błąd serwera")

    return get_json_response_from(frontend_message, 500)


def get_custom_response(frontend_msg, http_code):
    frontend_msg.http_response_status_code = http_code
    return get_json_response_from(frontend_msg, http_code)


class FrontendMessage:
    def __init__(self, response_code=200, csrf_token="", drf_token=""):
        self.http_response_status_code = response_code
        self.messages = []
        self.csrf_token = csrf_token
        self.drf_token = drf_token
        self.fields = []

    def add_message(self, message):
        if isinstance(message, str):
            self.messages.append(message)
        elif isinstance(message, list):
            for msg in message:
                self.messages.append(msg)
        else:
            raise ValueError("Nieprawidłowy typ message")

    def add_field(self, name, value):
        self.fields.append([name, value])

    def to_dict(self):
        d = {"http_response_status_code": self.http_response_status_code,
             "messages": self.messages}
        # dodawanie dodatkowych informacji
        if self.csrf_token != "":
            d["csrf_token"] = self.csrf_token
        if self.drf_token != "":
            d["drf_token"] = self.drf_token
        for p in self.fields:
            d[p[0]] = p[1]
        return d