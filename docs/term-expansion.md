# Term expansion

This tool uses [Term-Weaver](https://github.com/include-dcc/term-weaver) to materialize enumerations. 

## [LinkML properties](https://linkml.io/linkml-model/latest/docs/ReachabilityQuery/) currently supported *
- source_ontology 
- source_nodes
- relationship_types 
    - only supporting rdfs:subClassOf
- is_direct
    - true/false
- include_self
    - true/false

* It does not currently support 'traverse_up'

## just targets
- _source_enums
    - Uses [cam_source_enums](https://github.com/include-dcc/cam-source-enums) as a submodule to provide the source enumeration files for materialization. The _source_enums target automatically fetches the latest version of the source repo. 

- _expand
    - Runs the Term-Weaver script to materialize the enumerations.
    - _expand will be run at `just site` and `just testdoc`

## Dependencies
- _expand is now a depencency of gen-project. Running `just _expand` will run the enumeration materialization script without any further input needed by the user.
