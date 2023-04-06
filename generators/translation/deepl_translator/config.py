from util.configs import build_generator_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import deepl_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=deepl_translator,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=114,
        tabler_icon="LanguageKatakana",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="True",
        type="premium",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["translation", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "deepl_translator",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "API_KEY": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "<api-key-goes-here>",
                    "description": "Deepl API Key",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "TARGET_LANGUAGE": {
                    "selectionType": SelectionType.STRING.value,
                    "description": "only iso format",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LANGUAGE.value
                    ]
                }
            }
        }
    )