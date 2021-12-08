from malcolm.yamlutil import check_yaml_names, make_block_creator

motion01_block = make_block_creator(__file__, "motion01_block.yaml")
auto_scan_block = make_block_creator(__file__, "auto_scan_block.yaml")

__all__ = check_yaml_names(globals())
