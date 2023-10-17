from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import location_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=location_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=369,
        tabler_icon="Location",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "personal_identifiers",
        ],  # first entry should be parent directory
        # bricks integrator information 
        cognition_init_mapping={
            "@@LABEL@@": "Location"
        },       
        integrator_inputs={
            "name": "location_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "location",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )
