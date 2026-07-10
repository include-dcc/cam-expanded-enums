## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540
[group('model development')]
_source_enums:
  git submodule update --remote --merge --init

# Arguments:
# -s = the source directory of the enumeration files to be expanded
# -m = name to be assigned to the expanded model

[group('model development')]
_expand: _source_enums
  tweaver -s source/src/cam_source_enums/schema -m cam_expanded_enums
