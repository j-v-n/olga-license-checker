""" 
License Checker Tool Developed To Check OLGA Module/License Availability 

This script queries the OLGA license servers to check license availability

Requirements:
    - lmutil.exe in the same working directory as script


Arguments:
    - feature (string): The feature a user wants to check the availability of

Returns:
    - pprint output of server availability


"""

import subprocess
import pprint
import re


def feature_check(feature):
    """ Function to determine which servers to ping to check availability
    
    The base licenses and specific modules are housed in separate server locations(ports)
    This function checks which server list to query for each feature

    Arguments:
        feature (string): The feature a user wants to check the availability of
    
    Returns:
        servers (list of strings): The server list to query for availability of aforementioned
        feature
    
        """
    if feature in ["olga", "gui", "batch", "water"]:
        servers = []  # enter list of servers
    elif feature in [
        "olga_comptrack",
        "single_h2o",
        "etohtracking",
        "megtracking",
        "steam",
        "meohtracking",
        "tracertracking",
        "single_other",
        "single_co2",
        "compmodule",
        "corrosion",
        "bundle",
        "ifecorrmod",
        "femthermtool",
        "soil",
        "femthermviewer",
        "femtherm",
        "hydratekinetics",
        "slugtracking",
        "waxdeposition",
        "well-extended",
        "well",
        "wellsgui",
        "olga_wax",
    ]:
        servers = []  # enter list of servers
    return servers


def license_check(feature):
    """ Function to check license availability
    
    This function opens lmutil.exe and does the actual license check.
    This requires lmutil.exe to be in the same folder as script
    
    Arguments:
        feature (string): The feature a user wants to check the availability of
    
    Returns:
        out (string): Text output from the lmstat query
    
     """
    out = ""
    servers = feature_check(feature)
    for server in servers:
        lmstat = subprocess.Popen(
            ["lmutil", "lmstat", "-c", server, "-f", feature],
            shell=False,
            stdout=subprocess.PIPE,
            stderr=None,
            stdin=None,
            text=True,
        )
        out = out + lmstat.communicate()[0]
    return out


def print_output(output_text):
    """ Function to glean relevant information from the text output of lmstat query

    The current version of this function outputs a dictionary with server name
    and license availability
    
    Arguments:
        output_text (string): Text output from lmstat query
    
    Returns:
        pprint output of license availability
    
    
     """
    server_pattern = re.compile(r"\d+@.+\.com")
    server_matches = server_pattern.finditer(output_text)

    usage_pattern = re.compile(r"Users of.+")
    usage_matches = usage_pattern.finditer(output_text)

    servers = []
    usage = []

    for match in server_matches:
        servers.append(match.group(0))

    for match in usage_matches:
        usage.append(match.group(0))

    output_to_display = dict(zip(servers, usage))
    if output_to_display == {}:
        output_to_display = "The program is having issues connecting to the server. Please try again later or contact your license champion"
        pprint.pprint(output_to_display)
    else:
        pprint.pprint(
            "------Server Address----------------------------Feature Availability------"
        )
        pprint.pprint(output_to_display)


if __name__ == "__main__":
    print(
        "Please enter the name of the feature/module: \n(Please refer to module_names.txt to find correct names)"
    )
    feature = input()
    try:
        print_output(license_check(feature))
    except UnboundLocalError as e:
        print(
            "\nIncorrect entry.\nPlease make sure you have spelt the name of the feature correctly.\nKindly refer to module_names.txt"
        )

