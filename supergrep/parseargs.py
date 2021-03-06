"""Parse command line arguments"""
import argparse
from typing import Any

from supergrep.celerra import celerra
from supergrep.config import settings
from supergrep.eva import eva
from supergrep.ibmds import ibmds
from supergrep.isilon import isilon
from supergrep.three_par import three_par
from supergrep.vmax import vmax
from supergrep.vnx import vnx
from supergrep.xiv import xiv
from supergrep.parse import parse
from supergrep.xtremio import xtremio



def build_parser() -> argparse.ArgumentParser:
    """Build argument parser

    :return: argument parser
    :rtype: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(prog=settings.prog_name)
    # parser.add_argument(
    #     '-m', '--module',
    #     help='specifies which module will run (single, multiple)'
    #          'single being one template, one input file type, one output sheet')
    parser.add_argument(
        '-t', '--templates',
        help='Template files have to be xml format, <sgr> tag on first level,'
             '<fname>, <sheet>, <template> tags on second level', nargs='+')
    parser.add_argument(
        '-i', '--input-files', help='paths to input files', nargs='+')
    parser.add_argument('-o', '--output-file', help='path to output file')
    return parser


def parse_args(argv: Any) -> tuple:
    """Define accepted arguments and parse them

    :param list argv: sys.argv
    :return: func, options
    """
    array_options = {
        'vnx': vnx.main,
        'vmax': vmax.main,
        'xtremio': xtremio.main,
        'celerra': celerra.main,
        '3par': three_par.main,
        'ibmds': ibmds.main,
        'isilon': isilon.main,
        'xiv': xiv.main,
        'eva': eva.main,
        'parse': parse.main
    }
    parser = build_parser()
    options = vars(parser.parse_args(argv))
    input_files = options.pop('input_files')
    # if 'templates' not in options:
    #     parser.exit(1, parser.format_help())
    if 'output_file' not in options:
        parser.exit(1, parser.format_help())
    output_file = options.pop('output_file')
    if not output_file:
        parser.exit(1, parser.format_help())
    # command = options.pop('templates')
    # if command in array_options:
    #     func = array_options[command]
    # else:
    #     parser.exit(1, parser.format_help())

    # print(options['templates'])
    func = array_options['parse']
    temp = options.pop('templates')

    return func, temp, input_files, output_file


# def build_parser() -> argparse.ArgumentParser:
#     """Build argument parser
# 
#     :return: argument parser
#     :rtype: argparse.ArgumentParser
#     """
#     parser = argparse.ArgumentParser(prog=settings.prog_name)
#     parser.add_argument(
#         '-a', '--array',
#         help='specifies which parsers will be invoked '
#              '(vnx, vmax, xtremio, celerra, 3par, isilon, ibmds, xiv, eva)')
#     parser.add_argument(
#         '-i', '--input-files', help='paths to input files', nargs='+')
#     parser.add_argument('-o', '--output-file', help='path to output file')
#     return parser
# 
# 
# def parse_args(argv: Any) -> tuple:
#     """Define accepted arguments and parse them
# 
#     :param list argv: sys.argv
#     :return: func, options
#     """
#     array_options = {
#         'vnx': vnx.main,
#         'vmax': vmax.main,
#         'xtremio': xtremio.main,
#         'celerra': celerra.main,
#         '3par': three_par.main,
#         'ibmds': ibmds.main,
#         'isilon': isilon.main,
#         'xiv': xiv.main,
#         'eva': eva.main
#     }
#     parser = build_parser()
#     options = vars(parser.parse_args(argv))
#     input_files = options.pop('input_files')
#     if 'array' not in options:
#         parser.exit(1, parser.format_help())
#     if 'output_file' not in options:
#         parser.exit(1, parser.format_help())
#     output_file = options.pop('output_file')
#     command = options.pop('array')
#     if command in array_options:
#         func = array_options[command]
#     else:
#         parser.exit(1, parser.format_help())
# 
#     return func, input_files, output_file
