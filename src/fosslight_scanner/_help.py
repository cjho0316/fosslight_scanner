#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 LG Electronics Inc.
# SPDX-License-Identifier: Apache-2.0
from fosslight_util.help import PrintHelpMsg

_HELP_MESSAGE_SCANNER = """
    FOSSLight Scanner performs open source analysis after downloading the source from URL that can be cloned by git or wget.
    Instead, open source analysis and checking copyright/license rules can be performed for the local source path.
    The output result is generated in OSS Report format.

    Usage: fosslight [Mode] [option1] <arg1> [option2] <arg2>...

    Parameters:
        Mode
            source\t\t    Run FOSSLight Source
            dependency\t\t    Run FOSSLight Dependency
            binary\t\t    Run FOSSLight Binary
            reuse\t\t    Run FOSSLight Reuse
            all\t\t\t    Run all scanners
            compare\t\t    Compare two FOSSLight reports in yaml format

        Options:
            -h\t\t\t    Print help message
            -p <path>\t\t    Path to analyze
            -w <link>\t\t    Link to be analyzed can be downloaded by wget or git clone
            -f <format>\t\t    FOSSLight Report file format (excel, yaml)
                               \t\t(In compare mode, supports excel, json, yaml, html)
            -o <output>\t\t    Output directory or file
            -c <number>\t\t    Number of processes to analyze source
            -r\t\t\t    Keep raw data
            -t\t\t\t    Hide the progress bar
            -v\t\t\t    Print FOSSLight Scanner version

        Options for only 'all' or 'bin' mode
            -u <db_url>\t\t    DB Connection(format :'postgresql://username:password@host:port/database_name')

        Options for only 'all' or 'dependency' mode
            -d <dependency_argument>\t    Additional arguments for running dependency analysis

        Options for only 'compare' mode
            -y <before yaml> <after yaml>   Two FOSSLight reports in yaml format (ex, -y 'before.yaml' 'after.yaml')"""


def print_help_msg():
    helpMsg = PrintHelpMsg(_HELP_MESSAGE_SCANNER)
    helpMsg.print_help_msg(True)
