"""
Read parameter eggs from top of xmd file.
"""
import yaml


def get_header_param_eggs(file_lines):
    return _get_header_param_eggs(
        _get_header_lines(file_lines)
    )


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


def _get_header_lines(lines):
    header_lines = []
    if lines[0].startswith("---"):
        for line in lines[1:]:
            if line.startswith("---"):
                return header_lines
            else:
                header_lines.append(line)
        # TODO: handle EOF
