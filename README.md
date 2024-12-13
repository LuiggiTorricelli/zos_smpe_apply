# Ansible z/OS SMP/E APPLY role

The Ansible role `zos_smpe_apply` will perform a sequence of steps to execute the SMP/E APPLY command to apply SYSMODs to an existing SMP/E target zone, considering the variables informed by the user on the specified z/OS host(s).

## Requirements

Python and Z Open Automation Utilities must be installed on the remote z/OS system, since the modules `zos_find` and `zos_mvs_raw` from the collection `ibm.ibm_zos_core` are used along the role.

## Role Variables

This role has multiple variables. The descriptions and defaults for all these variables can be found in the **[`defaults/main.yml`](/defaults/main.yml)** file and **[`meta/argument_specs.yml`](/meta/argument_specs.yml)**, together with a detailed description below:

| Variable | Description | Optional? |
| -------- | ----------- | :-------: |
| **[`show_output`](/meta/argument_specs.yml)** | Determine if output should be displayed or not at the end | Yes<br>(default: `true`) |
| **[`smpe_apply_options`](/meta/argument__specs.yml)** | Options to be considered on the SMP/E APPLY command. Details below. | Yes<br>(default: `{}`) |
| **[`smpe_global_csi`](/meta/argument_specs.yml)** | Data set name of the SMP/E GLOBAL CSI | No |
| **[`smpe_smppts`](/meta/argument_specs.yml)** | Data set name of the SMPPTS data set | Yes<br>(default: `""`) |
| **[`smpe_target_zone`](/meta/argument_specs.yml)** | Zone name of the SMP/E target zone | No |

### Detailed structure of variable `smpe_apply_options`, based on IBM SMP/E documentation (see **[The APPLY Command: Operands](https://www.ibm.com/docs/en/zos/3.1.0?topic=s-operands)**):

Consider that if the option is not informed on the `smpe_apply_options`, it will not be included on the SMP/E APPLY command and it will assume its default value during the GIMSMP program execution.

If attributes `groupextend`, `nojclin`, `bypass.holdclass`, `bypass.holderror`, `bypass.holdfixcat`, `bypass.holdsystem` and its attributes, `bypass.holduser` and/or `bypass.xzifreq` is informed as an empty list (empty dictionary in case of `bypass.holdsystem`), it will be normally included on the SMP/E APPLY command.

Only inform the attributes you need on the SMP/E APPLY command statement.

