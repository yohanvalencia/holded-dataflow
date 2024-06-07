from typing import Dict, Any
import holded_dataflow


def parse_attributes(attributes: Dict[str, str]) -> Dict[str, Any]:
    """
    Parse attributes using the Rust function from my_module.

    Parameters:
        attributes (dict): A dictionary containing attribute key-value pairs.

    Returns:
        dict: A dictionary containing parsed attribute key-value pairs.
    """
    return holded_dataflow.parse_attributes(attributes)
