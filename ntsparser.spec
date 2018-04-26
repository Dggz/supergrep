# -*- mode: python -*-

# block_cipher = pyi_crypto.PyiBlockCipher(key=b'#jP9FUrRqiPPW$K@')


a = Analysis(
    ['ntsparser\\__main__.py'],
    pathex=['.'],
    binaries=None,
    datas=[('resources', 'resources')],
    hiddenimports=[
        'csv',
        'cytoolz._signatures',
        'cytoolz.curried',
        'cytoolz.utils',
        'fileinput',
        'typing',
        'openpyxl',
        'textfsm',
        'ntsparser.buildhash',
        'ntsparser.config',
        'ntsparser.formatting',
        'ntsparser.functional',
        'ntsparser.parseargs',
        'ntsparser.parsing',
        'ntsparser.utils',
        'ntsparser.celerra.backend_disk_info',
        'ntsparser.celerra.backend_storage',
        'ntsparser.celerra.backend_storage_details',
        'ntsparser.celerra.celerra',
        'ntsparser.celerra.disk_groups',
        'ntsparser.celerra.cifs_share',
        'ntsparser.celerra.fs_dedupe',
        'ntsparser.celerra.nas_fs_info_all',
        'ntsparser.celerra.nas_license',
        'ntsparser.celerra.nas_pool_info_all',
        'ntsparser.celerra.nas_replicate_info',
        'ntsparser.celerra.nas_summary',
        'ntsparser.celerra.physical_dm',
        'ntsparser.celerra.pool_configuration',
        'ntsparser.celerra.server_df',
        'ntsparser.celerra.system_details',
        'ntsparser.celerra.utils',
        'ntsparser.celerra.virtual_dm',
        'ntsparser.celerra.volume_size',
        'ntsparser.eva.controller',
        'ntsparser.eva.disk_enclosure',
        'ntsparser.eva.disk_group',
        'ntsparser.eva.disks',
        'ntsparser.eva.eva',
        'ntsparser.eva.hosts',
        'ntsparser.eva.storage_inventory',
        'ntsparser.eva.utils',
        'ntsparser.eva.virtual_disks',
        'ntsparser.ibmds.arrays',
        'ntsparser.ibmds.drives',
        'ntsparser.ibmds.features',
        'ntsparser.ibmds.ibmds',
        'ntsparser.ibmds.pools',
        'ntsparser.ibmds.san_hosts',
        'ntsparser.ibmds.storage_controllers',
        'ntsparser.ibmds.storage_enclosures',
        'ntsparser.ibmds.utils',
        'ntsparser.ibmds.volumes',
        'ntsparser.isilon.count_logical',
        'ntsparser.isilon.count_modified',
        'ntsparser.isilon.drive_list',
        'ntsparser.isilon.file_system_protocol',
        'ntsparser.isilon.hw_status',
        'ntsparser.isilon.isilon',
        'ntsparser.isilon.latency',
        'ntsparser.isilon.license_summary',
        'ntsparser.isilon.nfs_exports_list',
        'ntsparser.isilon.nfs_exports_zone',
        'ntsparser.isilon.ops',
        'ntsparser.isilon.performance_dashboard',
        'ntsparser.isilon.protocol_stats',
        'ntsparser.isilon.pstat',
        'ntsparser.isilon.quotas',
        'ntsparser.isilon.smb_shares_list',
        'ntsparser.isilon.smb_shares_zone',
        'ntsparser.isilon.storage_inventory',
        'ntsparser.isilon.storage_pool_summary',
        'ntsparser.isilon.sync_policies',
        'ntsparser.isilon.throughput',
        'ntsparser.isilon.top_level_directories',
        'ntsparser.isilon.utils',
        'ntsparser.isilon.zone_list',
        'ntsparser.three_par.cage',
        'ntsparser.three_par.cpg',
        'ntsparser.three_par.disks',
        'ntsparser.three_par.hosts',
        'ntsparser.three_par.license_sheet',
        'ntsparser.three_par.nodes',
        'ntsparser.three_par.ports',
        'ntsparser.three_par.storage_array_summary',
        'ntsparser.three_par.three_par',
        'ntsparser.three_par.volumes',
        'ntsparser.vmax.access_initiator',
        'ntsparser.vmax.access_view',
        'ntsparser.vmax.backend',
        'ntsparser.vmax.device_name_list',
        'ntsparser.vmax.disks',
        'ntsparser.vmax.dskgrp_summary',
        'ntsparser.vmax.list_wwn',
        'ntsparser.vmax.requests',
        'ntsparser.vmax.symcfg_list',
        'ntsparser.vmax.symdev_info',
        'ntsparser.vmax.thin_devices',
        'ntsparser.vmax.vmax',
        'ntsparser.vnx.disks',
        'ntsparser.vnx.disks_pivot',
        'ntsparser.vnx.initiator_type_pivot',
        'ntsparser.vnx.lun_storage_pivot',
        'ntsparser.vnx.luns',
        'ntsparser.vnx.luns_pivot',
        'ntsparser.vnx.mirror_view_a',
        'ntsparser.vnx.mirror_view_s',
        'ntsparser.vnx.raid_groups',
        'ntsparser.vnx.snap_clones',
        'ntsparser.vnx.snap_view',
        'ntsparser.vnx.software_packages',
        'ntsparser.vnx.sp_frontend_ports',
        'ntsparser.vnx.storage_array_pivot',
        'ntsparser.vnx.storage_array_summary',
        'ntsparser.vnx.storage_groups',
        'ntsparser.vnx.utils',
        'ntsparser.vnx.vnx',
        'ntsparser.xiv.disk_drives',
        'ntsparser.xiv.pools',
        'ntsparser.xiv.san_hosts',
        'ntsparser.xiv.storage_controllers',
        'ntsparser.xiv.utils',
        'ntsparser.xiv.volumes',
        'ntsparser.xiv.xiv',
        'ntsparser.xtremio.clusters',
        'ntsparser.xtremio.data_protection_groups',
        'ntsparser.xtremio.disks',
        'ntsparser.xtremio.initiators_and_groups',
        'ntsparser.xtremio.lun_mapping',
        'ntsparser.xtremio.performance_output',
        'ntsparser.xtremio.performance_summary',
        'ntsparser.xtremio.storage_array_summary',
        'ntsparser.xtremio.target_ports',
        'ntsparser.xtremio.utils',
        'ntsparser.xtremio.volume_performance',
        'ntsparser.xtremio.volumes',
        'ntsparser.xtremio.xtremio',
        'xmltodict'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    # cipher=block_cipher
)

# pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='ntsparser',
    debug=False,
    strip=False,
    upx=True,
    console=True
)
