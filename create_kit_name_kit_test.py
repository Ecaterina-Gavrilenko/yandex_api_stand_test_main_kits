import sender_stand_request
import data 

def get_new_user_token():
    auth_response = sender_stand_request.post_new_user(data.user_body)
    assert auth_response.status_code == 201

    auth_token = auth_response.json()["authToken"]
    assert auth_token != ""

    return auth_token

def positive_assert(kit_body):    
    auth_token = get_new_user_token()

    new_client_kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert new_client_kit_response.status_code == 201
    assert new_client_kit_response.json()["name"]

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()

    new_client_kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert new_client_kit_response.status_code == 400

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body 

def test_create_client_kit_1_letter_in_kit_name_success_response():
    positive_assert(get_kit_body("a"))

def test_create_client_kit_511_letters_in_kit_name_success_response():
    positive_assert(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"))
   
def test_create_client_kit_0_letters_in_kit_name_bad_request():
    negative_assert_code_400(get_kit_body(""))

def test_create_client_kit_512_letters_in_kit_name_bad_request():
    negative_assert_code_400(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"))

def test_create_client_kit_english_letters_in_kit_name_success_response():
    positive_assert(get_kit_body("QWErty"))

def test_create_client_kit_russian_letters_in_kit_name_success_response():
    positive_assert(get_kit_body("Мария"))

def test_create_client_kit_special_characters_in_kit_name_success_response():
    positive_assert(get_kit_body('"№%@",'))

def test_create_client_kit_with_spaces_in_kit_name_success_response():
    positive_assert(get_kit_body(" Человек и КО "))

def test_create_client_kit_numbers_in_kit_name_success_response():
    positive_assert(get_kit_body("123"))

def test_create_client_kit_parameter_not_passed_in_kit_name_bad_request():
    negative_assert_code_400({})

def test_create_client_kit_other_parameter_type_in_kit_name_bad_request():
    negative_assert_code_400(get_kit_body(123))