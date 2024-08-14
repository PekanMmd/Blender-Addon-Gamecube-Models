import bpy
from shared.IO.DAT_io import DATParser, DATBuilder
from shared.IO.ModelBuilder import ModelBuilder


def test_dat_write(file_path, out_path):
    importer_options = {
        "ik_hack": True,
        "verbose": True,
        "print_tree": False,
        "max_frame": 1000,
        "section_names": []
    }

    if bpy.ops.object.select_all.poll():
        bpy.ops.object.select_all(action='DESELECT')

    parser = DATParser(file_path, importer_options)
    parser.parseSections()
    parser.close()

    builder = ModelBuilder(bpy.context, parser.sections, importer_options)
    dat_builder = DATBuilder(out_path, [parser.header] + builder.sections)
    dat_builder.build()


if __name__ == "__main__":
    file_path = "test_model/eievui.pkx.dat"
    out_path = "test_model/eievui_recreated.pkx.dat"
    test_dat_write(file_path, out_path)
