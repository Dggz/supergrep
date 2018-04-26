"""IBM DS command entry point"""
import os

from openpyxl import load_workbook

from ntsparser.ibmds.arrays import process as arrays
from ntsparser.ibmds.drives import process as drives
from ntsparser.ibmds.features import process as features
from ntsparser.ibmds.pools import process as pools
from ntsparser.ibmds.san_hosts import process as san_hosts
from ntsparser.ibmds.storage_controllers import process as storage_controllers
from ntsparser.ibmds.storage_enclosures import process as storage_enclosures
from ntsparser.ibmds.volumes import process as volumes
from ntsparser.parsing import load_raw_content
from ntsparser.utils import get_bundle_dir, get_separated_content

__all__ = ('main',)


def main(input_files: str, output_file: str) -> None:
    """IBM DS Entry point

    :param input_files:
    :param output_file:
    """
    template_path = os.path.join(
        get_bundle_dir(), r'resources\ibmds-template.xlsx')
    workbook = load_workbook(template_path)

    raw_content_patterns = (
        '*.csv',
    )
    raw_content = load_raw_content(tuple(input_files), raw_content_patterns)

    ibmds_content = get_separated_content(
        raw_content, (raw_content_patterns[0], ))

    storage_controllers(workbook, ibmds_content)
    features(workbook, ibmds_content)
    storage_enclosures(workbook, ibmds_content)
    drives(workbook, ibmds_content)
    arrays(workbook, ibmds_content)
    volumes(workbook, ibmds_content)
    pools(workbook, ibmds_content)
    san_hosts(workbook, ibmds_content)

    workbook.save(output_file)