| Variable | Attribute | Type | Optional? | Comments |
| -------- | --------- | :--: | :-------: | -------- |
| `smpe_apply_options` | `apars` | boolean | Yes | |
| `smpe_apply_options` | `assem` | boolean | Yes | |
| `smpe_apply_options` | `bypass` | dictionary | Yes | |
| `smpe_apply_options` | `bypass.holdclass` | list | Yes | Possible elements are `ERREL`, `HIPER`, `PE`, `UCLREL` and/or `YR2000`. |
| `smpe_apply_options` | `bypass.holderror` | list | Yes | |
| `smpe_apply_options` | `bypass.holdfixcat` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem` | dictionary | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.action` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.ao` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.db2bind` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.dddef` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.delete` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.dep` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.doc` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.downld` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.dynact` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.ec` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.enh` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.exit` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.exrf` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.fullgen` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.iogen` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.ipl` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.msgskel` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.multsys` | list | Yes | |
| `smpe_apply_options` | `bypass.holdsystem.restart` | list | Yes | |
| `smpe_apply_options` | `bypass.holduser` | list | Yes | |
| `smpe_apply_options` | `bypass.id` | boolean | Yes | |
| `smpe_apply_options` | `bypass.ifreq` | boolean | Yes | |
| `smpe_apply_options` | `bypass.pre` | boolean | Yes | |
| `smpe_apply_options` | `bypass.req` | boolean | Yes | |
| `smpe_apply_options` | `bypass.xzifreq` | list | Yes | |
| `smpe_apply_options` | `check` | boolean | Yes | |
| `smpe_apply_options` | `compress` | string or list | Yes | String `ALL` or a list of strings |
| `smpe_apply_options` | `exclude` | list | Yes | |
| `smpe_apply_options` | `exsrcid` | list | Yes | |
| `smpe_apply_options` | `fixcat` | list | Yes | |
| `smpe_apply_options` | `forfmid` | list | Yes | |
| `smpe_apply_options` | `functions` | boolean | Yes | |
| `smpe_apply_options` | `group` | boolean | Yes | |
| `smpe_apply_options` | `groupextend` | list | Yes | Possible elements are `NOAPARS` and/or `NOUSERMODS` |
| `smpe_apply_options` | `jclinreport` | boolean | Yes | |
| `smpe_apply_options` | `nojclin` | list | Yes | |
| `smpe_apply_options` | `ptfs` | boolean | Yes | |
| `smpe_apply_options` | `redo` | boolean | Yes | |
| `smpe_apply_options` | `retry` | boolean | Yes | |
| `smpe_apply_options` | `reuse` | boolean | Yes | |
| `smpe_apply_options` | `select` | list | Yes | |
| `smpe_apply_options` | `sourceid` | list | Yes | |
| `smpe_apply_options` | `usermods` | boolean | Yes | |
| `smpe_apply_options` | `xzgroup` | list | Yes | |
| `smpe_apply_options` | `xzreq` | boolean | Yes | |

## Dependencies

None.

## Example Playbook

On the scenario below, the role `zos_smpe_apply` is being used to apply the fictitionous PTFs UI97000 and UI91000 and APAR PH12345 to the target zone `ZONEAAA`. The SMP/E CSI data set is `SMPE.GLOBAL.CSI`. The CHECK attribute is required to first verify the apply process for the specified SYSMODs. All system hold actions also needs to be bypassed.

Note that `bypass.holdsystem` is being informed as an empty dictionary. That would translate to `BYPASS(HOLDSYSTEM)` on the SMP/E APPLY command.

See that `smpe_smppts` is not being informed. This way, it is not added to the GIMSMP program call, causing it to look for the SMPPTS data set on the SMP/E CSI DDDEF entry.

    - hosts: zos_server
      roles:
        - role: zos_smpe_apply
          show_output: true
          smpe_global_csi: "SMPE.GLOBAL.CSI"
          smpe_target_zone: "ZONEAAA"
          smpe_apply_options:
            check: true
            select:
              - UI97000
              - UI91000
              - PH12345
            ptfs: true
            apars: true
            bypass:
              holdsystem: {}

## Sample Output

When this role is executed, it will perform a sequence of steps to apply the requested SYSMODs on the specified target zone, by generating the SMP/E APPLY command statement and executing it with the GIMSMP JCL program.

A fact named `zos_smpe_apply_details` is registered when the role is successfully executed, containing details about the result of SMP/E APPLY process, such as the applied SYSMODs, the CHECK usage and the element summary. It will be displayed if `show_output` is set to `true`.

    "zos_smpe_apply_details": {
        "applied_sysmods": [
            "UI97000",
            "UI91000",
            "UI91234",
            "UI99123",
        ],
        "check": false,
        "element_summary": [
            {
                "assem_names": [],
                "current_fmid": "HXXXXXX",
                "current_rmid": "UI97000",
                "distlib_library": "ADSNMACS",
                "element_name": "DSNDQWPZ",
                "element_status": "APPLIED",
                "element_type": "MAC",
                "load_modules": [],
                "other_status": [],
                "syslib_library": "SDSNMACS",
                "sysmod_name": "UI97000",
                "sysmod_status": "APPLIED"
            },
            {
                "assem_names": [],
                "current_fmid": "HXXXXXX",
                "current_rmid": "UI91000",
                "distlib_library": "ADSNLOAD",
                "element_name": "DSNB1CMU",
                "element_status": "APPLIED",
                "element_type": "MOD",
                "load_modules": [
                    {
                        "lmod_syslib": "SDSNLOAD",
                        "load_module": "DSNIDM"
                    }
                ],
                "other_status": [],
                "syslib_library": "",
                "sysmod_name": "UI91000",
                "sysmod_status": "APPLIED"
            },
            {
                "assem_names": [],
                "current_fmid": "HXXXXXX",
                "current_rmid": "UI91000",
                "distlib_library": "ADSNLOAD",
                "element_name": "DSNB1DCM",
                "element_status": "APPLIED",
                "element_type": "MOD",
                "load_modules": [
                    {
                        "lmod_syslib": "SDSNLOAD",
                        "load_module": "DSNIDM"
                    }
                ],
                "other_status": [
                    {
                        "element_status": "NOT SEL",
                        "sysmod_name": "UI91234",
                        "sysmod_status": "APPLIED"
                    }
                ],
                "syslib_library": "",
                "sysmod_name": "UI91000",
                "sysmod_status": "APPLIED"
            },
            {
                "assem_names": [],
                "current_fmid": "HXXXXXX",
                "current_rmid": "UI91234",
                "distlib_library": "ADSNLOAD",
                "element_name": "DSNB1DDN",
                "element_status": "APPLIED",
                "element_type": "MOD",
                "load_modules": [
                    {
                        "lmod_syslib": "SDSNLOAD",
                        "load_module": "DSNIDM"
                    }
                ],
                "other_status": [],
                "syslib_library": "",
                "sysmod_name": "UI91234",
                "sysmod_status": "APPLIED"
            },
            {
                "assem_names": [],
                "current_fmid": "HXXXXXX",
                "current_rmid": "UI99123",
                "distlib_library": "ADSNLOAD",
                "element_name": "DSNB1DGB",
                "element_status": "APPLIED",
                "element_type": "MOD",
                "load_modules": [
                    {
                        "lmod_syslib": "SDSNLOAD",
                        "load_module": "DSNIDM"
                    },
                    {
                        "lmod_syslib": "SDSNLOAD",
                        "load_module": "DSNXXX"
                    }
                ],
                "other_status": [],
                "syslib_library": "",
                "sysmod_name": "UI99123",
                "sysmod_status": "APPLIED"
            }
        ]
    }

## License

This role is licensed under licensed under [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

## Author Information

This role was created in 2024 by Luiggi Torricelli.
