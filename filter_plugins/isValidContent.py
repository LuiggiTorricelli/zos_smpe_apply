from __future__ import absolute_import, division, print_function
from ansible.errors import AnsibleFilterTypeError

__metaclass__ = type

class FilterModule(object):
    def filters(self):
        filters = {
            "isValidContent": self.isValidContent,
        }
        return filters

    def isValidContent(self, input_content):
        if not isinstance(input_content, dict):
            raise AnsibleFilterTypeError("isValidContent - Filter must be applied on a dictionary.")
        
        error_msgs = []
        result = True

        possible_options = ["apars", "assem", "bypass", "check", "compress", "exclude", "exsrcid", "fixcat", "forfmid", "functions", "group", "groupextend", "jclinreport", "nojclin", "ptfs", "redo", "retry", "reuse", "select", "sourceid", "usermods", "xzgroup", "xzreq"]

        # For each key informed on the original content
        for attr in input_content.keys():
            if attr not in possible_options:
                error_msgs.append("Attribute '%s' is not a possible attribute for the APPLY processing." % attr)
                continue
            elif attr in ["apars", "assem", "check", "functions", "group", "jclinreport", "ptfs", "redo", "retry", "reuse", "usermods", "xzreq"]:
                if input_content[attr] not in [False, True]:
                    error_msgs.append("Attribute '%s' must be a boolean." % attr)
                    continue
            elif attr == "groupextend":
                if not isinstance(input_content[attr], list):
                    error_msgs.append("Attribute '%s' must be a list, empty or containing one or both values: 'NOAPARS', 'NOUSERMODS'." % attr)
                    continue
                for elem in input_content[attr]:
                    if not isinstance(elem, str):
                        error_msgs.append("Attribute '%s' must be a list, empty or containing one or both values: 'NOAPARS', 'NOUSERMODS'." % attr)
                        break
                    elif str(elem).upper().strip() not in ["NOAPARS", "NOUSERMODS"]:
                        error_msgs.append("Attribute '%s' must be a list, empty or containing one or both values: 'NOAPARS', 'NOUSERMODS'." % attr)
                        break
            elif attr == "compress" and not isinstance(input_content[attr], list) and str(input_content[attr]).upper().strip() != "ALL":
                error_msgs.append("Attribute '%s' must be either the string 'ALL' or a list, empty or containing strings." % attr)
                continue
            
            elif attr == "bypass":
                if not isinstance(input_content[attr], dict):
                    error_msgs.append("Attribute '%s' must be a dictionary, empty or with multiple attributes." % attr)
                    continue
                
                possible_bypass_options = ["holdclass", "holderror", "holdfixcat", "holdsystem", "holduser", "id", "ifreq", "pre", "req", "xzifreq"]
                possible_system_reason_ids = ["action", "ao", "db2bind", "dddef", "delete", "dep", "doc", "downld", "dynact", "ec", "enh", "exit", "exrf", "fullgen", "iogen", "ipl", "msgskel", "multsys", "restart"]
                possible_class_names = ["ERREL", "HIPER", "PE", "UCLREL", "YR2000"]

                # For each key informed on the BYPASS content
                for key in input_content[attr].keys():
                    if key not in possible_bypass_options:
                        error_msgs.append("Attribute '%s' is not a possible attribute for the BYPASS attribute." % key)
                        continue
                    elif key in ['id', 'ifreq', 'pre', 'req'] and input_content[attr][key] not in [False, True]:
                        error_msgs.append("BYPASS option '%s' must be a boolean." % key)
                        continue
                    elif key in ['holdclass', 'holderror', 'holdfixcat', 'holduser', 'xzifreq'] and not isinstance(input_content[attr][key], list):
                        error_msgs.append("BYPASS option '%s' must be a list." % key)
                        continue
                    elif key in ['holdsystem'] and not isinstance(input_content[attr][key], dict):
                        error_msgs.append("BYPASS option '%s' must be a dictionary." % key)
                        continue
                    
                    if key == 'holdclass':
                        for elem in input_content[attr][key]:
                            if not isinstance(elem, str):
                                error_msgs.append("BYPASS HOLDCLASS must be a list of strings.")
                                break
                            elif elem.upper() not in possible_class_names:
                                error_msgs.append("BYPASS HOLDCLASS informed class '%s' is not one of the possible names: %s." % (elem.upper(), ', '.join(possible_class_names)))
                                continue
                    elif key == 'holdsystem':
                        for reason_id in input_content[attr][key].keys():
                            if reason_id not in possible_system_reason_ids:
                                error_msgs.append("BYPASS HOLDSYSTEM informed system reason ID '%s' is not one of the possible names: %s." % (reason_id, ', '.join(possible_system_reason_ids)))
                                continue
                            elif not isinstance(input_content[attr][key][reason_id], list):
                                error_msgs.append("BYPASS HOLDSYSTEM informed system reason ID '%s' must be a list, empty or not." % reason_id)
                                continue
                            elif isinstance(input_content[attr][key][reason_id], list):
                                for elem in input_content[attr][key][reason_id]:
                                    if not isinstance(elem, str):
                                        error_msgs.append("BYPASS HOLDSYSTEM informed system reason ID '%s' must be a list, empty or not." % reason_id)
                                        break
                    
                    if isinstance(input_content[attr][key], list):
                        for elem in input_content[attr][key]:
                            if not isinstance(elem, str):
                                error_msgs.append("BYPASS attribute '%s' must be a list, empty or containing strings." % key)
                                break

            elif attr in ["exclude", "exsrcid", "fixcat", "forfmid", "nojclin", "select", "sourceid", "xzgroup"] and not isinstance(input_content[attr], list):
                error_msgs.append("Attribute '%s' must be a list, empty or containing strings." % attr)
                continue
            
            if isinstance(input_content[attr], list):
                for elem in input_content[attr]:
                    if not isinstance(elem, str):
                        error_msgs.append("Attribute '%s' must be a list, empty or containing strings." % attr)
                        continue

        if ("groupextend" in input_content and "group" in input_content and input_content["group"] == True):
            error_msgs.append("Attribute 'group' and 'groupextend' are mutually exclusive if 'group' is true.")
        
        if ("xzreq" in input_content and "xzgroup" in input_content and input_content["xzreq"] == True and input_content["xzgroup"] == []):
            error_msgs.append("If the XZREQ operand is specified, the XZGROUP operand may not be specified as a null list.")

        if len(error_msgs) > 0:
            raise AnsibleFilterTypeError("isValidContent - %s" % "\n".join(error_msgs))

        return(result)