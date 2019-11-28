"""
Read parameter eggs from top of xmd file.
"""
import yaml


def _get_header_param_eggs(header_lines):
    """Reads parameter eggs from header lines"""
    # try:
    print('\n'.join(header_lines))
    header_dict = yaml.load('\n'.join(header_lines))
    print("---\n\n\t", header_dict, "\n\n---")
    params_dict = header_dict['params']
    return params_dict
    # except AttributeError as a_err:
    #     return {}
