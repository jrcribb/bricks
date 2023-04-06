from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, SelectionType, BricksVariableType
from . import emotionality_detection, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=emotionality_detection,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=97,
        tabler_icon="MoodSad2",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        gdpr_compliant="True",
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["distance", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "emotionality_detection",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": [
                "anger",
                "fear",
                "anticipation",
                "trust",
                "surprise",
                "sadness",
                "joy",
                "disgust"
            ],
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )
